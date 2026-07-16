#pragma once
#include <cstdint>
#include <string>
#include <vector>

namespace desktop_mtproto {

struct Config {
    int32_t api_id = 2040;
    std::string api_hash = "b18441a1ff607e10a989891a5462e627";
    std::string device_model = "Desktop PC";
    std::string system_version = "Windows 10";
    std::string app_version = "7.0.1";
    std::string lang_pack = "tdesktop";
    std::string lang_code = "en";
    std::string system_lang_code = "en";
};

struct DCEndpoint {
    int dc_id;
    const char* ip;
    int port;
};

struct ClientImpl;

class Client {
public:
    Client(const Config& config);
    ~Client();
    bool connect(int dc_id = 2);
    void disconnect();
    bool is_connected() const;
    int32_t api_id() const;
private:
    ClientImpl* impl_;
};

struct TLS {
    std::vector<uint8_t> buf_;
    void write_int32(int32_t v);
    void write_int64(int64_t v);
    void write_double(double v);
    void write_uint32(uint32_t v);
    void write_string(const std::string& v);
    void write_bytes(const uint8_t* data, size_t len);
    void write_int128(const uint8_t* v);
    void write_int256(const uint8_t* v);
    void write_bool(bool v);
    static void align(std::vector<uint8_t>& buf, int a = 4);
    static int32_t read_int32(const uint8_t* data, size_t& pos, size_t size);
    static int64_t read_int64(const uint8_t* data, size_t& pos, size_t size);
    static uint32_t read_uint32(const uint8_t* data, size_t& pos, size_t size);
    static std::vector<uint8_t> read_bytes(const uint8_t* data, size_t& pos, size_t size);
    static std::string read_string(const uint8_t* data, size_t& pos, size_t size);
};

} // namespace desktop_mtproto
