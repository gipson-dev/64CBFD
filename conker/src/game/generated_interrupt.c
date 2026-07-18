#include <ultra64.h>
#include "controller.h"

#ifdef __osDisableInt
#undef __osDisableInt
#endif
#ifdef __osRestoreInt
#undef __osRestoreInt
#endif

/* Non-matching C placeholders for C:/Users/grego/OneDrive/Desktop/.vscode/64CBFD/conker/asm/libultra/os/interrupt.s. */

u32 __osDisableInt(void) {
    return 0;
}

void __osRestoreInt(u32 arg0) {
}
