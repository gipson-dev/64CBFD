#include <ultra64.h>
extern f32 D_800AA570;
extern f32 D_800AA56C;

/* Non-matching placeholders for the text-only asm slice asm/1E6260.s. */

s32 func_151B8DB0() {
    return 0;
}

s32 func_151B9214() {
    return 0;
}

s32 func_151B9310() {
    return 0;
}

s32 func_151B9408() {
    return 0;
}

void func_151B9660(u8 *arg0) {
    *(f32 *) (arg0 + 0x188) = 5.0f;
    *(f32 *) (arg0 + 0x18C) = D_800AA56C;
    *(f32 *) (arg0 + 0x190) = D_800AA570;
}
