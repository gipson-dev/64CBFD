#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/21C4F0.s. */

s32 func_151EF040(s32 arg0, s32 arg1) {
    register s32 ret;

    __osPiGetAccess();
    ret = osPiRawReadIo(arg0, arg1);
    __osPiRelAccess();
    return ret;
}

f32 func_151EF080(f32 arg0) {
    return sqrtf(arg0);
}
