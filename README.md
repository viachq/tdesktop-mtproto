# desktop-mtproto

Pure C++ MTProto library extracted from Telegram Desktop protocol behavior.

**Identical to tdesktop at the protocol level:**
- `api_id=2040` with `lang_pack="tdesktop"` in initConnection
- `msg_id = time(nullptr)<<32` (NO lower-bit randomization — unlike TDLib)
- Transport Version D (`0xDDDDDDDD`) with 0-15 byte padding
- Real Telegram RSA keys used for auth handshake
- AES-IGE + MTProto 2.0 KDF for message encryption

**No Qt, no crl, no rpl.** Pure C++17 with only OpenSSL dependency.
Callable from Python via ctypes (.dll) or native .pyd extension.

## Build

```bash
cmake -B build
cmake --build build --config Release
```

## Python Usage

```python
from desktop_mtproto import Client

client = Client(
    api_id=2040,
    api_hash="b18441a1ff607e10a989891a5462e627",
)
client.connect(dc_id=2)  # TCP + obfuscation + auth key creation
# All protocol behavior matches tdesktop exactly
client.disconnect()
```
