#include "tdesktop_mtproto/mtproto.h"
#include <cstring>
#include <cassert>
#include <stdexcept>
#include <openssl/bn.h>
#include <openssl/rsa.h>
#include <openssl/pem.h>
#include <openssl/bio.h>
#include <openssl/err.h>

using namespace tdesktop::mtproto;
using namespace tdesktop::mtproto::crypto;

// Telegram's RSA public keys (from tdesktop)
// These are the production keys used for auth key creation
struct RSAKey {
    const char* modulus_hex;  // N
    const char* exponent_hex; // E (usually 010001 = 65537)
    const char* fingerprint;  // Lower 64 bits of SHA1(N + E) as hex
};

// Telegram's main production RSA public key
// From tdesktop: Telegram/SourceFiles/mtproto/details/mtproto_rsa_public_key.cpp
static const RSAKey kKnownKeys[] = {
    {
        // Production key 1 (primary)
        "c150023e2f70db7985ded064759cfecf0af328e69a41daf4d6f01b538135a6f91f8f8b2a0ec9ba9720ce352efcf6ad5a4ddbcee91f510c2c7ea32c6e10e9e122b"
        "d1d85dac695b3b1adc70bb6d469b3e0e4bf4df2ef80d3e5fe5ed1bb0d823e49a3c85a45acc2d865b3ddd02c3a6695ceda8e76e935967dbd27f0d29ec2ba40190e9"
        "5ceb5ebe06fdfc9a8e8af4ef176e8f53b4c68301d8b0c91fa5b1c8a1ef1b129ba90b5386c61b28a9ecfc975183bbaac5e68c3edfb3a7a6ee23db4d843cb105ab3b"
        "dda693aa1b45078122dec122edb59ce1111ad85e17f03def4b78f40528dac6bcf612dac4eed5d2b45db1795401a5ee3db1537a62bd2e13b77a09fea210c05d7d5f",
        "010001",
        "c3b42b026ce86b21"
    },
    {
        // Production key 2 (backup)
        "bd8e6bcc6a6bedf89a5b889b1cad1512296b7f2e2c1d15fcdc2b41c0765686bad7b0026d8f0cb1fb7e70b7364cd3e518e58c04999fdcd8274a0f689d029bb08e"
        "064dfb3355d0bec0db1f580ab7f0131efc5db8cbf06d5e1bb0ae468a80b7a98e9c28a99f2db91b9f4e4d07eb469919b621bc89b9c834f3ca206a98ffdb7bc3f437"
        "7c13b12c1d1f90bade5d20aeb561bd60770ffa3b3664705b20f81eff4e71c53ce7d101fa9850202f0a1f2b66b0d9e413a1e6f8bf445e586b80b4106356cf83d210"
        "ac7e43aef9d1f54a0b67ed7e45e186f7a7b4d2b95f1b2b6fbab9f7b5f9c7c1c71c5a80a3c07d3565c9702a5c049e54c80f4f6f5b28b2a44309ca3e1ff1217b25",
        "010001",
        "9a996a1ba11b74b2"
    }
};

// Given a fingerprint, find and return the matching RSA public key
RSAPublicKey::RSAPublicKey(uint64_t fingerprint) {
    for (const auto& k : kKnownKeys) {
        uint64_t fp;
        sscanf(k.fingerprint, "%llx", &fp);
        if (fp == fingerprint) {
            // Convert hex to binary
            auto hex_to_bin = [](const char* hex) -> std::vector<uint8_t> {
                size_t len = strlen(hex);
                std::vector<uint8_t> bin(len / 2);
                for (size_t i = 0; i < len / 2; i++) {
                    char byte[3] = {hex[i*2], hex[i*2+1], 0};
                    bin[i] = (uint8_t)strtol(byte, nullptr, 16);
                }
                return bin;
            };
            n_ = hex_to_bin(k.modulus_hex);
            e_ = hex_to_bin(k.exponent_hex);
            valid_ = true;
            return;
        }
    }
    valid_ = false;
}

// RSA encrypt with Telegram's variant:
// Encrypts the data using RSA with PKCS#1 v1.5 padding
// Returns the encrypted data (256 bytes for 2048-bit key)
std::vector<uint8_t> RSAPublicKey::encrypt(const std::vector<uint8_t>& data) const {
    if (!valid_) throw std::runtime_error("RSA: invalid key");

    // Convert hex modulus to BIGNUM
    BIGNUM* n = BN_new();
    BIGNUM* e = BN_new();
    BN_bin2bn(n_.data(), (int)n_.size(), n);
    BN_bin2bn(e_.data(), (int)e_.size(), e);

    // Create RSA key
    RSA* rsa = RSA_new();
    RSA_set0_key(rsa, n, e, nullptr);  // Takes ownership

    // Encrypt
    std::vector<uint8_t> result(256);
    int ret = RSA_public_encrypt(
        (int)data.size(), data.data(),
        result.data(), rsa, RSA_PKCS1_PADDING);

    // Don't free n, e (RSA owns them now)
    RSA_free(rsa);

    if (ret == -1) {
        char err_buf[256];
        ERR_error_string_n(ERR_get_error(), err_buf, sizeof(err_buf));
        throw std::runtime_error(std::string("RSA encrypt failed: ") + err_buf);
    }

    result.resize(ret);
    return result;
}

uint64_t RSAPublicKey::fingerprint() const {
    // SHA1 of DER-encoded N + E, take lower 64 bits
    // N and E are TL-serialized as bytes
    TLSerializer ser;
    ser.write_bytes(n_);
    ser.write_bytes(e_);
    uint8_t hash[20];
    sha1(ser.data().data(), ser.size(), hash);
    uint64_t fp;
    std::memcpy(&fp, hash + (20 - 8), 8);
    return fp;
}

// PQ factorization for Diffie-Hellman key exchange
// Telegram uses a specific PQ factorization algorithm
// The server sends a PQ (product of two primes) and the client
// must factor it to prove it's a real client
struct PQResult {
    std::vector<uint8_t> p;
    std::vector<uint8_t> q;
};

// Simple Pollard's Rho for factorization of small numbers
// In real MTProto, PQ is up to 2^64 - this is for demonstration
// tdesktop uses a more sophisticated algorithm (pollard_rho in mtproto_dh_utils.cpp)
static PQResult factorize_pq(uint64_t pq) {
    PQResult result;
    
    // Simple trial division for first test
    // Real implementation needs Pollard's Rho for large factors
    uint64_t p = 2;
    while (p * p <= pq) {
        if (pq % p == 0) {
            break;
        }
        p++;
    }
    
    if (p * p > pq) {
        throw std::runtime_error("PQ factorization failed");
    }
    
    uint64_t q = pq / p;
    if (p > q) std::swap(p, q);
    
    // Store as byte arrays (little-endian)
    result.p.resize(8);
    result.q.resize(8);
    std::memcpy(result.p.data(), &p, 8);
    std::memcpy(result.q.data(), &q, 8);
    
    // Trim leading zeros
    while (!result.p.empty() && result.p.back() == 0) result.p.pop_back();
    while (!result.q.empty() && result.q.back() == 0) result.q.pop_back();
    
    return result;
}

// MTProto 2.0 Key Derivation Function
// Used to generate encryption keys from auth key and message key
void mtproto_kdf(const uint8_t auth_key[256], const uint8_t msg_key[16],
                 uint8_t aes_key[32], uint8_t aes_iv[32],
                 bool is_server) {
    // MTProto 2.0 KDF:
    // sha256_a = SHA256(msg_key + (is_server ? auth_key[X:Y] : auth_key[X:Y]))
    // sha256_b = SHA256(auth_key[X:Y] + msg_key)
    // aes_key = sha256_a[0:8] + sha256_b[8:24] + sha256_a[24:32]
    // aes_iv  = sha256_b[0:8] + sha256_a[8:24] + sha256_b[24:32]
    
    // For client (is_server=false):
    // sha256_a = SHA256(msg_key + auth_key[0:32])
    // sha256_b = SHA256(auth_key[32:64] + msg_key)
    
    // For server (is_server=true): swapped
    int offset_a = is_server ? (256 - 32) : 0;
    int offset_b = is_server ? (256 - 64) : 32;
    
    uint8_t sha256_a_buf[32], sha256_b_buf[32];
    
    // sha256_a = SHA256(msg_key + auth_key[offset_a:offset_a+32])
    std::vector<uint8_t> input_a(16 + 32);
    std::memcpy(input_a.data(), msg_key, 16);
    std::memcpy(input_a.data() + 16, auth_key + offset_a, 32);
    sha256(input_a.data(), input_a.size(), sha256_a_buf);
    
    // sha256_b = SHA256(auth_key[offset_b:offset_b+32] + msg_key)
    std::vector<uint8_t> input_b(32 + 16);
    std::memcpy(input_b.data(), auth_key + offset_b, 32);
    std::memcpy(input_b.data() + 32, msg_key, 16);
    sha256(input_b.data(), input_b.size(), sha256_b_buf);
    
    // aes_key = sha256_a[0:8] + sha256_b[8:24] + sha256_a[24:32]
    std::memcpy(aes_key, sha256_a_buf, 8);
    std::memcpy(aes_key + 8, sha256_b_buf + 8, 16);
    std::memcpy(aes_key + 24, sha256_a_buf + 24, 8);
    
    // aes_iv = sha256_b[0:8] + sha256_a[8:24] + sha256_b[24:32]
    std::memcpy(aes_iv, sha256_b_buf, 8);
    std::memcpy(aes_iv + 8, sha256_a_buf + 8, 16);
    std::memcpy(aes_iv + 24, sha256_b_buf + 24, 8);
}


