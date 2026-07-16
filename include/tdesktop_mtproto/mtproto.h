#pragma once
#include <cstdint>
#include <string>
#include <vector>
#include <memory>

namespace tdesktop::mtproto {

// === Configuration ===
struct Config {
    int32_t api_id = 2040;
    std::string api_hash = "b18441a1ff607e10a989891a5462e627";
    std::string device_model = "Desktop PC";
    std::string system_version = "Windows 10";
    std::string app_version = "7.0.1";
    std::string lang_pack = "tdesktop";
    std::string lang_code = "en";
    std::string system_lang_code = "en";
    int32_t dc_id = 2;
};

// === Auth Key ===
struct AuthKey {
    std::vector<uint8_t> key;       // 256 bytes
    std::vector<uint8_t> server_salt; // 8 bytes
    int64_t key_id = 0;             // lower 64 bits of SHA1(key)

    bool valid() const { return key.size() == 256; }
};

// === Message ID (as tdesktop) ===
int64_t generate_msg_id();  // unixtime << 32 without randomization
bool is_even_msg_id(int64_t msg_id);  // client→server must be even
int64_t generate_msg_seqno(int64_t msg_id, bool content);

// === Obfuscated TCP Transport (0xDDDDDDDD) ===
class Transport {
public:
    struct Packet {
        std::vector<uint8_t> data;
        int64_t msg_id = 0;
        int32_t seqno = 0;
        int32_t length = 0;
    };

    Transport();
    ~Transport();

    bool connect(const std::string& ip, int port);
    void disconnect();
    bool is_connected() const;

    // Send/receive MTProto packets with obfuscation
    bool send_packet(const Packet& packet);
    bool receive_packet(Packet& packet, int timeout_ms = 5000);

    // Obfuscation handshake
    bool perform_obfuscation();

private:
    struct Impl;
    std::unique_ptr<Impl> impl_;
};

// === AES-IGE (MTProto encryption) ===
namespace crypto {

void aes_ige_encrypt(const uint8_t* data, size_t len,
                     const uint8_t key[32], const uint8_t iv[32],
                     uint8_t* out);

void aes_ige_decrypt(const uint8_t* data, size_t len,
                     const uint8_t key[32], const uint8_t iv[32],
                     uint8_t* out);

void aes_ctr_encrypt(const uint8_t* data, size_t len,
                     const uint8_t key[32], const uint8_t iv[16],
                     uint8_t* out);

void sha1(const uint8_t* data, size_t len, uint8_t out[20]);
void sha256(const uint8_t* data, size_t len, uint8_t out[32]);

} // namespace crypto

// === TL Serializer ===
class TLSerializer {
public:
    TLSerializer();

    void write_int32(int32_t v);
    void write_int64(int64_t v);
    void write_double(double v);
    void write_string(const std::string& v);
    void write_bytes(const std::vector<uint8_t>& v);
    void write_int128(const uint8_t v[16]);
    void write_int256(const uint8_t v[32]);
    void write_constructor(uint32_t cons);
    void write_bool(bool v);
    template<typename T>
    void write_vector(const std::vector<T>& items, void(*writer)(TLSerializer&, const T&));

    const std::vector<uint8_t>& data() const { return buf_; }
    size_t size() const { return buf_.size(); }
    void clear() { buf_.clear(); }

private:
    void pad_to(int alignment);
    std::vector<uint8_t> buf_;
};

class TLDeserializer {
public:
    TLDeserializer(const uint8_t* data, size_t size);

    int32_t read_int32();
    int64_t read_int64();
    double read_double();
    std::string read_string();
    std::vector<uint8_t> read_bytes();
    void read_int128(uint8_t out[16]);
    void read_int256(uint8_t out[32]);
    uint32_t read_constructor();
    bool read_bool();
    template<typename T>
    std::vector<T> read_vector(T(*reader)(TLDeserializer&));

    size_t remaining() const { return size_ - pos_; }
    bool ok() const { return pos_ <= size_; }

private:
    const uint8_t* data_;
    size_t size_;
    size_t pos_;
};

// === RSA Public Key ===
struct RSAPublicKey {
    RSAPublicKey() = default;
    RSAPublicKey(uint64_t fingerprint);

    std::vector<uint8_t> encrypt(const std::vector<uint8_t>& data) const;
    uint64_t fingerprint() const;
    bool valid() const { return valid_; }

private:
    std::vector<uint8_t> n_;
    std::vector<uint8_t> e_;
    bool valid_ = false;
};

// === MTProto 2.0 KDF ===
void mtproto_kdf(const uint8_t auth_key[256], const uint8_t msg_key[16],
                 uint8_t aes_key[32], uint8_t aes_iv[32],
                 bool is_server);

// === Auth Key Creation (PQ/DH handshake) ===
class AuthKeyCreator {
public:
    AuthKeyCreator();

    // Step 1: Process req_pq response (server sends PQ + fingerprints)
    // Returns the auth key creation request
    std::vector<uint8_t> process_pq(const uint8_t* pq, int pq_len,
                                    const uint64_t* fingerprints, int fp_count);

    // Step 2: Process Server-DH params, finalizes auth key
    bool process_dh_params(const uint8_t* encrypted_answer, int answer_len);

    AuthKey get_auth_key() const { return auth_key_; }

private:
    AuthKey auth_key_;
    uint8_t temp_key_[256]{};
    bool has_temp_key_ = false;
};

// === Session (msg_id, seqno, salt) ===
class Session {
public:
    Session();
    ~Session();

    void set_auth_key(const AuthKey& key);
    void set_salt(int64_t server_salt);
    int64_t next_msg_id();
    int32_t next_seqno(bool content);
    int64_t server_time() const { return server_time_diff_; }

    // Encrypt/decrypt a message
    std::vector<uint8_t> encrypt_message(const std::vector<uint8_t>& plaintext);
    std::vector<uint8_t> decrypt_message(const std::vector<uint8_t>& ciphertext);

private:
    AuthKey auth_key_;
    int64_t last_msg_id_ = 0;
    int32_t seqno_ = 0;
    int64_t server_time_diff_ = 0; // server_time - local_time
};

// === MTProto Client (high-level API) ===
class Client {
public:
    Client(const Config& config);
    ~Client();

    // Connection
    bool connect();
    void disconnect();
    bool is_connected() const;

    // Auth
    bool create_auth_key();  // Full PQ/DH handshake

    // RPC
    std::string call(const std::string& method,
                     const std::string& params_json);
    bool send_message(const std::string& peer,
                      const std::string& message);

private:
    struct Impl;
    std::unique_ptr<Impl> impl_;
};

} // namespace tdesktop::mtproto
