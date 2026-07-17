#include <os_internal.h>
#include "osint.h"

extern OSThread *D_8002BDF8;
extern void func_100078B4(OSThread **queue);
extern void func_100079D8(OSThread **queue, OSThread *thread);

void osSetThreadPri(OSThread *t, OSPri pri) {
    u32 saveMask;

    saveMask = __osDisableInt();

    if (t == 0) {
        t = __osRunningThread;
    }

    if (t->priority != pri) {
        t->priority = pri;

        if ((t != __osRunningThread) && (t->state != OS_STATE_STOPPED)) {
            __osDequeueThread(t->queue, t);
            func_100079D8(t->queue, t);
        }

        if (__osRunningThread->priority < D_8002BDF8->priority) {
            __osRunningThread->state = OS_STATE_RUNNABLE;
            func_100078B4(&D_8002BDF8);
        }
    }

    __osRestoreInt(saveMask);
}
