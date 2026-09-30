#include <ultra64.h>
#include "controller.h"

#ifdef osSetIntMask
#undef osSetIntMask
#endif

/* Non-matching C placeholders for C:/Users/grego/OneDrive/Desktop/.vscode/64CBFD/conker/asm/libultra/os/setintmask.s. */

#if 0
OSIntMask osSetIntMask(OSIntMask arg0) {
    return 0;
}
#endif
#pragma GLOBAL_ASM("asm/nonmatchings/generated_setintmask/osSetIntMask.s")
