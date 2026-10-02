#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/F4800.s. */

s32 func_1509BE40();

void func_150C7350(u8 *arg0) {
    *(u32 *)(arg0 + 0x84) |= 0x80004000;
    if (func_1509BE40(3, 0x2000, 0xAC, 0x4002, 0x4003, 0x4004) != 0) {
        *(u32 *)(arg0 + 0x84) |= 0x400000;
        return;
    }
    *(u32 *)(arg0 + 0x84) &= ~0x400000;
}
