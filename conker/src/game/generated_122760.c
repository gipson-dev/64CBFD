#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/122760.s. */

s32 func_1509BE40();

void func_150F52B0(u8 *arg0) {
    if (func_1509BE40(1, 0x401C, 6, 0x9000) != 0) {
        *(u32 *) (arg0 + 0x84) |= 0x80000000;
    } else {
        *(u32 *) (arg0 + 0x84) &= 0x7FFFFFFF;
    }
}

void func_150F5310(u8 arg0) {
    func_151827D0();
}
