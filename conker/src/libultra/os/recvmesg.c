#include <os_internal.h>
#include "osint.h"

extern void func_100078B4(OSThread **queue);
extern OSThread *func_10007A24(OSThread **queue);

s32 osRecvMesg(OSMesgQueue *mq, OSMesg *msg, s32 flags) {
    u32 saveMask;

    saveMask = __osDisableInt();

    while (MQ_IS_EMPTY(mq)) {
        if (flags == OS_MESG_NOBLOCK) {
            __osRestoreInt(saveMask);
            return -1;
        }

        __osRunningThread->state = OS_STATE_WAITING;
        func_100078B4(&mq->mtqueue);
    }

    if (msg != 0) {
        *msg = mq->msg[mq->first];
    }

    mq->first = (mq->first + 1) % mq->msgCount;
    mq->validCount--;

    if (mq->fullqueue->next != 0) {
        osStartThread(func_10007A24(&mq->fullqueue));
    }

    __osRestoreInt(saveMask);
    return 0;
}
