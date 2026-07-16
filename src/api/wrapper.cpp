// tdesktop-mtproto API wrapper
#include <mtproto/core_types.h>
#include <mtproto/facade.h>

extern "C" {
    __declspec(dllexport) const char* mtproto_version() {
        return "0.1.0";
    }
}
