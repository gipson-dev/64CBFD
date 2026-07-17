#include <os_internal.h>

typedef struct {
    u16 state;
    u16 retraceCount;
    void *framep;
} OSViContextHead;

extern OSViContextHead *D_8002BDE4;

void osViSwapBuffer(void *frameBufPtr) {
    u32 saveMask;

    saveMask = __osDisableInt();
    D_8002BDE4->framep = frameBufPtr;
    D_8002BDE4->state |= 0x10;
    __osRestoreInt(saveMask);
}
