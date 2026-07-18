#include <ultra64.h>
#include "controller.h"

#ifdef osContInit
#undef osContInit
#endif
#ifdef __osContGetInitData
#undef __osContGetInitData
#endif
#ifdef __osPackRequestData
#undef __osPackRequestData
#endif

/* Non-matching C placeholders for C:/Users/grego/OneDrive/Desktop/.vscode/64CBFD/conker/asm/libultra/io/controller.s. */

s32 osContInit(OSMesgQueue *arg0, u8 *arg1, OSContStatus *arg2) {
    return 0;
}

void __osContGetInitData(u8 *pattern, OSContStatus *data) {
}

void __osPackRequestData(u8 cmd) {
}
