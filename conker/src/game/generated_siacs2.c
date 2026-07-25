#include <ultra64.h>
extern s32 D_8002BE20;
extern OSMesgQueue D_80042AA8;
extern OSMesg D_800E0D20[1];
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

void __osSiCreateAccessQueue2(void) {
    D_8002BE20 = 1;
    osCreateMesgQueue(&D_80042AA8, D_800E0D20, 1);
    osSendMesg(&D_80042AA8, NULL, 0);
}

void __osSiGetAccess2(void) {
    OSMesg dummyMesg;
    if (!D_8002BE20) {
        __osSiCreateAccessQueue();
    }
    osRecvMesg(&D_80042AA8, &dummyMesg, OS_MESG_BLOCK);
}

void __osSiRelAccess2(void) {
    osSendMesg(&D_80042AA8, NULL, 0);
}
