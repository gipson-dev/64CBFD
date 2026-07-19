#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/1D92F0.s. */

s32 func_151AE3A8();

extern f32 D_800BE9A4;

s32 func_151ABE40() {
    return 0;
}

s32 func_151AC078() {
    return 0;
}

s32 func_151AC3CC(u8 *arg0) {
    u8 *temp_v0 = *(u8 **) (arg0 + 0x98);
    s32 temp_v1 = *(s16 *) (arg0 + 0x1C) << 3;

    if (temp_v1 >= 0x100) {
        temp_v1 = 0xFF;
    }
    if (temp_v1 < *(temp_v0 + 0x1B)) {
        *(temp_v0 + 0x1B) = temp_v1;
    }
    return 1;
}

s32 func_151AC408() {
    return 0;
}

s32 func_151AC550() {
    return 0;
}

s32 func_151AC61C() {
    return 0;
}

s32 func_151AC810() {
    return 0;
}

s32 func_151AC9EC(f32 *arg0) {
    f32 delta = arg0[0x4C / 4] * D_800BE9A4;

    arg0[0x2C / 4] += delta;
    arg0[0x30 / 4] += delta;
    return 1;
}

s32 func_151ACA20(u8 *arg0) {
    s32 temp_v1 = *(s16 *) (arg0 + 0x1C);
    s32 temp_v0 = 0xFF;

    if (temp_v1 < 0x10) {
        temp_v0 = temp_v1;
        temp_v0 = (s16) (temp_v0 << 4);
    }
    if (temp_v0 < *(arg0 + 0x5C)) {
        *(arg0 + 0x5C) = temp_v0;
    }
    return 1;
}

s32 func_151ACA60() {
    return 0;
}

s32 func_151ACB38(u8 *arg0, u8 *arg1) {
    s32 result = 0;

    if (arg0[0x3B] == 1) {
        *arg1 = 1;
        result = 1;
    }
    return result;
}

void func_151ACB60(u8 *arg0) {
    s32 temp_v0 = *(s32 *) (*(u32 *) (*(u32 *) (arg0 + 0x1C) + 0x31C) + 0x9C);

    if (temp_v0 != 0) {
        func_151AE3A8(arg0);
    }
}

void func_151ACB94(u8 *arg0, s32 arg1, u8 arg2) {
    func_15169850(arg1, arg2, (s32) (arg0 + 0x1C), (s32) (arg0 + 0x20), (s32) arg0);
}

s32 func_151ACBD4() {
    return 0;
}

s32 func_151AD174() {
    return 0;
}

s32 func_151AD92C() {
    return 0;
}

s32 func_151AE06C() {
    return 0;
}

s32 func_151AE0E4() {
    return 0;
}

s32 func_151AE264() {
    return 0;
}

s32 func_151AE2BC() {
    return 0;
}

s32 func_151AE3A8() {
    return 0;
}

s32 func_151AE590() {
    return 0;
}

s32 func_151AE640() {
    return 0;
}

s32 func_151AE6B0() {
    return 0;
}

s32 func_151AE7B0() {
    return 0;
}

s32 func_151AE890() {
    return 0;
}

s32 func_151AE984() {
    return 0;
}

s32 func_151AEAB4() {
    return 0;
}

s32 func_151AECA0() {
    return 0;
}

s32 func_151AF270() {
    return 0;
}

s32 func_151AF338() {
    return 0;
}

s32 func_151AF388() {
    return 0;
}

s32 func_151AF4D0() {
    return 0;
}
