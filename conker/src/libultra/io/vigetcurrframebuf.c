#include <os_internal.h>

typedef struct {
    u16 state;
    u16 retraceCount;
    void *framep;
} OSViContextHead;

extern OSViContextHead *D_8002BDE0;

void *osViGetCurrentFramebuffer(void) {
    register u32 saveMask;
    void *framep;

    saveMask = __osDisableInt();
    framep = D_8002BDE0->framep;
    __osRestoreInt(saveMask);
    return framep;
}
