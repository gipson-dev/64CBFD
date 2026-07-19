#include <ultra64.h>
extern u8 D_80089470[];

/* Non-matching placeholders for the text-only asm slice asm/193E50.s. */

s32 func_151669A0() {
    return 0;
}

s32 func_15166B50() {
    return 0;
}

s32 func_15166D68() {
    return 0;
}

s32 func_15166F6C() {
    return 0;
}

Gfx *func_15166FD8(Gfx *arg0, u8 arg1, u8 arg2) {
    Gfx *g = arg0++;

    g->words.w0 = 0xDA380003;
    g->words.w1 = (u32) D_80089470;
    return arg0;
}
