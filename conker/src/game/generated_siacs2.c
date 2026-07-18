#include <ultra64.h>
#include "controller.h"

#ifdef __osSiCreateAccessQueue2
#undef __osSiCreateAccessQueue2
#endif
#ifdef __osSiGetAccess2
#undef __osSiGetAccess2
#endif
#ifdef __osSiRelAccess2
#undef __osSiRelAccess2
#endif

/* Non-matching C placeholders for C:/Users/grego/OneDrive/Desktop/.vscode/64CBFD/conker/asm/libultra/io/siacs2.s. */

s32 __osSiCreateAccessQueue2() {
    return 0;
}

s32 __osSiGetAccess2() {
    return 0;
}

s32 __osSiRelAccess2() {
    return 0;
}
