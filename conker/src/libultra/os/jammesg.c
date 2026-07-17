#include <os_internal.h>
#include "osint.h"

extern void func_100078B4(OSThread **queue);
extern OSThread *func_10007A24(OSThread **queue);

s32 osJamMesg(OSMesgQueue *mq, OSMesg msg, s32 flags) {
    u32 saveMask;

    saveMask = __osDisableInt();

    while (MQ_IS_FULL(mq)) {
        if (flags == OS_MESG_BLOCK) {
            __osRunningThread->state = OS_STATE_WAITING;
            func_100078B4(&mq->fullqueue);
        } else {
            __osRestoreInt(saveMask);
            return -1;
        }
    }

    mq->first = (mq->first + mq->msgCount - 1) % mq->msgCount;
    mq->msg[mq->first] = msg;
    mq->validCount++;

    if (mq->mtqueue->next != 0) {
        osStartThread(func_10007A24(&mq->mtqueue));
    }

    __osRestoreInt(saveMask);
    return 0;
}
