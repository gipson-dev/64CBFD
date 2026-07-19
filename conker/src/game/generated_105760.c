#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/105760.s. */

void func_150D82B0(s32 arg0) {
}

s32 func_150D82BC() {
    return 0;
}

s32 func_150D83D8() {
    return 0;
}

u8 *func_150D8590(u16 *arg0, s32 arg1) {
    arg0[0] = 0x42;
    arg0[1] = 0;
    return (u8 *)(arg0 + 2);
}

s32 func_150D85AC() {
    return 0;
}

s32 func_150D88AC(u8 *arg0) {
    if (*(u8 *) (*(u8 **) (arg0 + 0x18) + 0x6F) != 0) {
        *(u8 *) (*(u8 **) (arg0 + 0x14) + 9) = 0;
    } else {
        *(u8 *) (*(u8 **) (arg0 + 0x14) + 9) = 1;
    }
    return 1;
}

s32 func_150D88E0() {
    return 0;
}

s32 func_150D8A20(s32 arg0, s32 arg1) {
    return 8;
}

s32 func_150D8A34() {
    return 0;
}
