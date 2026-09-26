#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/13AE20.s. */

s32 func_1510D970() {
    return 0;
}

s32 func_1510DA84() {
    return 0;
}

s32 func_1510E120() {
    return 0;
}

s32 func_1510E388() {
    return 0;
}

/* Note 317: guarded expansion preserves the retail display-list cursor lifetime. */
Gfx *func_1510E634(Gfx *arg0, s32 arg1, s32 arg2) {
    extern u8 D_80089470[];
    Gfx *g = arg0++;

    g->words.w0 = 0xDA380003;
    g->words.w1 = (u32) D_80089470;
    return arg0;
}
