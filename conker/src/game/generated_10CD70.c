#include <ultra64.h>
extern f32 D_800A0FB0;

/* Non-matching placeholders for the text-only asm slice asm/10CD70.s. */

s32 func_150DF8C0() {
    return 0;
}

s32 func_150DF920() {
    return 0;
}

s32 func_150DFBD0() {
    return 0;
}

s32 func_150DFCA8() {
    return 0;
}

void func_150DFDA4(u8 *arg0) {
    u8 *temp_v0 = *(u8 **) (arg0 + 0x1D4) + 0x40;

    *(f32 *) (temp_v0 + 0x30) = *(f32 *) (arg0 + 0x14);
    *(f32 *) (temp_v0 + 0x34) = D_800A0FB0;
    *(f32 *) (temp_v0 + 0x38) = *(f32 *) (arg0 + 0x1C);
}

s32 func_150DFDD0() {
    return 0;
}

s32 func_150DFEFC() {
    return 0;
}

void func_150E02C0(u8 *arg0, s32 arg1, u8 arg2) {
    func_15149514(arg1, arg2, (s32) (arg0 + 0x28), (s32) (arg0 + 0x2C), (s32) arg0);
}

s32 func_150E0300() {
    return 0;
}

s32 func_150E0348() {
    return 0;
}

s32 func_150E03F8() {
    return 0;
}

s32 func_150E05F8() {
    return 0;
}

s32 func_150E06D8() {
    return 0;
}
