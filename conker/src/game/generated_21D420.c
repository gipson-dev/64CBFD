#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/21D420.s. */

void *memcpy(void *dst, const void *src, unsigned int len);

u8 *func_151EFF70(void *arg0, void *arg1, s32 arg2) {
    return (u8 *) memcpy(arg0, arg1, arg2) + arg2;
}

s32 func_151EFF94() {
    return 0;
}
