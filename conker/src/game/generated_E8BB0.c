#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/E8BB0.s. */

s32 func_1509BE40();

void func_150BB700(u8 *arg0) {
    if (func_1509BE40(1, 0x4047, 6, 0x2000) != 0) {
        *(u32 *) (arg0 + 0x84) |= 0x1000;
    } else {
        *(u32 *) (arg0 + 0x84) &= ~0x1000;
    }
}
