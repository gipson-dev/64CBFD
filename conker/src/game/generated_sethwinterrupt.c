#include <ultra64.h>
#include "controller.h"

#ifdef __osSetHWIntrRoutine
#undef __osSetHWIntrRoutine
#endif

/* Non-matching C placeholders for C:/Users/grego/OneDrive/Desktop/.vscode/64CBFD/conker/asm/libultra/os/sethwinterrupt.s. */

void __osSetHWIntrRoutine(OSHWIntr interrupt, s32 (*handler)(void)) {
}
