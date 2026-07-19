#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/1A89B0.s. */

extern s16 D_800DD470[];

s32 func_1517B500() {
    return 0;
}

s32 func_1517B6E8() {
    return 0;
}

s32 func_1517B7A8(s16 *arg0, s16 *arg1, s32 *arg2, s32 arg3) {
    s32 temp_v0 = *arg2;

    if (temp_v0 >= 0x300) {
        if (temp_v0 < 0x501) {
            *arg2 = temp_v0 - 0x200;
        } else {
            *arg2 = 0x300;
        }
    }
    arg1[0] = arg0[0];
    arg1[1] = arg0[1];
    arg1[2] = arg0[2];
    return 0;
}

s32 func_1517B7F8() {
    return 0;
}

s32 func_1517B89C() {
    return 0;
}

s32 func_1517BBAC() {
    return 0;
}

s32 func_1517CFC4() {
    return 0;
}

s32 func_1517D074() {
    return 0;
}

s32 func_1517D578() {
    return 0;
}

s32 func_1517D5FC() {
    return 0;
}

s32 func_1517D690() {
    return 0;
}

s32 func_1517D7B0() {
    return 0;
}

s32 func_1517DE5C() {
    return 0;
}

void func_1517E05C(s32 arg0, s32 arg1, s32 arg2) {
    D_800DD470[0] = arg0;
    D_800DD470[1] = arg1;
    D_800DD470[2] = arg2;
}
