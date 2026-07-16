#include "tdesktop_mtproto/mtproto.h"
#include <cstring>
#include <vector>
#include <stdexcept>
#include <random>

#ifdef _WIN32
    #define WIN32_LEAN_AND_MEAN
    #include <winsock2.h>
    #include <ws2tcpip.h>
    #pragma comment(lib, "ws2_32.lib")
#else
    #include <sys/socket.h>
    #include <netinet/in.h>
    #include <arpa/inet.h>
    #include <unistd.h>
    #include <netdb.h>
    #define SOCKET int
    #define INVALID_SOCKET -1
    #define SOCKET_ERROR -1
#endif

namespace tdesktop::mtproto {

// MTProto transport protocol constants
// VersionD (0xDDDDDDDD) = with padding (what tdesktop uses)
constexpr uint32_t kProtocolVersionD = 0xDDDDDDDDU;
// Version1 (0xEEEEEEEE) = without padding
constexpr uint32_t kProtocolVersion1 = 0xEEEEEEEEU;
// Encrypted header marker
constexpr uint32_t kEncryptedHeader = 0xEFEFEFEFU;

// Forbidden magic values in first 4 bytes of obfuscation header
constexpr uint32_t kForbidden[] = {
    0x44414548U, 0x54534F50U, 0x20544547U,
    0x4954504FU, 0xEEEEEEEEU, 0xDDDDDDDDU
};

struct Transport::Impl {
    SOCKET sock = INVALID_SOCKET;
    bool obfuscated = false;

    // AES-CTR state for obfuscation
    uint8_t encrypt_key[32]{};
    uint8_t encrypt_iv[16]{};
    uint8_t decrypt_key[32]{};
    uint8_t decrypt_iv[16]{};

    // Random generator
    std::mt19937_64 rng{ std::random_device{}() };

    void generate_random(uint8_t* buf, size_t len) {
        for (size_t i = 0; i < len; i++) {
            buf[i] = (uint8_t)(rng() & 0xFF);
        }
    }
};

Transport::Transport()
    : impl_(std::make_unique<Impl>()) {
#ifdef _WIN32
    WSADATA wsa;
    WSAStartup(MAKEWORD(2, 2), &wsa);
#endif
}

Transport::~Transport() {
    disconnect();
#ifdef _WIN32
    WSACleanup();
#endif
}

bool Transport::connect(const std::string& ip, int port) {
    impl_->sock = ::socket(AF_INET, SOCK_STREAM, 0);
    if (impl_->sock == INVALID_SOCKET) return false;

    sockaddr_in addr{};
    addr.sin_family = AF_INET;
    addr.sin_port = htons(port);
    inet_pton(AF_INET, ip.c_str(), &addr.sin_addr);

    if (::connect(impl_->sock, (sockaddr*)&addr, sizeof(addr)) == SOCKET_ERROR) {
        disconnect();
        return false;
    }

    return true;
}

void Transport::disconnect() {
    if (impl_->sock != INVALID_SOCKET) {
#ifdef _WIN32
        closesocket(impl_->sock);
#else
        close(impl_->sock);
#endif
        impl_->sock = INVALID_SOCKET;
    }
    impl_->obfuscated = false;
}

bool Transport::is_connected() const {
    return impl_->sock != INVALID_SOCKET;
}

bool Transport::perform_obfuscation() {
    if (!is_connected()) return false;

    // Generate 64 random bytes for obfuscation header
    uint8_t header[64];
    impl_->generate_random(header, 64);

    // Ensure first 4 bytes are not forbidden
    uint32_t* first4 = (uint32_t*)header;
    for (auto forbidden : kForbidden) {
        if (*first4 == forbidden) {
            // Regenerate just the first 4 bytes
            impl_->generate_random(header, 4);
            first4 = (uint32_t*)header;
        }
    }

    // Bytes 56-59: protocol magic (VersionD with padding)
    *(uint32_t*)(header + 56) = kProtocolVersionD;
    // Bytes 60-63: encrypted header marker
    *(uint32_t*)(header + 60) = kEncryptedHeader;

    // Derive encryption key/iv from header
    // Encrypt key = header[0..31]
    std::memcpy(impl_->encrypt_key, header, 32);
    // Encrypt IV = header[32..47]
    std::memcpy(impl_->encrypt_iv, header + 32, 16);
    // Decrypt key = header[0..31] too (after swapping)
    std::memcpy(impl_->decrypt_key, header, 32);
    // Decrypt IV = header[32..47]
    std::memcpy(impl_->decrypt_iv, header + 32, 16);
    // Swap keys for decrypt vs encrypt
    std::memcpy(impl_->decrypt_key, header + 32, 16);
    std::memcpy(impl_->decrypt_key + 16, header + 48, 16);
    std::memcpy(impl_->decrypt_iv, header + 16, 16);

    // Send the 64-byte obfuscation header
    int sent = ::send(impl_->sock, (const char*)header, 64, 0);
    if (sent != 64) return false;

    // Receive server's response (64 bytes)
    uint8_t response[64];
    int received = 0;
    while (received < 64) {
        int n = ::recv(impl_->sock, (char*)(response + received),
                       64 - received, 0);
        if (n <= 0) return false;
        received += n;
    }

    // Verify the encrypted header marker
    uint32_t server_marker = *(uint32_t*)(response + 60);
    if (server_marker != kEncryptedHeader) {
        // Non-obfuscated connection or protocol mismatch
        return false;
    }

    impl_->obfuscated = true;
    return true;
}

bool Transport::send_packet(const Packet& packet) {
    if (!is_connected()) return false;

    // Build the packet with length prefix
    std::vector<uint8_t> frame;

    // For VersionD: 4 bytes length (including seqno + msg_id? depends on mode)
    // Actually in VersionD: 4 bytes length, then payload, then 0-15 random padding
    // The length includes payload + padding

    // Get payload to send
    const auto& data = packet.data;

    // Calculate padding (0-15 bytes random for VersionD)
    int padding = (int)(impl_->rng() & 0x0F);
    size_t total_len = data.size() + padding;
    while (total_len % 4 != 0) {
        padding++;
        total_len = data.size() + padding;
    }

    // Length prefix (4 bytes, LE)
    uint32_t length_prefix = (uint32_t)total_len / 4;
    frame.resize(4);
    std::memcpy(frame.data(), &length_prefix, 4);

    // Payload
    frame.insert(frame.end(), data.begin(), data.end());

    // Padding
    std::vector<uint8_t> pad_buf(padding);
    impl_->generate_random(pad_buf.data(), padding);
    frame.insert(frame.end(), pad_buf.begin(), pad_buf.end());

    // Apply obfuscation (AES-CTR)
    if (impl_->obfuscated && frame.size() > 4) {
        // First 4 bytes (length) are NOT encrypted
        // Rest of packet is encrypted with CTR
        crypto::aes_ctr_encrypt(
            frame.data() + 4, frame.size() - 4,
            impl_->encrypt_key, impl_->encrypt_iv,
            frame.data() + 4);
    }

    int sent = ::send(impl_->sock, (const char*)frame.data(),
                      (int)frame.size(), 0);
    return sent == (int)frame.size();
}

bool Transport::receive_packet(Packet& packet, int timeout_ms) {
    if (!is_connected()) return false;

    // Set timeout
#ifdef _WIN32
    DWORD tv = timeout_ms;
    setsockopt(impl_->sock, SOL_SOCKET, SO_RCVTIMEO,
               (const char*)&tv, sizeof(tv));
#else
    timeval tv{ timeout_ms / 1000, (timeout_ms % 1000) * 1000 };
    setsockopt(impl_->sock, SOL_SOCKET, SO_RCVTIMEO, &tv, sizeof(tv));
#endif

    // Read 4 bytes length prefix
    uint8_t len_buf[4];
    int received = 0;
    while (received < 4) {
        int n = ::recv(impl_->sock, (char*)(len_buf + received),
                       4 - received, 0);
        if (n <= 0) return false;
        received += n;
    }

    uint32_t length = *(uint32_t*)len_buf;
    size_t payload_len = length * 4;
    if (payload_len > 1048576 * 16) return false; // sanity: 16MB max

    // Read the payload
    std::vector<uint8_t> buf(payload_len);
    received = 0;
    while (received < (int)payload_len) {
        int n = ::recv(impl_->sock, (char*)(buf.data() + received),
                       (int)payload_len - received, 0);
        if (n <= 0) return false;
        received += n;
    }

    // Decrypt obfuscation
    if (impl_->obfuscated && buf.size() > 0) {
        crypto::aes_ctr_encrypt(
            buf.data(), buf.size(),
            impl_->decrypt_key, impl_->decrypt_iv,
            buf.data());
    }

    packet.data = std::move(buf);
    packet.length = (int)payload_len;

    return true;
}

} // namespace tdesktop::mtproto
