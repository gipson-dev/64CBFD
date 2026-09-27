#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/21D420.s. */

void *memcpy(void *dst, const void *src, unsigned int len);
s32 func_100020D0();

u8 *func_151EFF70(void *arg0, void *arg1, s32 arg2) {
    return (u8 *) memcpy(arg0, arg1, arg2) + arg2;
}

s32 func_151EFF94(u8 *arg0, u8 *arg1, ...) {
    s32 ret = func_100020D0(func_151EFF70, arg0, arg1, &arg1 + 1);

    if (ret >= 0) {
        arg0[ret] = 0;
    }
    return ret;
}
