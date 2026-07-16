"""desktop-mtproto - Python TL serialization layer + C++ MTProto engine."""
from .tl import Session, TL

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
        """Execute an MTProto API method and return parsed response.

        Args:
            method: e.g. "auth.sendCode", "messages.sendMessage"
            params: Parameters for the method as a dict

        Returns:
            Parsed TL response as nested dicts
        """
        # 1. Build the raw method call body
        tl = TL()
        
        # Write constructor number
        from .tl_constructors import FUNCTIONS
        cons = FUNCTIONS.get(method)
        if cons is None:
            raise ValueError(f"Unknown method: {method}")
        tl.write_uint(cons)
        
        # Write parameters according to TL schema
        if params:
            # For simple methods, write params in order as TL values
            # Complex methods need proper schema parsing
            for key, value in params.items():
                tl.write_value(value)

        # 2. Wrap in initConnection (for stateful methods)
        wrapped = self._build_invoke_with_layer(tl.data)

        # 3. Send through encrypted session
        result_bytes = self._session.encrypted_call(bytes(wrapped))
        if result_bytes is None:
            return {"error": "RPC call failed"}

        # 4. Parse response
        return self._parse_response(result_bytes)

    def _build_invoke_with_layer(self, body: bytes) -> bytes:
        """Wrap in invokeWithLayer + initConnection as tdesktop does."""
        tl = TL()
        tl.write_uint(0xda9b0d0d)  # invokeWithLayer
        tl.write_int(177)           # layer version
        tl.write_uint(0xc1cd5ea9)  # initConnection
        tl.write_uint(2)            # flags (has params)
        tl.write_int(self._api_id)
        tl.write_string("Desktop PC")
        tl.write_string("Windows 10")
        tl.write_string("7.0.1")
        tl.write_string("en")       # system_lang_code
        tl.write_string("tdesktop") # lang_pack
        tl.write_string("en")       # lang_code
        # params: tz_offset
        tl.write_uint(0x99c1d49d)   # jsonObject
        tl.write_string("tz_offset")
        tl.write_uint(0x2be0df57)   # jsonNumber
        tl.write_double(10800.0)    # UTC+3
        tl.data += body
        return bytes(tl.data)

    def _parse_response(self, data: bytes) -> dict:
        """Parse TL response into Python dict."""
        if not data or len(data) < 4:
            return {"error": "empty response"}
        
        # Simple response parser - for complex types we need full schema
        result = {"_raw": data.hex()}
        pos = [0]
        
        try:
            cons = TL.read_uint(data, pos)
            result["_constructor"] = hex(cons)
            
            # Try to identify common response types
            if cons == 0xf35c6d01:  # rpc_result
                result["_type"] = "rpc_result"
            elif cons == 0x2144ca19:  # rpc_error
                result["_type"] = "rpc_error"
                
            result["_hex"] = data.hex()
        except:
            pass
        
        return result

    def __del__(self):
        self.disconnect()
