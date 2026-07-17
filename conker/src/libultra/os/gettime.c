#include <os_internal.h>

extern OSTime D_800429B0;
extern u32 D_800429B8;

OSTime osGetTime(void) {
    u32 tmptime;
    u32 elapsedCount;
    OSTime currentCount;
    u32 saveMask;

    saveMask = __osDisableInt();
    tmptime = osGetCount();
    elapsedCount = tmptime - D_800429B8;
    currentCount = D_800429B0;
    __osRestoreInt(saveMask);
    return currentCount + elapsedCount;
}
