#include <os_internal.h>
#include "osint.h"

extern __OSEventState D_80042910[OS_NUM_EVENTS];

void osSetEventMesg(OSEvent event, OSMesgQueue *mq, OSMesg msg) {
    u32 saveMask;
    __OSEventState *state;

    saveMask = __osDisableInt();
    state = &D_80042910[event];
    state->messageQueue = mq;
    state->message = msg;
    __osRestoreInt(saveMask);
}
