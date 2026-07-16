"""
desktop-mtproto — Python TL serialization layer.

Builds MTProto API calls using constructors from tl_constructors.py,
sends them through the encrypted C++ session, and parses responses.

Usage:
    from desktop_mtproto import Client
    client = Client()
    client.connect(dc_id=2)
    
    # Send code
    result = client.call("auth.sendCode", {
        "phone_number": "+380501234567",
        "api_id": 2040,
        "api_hash": "b18441a1ff607e10a989891a5462e627",
        "settings": {"_": "codeSettings"}
    })
"""

import ctypes
import random
import struct
from pathlib import Path
from typing import Optional, Dict, Any, List, Union
from .tl_constructors import FUNCTIONS, TYPES, INPUT_PEER_SELF


class TL:
    """TL serializer/deserializer for Python."""
    
    def __init__(self):
        self.data = bytearray()
    
    # === WRITERS ===
    def write_int(self, v: int):
        self.data += struct.pack('<i', v & 0xFFFFFFFF)
    
    def write_long(self, v: int):
        self.data += struct.pack('<q', v & 0xFFFFFFFFFFFFFFFF)
    
    def write_double(self, v: float):
        self.data += struct.pack('<d', v)
    
    def write_uint(self, v: int):
        self.write_int(v)
    
    def write_string(self, s: str):
        b = s.encode('utf-8')
        if len(b) <= 253:
            self.data.append(len(b))
        else:
            self.data.append(254)
            self.data += bytes([len(b) & 0xFF, (len(b) >> 8) & 0xFF, (len(b) >> 16) & 0xFF])
        self.data += b
        while len(self.data) % 4:
            self.data.append(0)
    
    def write_bytes(self, b: bytes):
        if len(b) <= 253:
            self.data.append(len(b))
        else:
            self.data.append(254)
            self.data += struct.pack('<I', len(b))[:3]
        self.data += b
        while len(self.data) % 4:
            self.data.append(0)
    
    def write_int128(self, b: bytes):
        assert len(b) == 16
        self.align()
        self.data += b
    
    def write_int256(self, b: bytes):
        assert len(b) == 32
        self.align()
        self.data += b
    
    def write_bool(self, v: bool):
        self.write_uint(0x997275b5 if v else 0xbc799737)
    
    def write_vector(self, items, writer=None):
        """Write a TL vector. items is a list, writer is a callable or type-based."""
        self.write_uint(0x1cb5c415)  # vector constructor
        self.write_int(len(items))
        for item in items:
            if writer:
                writer(item)
            else:
                self.write_value(item)
    
    def write_value(self, v):
        """Auto-detect type and write."""
        if v is None:
            self.write_uint(0x56730bcc)  # null
        elif isinstance(v, bool):
            self.write_bool(v)
        elif isinstance(v, int):
            if -0x80000000 <= v <= 0x7FFFFFFF:
                self.write_int(v)
            else:
                self.write_long(v)
        elif isinstance(v, float):
            self.write_double(v)
        elif isinstance(v, str):
            self.write_string(v)
        elif isinstance(v, bytes):
            self.write_bytes(v)
        elif isinstance(v, list):
            self.write_vector(v)
        elif isinstance(v, dict):
            self.write_object(v)
        else:
            raise TypeError(f"Unsupported TL type: {type(v)}")
    
    def write_object(self, obj: dict):
        """Write a TL object (dict with _ key for constructor)."""
        name = obj.get('_', '')
        if not name:
            raise ValueError(f"TL object missing '_' key: {obj}")
        
        # Look up constructor
        cons = self._get_constructor(name)
        if cons is None:
            raise ValueError(f"Unknown TL type: {name}")
        
        self.write_uint(cons)
        
        # Serialize args based on TL schema field ordering
        schema_args = self._get_schema_args(name)
        flags_mask = 0
        
        # First pass: calculate flags
        for arg in schema_args:
            if arg['is_flag']:
                continue  # flags field itself - skip
            cond = arg.get('cond')
            if cond is not None:
                field_name = arg['name']
                if field_name in obj and obj[field_name] is not None:
                    if arg['cond_true']:
                        flags_mask |= (1 << cond)
        
        # Second pass: write
        for arg in schema_args:
            if arg['is_flag']:
                self.write_uint(flags_mask)
                continue
            
            field_name = arg['name']
            cond = arg.get('cond')
            
            # Check if this is a conditional field that should be omitted
            if cond is not None:
                if not (flags_mask & (1 << cond)):
                    continue
            
            value = obj.get(field_name)
            if value is None and cond is not None:
                continue
            
            self._write_field(arg, value, flags_mask)
    
    def _write_field(self, arg, value, flags):
        tl_type = arg.get('tl_type', '')
        
        # Type-based dispatch
        if tl_type == 'int':
            self.write_int(value)
        elif tl_type == 'long':
            self.write_long(value)
        elif tl_type == 'double':
            self.write_double(value)
        elif tl_type == 'string':
            self.write_string(value)
        elif tl_type == 'bytes':
            self.write_bytes(value)
        elif tl_type == 'Bool':
            self.write_bool(value)
        elif tl_type.startswith('Vector<'):
            self.write_vector(value)
        elif tl_type.startswith('flags.'):
            pass  # Already handled
        else:
            # Complex type - serialize as object
            if isinstance(value, dict):
                self.write_object(value)
            elif isinstance(value, str):
                # Could be a bare constructor name
                bare = self._find_bare_constructor(tl_type, value)
                self.write_uint(bare)
            else:
                raise ValueError(f"Cant serialize field {arg['name']} type={tl_type} val={value}")
    
    def _get_constructor(self, name):
        """Look up constructor number for a type/function name."""
        # First check TYPES (e.g. inputPeerSelf -> 0x7da07ec9)
        for type_name, variants in TYPES.items():
            if name in variants:
                return variants[name]
        # Could be in format "ns.name" for functions
        for ns_name, hexval in FUNCTIONS.items():
            if ns_name == name or ns_name.endswith('.' + name):
                return hexval
        return None
    
    def _get_schema_args(self, name):
        """Get the argument definitions for a TL object type."""
        # Look up in our schema knowledge base
        return TL_SCHEMA.get(name, [])
    
    def _find_bare_constructor(self, type_name, value):
        """Find constructor for bare type reference."""
        if type_name in TYPES:
            for name, cons in TYPES[type_name].items():
                if name == value or name.lower() == value.lower():
                    return cons
        raise ValueError(f"No constructor for {type_name}: {value}")
    
    
    # === READERS ===
    @staticmethod
    def read_int(data, pos):
        v = struct.unpack_from('<i', data, pos[0])[0]
        pos[0] += 4
        return v
    
    @staticmethod
    def read_long(data, pos):
        v = struct.unpack_from('<q', data, pos[0])[0]
        pos[0] += 8
        return v
    
    @staticmethod
    def read_uint(data, pos):
        return TL.read_int(data, pos) & 0xFFFFFFFF
    
    @staticmethod
    def read_string(data, pos):
        first = data[pos[0]]
        pos[0] += 1
        if first <= 253:
            length = first
        elif first == 254:
            length = data[pos[0]] | (data[pos[0]+1] << 8) | (data[pos[0]+2] << 16)
            pos[0] += 3
        else:
            raise ValueError('Invalid string')
        s = data[pos[0]:pos[0]+length].decode('utf-8')
        pos[0] += length
        while pos[0] % 4: pos[0] += 1
        return s
    
    @staticmethod
    def read_bytes(data, pos):
        first = data[pos[0]]
        pos[0] += 1
        if first <= 253:
            length = first
        elif first == 254:
            length = data[pos[0]] | (data[pos[0]+1] << 8) | (data[pos[0]+2] << 16)
            pos[0] += 3
        else:
            raise ValueError('Invalid bytes')
        b = bytes(data[pos[0]:pos[0]+length])
        pos[0] += length
        while pos[0] % 4: pos[0] += 1
        return b
    def align(self):
        while len(self.data) % 4:
            self.data.append(0)


# === TL SCHEMA KNOWLEDGE BASE ===
# Minimal set of arg definitions for commonly used types
# Full version would be generated from api.tl
TL_SCHEMA = {
    'codeSettings': [
        {'name': 'flags', 'is_flag': True},
        {'name': 'allow_flashcall', 'tl_type': 'flags.0?true', 'cond': 0},
        {'name': 'current_number', 'tl_type': 'flags.1?Bool', 'cond': 1},
        {'name': 'allow_app_hash', 'tl_type': 'flags.4?Bool', 'cond': 4},
        {'name': 'allow_missed_call', 'tl_type': 'flags.5?Bool', 'cond': 5},
        {'name': 'allow_firebase', 'tl_type': 'flags.7?Bool', 'cond': 7},
        {'name': 'logout_tokens', 'tl_type': 'flags.6?Vector<bytes>', 'cond': 6},
        {'name': 'token', 'tl_type': 'flags.3?string', 'cond': 3},
        {'name': 'app_sandbox', 'tl_type': 'flags.8?Bool', 'cond': 8},
    ],
    'inputPeerSelf': [],
    'inputPeerUser': [
        {'name': 'user_id', 'tl_type': 'long'},
        {'name': 'access_hash', 'tl_type': 'long'},
    ],
    'inputPeerChat': [
        {'name': 'chat_id', 'tl_type': 'long'},
    ],
    'inputPeerChannel': [
        {'name': 'channel_id', 'tl_type': 'long'},
        {'name': 'access_hash', 'tl_type': 'long'},
    ],
}


class Session:
    """Manages a Telegram session using the C++ desktop_mtproto library."""
    
    def __init__(self, dll_path: Optional[str] = None):
        self._lib = self._load(dll_path)
        self._handle = None
    
    def _load(self, dll_path):
        if not dll_path:
            for p in [
                Path(__file__).parent / "desktop_mtproto.dll",
                Path(__file__).parent.parent / "build" / "Release" / "desktop_mtproto.dll",
                Path("E:/desktop-mtproto/build/Release/desktop_mtproto.dll"),
            ]:
                if p.exists():
                    dll_path = str(p)
                    break
        lib = ctypes.CDLL(dll_path)
        
        # Setup C API signatures
        lib.mtproto_create.argtypes = [ctypes.c_int] + [ctypes.c_char_p] * 7
        lib.mtproto_create.restype = ctypes.c_void_p
        lib.mtproto_connect.argtypes = [ctypes.c_void_p, ctypes.c_int]
        lib.mtproto_connect.restype = ctypes.c_int
        lib.mtproto_destroy.argtypes = [ctypes.c_void_p]
        lib.mtproto_version.restype = ctypes.c_char_p
        
        # Encrypted RPC
        lib.mtproto_call.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint8), ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
        lib.mtproto_call.restype = ctypes.POINTER(ctypes.c_uint8)
        lib.mtproto_free.argtypes = [ctypes.POINTER(ctypes.c_uint8)]
        
        return lib
    
    def create(self, api_id=2040, api_hash="b18441a1ff607e10a989891a5462e627",
               device="Desktop PC", sv="Windows 10", av="7.0.1",
               lp="tdesktop", lc="en", slc="en") -> bool:
        self._handle = self._lib.mtproto_create(
            api_id, api_hash.encode(), device.encode(), sv.encode(),
            av.encode(), lp.encode(), lc.encode(), slc.encode()
        )
        return self._handle is not None
    
    def connect(self, dc_id=2) -> bool:
        return bool(self._lib.mtproto_connect(self._handle, dc_id))
    
    def encrypted_call(self, body: bytes) -> Optional[bytes]:
        req = (ctypes.c_uint8 * len(body)).from_buffer_copy(body)
        resp_len = ctypes.c_int(0)
        
        resp_ptr = self._lib.mtproto_call(self._handle, req, len(body), ctypes.byref(resp_len))
        if not resp_ptr or resp_len.value == 0:
            return None
        
        result = bytes(resp_ptr[:resp_len.value])
        self._lib.mtproto_free(resp_ptr)
        return result
    
    def destroy(self):
        if self._handle:
            self._lib.mtproto_destroy(self._handle)
            self._handle = None
    
    def __del__(self):
        self.destroy()
