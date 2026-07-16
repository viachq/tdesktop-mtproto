#include "tdesktop_mtproto/mtproto.h"
#include <openssl/evp.h>
#include <openssl/sha.h>
#include <cstring>
#include <stdexcept>

namespace tdesktop::mtproto::crypto {

// AES-IGE: MTProto uses this for message encryption
// AES-IGE is not standard in OpenSSL < 3.2, so we implement it manually

extern "C" {
#include <openssl/aes.h>
}

static void aes_ige_internal(const uint8_t* data, size_t len,
                              const uint8_t key[32], const uint8_t iv[32],
                              uint8_t* out, int enc) {
    if (len % 16 != 0) {
        throw std::runtime_error("AES-IGE: data length must be multiple of 16");
    }

    AES_KEY aes_key;
    if (enc) {
        AES_set_encrypt_key(key, 256, &aes_key);
    } else {
        AES_set_decrypt_key(key, 256, &aes_key);
    }

    // IGE mode: XOR with previous ciphertext (enc) or previous plaintext (dec)
    uint8_t x[16], y[16];
    std::memcpy(x, iv, 16);        // iv[0..15] = previous ciphertext
    std::memcpy(y, iv + 16, 16);   // iv[16..31] = previous plaintext

    for (size_t i = 0; i < len; i += 16) {
        if (enc) {
            // out = AES(key, plain XOR y) XOR x
            uint8_t block[16];
            for (int j = 0; j < 16; j++) block[j] = data[i + j] ^ y[j];
            AES_encrypt(block, out + i, &aes_key);
            for (int j = 0; j < 16; j++) out[i + j] ^= x[j];
            std::memcpy(x, out + i, 16);  // x = cipher
            std::memcpy(y, data + i, 16); // y = plain
        } else {
            // out = AES(key, cipher XOR x) XOR y
            uint8_t block[16];
            for (int j = 0; j < 16; j++) block[j] = data[i + j] ^ x[j];
            AES_decrypt(block, out + i, &aes_key);
            for (int j = 0; j < 16; j++) out[i + j] ^= y[j];
            std::memcpy(x, data + i, 16); // x = cipher
            std::memcpy(y, out + i, 16);  // y = plain
        }
    }
}

void aes_ige_encrypt(const uint8_t* data, size_t len,
                      const uint8_t key[32], const uint8_t iv[32],
                      uint8_t* out) {
    aes_ige_internal(data, len, key, iv, out, 1);
}

void aes_ige_decrypt(const uint8_t* data, size_t len,
                      const uint8_t key[32], const uint8_t iv[32],
                      uint8_t* out) {
    aes_ige_internal(data, len, key, iv, out, 0);
}

// AES-CTR: used for TCP obfuscation
void aes_ctr_encrypt(const uint8_t* data, size_t len,
                      const uint8_t key[32], const uint8_t iv[16],
                      uint8_t* out) {
    EVP_CIPHER_CTX* ctx = EVP_CIPHER_CTX_new();
    if (!ctx) throw std::runtime_error("AES-CTR: failed to create context");

    EVP_CIPHER_CTX_init(ctx);
    EVP_EncryptInit_ex(ctx, EVP_aes_256_ctr(), nullptr, key, iv);

    int outlen = 0;
    if (EVP_EncryptUpdate(ctx, out, &outlen, data, (int)len) != 1) {
        EVP_CIPHER_CTX_free(ctx);
        throw std::runtime_error("AES-CTR: encryption failed");
    }

    EVP_CIPHER_CTX_free(ctx);
}

} // namespace tdesktop::mtproto::crypto
