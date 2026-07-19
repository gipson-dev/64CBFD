#include <ultra64.h>
extern s32 D_8002BE20;
extern OSMesgQueue D_80042AA8;
#include "controller.h"

#ifdef __osSiCreateAccessQueue2
#undef __osSiCreateAccessQueue2
#endif
#ifdef __osSiGetAccess2
#undef __osSiGetAccess2
#endif
#ifdef __osSiRelAccess2
#undef __osSiRelAccess2
#endif

/* Non-matching C placeholders for C:/Users/grego/OneDrive/Desktop/.vscode/64CBFD/conker/asm/libultra/io/siacs2.s. */

s32 __osSiCreateAccessQueue2() {
    return 0;
}

void __osSiGetAccess2(void) {
    OSMesg mesg;

    if (D_8002BE20 == 0) {
        __osSiCreateAccessQueue();
    }
    osRecvMesg(&D_80042AA8, &mesg, 1);
}

s32 __osSiRelAccess2() {
    return 0;
}
