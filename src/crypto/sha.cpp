#include "tdesktop_mtproto/mtproto.h"
#include <openssl/sha.h>

namespace tdesktop::mtproto::crypto {

void sha1(const uint8_t* data, size_t len, uint8_t out[20]) {
    SHA1(data, len, out);
}

void sha256(const uint8_t* data, size_t len, uint8_t out[32]) {
    SHA256(data, len, out);
}

} // namespace tdesktop::mtproto::crypto
