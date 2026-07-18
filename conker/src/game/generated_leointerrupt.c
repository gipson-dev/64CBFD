#include <ultra64.h>
#include "controller.h"

#ifdef __osLeoInterrupt
#undef __osLeoInterrupt
#endif
#ifdef __osLeoAbnormalResume
#undef __osLeoAbnormalResume
#endif
#ifdef __osLeoResume
#undef __osLeoResume
#endif

/* Non-matching C placeholders for C:/Users/grego/OneDrive/Desktop/.vscode/64CBFD/conker/asm/libultra/io/leointerrupt.s. */

s32 __osLeoInterrupt() {
    return 0;
}

s32 __osLeoAbnormalResume() {
    return 0;
}

s32 __osLeoResume() {
    return 0;
}
