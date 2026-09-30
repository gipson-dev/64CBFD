#include <ultra64.h>

extern u8 D_80038080;
extern s32 D_800BE570;
extern u8 D_800BE574;
extern u8 D_800BE575;
extern s32 D_800BE9F0;

void func_100043B4(s32 *, u32);

/* Non-matching placeholders for the text-only asm slice asm/203340.s. */

s32 func_151D5E90() {
    return 0;
}

s32 func_151D61B0() {
    return 0;
}

s32 func_151D6418() {
    return 0;
}

void func_151D66F0(s32 arg0, s32 arg1) {
    if ((D_800BE9F0 == 6) && (D_80038080 == 0)) {
        return;
    }

    if (arg1 == 0) {
        arg0 = 0;
    }

    D_800BE574 = arg0;
    if (arg0 != 0) {
        D_800BE575 = arg1;
    } else {
        D_800BE575 = 0;
    }

    if ((arg0 == 0) && (D_800BE570 != 0)) {
        func_100043B4((s32 *)D_800BE570, 3);
        D_800BE570 = 0;
    }
}

s32 func_151D6778() {
    return 0;
}
