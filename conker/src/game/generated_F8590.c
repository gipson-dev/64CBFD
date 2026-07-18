#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/F8590.s. */

s32 func_150CB0E0() {
    return 0;
}

s32 func_150CB1E0(s32 arg0, s32 arg1) {
    return 0xB;
}

s32 func_150CB1F4() {
    return 0;
}

s32 func_150CB7CC() {
    return 0;
}

s32 func_150CB800() {
    return 0;
}

s32 func_150CBA30() {
    return 0;
}

s32 func_150CBABC() {
    return 0;
}

s32 func_150CBCE0() {
    return 0;
}

s32 func_150CBE88() {
    return 0;
}

void func_150CBF5C(u8 *arg0) {
    u32 temp_t6 = *(u32 *)(arg0 + 0x58);
    s32 temp_t8 = 0x20;

    *(s16 *)(arg0 + 0x1C) = temp_t8;
    *(u32 *)(arg0 + 0x58) = temp_t6 | 1;
}
