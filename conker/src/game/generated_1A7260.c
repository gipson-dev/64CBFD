#include <ultra64.h>
extern s16 D_800DD450;
extern s32 D_800DD1B0;
extern u8 D_80090614[];

s32 func_15094F70(s32, u8 *, s32, u8 *, s32, s32, s32, s32, s32);

/* Non-matching placeholders for the text-only asm slice asm/1A7260.s. */

s32 func_15179DB0() {
    return 0;
}

s32 func_15179FE0() {
    return 0;
}

s32 func_1517A1EC() {
    return 0;
}

s32 func_1517A394(register s32 arg0) {
    return arg0;
}

s32 func_1517A3A0() {
    return 0;
}

s32 func_1517A644() {
    return 0;
}

s32 func_1517A84C() {
    return 0;
}

u8 *func_1517A958(u8 *arg0, s32 arg1, s32 arg2, s32 arg3) {
    D_800DD450 = -1;
    if ((arg1 == 0xC) || (arg1 == 0x59)) {
        arg0 = (u8 *) func_1517A394((s32) arg0);
    }
    return arg0;
}

s32 func_1517A9A8(s32 arg0, volatile s32 arg1) {
    u8 output[0x14];

    if (arg1 != D_800DD1B0) {
        arg0 = func_15094F70(arg0, D_80090614, arg1 << 8, output,
                            0, 0, 0, 2, 3);
        D_800DD1B0 = arg1;
    }
    return arg0;
}

s32 func_1517AA20() {
    return 0;
}

void func_1517AB7C(arg0, arg1, arg2)
s32 arg0;
s16 arg1;
s16 arg2;
{
    func_1510B7B4(arg0, arg2);
}
