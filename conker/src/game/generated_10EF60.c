#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/10EF60.s. */

s32 func_150E1AB0() {
    return 0;
}

s32 func_150E1D14() {
    return 0;
}

s32 func_150E28DC() {
    return 0;
}

s32 func_150E2DA4(register s32 arg0, s32 arg1) {
    return arg0;
}

s32 func_150E2DB4() {
    return 0;
}

s32 func_150E2EA4() {
    return 0;
}

void func_150E2F90(arg0, arg1, arg2)
s32 arg0;
s16 arg1;
s16 arg2;
{
    func_150E2DA4(arg0, arg2);
}

void func_150E2FC0(u8 *arg0, u8 *arg1, u8 arg2) {
    s32 current;
    s32 source;

    if (arg2 == 0x2D) {
        source = *(s32 *)arg1;
        current = *(s32 *)(arg0 + 0xDC);
        if (source == current) {
            *(s32 *)(arg0 + 0xDC) = *(s32 *)(arg1 + 4);
            arg0[0xDA] = arg1[9];
        } else if (current == *(s32 *)(arg1 + 4)) {
            *(s32 *)(arg0 + 0xDC) = source;
            arg0[0xDA] = arg1[8];
        }
    }
}
