#include "tdesktop_mtproto/mtproto.h"
#include <cstdio>
#include <cstring>
#include <cassert>

using namespace tdesktop::mtproto;

int main() {
    // Test 1: msg_id generation
    printf("[TEST] msg_id generation...\n");
    int64_t id1 = generate_msg_id();
    int64_t id2 = generate_msg_id();
    assert(is_even_msg_id(id1));
    assert(is_even_msg_id(id2));
    assert(id2 >= id1);  // monotonic
    printf("  PASS: id1=%llx id2=%llx\n", id1, id2);

    // Test 2: TL serializer
    printf("[TEST] TL serializer...\n");
    TLSerializer ser;
    ser.write_int32(42);
    ser.write_int64(0xDEADBEEF);
    ser.write_string("hello");
    assert(ser.size() > 0);
    printf("  PASS: %zu bytes\n", ser.size());

    // Test 3: TL deserializer
    printf("[TEST] TL deserializer...\n");
    TLDeserializer deser(ser.data().data(), ser.size());
    int32_t v32 = deser.read_int32();
    int64_t v64 = deser.read_int64();
    std::string str = deser.read_string();
    assert(v32 == 42);
    assert(v64 == 0xDEADBEEF);
    assert(str == "hello");
    printf("  PASS: int32=%d int64=%llx string=%s\n", v32, v64, str.c_str());

    // Test 4: SHA1
    printf("[TEST] SHA1...\n");
    uint8_t sha1_out[20];
    crypto::sha1((const uint8_t*)"test", 4, sha1_out);
    printf("  SHA1: ");
    for (int i = 0; i < 20; i++) printf("%02x", sha1_out[i]);
    printf("\n");

    // Test 5: AES-IGE roundtrip
    printf("[TEST] AES-IGE...\n");
    uint8_t key[32], iv[32], data[32], out[32], dec[32];
    memset(key, 0x42, 32);
    memset(iv, 0x24, 32);
    memset(data, 0xAA, 32);
    crypto::aes_ige_encrypt(data, 32, key, iv, out);
    crypto::aes_ige_decrypt(out, 32, key, iv, dec);
    assert(memcmp(data, dec, 32) == 0);
    printf("  PASS: AES-IGE roundtrip OK\n");

    printf("\nAll tests passed!\n");
    return 0;
}
