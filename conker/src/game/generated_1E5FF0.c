#include <ultra64.h>

extern f32 D_800BE9A4;
f32 func_15144B68(f32 arg0);

/* Non-matching placeholders for the text-only asm slice asm/1E5FF0.s. */

s32 func_151B8B40() {
    return 0;
}

void func_151B8BE0(u8 *arg0, s32 arg1) {
    *(f32 *) (arg0 + 0x44) = sinf(*(f32 *) (arg0 + 0x58)) *
        *(f32 *) (arg0 + 0x64) + *(f32 *) (arg0 + 0x5C);
    *(f32 *) (arg0 + 0x58) += *(f32 *) (arg0 + 0x60) * D_800BE9A4;
    *(f32 *) (arg0 + 0x58) = func_15144B68(*(f32 *) (arg0 + 0x58));
    func_151D9450(arg0, arg1);
}

s32 func_151B8C54() {
    return 0;
}

s32 func_151B8CFC() {
    return 0;
}
