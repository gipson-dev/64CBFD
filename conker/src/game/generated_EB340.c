#include <ultra64.h>
extern f32 D_800BE9A4;

/* Non-matching placeholders for the text-only asm slice asm/EB340.s. */

s32 func_150BDE90() {
    return 0;
}

s32 func_150BDF0C() {
    return 0;
}

s32 func_150BE150() {
    return 0;
}

s32 func_150BE1C4(u8 *arg0) {
    *(f32 *) (arg0 + 0x14) = *(f32 *) (arg0 + 0x80) * D_800BE9A4 + *(f32 *) (arg0 + 0x14);
    if (120.0f < *(f32 *) (arg0 + 0x14)) {
        return 0;
    }
    return 1;
}

s32 func_150BE210() {
    return 0;
}

s32 func_150BE2E8() {
    return 0;
}

s32 func_150BE438() {
    return 0;
}

s32 func_150BE494() {
    return 0;
}
