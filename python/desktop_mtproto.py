#!/usr/bin/env python3
"""desktop-mtproto — Python bindings for tdesktop-level MTProto library.

Provides a Client class with protocol-identical behavior to Telegram Desktop:
- api_id=2040, lang_pack="tdesktop"
- msg_id = time(nullptr) << 32 (no randomization)
- Transport Version D (0xDDDDDDDD) with 0-15 byte padding
- Full MTProto 2.0 encryption (AES-IGE + KDF)
"""

import ctypes
from pathlib import Path
from typing import Optional


class _Library:
    """Low-level wrapper around desktop_mtproto.dll."""

    def __init__(self, dll_path: Optional[str] = None):
        self._lib = ctypes.CDLL(str(dll_path or self._find()))
        L = self._lib

        L.mtproto_create.argtypes = [ctypes.c_int] + [ctypes.c_char_p] * 7
        L.mtproto_create.restype = ctypes.c_void_p

        L.mtproto_connect.argtypes = [ctypes.c_void_p, ctypes.c_int]
        L.mtproto_connect.restype = ctypes.c_int

        L.mtproto_destroy.argtypes = [ctypes.c_void_p]
        L.mtproto_api_id.argtypes = [ctypes.c_void_p]
        L.mtproto_api_id.restype = ctypes.c_int
        L.mtproto_version.restype = ctypes.c_char_p

    @staticmethod
    def _find() -> Path:
        for p in [
            Path(__file__).resolve().parent / "desktop_mtproto.dll",
            Path(__file__).resolve().parent.parent
            / "build" / "Release" / "desktop_mtproto.dll",
            Path("E:/tdesktop-mtproto/build/Release/desktop_mtproto.dll"),
        ]:
            if p.exists():
                return p
        raise RuntimeError(
            "desktop_mtproto.dll not found. Build it first:\n"
            "  cd E:\\tdesktop-mtproto && cmake --build build --config Release"
        )

    def __getattr__(self, name):
        return getattr(self._lib, name)


class Client:
    """MTProto client with tdesktop-identical protocol behavior.

    Args:
        api_id: Telegram API ID (default: 2040 — tdesktop's)
        api_hash: Telegram API hash (default: tdesktop's)
    """

    def __init__(
        self,
        api_id: int = 2040,
        api_hash: str = "b18441a1ff607e10a989891a5462e627",
    ):
        self._config = dict(
            api_id=api_id,
            api_hash=api_hash,
            device_model="Desktop PC",
            system_version="Windows 10",
            app_version="7.0.1",
            lang_pack="tdesktop",
            lang_code="en",
            system_lang_code="en",
        )
        self._handle: Optional[int] = None
        self._lib = _Library()

    def connect(self, dc_id: int = 2) -> bool:
        """Connect to a Telegram datacenter."""
        c = self._config
        self._handle = self._lib.mtproto_create(
            c["api_id"], c["api_hash"].encode(),
            c["device_model"].encode(), c["system_version"].encode(),
            c["app_version"].encode(), c["lang_pack"].encode(),
            c["lang_code"].encode(), c["system_lang_code"].encode(),
        )
        return bool(self._lib.mtproto_connect(self._handle, dc_id))

    def disconnect(self) -> None:
        if self._handle:
            self._lib.mtproto_destroy(self._handle)
            self._handle = None

    @property
    def api_id(self) -> int:
        return self._config["api_id"]

    @property
    def version(self) -> str:
        return self._lib.mtproto_version().decode()

    def __del__(self):
        self.disconnect()
