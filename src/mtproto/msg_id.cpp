#include "tdesktop_mtproto/mtproto.h"
#include <ctime>

namespace tdesktop::mtproto {

// Generate msg_id EXACTLY as tdesktop does:
// base::unixtime::mtproto_msg_id() = (uint64)time(nullptr) << 32
// NO randomization of lower bits (unlike TDLib which XORs with 22 random bits)
//
// Monotonicity is enforced by the Session class:
// if newId <= lastMsgId: newId = lastMsgId + 4
int64_t generate_msg_id() {
    return (int64_t)((uint64_t)std::time(nullptr) << 32);
}

bool is_even_msg_id(int64_t msg_id) {
    return (msg_id & 3) == 0;
}

} // namespace tdesktop::mtproto
