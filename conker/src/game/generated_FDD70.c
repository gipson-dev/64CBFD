#include <ultra64.h>
extern f32 D_800A0894;
f32 func_150ADA68();

/* Non-matching placeholders for the text-only asm slice asm/FDD70.s. */

s32 func_150D08C0() {
    return 0;
}

s32 func_150D0E90() {
    return 0;
}

s32 func_150D10E4() {
    return 0;
}

s32 func_150D11B4(u8 *arg0) {
    *(f32 *) (arg0 + 0x74) = (func_150ADA68() * 150.0f + 350.0f) * D_800A0894;
    return 1;
}

s32 func_150D1204() {
    return 0;
}
