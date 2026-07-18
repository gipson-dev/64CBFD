#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/1C0B10.s. */

extern f32 D_800A81E8;

s32 func_15193660() {
    return 0;
}

s32 func_151937F4() {
    return 0;
}

s32 func_151938E4(u8 *arg0) {
    *(f32 *)(arg0 + 0x74) = D_800A81E8;
    return 1;
}

s32 func_151938FC() {
    return 0;
}
