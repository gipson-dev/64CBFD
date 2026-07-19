#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/128D70.s. */

s32 func_150FB8C0() {
    return 0;
}

s32 func_150FC368() {
    return 0;
}

s32 func_150FC438() {
    return 0;
}

s32 func_150FC614() {
    return 0;
}

s32 func_150FC818() {
    return 0;
}

s32 func_150FC930(u8 *arg0, u8 arg1, u8 arg2) {
    u8 temp_v0 = *(arg0 + 4);

    if ((temp_v0 == 0x12) || (temp_v0 == 0x23) || (temp_v0 == 0x73) || (temp_v0 == 0x8A)) {
        return 0;
    }
    return 1;
}

s32 func_150FC974(u8 *arg0) {
    u8 *temp_a1 = arg0;

    if (*(s32 volatile *)(temp_a1 + 0x38) != 0) {
        func_1516972C(*(s32 volatile *)(temp_a1 + 0x38));
    }
}

s32 func_150FC9A4(s32 arg0) {
    func_150FC974(arg0);
    func_1514933C(arg0);
}

s32 func_150FC9D0(s32 arg0) {
    func_150FC974(arg0);
    func_15149368(arg0);
}
