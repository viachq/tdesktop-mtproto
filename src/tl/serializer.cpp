#include "tdesktop_mtproto/mtproto.h"
#include <cstring>
#include <stdexcept>
#include <algorithm>

namespace tdesktop::mtproto {

TLSerializer::TLSerializer() {
    buf_.reserve(256);
}

void TLSerializer::pad_to(int alignment) {
    // TL serialization aligns to 4 bytes
    while (buf_.size() % (size_t)alignment != 0) {
        buf_.push_back(0);
    }
}

void TLSerializer::write_int32(int32_t v) {
    pad_to(4);
    uint8_t bytes[4];
    std::memcpy(bytes, &v, 4);
    buf_.insert(buf_.end(), bytes, bytes + 4);
}

void TLSerializer::write_int64(int64_t v) {
    pad_to(4);
    uint8_t bytes[8];
    std::memcpy(bytes, &v, 8);
    buf_.insert(buf_.end(), bytes, bytes + 8);
}

void TLSerializer::write_double(double v) {
    pad_to(4);
    uint8_t bytes[8];
    std::memcpy(bytes, &v, 8);
    buf_.insert(buf_.end(), bytes, bytes + 8);
}

void TLSerializer::write_string(const std::string& v) {
    // TL string serialization:
    // If len <= 253: 1 byte len, data, pad to 4
    // If len >= 254: 0xFE + 3 bytes len (LE), data, pad to 4
    size_t len = v.size();
    if (len <= 253) {
        buf_.push_back((uint8_t)len);
        buf_.insert(buf_.end(), v.begin(), v.end());
        // Pad to 4: (1 + len) must be divisible by 4
        size_t total = 1 + len;
        while (total % 4 != 0) {
            buf_.push_back(0);
            total++;
        }
    } else {
        buf_.push_back(0xFE);
        uint8_t len_bytes[3];
        std::memcpy(len_bytes, &len, 3);
        buf_.insert(buf_.end(), len_bytes, len_bytes + 3);
        buf_.insert(buf_.end(), v.begin(), v.end());
        // Pad to 4: (4 + len) must be divisible by 4
        size_t total = 4 + len;
        while (total % 4 != 0) {
            buf_.push_back(0);
            total++;
        }
    }
}

void TLSerializer::write_bytes(const std::vector<uint8_t>& v) {
    // Same as string but raw bytes
    size_t len = v.size();
    if (len <= 253) {
        buf_.push_back((uint8_t)len);
        buf_.insert(buf_.end(), v.begin(), v.end());
        size_t total = 1 + len;
        while (total % 4 != 0) { buf_.push_back(0); total++; }
    } else {
        buf_.push_back(0xFE);
        uint8_t len_bytes[3];
        std::memcpy(len_bytes, &len, 3);
        buf_.insert(buf_.end(), len_bytes, len_bytes + 3);
        buf_.insert(buf_.end(), v.begin(), v.end());
        size_t total = 4 + len;
        while (total % 4 != 0) { buf_.push_back(0); total++; }
    }
}

void TLSerializer::write_int128(const uint8_t v[16]) {
    pad_to(4);
    buf_.insert(buf_.end(), v, v + 16);
}

void TLSerializer::write_int256(const uint8_t v[32]) {
    pad_to(4);
    buf_.insert(buf_.end(), v, v + 32);
}

void TLSerializer::write_constructor(uint32_t cons) {
    write_int32((int32_t)cons);
}

void TLSerializer::write_bool(bool v) {
    // In MTProto bool is either 0x997275b5 (true) or 0xbc799737 (false)
    write_constructor(v ? 0x997275b5U : 0xbc799737U);
}

// === TLDeserializer ===

TLDeserializer::TLDeserializer(const uint8_t* data, size_t size)
    : data_(data), size_(size), pos_(0) {}

int32_t TLDeserializer::read_int32() {
    if (pos_ + 4 > size_) throw std::runtime_error("TL: int32 overflow");
    int32_t v;
    std::memcpy(&v, data_ + pos_, 4);
    pos_ += 4;
    return v;
}

int64_t TLDeserializer::read_int64() {
    if (pos_ + 8 > size_) throw std::runtime_error("TL: int64 overflow");
    int64_t v;
    std::memcpy(&v, data_ + pos_, 8);
    pos_ += 8;
    return v;
}

double TLDeserializer::read_double() {
    if (pos_ + 8 > size_) throw std::runtime_error("TL: double overflow");
    double v;
    std::memcpy(&v, data_ + pos_, 8);
    pos_ += 8;
    return v;
}

std::string TLDeserializer::read_string() {
    if (pos_ >= size_) throw std::runtime_error("TL: string overflow");
    uint8_t first = data_[pos_];
    size_t len;
    if (first <= 253) {
        len = first;
        pos_ += 1;
    } else if (first == 254) {
        if (pos_ + 4 > size_) throw std::runtime_error("TL: long string overflow");
        len = (size_t)data_[pos_ + 1]
            | ((size_t)data_[pos_ + 2] << 8)
            | ((size_t)data_[pos_ + 3] << 16);
        pos_ += 4;
    } else {
        throw std::runtime_error("TL: invalid string prefix");
    }
    if (pos_ + len > size_) throw std::runtime_error("TL: string data overflow");
    std::string result((const char*)(data_ + pos_), len);
    pos_ += len;
    // Skip padding
    size_t total = (first <= 253) ? (1 + len) : (4 + len);
    while (total % 4 != 0) { pos_++; total++; }
    return result;
}

std::vector<uint8_t> TLDeserializer::read_bytes() {
    // Same as string but returns raw bytes
    if (pos_ >= size_) throw std::runtime_error("TL: bytes overflow");
    uint8_t first = data_[pos_];
    size_t len;
    if (first <= 253) {
        len = first;
        pos_ += 1;
    } else if (first == 254) {
        if (pos_ + 4 > size_) throw std::runtime_error("TL: long bytes overflow");
        len = (size_t)data_[pos_ + 1]
            | ((size_t)data_[pos_ + 2] << 8)
            | ((size_t)data_[pos_ + 3] << 16);
        pos_ += 4;
    } else {
        throw std::runtime_error("TL: invalid bytes prefix");
    }
    if (pos_ + len > size_) throw std::runtime_error("TL: bytes data overflow");
    std::vector<uint8_t> result(data_ + pos_, data_ + pos_ + len);
    pos_ += len;
    size_t total = (first <= 253) ? (1 + len) : (4 + len);
    while (total % 4 != 0) { pos_++; total++; }
    return result;
}

void TLDeserializer::read_int128(uint8_t out[16]) {
    if (pos_ + 16 > size_) throw std::runtime_error("TL: int128 overflow");
    std::memcpy(out, data_ + pos_, 16);
    pos_ += 16;
}

void TLDeserializer::read_int256(uint8_t out[32]) {
    if (pos_ + 32 > size_) throw std::runtime_error("TL: int256 overflow");
    std::memcpy(out, data_ + pos_, 32);
    pos_ += 32;
}

uint32_t TLDeserializer::read_constructor() {
    return (uint32_t)read_int32();
}

bool TLDeserializer::read_bool() {
    uint32_t cons = read_constructor();
    if (cons == 0x997275b5) return true;
    if (cons == 0xbc799737) return false;
    throw std::runtime_error("TL: invalid bool constructor");
}

} // namespace tdesktop::mtproto
