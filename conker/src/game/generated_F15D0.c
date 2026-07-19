#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/F15D0.s. */

s32 func_150C4120() {
    return 0;
}

s32 func_150C44A4() {
    return 0;
}

s32 func_150C4AD8(u8 *arg0) {
    u8 *temp_a1 = arg0;

    if (*(s32 volatile *)(temp_a1 + 0x34) != 0) {
        func_1516972C(*(s32 volatile *)(temp_a1 + 0x34));
    }
}

s32 func_150C4B08(s32 arg0) {
    func_150C4AD8(arg0);
    func_1514933C(arg0);
}

s32 func_150C4B34(s32 arg0) {
    func_150C4AD8(arg0);
    func_15149368(arg0);
}

s32 func_150C4B60() {
    return 0;
}
