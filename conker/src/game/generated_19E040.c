#include <ultra64.h>

extern s32 D_800BE9F0;

/* Non-matching placeholders for the text-only asm slice asm/19E040.s. */

s32 func_15170B90() {
    return 0;
}

void func_15170EC4(u8 *arg0, u8 arg1, s32 arg2) {
    switch (D_800BE9F0) {
        case 2:
            func_15170B90(arg0, 1, 1, 1, arg1, arg2);
            break;
        case 0x10:
            func_15170B90(arg0, 0xA9, 8, 0, arg1, arg2);
            break;
    }
}

s32 func_15170F4C() {
    return 0;
}

void func_151711C4(u8 *arg0) {
    if (*(arg0 + 4) == 0x33) {
        func_150C3D5C(arg0);
    }
    func_15060F28(arg0, 1);
}

s32 func_15171200() {
    return 0;
}

s32 func_15171600() {
    return 0;
}

s32 func_151717FC() {
    return 0;
}

s32 func_151718F0() {
    return 0;
}

s32 func_15171BF4() {
    return 0;
}
