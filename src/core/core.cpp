#include "desktop_mtproto/client.h"
#include <cstring>
#include <thread>
#include <chrono>
#include <random>
#include <ctime>
#include <mutex>
#include <algorithm>
#include <sstream>

#ifdef _WIN32
#include <winsock2.h>
#include <ws2tcpip.h>
#pragma comment(lib, "ws2_32")
#else
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <netdb.h>
#endif

#include <openssl/evp.h>
#include <openssl/rand.h>
#include <openssl/aes.h>
#include <openssl/sha.h>
#include <openssl/bn.h>
#include <openssl/rsa.h>
#include <openssl/err.h>

namespace desktop_mtproto {

// ======== CONSTANTS FROM TDESKTOP ========
constexpr uint32_t kProtoVersionD = 0xDDDDDDDD;
constexpr uint32_t kEncryptedHeader = 0xEFEFEFEF;
constexpr uint32_t kResPQ = 0x05162463;
constexpr uint32_t kReqPQMulti = 0xbe7e8ef1;
constexpr uint32_t kReqDHParams = 0xd712e4be;
constexpr uint32_t kServerDHParamsOk = 0x79cb045d;
constexpr uint32_t kSetClientDHParams = 0xf5045f1f;
constexpr uint32_t kDhGenOk = 0x3bcb7346;
constexpr uint32_t kRpcResult = 0xf35c6d01;
constexpr uint32_t kPing = 0x7abe77ec;
constexpr uint32_t kInvokeWithLayer = 0xda9b0d0d;
constexpr uint32_t kInitConnection = 0xc1cd5ea9;
constexpr uint32_t kJsonObject = 0x99c1d49d;
constexpr uint32_t kJsonNumber = 0x2be0df57;
constexpr uint32_t kTrue = 0x997275b5;
constexpr uint32_t kFalse = 0xbc799737;

const DCEndpoint kDCs[] = {
    {1, "149.154.175.53", 443},
    {2, "149.154.167.51", 443},
    {3, "149.154.175.100", 443},
    {4, "149.154.167.91", 443},
    {5, "149.154.171.5", 443},
};

// RSA key from tdesktop
static const uint8_t kRSA_N[] = {
    0xC1,0x50,0x02,0x3E,0x2F,0x70,0xDB,0x79,0x85,0xDE,0xD0,0x64,0x75,0x9C,0xFE,0xCF,
    0x0A,0xF3,0x28,0xE6,0x9A,0x41,0xDA,0xF4,0xD6,0xF0,0x1B,0x53,0x81,0x35,0xA6,0xF9,
    0x1F,0x8F,0x8B,0x2A,0x0E,0xC9,0xBA,0x97,0x20,0xCE,0x35,0x2E,0xFC,0xF6,0xAD,0x5A,
    0x4D,0xDB,0xCE,0xE9,0x1F,0x51,0x0C,0x2C,0x7E,0xA3,0x2C,0x6E,0x10,0xE9,0xE1,0x22,
    0xBD,0x1D,0x85,0xDA,0xC6,0x95,0xB3,0xB1,0xAD,0xC7,0x0B,0xB6,0xD4,0x69,0xB3,0xE0,
    0xE4,0xBF,0x4D,0xF2,0xEF,0x80,0xD3,0xE5,0xFE,0x5E,0xD1,0xBB,0x0D,0x82,0x3E,0x49,
    0xA3,0xC8,0x5A,0x45,0xAC,0xC2,0xD8,0x65,0xB3,0xDD,0xD0,0x2C,0x3A,0x66,0x95,0xCE,
    0xDA,0x8E,0x76,0xE9,0x35,0x96,0x7D,0xB2,0x7F,0x0D,0x29,0xEC,0x2B,0xA4,0x01,0x90,
    0xE9,0x5C,0xEB,0x5E,0xBE,0x06,0xFD,0xFC,0x9A,0x8E,0x8A,0xF4,0xEF,0x17,0x6E,0x8F,
    0x53,0xB4,0xC6,0x83,0x01,0xD8,0xB0,0xC9,0x1F,0xA5,0xB1,0xC8,0xA1,0xEF,0x1B,0x12,
    0x9B,0xA9,0x0B,0x53,0x86,0xC6,0x1B,0x28,0xA9,0xEC,0xFC,0x97,0x51,0x83,0xBB,0xAA,
    0xC5,0xE6,0x8C,0x3E,0xDF,0xB3,0xA7,0xA6,0xEE,0x23,0xDB,0x4D,0x84,0x3C,0xB1,0x05,
    0xAB,0x3B,0xDD,0xA6,0x93,0xAA,0x1B,0x45,0x07,0x81,0x22,0xDE,0xC1,0x22,0xED,0xB5,
    0x9C,0xE1,0x11,0x1A,0xD8,0x5E,0x17,0xF0,0x3D,0xEF,0x4B,0x78,0xF4,0x05,0x28,0xDA,
    0xC6,0xBC,0xF6,0x12,0xDA,0xC4,0xEE,0xD5,0xD2,0xB4,0x5D,0xB1,0x79,0x54,0x01,0xA5,
    0xEE,0x3D,0xB1,0x53,0x7A,0x62,0xBD,0x2E,0x13,0xB7,0x7A,0x09,0xFE,0xA2,0x10,0xC0,0x5D,0x7D,0x5F
};
constexpr size_t kRSA_N_LEN = sizeof(kRSA_N);
constexpr uint64_t kRSAFingerprint = 0xC3B42B026CE86B21ULL;

// ======== RNG ========
static std::mt19937_64& rng() {
    static std::mt19937_64 r(std::random_device{}());
    return r;
}
static void rand_fill(uint8_t* buf, size_t len) {
    for (size_t i = 0; i < len; i++) buf[i] = (uint8_t)(rng()() & 0xFF);
}

// ======== TL SERIALIZER ========
void TLS::align(std::vector<uint8_t>& buf, int a) {
    while (buf.size() % (size_t)a != 0) buf.push_back(0);
}
void TLS::write_int32(int32_t v) { align(buf_, 4); auto p = (const uint8_t*)&v; buf_.insert(buf_.end(), p, p+4); }
void TLS::write_int64(int64_t v) { align(buf_, 4); auto p = (const uint8_t*)&v; buf_.insert(buf_.end(), p, p+8); }
void TLS::write_double(double v) { align(buf_, 4); auto p = (const uint8_t*)&v; buf_.insert(buf_.end(), p, p+8); }
void TLS::write_uint32(uint32_t v) { write_int32((int32_t)v); }
void TLS::write_bool(bool v) { write_uint32(v ? kTrue : kFalse); }
void TLS::write_int128(const uint8_t* v) { align(buf_, 4); buf_.insert(buf_.end(), v, v+16); }
void TLS::write_int256(const uint8_t* v) { align(buf_, 4); buf_.insert(buf_.end(), v, v+32); }
void TLS::write_bytes(const uint8_t* d, size_t n) { write_string(std::string((const char*)d, n)); }

void TLS::write_string(const std::string& v) {
    if (v.size() <= 253) {
        buf_.push_back((uint8_t)v.size());
        buf_.insert(buf_.end(), v.begin(), v.end());
        while ((1 + buf_.size() + 0) % 4 != 0) buf_.push_back(0);
    } else {
        buf_.push_back(254);
        uint32_t len = (uint32_t)v.size();
        buf_.push_back(len & 0xFF); buf_.push_back((len>>8)&0xFF); buf_.push_back((len>>16)&0xFF);
        buf_.insert(buf_.end(), v.begin(), v.end());
        while ((4 + buf_.size() + 0) % 4 != 0) buf_.push_back(0);
    }
}

int32_t TLS::read_int32(const uint8_t* d, size_t& p, size_t s) { p += 4; return *(const int32_t*)(d+p-4); }
int64_t TLS::read_int64(const uint8_t* d, size_t& p, size_t s) { p += 8; return *(const int64_t*)(d+p-8); }
uint32_t TLS::read_uint32(const uint8_t* d, size_t& p, size_t s) { return (uint32_t)read_int32(d, p, s); }

std::vector<uint8_t> TLS::read_bytes(const uint8_t* d, size_t& p, size_t s) {
    auto str = read_string(d, p, s);
    return std::vector<uint8_t>(str.begin(), str.end());
}

std::string TLS::read_string(const uint8_t* d, size_t& p, size_t s) {
    if (p >= s) return {};
    auto first = d[p++];
    size_t len;
    if (first <= 253) len = first;
    else if (first == 254) {
        len = (size_t)d[p] | ((size_t)d[p+1]<<8) | ((size_t)d[p+2]<<16);
        p += 3;
    } else return {};
    if (p + len > s) return {};
    std::string result((const char*)(d+p), len);
    p += len;
    while (p % 4 != 0) p++;
    return result;
}

// ======== AES-IGE ========
static void aes_ige_crypt(const uint8_t* in, size_t len, const uint8_t key[32],
                           const uint8_t iv[32], uint8_t* out, bool enc) {
    AES_KEY k;
    if (enc) AES_set_encrypt_key(key, 256, &k);
    else AES_set_decrypt_key(key, 256, &k);
    uint8_t x[16], y[16];
    memcpy(x, iv, 16); memcpy(y, iv+16, 16);
    for (size_t i = 0; i < len; i += 16) {
        if (enc) {
            uint8_t b[16];
            for (int j = 0; j < 16; j++) b[j] = in[i+j] ^ y[j];
            AES_encrypt(b, out+i, &k);
            for (int j = 0; j < 16; j++) out[i+j] ^= x[j];
            memcpy(x, out+i, 16); memcpy(y, in+i, 16);
        } else {
            uint8_t b[16];
            for (int j = 0; j < 16; j++) b[j] = in[i+j] ^ x[j];
            AES_decrypt(b, out+i, &k);
            for (int j = 0; j < 16; j++) out[i+j] ^= y[j];
            memcpy(x, in+i, 16); memcpy(y, out+i, 16);
        }
    }
}

// ======== KDF ========
static void mtproto_kdf(const uint8_t ak[256], const uint8_t mk[16],
                         uint8_t ek[32], uint8_t iv[32], bool srv) {
    int x = srv ? 8 : 0;
    uint8_t a[32], b[32], t[48];
    memcpy(t, mk, 16); memcpy(t+16, ak+x, 32); SHA256(t, 48, a);
    memcpy(t, ak+x+32, 32); memcpy(t+32, mk, 16); SHA256(t, 48, b);
    memcpy(ek, a, 8); memcpy(ek+8, b+8, 16); memcpy(ek+24, a+24, 8);
    memcpy(iv, b, 8); memcpy(iv+8, a+8, 16); memcpy(iv+24, b+24, 8);
}

// ======== RSA ========
static std::vector<uint8_t> rsa_enc(const uint8_t* d, size_t n) {
    auto* r = RSA_new();
    auto* bn_n = BN_bin2bn(kRSA_N, (int)kRSA_N_LEN, nullptr);
    auto* bn_e = BN_bin2bn((const uint8_t*)"\x01\x00\x01", 3, nullptr);
    RSA_set0_key(r, bn_n, bn_e, nullptr);
    std::vector<uint8_t> out(256);
    int ret = RSA_public_encrypt((int)n, d, out.data(), r, RSA_PKCS1_PADDING);
    if (ret == -1) { RSA_free(r); return {}; }
    RSA_free(r); out.resize(ret);
    return out;
}

// ======== POLLARD RHO ========
static uint64_t gcd64(uint64_t a, uint64_t b) {
    while (b) { uint64_t t = b; b = a % b; a = t; }
    return a;
}

static uint64_t pollard_rho(uint64_t n) {
    if (n % 2 == 0) return 2;
    std::mt19937_64 rng2(std::random_device{}());
    while (true) {
        uint64_t c = (rng2() % (n - 1)) + 1;
        uint64_t x = rng2() % n, y = x, d = 1;
        auto f = [=](uint64_t x) { return (x * x + c) % n; };
        while (d == 1) {
            x = f(x);
            y = f(f(y));
            // Safe subtraction (handles overflow)
            uint64_t diff = (x > y) ? (x - y) : (y - x);
            d = gcd64(diff, n);
        }
        if (d != n) return d;
    }
}

// ======== TCP TRANSPORT ========
struct TcpTransport {
    SOCKET s = INVALID_SOCKET;
    uint8_t ek[32], eiv[16], dk[32], div[16];

    bool conn(const char* ip, int port) {
        s = ::socket(AF_INET, SOCK_STREAM, 0);
        if (s == INVALID_SOCKET) return false;
        sockaddr_in a = {}; a.sin_family = AF_INET;
        a.sin_port = htons(port);
        inet_pton(AF_INET, ip, &a.sin_addr);
        return ::connect(s, (sockaddr*)&a, sizeof(a)) != SOCKET_ERROR;
    }
    void disc() { if (s != INVALID_SOCKET) { closesocket(s); s = INVALID_SOCKET; } }
    bool send_all(const uint8_t* d, int n) {
        while (n > 0) { int r = ::send(s, (const char*)d, n, 0); if (r<=0) return false; d+=r; n-=r; }
        return true;
    }
    bool recv_all(uint8_t* d, int n) {
        while (n > 0) { int r = ::recv(s, (char*)d, n, 0); if (r<=0) return false; d+=r; n-=r; }
        return true;
    }
    bool obfuscate() {
        uint8_t h[64]; rand_fill(h, 64);
        *(uint32_t*)(h+56) = kProtoVersionD; *(uint32_t*)(h+60) = kEncryptedHeader;
        memcpy(ek, h, 32); memcpy(eiv, h+32, 16);
        memcpy(dk, h+32, 16); memcpy(dk+16, h+48, 16); memcpy(div, h+16, 16);
        if (!send_all(h, 64)) return false;
        uint8_t r[64]; if (!recv_all(r, 64)) return false;
        return *(uint32_t*)(r+60) == kEncryptedHeader;
    }
    bool send_packet(const std::vector<uint8_t>& data) {
        int pad = (int)(rng()() & 0x0F);
        size_t total = data.size() + pad;
        while (total % 4) { pad++; total = data.size() + pad; }
        auto len = (uint32_t)(total / 4);
        if (!send_all((const uint8_t*)&len, 4)) return false;
        std::vector<uint8_t> pld(total);
        memcpy(pld.data(), data.data(), data.size());
        if ((size_t)pad > pld.size() - data.size()) return false;
        rand_fill(pld.data() + data.size(), pad);
        EVP_CIPHER_CTX* ctx = EVP_CIPHER_CTX_new();
        EVP_EncryptInit_ex(ctx, EVP_aes_256_ctr(), 0, ek, eiv);
        int o = 0; EVP_EncryptUpdate(ctx, pld.data(), &o, pld.data(), (int)total);
        EVP_CIPHER_CTX_free(ctx);
        return send_all(pld.data(), (int)total);
    }
    bool recv_packet(std::vector<uint8_t>& out) {
        uint8_t lb[4]; if (!recv_all(lb, 4)) return false;
        uint32_t l = *(uint32_t*)lb;
        size_t pl = l * 4; if (pl > 1024*1024) return false;
        out.resize(pl);
        if (!recv_all(out.data(), (int)pl)) return false;
        EVP_CIPHER_CTX* ctx = EVP_CIPHER_CTX_new();
        EVP_DecryptInit_ex(ctx, EVP_aes_256_ctr(), 0, dk, div);
        int o = 0; EVP_DecryptUpdate(ctx, out.data(), &o, out.data(), (int)pl);
        EVP_CIPHER_CTX_free(ctx);
        return true;
    }
};

// ======== CLIENT IMPL ========
struct ClientImpl {
    TcpTransport tr;
    uint8_t ak[256] = {};
    int64_t akid = 0, slt = 0, lmid = 0;
    int sqn = 0;
    Config cfg;

    ClientImpl(const Config& c) : cfg(c) {}

    int64_t nid() {
        auto id = (int64_t)((uint64_t)std::time(nullptr) << 32);
        if (id <= lmid) id = lmid + 4;
        id &= ~3LL; lmid = id;
        return id;
    }
    int32_t nsqn(bool c) { if (c) return sqn++ * 2 + 1; return sqn * 2; }

    // Unencrypted RPC (for auth key creation)
    std::vector<uint8_t> unrpc(int64_t mid, const std::vector<uint8_t>& body) {
        TLS t; t.write_int64(0); t.write_int64(mid); t.write_bytes(body.data(), body.size());
        tr.send_packet(t.buf_);
        std::vector<uint8_t> r; return tr.recv_packet(r) ? r : std::vector<uint8_t>{};
    }

    // Encrypted RPC
    std::vector<uint8_t> encrpc(const std::vector<uint8_t>& body) {
        auto mid = nid();
        auto s = nsqn(true);
        TLS t;
        t.write_int64(slt); t.write_int64(0); t.write_int64(mid);
        t.write_int32(s); t.write_int32((int32_t)body.size());
        t.buf_.insert(t.buf_.end(), body.begin(), body.end());
        while (t.buf_.size() % 16) t.buf_.push_back(0);
        uint8_t mk[16], sha[20];
        SHA1(t.buf_.data(), t.buf_.size(), sha);
        memcpy(mk, sha+4, 16);
        uint8_t ek[32], iv[32];
        mtproto_kdf(ak, mk, ek, iv, false);
        std::vector<uint8_t> enc(t.buf_.size());
        aes_ige_crypt(t.buf_.data(), t.buf_.size(), ek, iv, enc.data(), true);
        TLS p; p.write_int64(akid); p.write_bytes(mk, 16);
        p.buf_.insert(p.buf_.end(), enc.begin(), enc.end());
        tr.send_packet(p.buf_);
        std::vector<uint8_t> rr; if (!tr.recv_packet(rr)) return {};
        if (rr.size() < 24) return {};
        auto* rmk = rr.data()+8; auto* renc = rr.data()+24;
        size_t rlen = rr.size()-24;
        uint8_t rk[32], rv[32];
        mtproto_kdf(ak, rmk, rk, rv, true);
        std::vector<uint8_t> dec(rlen);
        aes_ige_crypt(renc, rlen, rk, rv, dec.data(), false);
        size_t pos = 0;
        TLS::read_int64(dec.data(), pos, dec.size()); // salt
        TLS::read_int64(dec.data(), pos, dec.size()); // session
        TLS::read_int64(dec.data(), pos, dec.size()); // msg_id
        TLS::read_int32(dec.data(), pos, dec.size()); // seqno
        int bl = TLS::read_int32(dec.data(), pos, dec.size());
        if (bl < 0 || (size_t)bl > dec.size()-pos) return {};
        std::vector<uint8_t> b(dec.begin()+pos, dec.begin()+pos+bl);
        size_t bp = 0;
        auto cons = TLS::read_uint32(b.data(), bp, b.size());
        if (cons == kRpcResult) {
            TLS::read_int64(b.data(), bp, b.size());
            return std::vector<uint8_t>(b.begin()+bp, b.end());
        }
        return b;
    }
};

// ======== PUBLIC API ========
Client::Client(const Config& c) : impl_(new ClientImpl(c)) {}
Client::~Client() { delete impl_; }

bool Client::connect(int dc) {
    const DCEndpoint* ep = nullptr;
    for (auto& d : kDCs) { if (d.dc_id == dc) { ep = &d; break; } }
    if (!ep) return false;
    WSADATA w; WSAStartup(MAKEWORD(2,2), &w);
    if (!impl_->tr.conn(ep->ip, ep->port)) return false;
    if (!impl_->tr.obfuscate()) { disconnect(); return false; }
    // Auth key creation
    TLS r; r.write_uint32(kReqPQMulti);
    auto resp = impl_->unrpc(impl_->nid(), r.buf_);
    if (resp.empty()) { disconnect(); return false; }
    return true;
}

void Client::disconnect() { impl_->tr.disc(); }
bool Client::is_connected() const { return impl_->tr.s != INVALID_SOCKET; }
int32_t Client::api_id() const { return impl_->cfg.api_id; }

// ======== C API (for Python ctypes) ========
extern "C" {
    __declspec(dllexport) void* mtproto_create(
        int api_id, const char* api_hash,
        const char* device, const char* system_ver,
        const char* app_ver, const char* lang_pack,
        const char* lang_code, const char* sys_lang) {
        Config cfg;
        cfg.api_id = api_id;
        cfg.api_hash = api_hash ? api_hash : "";
        cfg.device_model = device ? device : "Desktop PC";
        cfg.system_version = system_ver ? system_ver : "Windows 10";
        cfg.app_version = app_ver ? app_ver : "7.0.1";
        cfg.lang_pack = lang_pack ? lang_pack : "tdesktop";
        cfg.lang_code = lang_code ? lang_code : "en";
        cfg.system_lang_code = sys_lang ? sys_lang : "en";
        return new Client(cfg);
    }
    
    __declspec(dllexport) int mtproto_connect(void* client, int dc_id) {
        return ((Client*)client)->connect(dc_id) ? 1 : 0;
    }
    
    __declspec(dllexport) void mtproto_destroy(void* client) {
        delete (Client*)client;
    }
    
    __declspec(dllexport) int mtproto_api_id(void* client) {
        return ((Client*)client)->api_id();
    }
    
    __declspec(dllexport) const char* mtproto_version() {
        return "0.1.0";
    }
}

} // namespace desktop_mtproto
