#include <ultra64.h>
#include "controller.h"

#ifdef osPfsInit
#undef osPfsInit
#endif
#ifdef __osPfsGetStatus
#undef __osPfsGetStatus
#endif

/* Non-matching C placeholders for C:/Users/grego/OneDrive/Desktop/.vscode/64CBFD/conker/asm/libultra/io/pfsinit.s. */

s32 osPfsInit(OSMesgQueue *arg0, OSPfs *arg1, int arg2) {
    return 0;
}

s32 __osPfsGetStatus(OSMesgQueue *queue, int channel) {
    return 0;
}
