#include <os_internal.h>
#include "osint.h"

extern void func_100078B4(OSThread **queue);

void osStopThread(OSThread *t) {
    u32 saveMask;
    u16 state;

    saveMask = __osDisableInt();
    state = (t == 0) ? OS_STATE_RUNNING : t->state;

    switch (state) {
        case OS_STATE_RUNNING:
            __osRunningThread->state = OS_STATE_STOPPED;
            func_100078B4(0);
            break;

        case OS_STATE_RUNNABLE:
        case OS_STATE_WAITING:
            t->state = OS_STATE_STOPPED;
            __osDequeueThread(t->queue, t);
            break;
    }

    __osRestoreInt(saveMask);
}
