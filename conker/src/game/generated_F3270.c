#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/F3270.s. */

s32 func_150C6460();

void func_150C5DC0(u8 *arg0) {
    if (*(u32 *) (arg0 + 0x58) != 0) {
        u8 *temp_v0 = *(u8 **) (arg0 + 0x58) + 0xB0;

        *(temp_v0 + 4) = 1;
    } else {
        *(u32 *) (arg0 + 0x58) = func_150C6460(arg0);
    }
}

s32 func_150C5E0C() {
    return 0;
}

// Retail retains the otherwise dead temp_v0 + 0x58 update before the call.
#pragma GLOBAL_ASM("asm/nonmatchings/generated_F3270/func_150C5EFC.s")

s32 func_150C5F40() {
    return 0;
}

s32 func_150C5F94() {
    return 0;
}

s32 func_150C60D8() {
    return 0;
}

s32 func_150C63EC(u8 *arg0) {
    s32 result = 1;

    if (*(u8 *)(arg0 + 0x5C) == 0) {
        result = 0;
    }
    *(u8 *)(arg0 + 0x5C) = 0;
    return result;
}

s32 func_150C6410(u8 *arg0) {
    u8 *temp_v0 = *(u8 **)(arg0 + 0x58) + 0x58;

    *(s32 *)(temp_v0 + 0x4) = 0;
    func_151346EC(arg0);
}

s32 func_150C6438(u8 *arg0) {
    u8 *temp_v0 = *(u8 **)(arg0 + 0x58) + 0x58;

    *(s32 *)(temp_v0 + 0x4) = 0;
    func_1513470C(arg0);
}

s32 func_150C6460() {
    return 0;
}
