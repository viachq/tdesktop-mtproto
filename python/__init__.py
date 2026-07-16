"""desktop-mtproto — Python TL serialization engine + C++ MTProto transport.
"""
from .tl import Session, TL
from .tl_schema import FUNCTIONS, TL_SCHEMA

class Client:
    """Telegram client using tdesktop-level MTProto.

    Args:
        api_id: Default 2040 (tdesktop's)
        api_hash: Default tdesktop's hash
    """

    def __init__(self, api_id=2040, api_hash="b18441a1ff607e10a989891a5462e627"):
        self._api_id = api_id
        self._api_hash = api_hash
        self._session = Session()

    def connect(self, dc_id=2):
        if not self._session.create(api_id=self._api_id, api_hash=self._api_hash):
            return False
        return self._session.connect(dc_id)

    def disconnect(self):
        self._session.destroy()

    @property
    def api_id(self):
        return self._api_id

    def call(self, method: str, params: dict = None) -> dict:
        """Execute an MTProto API method.

        Args:
            method: e.g. "auth.sendCode", "messages.sendMessage"
            params: Parameters as dict with field names matching the TL schema

        Returns:
            Parsed TL response as dict
        """
        if params is None:
            params = {}

        # 1. Build method body using schema args for field ordering
        tl = TL()

        # Write constructor
        cons = FUNCTIONS.get(method)
        if cons is None:
            raise ValueError(f"Unknown method: {method}")
        tl.write_uint(cons)

        # Get schema args for field ordering
        schema_args = TL_SCHEMA.get(method, [])
        flags_mask = 0

        # First pass: calculate flags
        for arg in schema_args:
            if arg.get('is_flag'):
                continue
            cond = arg.get('cond')
            if cond is not None:
                fn = arg['name']
                if fn in params and params[fn] is not None:
                    flags_mask |= (1 << cond)

        # Second pass: write fields in schema order
        for arg in schema_args:
            if arg.get('is_flag'):
                tl.write_uint(flags_mask)
                continue

            fn = arg['name']
            cond = arg.get('cond')
            if cond is not None and not (flags_mask & (1 << cond)):
                continue

            value = params.get(fn)
            if value is None and cond is not None:
                continue

            tl._write_field(arg, value, flags_mask)

        # 2. Wrap in initConnection + invokeWithLayer
        wrapped = self._build_invoke_with_layer(tl.data)

        # 3. Send through encrypted session
        result_bytes = self._session.encrypted_call(bytes(wrapped))
        if result_bytes is None:
            return {"error": "RPC call failed", "_rpc_error": True}

        # 4. Parse response
        return self._parse_response(result_bytes)

    def _build_invoke_with_layer(self, body):
        """Wrap in invokeWithLayer + initConnection as tdesktop does."""
        tl = TL()
        tl.write_uint(0xda9b0d0d)  # invokeWithLayer
        tl.write_int(177)
        tl.write_uint(0xc1cd5ea9)  # initConnection
        tl.write_uint(2)            # flags: has params
        tl.write_int(self._api_id)
        tl.write_string("Desktop PC")
        tl.write_string("Windows 10")
        tl.write_string("7.0.1")
        tl.write_string("en")
        tl.write_string("tdesktop")
        tl.write_string("en")
        # params: tz_offset
        tl.write_uint(0x99c1d49d)   # jsonObject
        tl.write_string("tz_offset")
        tl.write_uint(0x2be0df57)   # jsonNumber
        tl.write_double(10800.0)     # UTC+3
        tl.data += body
        return bytes(tl.data)

    def _parse_response(self, data):
        """Parse TL response into Python dict."""
        result = {}
        pos = [0]

        try:
            cons = TL.read_uint(data, pos)
            result["_"] = hex(cons)

            # Check for rpc_result wrapper
            if cons == 0xf35c6d01:  # rpc_result
                req_msg_id = TL.read_long(data, pos)
                result["_req_msg_id"] = req_msg_id
                # Next is the actual response object
                if pos[0] < len(data):
                    inner = self._parse_object(data, pos)
                    result.update(inner)

            elif cons == 0x2144ca19:  # rpc_error
                error_code = TL.read_int(data, pos)
                error_msg = TL.read_string(data, pos)
                result["_type"] = "rpc_error"
                result["error_code"] = error_code
                result["error_message"] = error_msg

            else:
                result["_hex"] = data.hex()

        except Exception as e:
            result["_parse_error"] = str(e)
            result["_hex"] = data.hex()

        return result

    def _parse_object(self, data, pos):
        """Parse a TL object from response data."""
        result = {}
        if pos[0] >= len(data):
            return result

        cons = TL.read_uint(data, pos)
        result["_"] = hex(cons)
        return result

    def __del__(self):
        self.disconnect()
