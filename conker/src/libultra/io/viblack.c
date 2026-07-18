#include <os_internal.h>

typedef struct {
    u16 state;
} OSViContextState;

extern OSViContextState *D_8002BDE4;

void osViBlack(u8 active) {
    register u32 saveMask;

    saveMask = __osDisableInt();
    if (active) {
        D_8002BDE4->state |= 0x20;
    } else {
        D_8002BDE4->state &= ~0x20;
    }
    __osRestoreInt(saveMask);
}
