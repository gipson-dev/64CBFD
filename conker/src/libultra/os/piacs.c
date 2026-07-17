#include <os_internal.h>
#include "piint.h"

extern OSMesg D_800428F0[1];

void __osPiCreateAccessQueue(void) {
    __osPiAccessQueueEnabled = 1;
    osCreateMesgQueue(&__osPiAccessQueue, D_800428F0, 1);
    osSendMesg(&__osPiAccessQueue, 0, OS_MESG_NOBLOCK);
}

void __osPiGetAccess(void) {
    OSMesg msg;

    if (!__osPiAccessQueueEnabled) {
        __osPiCreateAccessQueue();
    }
    osRecvMesg(&__osPiAccessQueue, &msg, OS_MESG_BLOCK);
}

void __osPiRelAccess(void) {
    osSendMesg(&__osPiAccessQueue, 0, OS_MESG_NOBLOCK);
}
