#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/129EE0.s. */

s32 func_15103828();
f32 func_15165BB0(u8 *, f32 *, s32, s32, f32);
extern s16 *D_800D9AA0;
extern f32 D_800A1F2C;

s32 func_150FCA30() {
    return 0;
}

s32 func_150FCBC0() {
    return 0;
}

f32 func_150FCF1C(u8 *arg0) {
    f32 position[3];

    if (D_800D9AA0 == NULL) {
        return 1.0f;
    }
    position[0] = D_800D9AA0[0];
    position[1] = D_800D9AA0[1];
    position[2] = D_800D9AA0[2];
    return func_15165BB0(arg0, position, 0x44FAE000, 0x460CB400, D_800A1F2C);
}

void func_150FCFB0(s32 arg0) {
    func_15103828();
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_129EE0/func_150FCFD4.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_129EE0/func_150FD514.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_129EE0/func_150FDB0C.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_129EE0/func_150FDBA0.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_129EE0/func_150FDC2C.s")

s32 func_150FDCAC(s32 arg0) {
    func_150FDC2C(arg0);
    func_1513CA6C(arg0);
}

s32 func_150FDCD8(s32 arg0) {
    func_150FDC2C(arg0);
    func_1513CAA0(arg0);
}
