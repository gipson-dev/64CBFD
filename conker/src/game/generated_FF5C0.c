#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/FF5C0.s. */

void func_150D22D4();
s32 func_1517F08C();

extern u8 D_800D9900;

s32 func_150D2110() {
    return 0;
}

s32 func_150D21CC() {
    return 0;
}

s32 func_150D227C(s32 arg0) {
    func_150D22D4(arg0);
    func_1514933C(arg0);
}

s32 func_150D22A8(s32 arg0) {
    func_150D22D4(arg0);
    func_15149368(arg0);
}

void func_150D22D4(s32 arg0) {
    D_800D9900--;
}

/* Note 528: mode-selected color arguments and updated-handle return. */
s32 func_150D22F4(s32 arg0, u8 *arg1, s16 arg2) {
    if (arg1[0x28] == 1) {
        arg0 = func_1517F08C(arg0, arg1[0x3C], 0xFF, 0xFF, 0xFF, arg2);
    } else {
        arg0 = func_1517F08C(arg0, arg1[0x3D], 0, 0, 0, arg2);
    }
    return arg0;
}

s32 func_150D2374() {
    return 0;
}
