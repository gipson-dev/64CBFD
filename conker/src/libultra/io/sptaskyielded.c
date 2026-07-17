#include <os_internal.h>
#include <rcp.h>
#include <sptask.h>

u32 __osSpGetStatus(void);

OSYieldResult osSpTaskYielded(OSTask *task) {
    u32 status;
    OSYieldResult result;

    status = __osSpGetStatus();
    result = (status & SP_STATUS_YIELDED) ? OS_TASK_YIELDED : 0;
    if (status & SP_STATUS_YIELD) {
        task->t.flags |= result;
        task->t.flags &= ~OS_TASK_DP_WAIT;
    }
    return result;
}
