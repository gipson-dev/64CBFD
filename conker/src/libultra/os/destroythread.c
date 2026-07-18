#include <os_internal.h>
#include "osint.h"

extern void func_10007A38(void);

void osDestroyThread(OSThread *t) {
    register u32 saveMask;
    register OSThread *pred;
    register OSThread *succ;

    saveMask = __osDisableInt();

    if (t == 0) {
        t = __osRunningThread;
    } else if (t->state != OS_STATE_STOPPED) {
        __osDequeueThread(t->queue, t);
    }

    if (__osActiveQueue == t) {
        __osActiveQueue = __osActiveQueue->tlnext;
    } else {
        pred = __osActiveQueue;
        succ = pred->tlnext;
        while (succ != 0) {
            if (succ == t) {
                pred->tlnext = t->tlnext;
                break;
            }

            pred = succ;
            succ = pred->tlnext;
        }
    }

    if (t == __osRunningThread) {
        func_10007A38();
    }

    __osRestoreInt(saveMask);
}
