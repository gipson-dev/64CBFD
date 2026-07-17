#include <os_internal.h>

extern s32 D_8002BE20;
extern OSMesg D_80042AA0[1];
extern OSMesgQueue D_80042AA8;

void __osSiCreateAccessQueue(void) {
    D_8002BE20 = 1;
    osCreateMesgQueue(&D_80042AA8, D_80042AA0, 1);
    osSendMesg(&D_80042AA8, 0, OS_MESG_NOBLOCK);
}

void __osSiGetAccess(void) {
    OSMesg msg;

    if (!D_8002BE20) {
        __osSiCreateAccessQueue();
    }
    osRecvMesg(&D_80042AA8, &msg, OS_MESG_BLOCK);
}

void __osSiRelAccess(void) {
    osSendMesg(&D_80042AA8, 0, OS_MESG_NOBLOCK);
}
