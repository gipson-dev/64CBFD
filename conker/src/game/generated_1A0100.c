#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/1A0100.s. */

extern s8 D_800DD2B0[];
extern s8 D_800DD2C0[];
extern u8 D_800BE9B4;
s32 func_15085430();

void func_15172C50(s32 value) {
    s32 i;

    for (i = 0; i < 16; i++) {
        D_800DD2B0[i] = -1;
        D_800DD2C0[i] = 0;
    }

    D_800DD2C0[0] = value;
}

s32 func_15172CA8() {
    return 0;
}

void func_15172D28(u8 *arg0, s32 arg1) {
    u8 *target;

    func_15085430(arg0, arg1, 1);
    *(u16 *) (arg0 + 0x2F8) &= ~0x10;

    if (D_800BE9B4 == 0) {
        target = *(u8 **) (arg0 + 0x31C);
        if (target != NULL) {
            target[0x56] = 3;
        }
    }
}

s32 func_15172D80() {
    return 0;
}

s32 func_15172E7C() {
    return 0;
}
