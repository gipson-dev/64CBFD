#include <ultra64.h>
#include "variables.h"

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

s32 func_150CB7CC(u8 *arg0) {
    s32 temp_v0 = *(s16 *)(arg0 + 0x1C);

    if (temp_v0 < 0x20) {
        s32 temp_v1 = temp_v0 << 3;
        if (temp_v1 < *(u8 *)(arg0 + 0x28)) {
            *(u8 *)(arg0 + 0x28) = temp_v1;
        }
    }
    return 1;
}

s32 func_150CB800() {
    return 0;
}

s32 func_150CBA30(u8 *arg0) {
    s32 value;
    f32 delta;

    *(s16 *)(arg0 + 0x128) -= D_800BE9E4;
    if (*(s16 *)(arg0 + 0x128) > 0) {
        delta = *(f32 *)(arg0 + 0x12C) * D_800BE9A4;
        *(f32 *)(arg0 + 0x2C) += delta;
        *(f32 *)(arg0 + 0x30) += delta;
    }

    if ((*(u32 *)(arg0 + 0x58) & 1) != 0) {
        value = *(s16 *)(arg0 + 0x1C);
        if ((value < 0x20) && ((value << 3) < *(u8 *)(arg0 + 0x5C))) {
            *(u8 *)(arg0 + 0x5C) = value << 3;
        }
    }

    return 1;
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
    *(u32 *)(arg0 + 0x58) |= 1;
    *(s16 *)(arg0 + 0x1C) = 0x20;
}
