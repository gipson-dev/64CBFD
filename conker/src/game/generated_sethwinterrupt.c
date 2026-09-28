#include <ultra64.h>
#include "controller.h"

#ifdef __osSetHWIntrRoutine
#undef __osSetHWIntrRoutine
#endif

/* Non-matching C placeholders for C:/Users/grego/OneDrive/Desktop/.vscode/64CBFD/conker/asm/libultra/os/sethwinterrupt.s. */

extern s32 (*D_8002AC70[])(void);

void __osSetHWIntrRoutine(OSHWIntr interrupt, s32 (*handler)(void)) {
    register u32 saveMask;

    saveMask = __osDisableInt();
    D_8002AC70[interrupt] = handler;
    __osRestoreInt(saveMask);
}
