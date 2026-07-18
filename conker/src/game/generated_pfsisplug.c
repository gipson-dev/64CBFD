#include <ultra64.h>
#include "controller.h"

#ifdef osPfsIsPlug
#undef osPfsIsPlug
#endif
#ifdef __osPfsRequestData
#undef __osPfsRequestData
#endif
#ifdef __osPfsGetInitData
#undef __osPfsGetInitData
#endif

/* Non-matching C placeholders for C:/Users/grego/OneDrive/Desktop/.vscode/64CBFD/conker/asm/libultra/io/pfsisplug.s. */

s32 osPfsIsPlug(OSMesgQueue *arg0, u8 *arg1) {
    return 0;
}

void __osPfsRequestData(u8 cmd) {
}

void __osPfsGetInitData(u8* pattern, OSContStatus* data) {
}
