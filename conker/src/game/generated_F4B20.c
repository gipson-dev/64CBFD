#include <ultra64.h>
void *memcpy(void *dst, const void *src, unsigned int len);
extern u8 D_80089470[];

/* Non-matching placeholders for the text-only asm slice asm/F4B20.s. */

s32 func_150C7670() {
    return 0;
}

s32 func_150C773C(void *arg0, u8 arg1) {
    memcpy(arg0, D_80089470, 0x40);
    return 1;
}
