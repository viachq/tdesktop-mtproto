#include "tdesktop_mtproto/mtproto.h"
#include <cstring>
#include <vector>

namespace tdesktop::mtproto {

// Build initConnection wrapper as tdesktop does
// MTProto constructor numbers (from TL schema)
constexpr uint32_t kInvokeWithLayer = 0xda9b0d0d;
constexpr uint32_t kInitConnection = 0xc1cd5ea9;
constexpr uint32_t kJsonObject = 0x99c1d49d;
constexpr uint32_t kJsonString = 0xb71e767a;
constexpr uint32_t kJsonNumber = 0x2be0df57;

// Layer version (tdesktop uses current layer)
constexpr int32_t kLayerVersion = 177;

// Build a complete initConnection wrapper as tdesktop does:
// invokeWithLayer<177>(
//   initConnection<{
//     api_id=2040,
//     device_model="Desktop PC",
//     system_version="Windows 10",
//     app_version="7.0.1",
//     lang_pack="tdesktop",
//     system_lang_code="en",
//     lang_code="en",
//     params={tz_offset=10800}
//   }>(... inner_query ...)
// )
std::vector<uint8_t> build_init_connection(
    const Config& config,
    const std::vector<uint8_t>& inner_query) {

    TLSerializer ser;

    // === invokeWithLayer (0xda9b0d0d) ===
    ser.write_constructor(kInvokeWithLayer);
    ser.write_int32(kLayerVersion);

    // === initConnection (0xc1cd5ea9) ===
    ser.write_constructor(kInitConnection);

    // Flags: bit 0 = proxy, bit 1 = params
    uint32_t flags = 0;
    // We always send params (tz_offset)
    flags |= (1 << 1);
    // No proxy by default

    ser.write_int32(flags);
    ser.write_int32(config.api_id);
    ser.write_string(config.device_model);
    ser.write_string(config.system_version);
    ser.write_string(config.app_version);
    ser.write_string(config.system_lang_code);
    ser.write_string(config.lang_pack);
    ser.write_string(config.lang_code);
    // No proxy field (flag bit 0 = 0)
    ser.write_constructor(kJsonObject);
    {
        // params map (flag bit 1 = 1)
        // tz_offset: JSON number
        ser.write_string("tz_offset");
        // 10800 = UTC+3 (Kiev). In real tdesktop this is computed
        int32_t tz_offset = 10800;
        ser.write_constructor(kJsonNumber);
        ser.write_double((double)tz_offset);
    }

    // Append the inner query (e.g., help.getConfig)
    ser.write_bytes(inner_query);

    return ser.data();
}

} // namespace tdesktop::mtproto
