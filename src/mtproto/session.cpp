#include "tdesktop_mtproto/mtproto.h"
#include <cstring>
#include <stdexcept>
#include <algorithm>

namespace tdesktop::mtproto {

Session::Session() {}

Session::~Session() {}

void Session::set_auth_key(const AuthKey& key) {
    auth_key_ = key;
}

void Session::set_salt(int64_t server_salt) {
    auth_key_.server_salt.resize(8);
    std::memcpy(auth_key_.server_salt.data(), &server_salt, 8);
}

int64_t Session::next_msg_id() {
    // Generate as tdesktop: time(nullptr) << 32
    int64_t id = generate_msg_id();

    // Enforce monotonicity: if same-second, increment
    if (id <= last_msg_id_) {
        id = last_msg_id_ + 4;  // tdesktop: ensures strictly increasing
    }

    // Ensure divisible by 4 (client→server)
    id &= ~((int64_t)3);

    last_msg_id_ = id;
    return id;
}

int32_t Session::next_seqno(bool content) {
    if (content) {
        return seqno_++ * 2 + 1;
    }
    return seqno_ * 2;
}

// MTProto 2.0 message encryption
// Structure: auth_key_id (8) + msg_key (16) + encrypted_data (N)
// msg_key = SHA1(plaintext)[4:20] — lower 16 bytes
// encrypted_data = AES-IGE(plaintext + padding)
std::vector<uint8_t> Session::encrypt_message(
    const std::vector<uint8_t>& plaintext) {
    if (!auth_key_.valid()) {
        throw std::runtime_error("Session: no auth key");
    }

    // 1. Compute msg_key = SHA1(plaintext)[4:20] (middle 16 bytes)
    uint8_t sha1_hash[20];
    crypto::sha1(plaintext.data(), plaintext.size(), sha1_hash);
    uint8_t msg_key[16];
    std::memcpy(msg_key, sha1_hash + 4, 16);

    // 2. Derive AES key/iv from auth_key and msg_key (MTProto 2.0 KDF)
    uint8_t aes_key[32], aes_iv[32];
    mtproto_kdf(auth_key_.key.data(), msg_key,
                        aes_key, aes_iv, false);

    // 3. Pad plaintext to 16-byte boundary
    size_t pad_len = plaintext.size();
    size_t padded = ((pad_len + 15) / 16) * 16;
    // Add random padding of 0-15 bytes (like tdesktop)
    std::vector<uint8_t> padded_data(padded, 0);
    std::memcpy(padded_data.data(), plaintext.data(), plaintext.size());

    // 4. Encrypt with AES-IGE
    std::vector<uint8_t> encrypted(padded);
    crypto::aes_ige_encrypt(padded_data.data(), padded,
                            aes_key, aes_iv, encrypted.data());

    // 5. Build final message: auth_key_id (8) + msg_key (16) + encrypted
    std::vector<uint8_t> result(8 + 16 + padded);
    std::memcpy(result.data(), &auth_key_.key_id, 8);
    std::memcpy(result.data() + 8, msg_key, 16);
    std::memcpy(result.data() + 24, encrypted.data(), padded);

    return result;
}

std::vector<uint8_t> Session::decrypt_message(
    const std::vector<uint8_t>& ciphertext) {
    if (!auth_key_.valid()) {
        throw std::runtime_error("Session: no auth key");
    }
    if (ciphertext.size() < 24) {
        throw std::runtime_error("Session: ciphertext too short");
    }

    // Extract msg_key and encrypted data
    const uint8_t* msg_key = ciphertext.data() + 8;
    const uint8_t* encrypted = ciphertext.data() + 24;
    size_t encrypted_len = ciphertext.size() - 24;

    // Derive AES key/iv (server side)
    uint8_t aes_key[32], aes_iv[32];
    mtproto_kdf(auth_key_.key.data(), msg_key,
                        aes_key, aes_iv, true);

    // Decrypt
    std::vector<uint8_t> decrypted(encrypted_len);
    crypto::aes_ige_decrypt(encrypted, encrypted_len,
                            aes_key, aes_iv, decrypted.data());

    return decrypted;
}

} // namespace tdesktop::mtproto
