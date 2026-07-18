#include <os_internal.h>
#include "osint.h"

extern OSThread *D_8002BDF8;
extern void func_100078B4(OSThread **queue);
extern void func_100079D8(OSThread **queue, OSThread *thread);
extern OSThread *func_10007A24(OSThread **queue);
extern void func_10007A38(void);

void osStartThread(OSThread *t) {
    register u32 saveMask;

    saveMask = __osDisableInt();

    switch (t->state) {
        case OS_STATE_WAITING:
            t->state = OS_STATE_RUNNABLE;
            func_100079D8(&D_8002BDF8, t);
            break;

        case OS_STATE_STOPPED:
            if ((t->queue == 0) || (t->queue == &D_8002BDF8)) {
                t->state = OS_STATE_RUNNABLE;
                func_100079D8(&D_8002BDF8, t);
            } else {
                t->state = OS_STATE_WAITING;
                func_100079D8(t->queue, t);
                func_100079D8(&D_8002BDF8, func_10007A24(t->queue));
            }
            break;
    }

    if (__osRunningThread == 0) {
        func_10007A38();
    } else if (__osRunningThread->priority < D_8002BDF8->priority) {
        __osRunningThread->state = OS_STATE_RUNNABLE;
        func_100078B4(&D_8002BDF8);
    }

    __osRestoreInt(saveMask);
}
