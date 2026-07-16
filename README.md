# tdesktop-mtproto

Standalone MTProto library extracted from Telegram Desktop.

Goal: Pure C++ MTProto implementation that behaves **identically** to tdesktop
at the protocol level, with zero Qt dependencies, callable from Python.

## Architecture (bottom-up)

```
┌──────────────────────────────────┐
│  Python bindings (ctypes/cffi)   │
├──────────────────────────────────┤
│  C API (mtproto.h)               │
├──────────────────────────────────┤
│  Session / RPC layer             │  ← session.cpp, session_private.cpp
├──────────────────────────────────┤
│  initConnection params           │  ← tdesktop device_model, lang_pack
├──────────────────────────────────┤
│  TCP transport (obfuscation)     │  ← 0xDDDDDDDD, TLS emulation
├──────────────────────────────────┤
│  Auth key creation               │  ← PQ, DH, RSA
├──────────────────────────────────┤
│  TL serializer                   │  ← int32/64, string, vector, bytes
├──────────────────────────────────┤
│  Crypto (AES-IGE, AES-CTR, SHA)  │
└──────────────────────────────────┘
```

## Dependencies

- C++17 compiler (MSVC, GCC, Clang)
- OpenSSL (libcrypto) — AES, SHA, RSA, DH
- No Qt
- No boost

## Build

```bash
cmake -B build
cmake --build build
```

## Python

```python
from tdesktop_mtproto import Client

client = Client(
    api_id=2040,
    api_hash="b18441a1ff607e10a989891a5462e627",
    device="Desktop PC",
    system_version="Windows 10",
    app_version="7.0.1",
    lang_pack="tdesktop"
)

client.connect(dc_id=2)
client.send_message("@username", "Hello from tdesktop MTProto!")
```
