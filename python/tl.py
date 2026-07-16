"""
desktop-mtproto — Python TL serialization/deserialization layer.
"""
import ctypes, random, struct, zlib
from pathlib import Path
from typing import Optional
try:
    from .tl_schema import FUNCTIONS, TYPES, TL_SCHEMA
except ImportError:
    from tl_schema import FUNCTIONS, TYPES, TL_SCHEMA


class TL:
    """TL serializer/deserializer for Python."""
    
    def __init__(self):
        self.data = bytearray()
    
    # === WRITERS ===
    def write_int(self, v): self.data += struct.pack('<i', v if v < 0x80000000 else v - 0x100000000)
    def write_long(self, v): self.data += struct.pack('<q', v if v < 0x8000000000000000 else v - 0x10000000000000000)
    def write_double(self, v): self.data += struct.pack('<d', v)
    def write_uint(self, v): self.write_int(v if v < 0x80000000 else v - 0x100000000)
    
    def write_string(self, s):
        b = s.encode('utf-8')
        if len(b) <= 253: self.data.append(len(b))
        else: self.data += bytes([254, len(b)&0xFF, (len(b)>>8)&0xFF, (len(b)>>16)&0xFF])
        self.data += b
        while len(self.data) % 4: self.data.append(0)
    
    def write_bytes(self, b):
        if len(b) <= 253: self.data.append(len(b))
        else: self.data += bytes([254, len(b)&0xFF, (len(b)>>8)&0xFF, (len(b)>>16)&0xFF])
        self.data += b
        while len(self.data) % 4: self.data.append(0)
    
    def write_int128(self, b): self.align(); self.data += b
    def write_int256(self, b): self.align(); self.data += b
    def write_bool(self, v): self.write_uint(0x997275b5 if v else 0xbc799737)
    
    def write_vector(self, items, writer=None):
        self.write_uint(0x1cb5c415)
        self.write_int(len(items))
        for item in items:
            writer(item) if writer else self.write_value(item)
    
    def write_value(self, v):
        if v is None: self.write_uint(0x56730bcc)
        elif isinstance(v, bool): self.write_bool(v)
        elif isinstance(v, int):
            self.write_long(v) if abs(v) > 0x7FFFFFFF else self.write_int(v)
        elif isinstance(v, float): self.write_double(v)
        elif isinstance(v, str): self.write_string(v)
        elif isinstance(v, bytes): self.write_bytes(v)
        elif isinstance(v, list): self.write_vector(v)
        elif isinstance(v, dict): self.write_object(v)
        else: raise TypeError(f'Unsupported type: {type(v)}')
    
    def write_object(self, obj):
        name = obj.get('_', '')
        if not name: raise ValueError(f"Missing '_': {obj}")
        cons = self._get_constructor(name)
        if cons is None: raise ValueError(f'Unknown type: {name}')
        
        self.write_uint(cons)
        schema_args = TL_SCHEMA.get(name, [])
        flags_mask = 0
        
        for arg in schema_args:
            if arg.get('is_flag'): continue
            cond = arg.get('cond')
            if cond is not None and obj.get(arg['name']) is not None:
                flags_mask |= (1 << cond)
        
        for arg in schema_args:
            if arg.get('is_flag'): self.write_uint(flags_mask); continue
            cond = arg.get('cond')
            if cond is not None and not (flags_mask & (1 << cond)): continue
            value = obj.get(arg['name'])
            if value is None and cond is not None: continue
            self._write_field(arg, value, flags_mask)
    
    def _write_field(self, arg, value, flags):
        t = arg.get('tl_type', '')
        if t == 'int': self.write_int(value)
        elif t == 'long': self.write_long(value)
        elif t == 'double': self.write_double(value)
        elif t == 'string': self.write_string(value)
        elif t == 'bytes': self.write_bytes(value)
        elif t == 'Bool': self.write_bool(value)
        elif t.startswith('Vector<'): self.write_vector(value)
        elif t.startswith('flags.'): pass
        elif isinstance(value, dict): self.write_object(value)
        elif isinstance(value, str): self.write_uint(self._find_bare_constructor(t, value))
        else: raise ValueError(f'Bad field {arg["name"]}: {t}={value}')
    
    def _get_constructor(self, name):
        for tn, vr in TYPES.items():
            if name in vr:
                v = vr[name]
                return int(v, 16) if isinstance(v, str) else v
        for fn, hv in FUNCTIONS.items():
            if fn == name or fn.endswith('.' + name):
                return int(hv, 16) if isinstance(hv, str) else hv
        return None
    
    def _get_schema_args(self, name):
        return TL_SCHEMA.get(name, [])
    
    def _find_bare_constructor(self, type_name, value):
        if type_name in TYPES:
            for name, hv in TYPES[type_name].items():
                cons = int(hv, 16) if isinstance(hv, str) else hv
                if name == value or name.lower() == value.lower(): return cons
        raise ValueError(f'No constructor for {type_name}: {value}')
    
    def align(self):
        while len(self.data) % 4: self.data.append(0)
    
    # === READERS ===
    @staticmethod
    def read_int(data, pos):
        v = struct.unpack_from('<i', data, pos[0])[0]
        pos[0] += 4; return v
    
    @staticmethod
    def read_long(data, pos):
        v = struct.unpack_from('<q', data, pos[0])[0]
        pos[0] += 8; return v
    
    @staticmethod
    def read_uint(data, pos):
        return TL.read_int(data, pos) & 0xFFFFFFFF
    
    @staticmethod
    def read_double(data, pos):
        v = struct.unpack_from('<d', data, pos[0])[0]
        pos[0] += 8; return v
    
    @staticmethod
    def read_bool(data, pos):
        v = TL.read_uint(data, pos)
        return v == 0x997275b5  # boolTrue
    
    @staticmethod
    def read_string(data, pos):
        first = data[pos[0]]; pos[0] += 1
        if first <= 253: length = first
        elif first == 254:
            length = data[pos[0]] | (data[pos[0]+1] << 8) | (data[pos[0]+2] << 16)
            pos[0] += 3
        else: raise ValueError('Bad string')
        s = data[pos[0]:pos[0]+length].decode('utf-8', errors='replace')
        pos[0] += length
        while pos[0] % 4: pos[0] += 1
        return s
    
    @staticmethod
    def read_bytes(data, pos):
        first = data[pos[0]]; pos[0] += 1
        if first <= 253: length = first
        elif first == 254:
            length = data[pos[0]] | (data[pos[0]+1] << 8) | (data[pos[0]+2] << 16)
            pos[0] += 3
        else: raise ValueError('Bad bytes')
        b = bytes(data[pos[0]:pos[0]+length])
        pos[0] += length
        while pos[0] % 4: pos[0] += 1
        return b
    
    @staticmethod
    def read_value(data, pos, tl_type=None):
        """Read a value based on expected TL type."""
        if tl_type == 'int': return TL.read_int(data, pos)
        if tl_type == 'long': return TL.read_long(data, pos)
        if tl_type == 'double': return TL.read_double(data, pos)
        if tl_type == 'string': return TL.read_string(data, pos)
        if tl_type == 'bytes': return TL.read_bytes(data, pos)
        if tl_type == 'Bool' or tl_type == 'true': return TL.read_bool(data, pos)
        if tl_type == '#': return TL.read_uint(data, pos)
        if tl_type and tl_type.startswith('Vector<'):
            return TL.read_vector(data, pos)
        # Unknown type - try reading as object
        if pos[0] < len(data):
            return TL.read_object(data, pos)
        return None
    
    @staticmethod
    def peek_constructor(data, pos):
        """Peek at the constructor without advancing."""
        if pos[0] + 4 > len(data): return None
        return struct.unpack_from('<I', data, pos[0])[0]
    
    @staticmethod
    def read_vector(data, pos):
        """Read a TL vector."""
        cons = TL.peek_constructor(data, pos)
        if cons == 0x1cb5c415:  # vector
            TL.read_uint(data, pos)  # skip constructor
            count = TL.read_int(data, pos)
            items = []
            for _ in range(count):
                items.append(TL.read_object(data, pos))
            return items
        elif cons == 0x3072cfa1:  # gzip_packed
            TL.read_uint(data, pos)  # skip constructor
            packed = TL.read_bytes(data, pos)
            decompressed = zlib.decompress(packed)
            inner_pos = [0]
            return TL.read_vector(decompressed, inner_pos)
        else:
            # Maybe it's a single item
            return [TL.read_object(data, pos)]
    
    @staticmethod
    def read_object(data, pos):
        """Recursively parse a TL object using TL_SCHEMA."""
        if pos[0] >= len(data):
            return {}
        
        cons = TL.read_uint(data, pos)
        result = {'_': f'0x{cons:08x}'}
        
        # Special constructors
        if cons == 0x1cb5c415:  # vector
            pos[0] -= 4  # put back, read_vector handles it
            return TL.read_vector(data, pos)
        
        if cons == 0x3072cfa1:  # gzip_packed
            packed = TL.read_bytes(data, pos)
            try:
                decompressed = zlib.decompress(packed)
                inner_pos = [0]
                return TL.read_object(decompressed, inner_pos)
            except: pass
            return result
        
        if cons == 0x56730bcc:  # null
            return None
        
        if cons == 0x997275b5:  # boolTrue
            pos[0] -= 4; return True
        if cons == 0xbc799737:  # boolFalse
            pos[0] -= 4; return False
        
        # Find type name from constructor
        type_name = None
        constructor_name = None
        for tn, vr in TYPES.items():
            for name, hv in vr.items():
                hv_int = int(hv, 16) if isinstance(hv, str) else hv
                if hv_int == cons:
                    type_name = tn
                    constructor_name = name
                    break
            if type_name: break
        
        if constructor_name:
            result['_'] = constructor_name
            # Parse fields using schema
            schema_args = TL_SCHEMA.get(constructor_name, [])
            flags_mask = 0
            
            i = 0
            while i < len(schema_args) and pos[0] < len(data):
                arg = schema_args[i]
                if arg.get('is_flag'):
                    flags_mask = TL.read_uint(data, pos)
                    i += 1; continue
                
                cond = arg.get('cond')
                if cond is not None and not (flags_mask & (1 << cond)):
                    i += 1; continue
                
                raw_type = arg['tl_type']
                if raw_type == 'true':
                    result[arg['name']] = True
                elif raw_type.startswith('flags.'):
                    pass  # handled by flags_mask
                else:
                    val = TL.read_value(data, pos, raw_type)
                    result[arg['name']] = val
                i += 1
        
        return result


class Session:
    """Manages a Telegram session using the C++ desktop_mtproto library."""
    
    def __init__(self, dll_path=None):
        self._lib = self._load(dll_path)
        self._handle = None
    
    def _load(self, dll_path):
        if not dll_path:
            for p in [
                Path(__file__).parent / 'desktop_mtproto.dll',
                Path(__file__).parent.parent / 'build' / 'Release' / 'desktop_mtproto.dll',
                Path('E:/desktop-mtproto/build/Release/desktop_mtproto.dll'),
            ]: 
                if p.exists(): dll_path = str(p); break
        if not dll_path:
            raise RuntimeError('desktop_mtproto.dll not found. Build with: cmake --build build --config Release')
        
        lib = ctypes.CDLL(dll_path)
        lib.mtproto_create.argtypes = [ctypes.c_int] + [ctypes.c_char_p]*7
        lib.mtproto_create.restype = ctypes.c_void_p
        lib.mtproto_connect.argtypes = [ctypes.c_void_p, ctypes.c_int]
        lib.mtproto_connect.restype = ctypes.c_int
        lib.mtproto_destroy.argtypes = [ctypes.c_void_p]
        lib.mtproto_version.restype = ctypes.c_char_p
        lib.mtproto_call.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint8), ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
        lib.mtproto_call.restype = ctypes.POINTER(ctypes.c_uint8)
        lib.mtproto_free.argtypes = [ctypes.POINTER(ctypes.c_uint8)]
        return lib
    
    def create(self, api_id=2040, api_hash="b18441a1ff607e10a989891a5462e627",
               device="Desktop PC", sv="Windows 10", av="7.0.1",
               lp="tdesktop", lc="en", slc="en"):
        self._handle = self._lib.mtproto_create(
            api_id, api_hash.encode(), device.encode(), sv.encode(),
            av.encode(), lp.encode(), lc.encode(), slc.encode())
        return self._handle is not None
    
    def connect(self, dc_id=2):
        return bool(self._lib.mtproto_connect(self._handle, dc_id))
    
    def encrypted_call(self, body):
        req = (ctypes.c_uint8 * len(body)).from_buffer_copy(body)
        resp_len = ctypes.c_int(0)
        resp_ptr = self._lib.mtproto_call(self._handle, req, len(body), ctypes.byref(resp_len))
        if not resp_ptr or resp_len.value == 0: return None
        result = bytes(resp_ptr[:resp_len.value])
        self._lib.mtproto_free(resp_ptr)
        return result
    
    def destroy(self):
        if self._handle: self._lib.mtproto_destroy(self._handle); self._handle = None
    def __del__(self): self.destroy()
