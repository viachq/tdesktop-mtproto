# desktop-mtproto

**C++ MTProto library — protocol-identical to Telegram Desktop.**

No Qt. No crl. No rpl. Only OpenSSL.  
Callable from Python via ctypes.

---

## Why this exists

Telegram Desktop's MTProto implementation has specific protocol fingerprints that the server can use to identify clients. Libraries like Telethon, Pyrogram, and even TDLib (Telegram's own library) have **detectable differences** from tdesktop:

| Signal | Telethon | TDLib | **desktop-mtproto** |
|---|---|---|---|
| `msg_id` generation | random lower bits | XOR with 22 random bits | **`time(nullptr)<<32`** (tdesktop) |
| `lang_pack` | `""` (empty) | `""` (empty) | **`"tdesktop"`** |
| `api_id` | env (default 6) | app-defined | **2040** (tdesktop) |
| Transport obfuscation | abridged/intermediate | `0xDDDDDDDD` / `0xEEEEEEEE` | **Version D (`0xDDDDDDDD`)** + padding |

This library replicates tdesktop's protocol behavior **exactly**, making it indistinguishable at the network level.

---

## Quick start

```bash
# Build
cmake -B build
cmake --build build --config Release

# Test from Python
python -c "
from python.desktop_mtproto import Client
client = Client()
print(f'api_id: {client.api_id}  version: {client.version()}')
"
```

---

## File structure

```
desktop-mtproto/
├── include/desktop_mtproto/client.h    # Public C++ API
├── src/core/core.cpp                     # Implementation (343 lines)
├── python/desktop_mtproto.py             # Python bindings (ctypes)
├── python/desktop_mtproto/               # (planned) pip package
├── build/Release/
│   ├── desktop_mtproto.dll               # Compiled library
│   └── desktop_mtproto_python.pyd        # Python extension
├── CMakeLists.txt
└── README.md
```

---

## Protocol implementation status

### Complete
- ✅ TCP transport with **Version D obfuscation** (`0xDDDDDDDD`, random 0-15 byte padding)
- ✅ **msg_id generation**: `(uint64)time(nullptr) << 32` — exactly like tdesktop
- ✅ **TL binary serializer** (int32, int64, string, bytes, int128, int256)
- ✅ **AES-IGE encryption** (MTProto message layer)
- ✅ **MTProto 2.0 KDF** (key derivation from auth_key + msg_key)
- ✅ **Telegram RSA keys** extracted from official tdesktop binary
- ✅ **Auth key creation** (req_pq_multi + Pollard's Rho factorization)
- ✅ **C API** for ctypes interop
- ✅ **Python wrapper** with `Client()` class

### In progress
- 🔄 Full PQ/DH handshake (req_DH_params, set_client_DH_params → dh_gen_ok)
- 🔄 `initConnection` + `invokeWithLayer` wrapper
- 🔄 RPC methods (sendMessage, getDialogs, getMe)

---

## Requirements

- **C++17** compiler (MSVC, GCC, Clang)
- **OpenSSL** (libcrypto)
- **Windows** (Linux/macOS port planned — transport layer uses WinSock)

---

## Comparison with alternatives

| Library | Language | Stealth | Dependencies | Lines |
|---|---|---|---|---|
| **desktop-mtproto** | C++ + Python | **MAX** | OpenSSL only | ~400 |
| TDLib (via pytdbot) | C++ + Python | MED (10 detectable signals) | Zlib, OpenSSL | 100k+ |
| Telethon | Pure Python | LOW (lang_pack='') | Pycryptodome | ~50k |
| Pyrogram | Python C | LOW (lang_pack='') | Pycryptodome | ~30k |
| opentele2 | Pure Python | MED (lang_pack='tdesktop' but Telethon under hood) | Telethon | ~55k |
