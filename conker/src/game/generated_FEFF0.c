#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/FEFF0.s. */

s32 func_1509BE40();

s32 func_150D1B40() {
    return 0;
}

void func_150D1BD0(u8 *arg0) {
    if (func_1509BE40(1, 0x402C, 6, 0x2000) != 0) {
        *(u32 *) (arg0 + 0x84) |= 0x10;
    } else {
        *(u32 *) (arg0 + 0x84) &= ~0x10;
    }
}
