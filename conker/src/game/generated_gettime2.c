#include <os_internal.h>

#ifdef getTime2
#undef getTime2
#endif

extern OSTime D_800429B0;
extern u32 D_800429B8;

OSTime getTime2(void) {
    u32 tmptime;
    u32 elapsedCount;
    OSTime currentCount;
    register u32 saveMask;

    saveMask = __osDisableInt();
    tmptime = osGetCount();
    elapsedCount = tmptime - D_800429B8;
    currentCount = D_800429B0;
    __osRestoreInt(saveMask);
    return currentCount + elapsedCount;
}
