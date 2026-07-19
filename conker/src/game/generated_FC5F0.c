#include <ultra64.h>
void func_151CF898(u8 *, f32, f32);
extern u8 D_800CC2D0[];

/* Non-matching placeholders for the text-only asm slice asm/FC5F0.s. */

s32 func_150CF140() {
    return 0;
}

s32 func_150CF484() {
    return 0;
}

void func_150CF530(s32 arg0) {
    func_151CF898(D_800CC2D0, *(f32 *) (D_800CC2D0 + 0x18) + 300.0f, -10000.0f);
}

s32 func_150CF578() {
    return 0;
}

s32 func_150CF5E8() {
    return 0;
}

s32 func_150CF680() {
    return 0;
}

s32 func_150CF800() {
    return 0;
}

void func_150CFBEC(u8 *arg0, f32 *arg1, u8 arg2) {
    if (arg2 == 0x52) {
        u8 *temp_v0 = arg0 + 0x70;

        *temp_v0 |= 1;
        *(f32 *) (temp_v0 + 4) = 0.0f;
        *(f32 *) (temp_v0 + 8) = *(f32 *) (arg0 + 0x10);
        *(f32 *) (temp_v0 + 0xC) = *arg1 - *(f32 *) (arg0 + 0x10);
    }
}

s32 func_150CFC38(f32 arg0) {
    f32 value = arg0;

    func_1515572C(&value, 0x52);
}

s32 func_150CFC60() {
    return 0;
}

s32 func_150CFD20() {
    return 0;
}

u8 *func_150CFD5C(u8 *arg0) {
    if (*arg0 != 0) {
        do {
            arg0++;
        } while (*arg0 != 0);
    }
    return arg0;
}

s32 func_150CFD84(u8 *arg0, u8 **arg1) {
    u8 *end = (u8 *) func_150CFD20(arg0);

    *arg1 = end;
    return end - arg0;
}

s32 func_150CFDB8() {
    return 0;
}

s32 func_150CFE3C() {
    return 0;
}

s32 func_150CFE98() {
    return 0;
}

s32 func_150CFF10() {
    return 0;
}

s32 func_150D0034() {
    return 0;
}

s32 func_150D00C0() {
    return 0;
}

s32 func_150D0134() {
    return 0;
}

s32 func_150D01A0() {
    return 0;
}

s32 func_150D02B4() {
    return 0;
}

s32 func_150D032C() {
    return 0;
}

s32 func_150D04C4() {
    return 0;
}

s32 func_150D0534() {
    return 0;
}
