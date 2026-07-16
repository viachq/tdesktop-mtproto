"""desktop_mtproto - C++ MTProto library behaving like Telegram Desktop."""
import ctypes
from pathlib import Path

class MTProtoLibrary:
    def __init__(self, dll_path=None):
        if not dll_path:
            dll_path = self._find_dll()
        self._lib = ctypes.CDLL(str(dll_path))
        L = self._lib
        L.mtproto_create.argtypes = [ctypes.c_int, ctypes.c_char_p]*8
        L.mtproto_create.restype = ctypes.c_void_p
        L.mtproto_connect.argtypes = [ctypes.c_void_p, ctypes.c_int]
        L.mtproto_connect.restype = ctypes.c_int
        L.mtproto_destroy.argtypes = [ctypes.c_void_p]
        L.mtproto_api_id.argtypes = [ctypes.c_void_p]
        L.mtproto_api_id.restype = ctypes.c_int
        L.mtproto_version.restype = ctypes.c_char_p
        self.L = L

    def _find_dll(self):
        for p in [Path(__file__).parent.parent/"build"/"Release"/"desktop_mtproto.dll",
                  Path("E:/tdesktop-mtproto/build/Release/desktop_mtproto.dll")]:
            if p.exists(): return p
        raise RuntimeError("Build first: cd E:\tdesktop-mtproto && cmake --build build --config Release")

class Client:
    def __init__(self, api_id=2040, api_hash="b18441a1ff607e10a989891a5462e627",
                 device="Desktop PC", sv="Windows 10", av="7.0.1",
                 lp="tdesktop", lc="en", slc="en"):
        self.c = {"api_id":api_id,"api_hash":api_hash,"device":device,
                  "sv":sv,"av":av,"lp":lp,"lc":lc,"slc":slc}
        self._h = None
        self._m = MTProtoLibrary()

    def connect(self, dc_id=2):
        c = self.c
        self._h = self._m.L.mtproto_create(c["api_id"], c["api_hash"].encode(),
            c["device"].encode(), c["sv"].encode(), c["av"].encode(),
            c["lp"].encode(), c["lc"].encode(), c["slc"].encode())
        return bool(self._m.L.mtproto_connect(self._h, dc_id))

    def disconnect(self):
        if self._h: self._m.L.mtproto_destroy(self._h); self._h = None
    def __del__(self): self.disconnect()

    @property
    def api_id(self): return self.c["api_id"]
