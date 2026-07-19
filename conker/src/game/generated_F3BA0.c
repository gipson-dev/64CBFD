#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/F3BA0.s. */

s32 func_150C66F0() {
    return 0;
}

s32 func_150C673C() {
    return 0;
}

s32 func_150C682C() {
    return 0;
}

s32 func_150C6870() {
    return 0;
}

s32 func_150C68C4() {
    return 0;
}

s32 func_150C6A08() {
    return 0;
}

s32 func_150C6D1C(u8 *arg0) {
    s32 result = 1;

    if (*(u8 *)(arg0 + 0x5C) == 0) {
        result = 0;
    }
    *(u8 *)(arg0 + 0x5C) = 0;
    return result;
}

s32 func_150C6D40(u8 *arg0) {
    u8 *temp_v0 = *(u8 **)(arg0 + 0x58) + 0x58;

    *(s32 *)(temp_v0 + 0x18) = 0;
    func_151346EC(arg0);
}

s32 func_150C6D68(u8 *arg0) {
    u8 *temp_v0 = *(u8 **)(arg0 + 0x58) + 0x58;

    *(s32 *)(temp_v0 + 0x18) = 0;
    func_1513470C(arg0);
}

s32 func_150C6D90() {
    return 0;
}
