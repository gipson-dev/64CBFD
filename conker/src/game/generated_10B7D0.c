#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/10B7D0.s. */

extern u8 D_800A0D0B[];
extern u8 D_800A0D2B[];

s32 func_150DEC28();

void func_150DE320(s32 arg0) {
}

s32 func_150DE32C() {
    return 0;
}

s32 func_150DE458() {
    return 0;
}

s32 func_150DE6D8() {
    return 0;
}

s32 func_150DE7C0() {
    return 0;
}

s32 func_150DEACC() {
    return 0;
}

s32 func_150DEB58() {
    return 0;
}

void func_150DEBE0(s32 arg0) {
    s32 i = 0;

    do {
        func_150DEC28(i & 0xFF, 1);
        i += 1;
        i = i & 0xFF;
    } while (i < 4);
}

s32 func_150DEC28(arg0, arg1)
u8 arg0;
u8 arg1;
{
    s32 offset = arg0 * 4;

    func_151616D0(D_800A0D0B[offset], 0x22, 0);
    func_151417C4(D_800A0D2B[offset], 0x22);
}
