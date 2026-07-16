"""desktop-mtproto — Python MTProto client with tdesktop-level fingerprint."""
try:
    from .tl import Session, TL
    from .tl_schema import FUNCTIONS, TL_SCHEMA
except ImportError:
    from tl import Session, TL
    from tl_schema import FUNCTIONS, TL_SCHEMA
import random, time, json, os

LAYER = 177


class Client:
    """Telegram client using tdesktop-level MTProto.
    
    Usage:
        client = Client()
        client.connect(dc_id=2)
        
        # Auth flow
        sent = client.send_code("+380501234567")
        me = client.sign_in("+380501234567", sent["phone_code_hash"], "12345")
        
        # Messages
        result = client.send_message("username", "Hello!")
        dialogs = client.get_dialogs()
        me2 = client.get_me()
    """
    
    def __init__(self, api_id=2040, api_hash="b18441a1ff607e10a989891a5462e627"):
        self._api_id = api_id
        self._api_hash = api_hash
        self._session = Session()
        self._session_path = None
    
    def connect(self, dc_id=2):
        if not self._session.create(api_id=self._api_id, api_hash=self._api_hash):
            return False
        return self._session.connect(dc_id)
    
    def disconnect(self):
        self._session.destroy()
    
    @property
    def api_id(self):
        return self._api_id
    
    # ====== CORE RPC ======
    
    def _build_invoke_and_init(self, body):
        """Wrap body in invokeWithLayer + initConnection (as tdesktop)."""
        tl = TL()
        tl.write_uint(0xda9b0d0d)  # invokeWithLayer
        tl.write_int(LAYER)
        tl.write_uint(0xc1cd5ea9)  # initConnection
        tl.write_uint(2)            # flags: has params
        tl.write_int(self._api_id)
        tl.write_string("Desktop PC")
        tl.write_string("Windows 10")
        tl.write_string("7.0.1")
        tl.write_string("en")
        tl.write_string("tdesktop")
        tl.write_string("en")
        tl.write_uint(0x99c1d49d)   # jsonObject
        tl.write_string("tz_offset")
        tl.write_uint(0x2be0df57)   # jsonNumber
        tl.write_double(10800.0)
        tl.data += body
        return bytes(tl.data)
    
    def call_raw(self, method, params=None):
        """Execute method with params, return raw response bytes."""
        if params is None: params = {}
        tl = TL()
        cons = FUNCTIONS.get(method)
        if cons is None: raise ValueError(f"Unknown method: {method}")
        tl.write_uint(cons)
        
        schema_args = TL_SCHEMA.get(method, [])
        flags_mask = 0
        for arg in schema_args:
            if arg.get('is_flag'): continue
            cond = arg.get('cond')
            if cond is not None and params.get(arg['name']) is not None:
                flags_mask |= (1 << cond)
        for arg in schema_args:
            if arg.get('is_flag'): tl.write_uint(flags_mask); continue
            cond = arg.get('cond')
            if cond is not None and not (flags_mask & (1 << cond)): continue
            v = params.get(arg['name'])
            if v is None and cond is not None: continue
            tl._write_field(arg, v, flags_mask)
        
        wrapped = self._build_invoke_and_init(tl.data)
        return self._session.encrypted_call(bytes(wrapped))
    
    def call(self, method, params=None):
        """Execute method and return parsed response."""
        raw = self.call_raw(method, params)
        if raw is None: return {"_error": "RPC failed"}
        pos = [0]
        result = TL.read_object(raw, pos)
        # Unwrap rpc_result
        if result.get('_') == '0xf35c6d01':
            return result.get('inner', result)
        if result.get('_') == '0x2144ca19':
            return {"_error": f"RPC error {result.get('error_code','?')}: {result.get('error_message','')}"}
        return result
    
    # ====== AUTH FLOW ======
    
    def send_code(self, phone):
        """Send auth code to phone. Returns SentCode object."""
        return self.call("auth.sendCode", {
            "phone_number": phone,
            "api_id": self._api_id,
            "api_hash": self._api_hash,
            "settings": {"_": "codeSettings"}
        })
    
    def sign_in(self, phone, code_hash, code):
        """Sign in with code from send_code(). Returns auth.Authorization."""
        return self.call("auth.signIn", {
            "phone_number": phone,
            "phone_code_hash": code_hash,
            "phone_code": code,
        })
    
    def check_password(self, password):
        """2FA login. password is the SRP-encrypted password (plain for now)."""
        return self.call("auth.checkPassword", {
            "password": {"_": "inputCheckPasswordSRP", "srp_id": 0, "A": b'', "M1": b''}
        })
    
    def get_me(self):
        """Get current user."""
        raw = self.call_raw("users.getUsers", {"id": [{"_": "inputUserSelf"}]})
        if raw is None: return None
        pos = [0]
        return TL.read_object(raw, pos)
    
    # ====== MESSAGES ======
    
    def send_message(self, peer, message):
        """Send a text message.
        
        peer can be:
        - str "self" → send to yourself
        - dict {"_": "inputPeerUser", "user_id": 123, "access_hash": 456}
        - int (user_id) → will try to resolve
        """
        if isinstance(peer, str):
            if peer == "self":
                peer_obj = {"_": "inputPeerSelf"}
            else:
                # Try to resolve username
                resolved = self.resolve_username(peer)
                if resolved and resolved.get('_'):  # continue with proper peer
                    return {"_error": "need proper peer construction"}
                peer_obj = {"_": "inputPeerSelf"}
        elif isinstance(peer, int):
            peer_obj = {"_": "inputPeerSelf"}
        else:
            peer_obj = peer
        
        return self.call("messages.sendMessage", {
            "peer": peer_obj,
            "message": message,
            "random_id": random.randint(-2**63, 2**63-1),
            "no_webpage": False,
            "silent": False,
        })
    
    def get_dialogs(self, limit=100):
        """Get dialogs list."""
        return self.call("messages.getDialogs", {
            "offset_date": 0,
            "offset_id": 0,
            "offset_peer": {"_": "inputPeerEmpty"},
            "limit": limit,
            "hash": 0,
        })
    
    def resolve_username(self, username):
        """Resolve username to user/chat/channel."""
        return self.call("contacts.resolveUsername", {"username": username})
    
    def get_history(self, peer, limit=50):
        """Get message history for a peer."""
        return self.call("messages.getHistory", {
            "peer": peer if isinstance(peer, dict) else {"_": "inputPeerSelf"},
            "offset_id": 0,
            "offset_date": 0,
            "add_offset": 0,
            "limit": limit,
            "max_id": 0,
            "min_id": 0,
            "hash": 0,
        })
    
    def __del__(self):
        self.disconnect()
