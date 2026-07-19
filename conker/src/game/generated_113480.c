#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/113480.s. */

s32 func_150E5FD0() {
    return 0;
}

s32 func_150E6230() {
    return 0;
}

s32 func_150E63A0() {
    return 0;
}

s32 func_150E679C(u8 *arg0) {
    s32 temp_v0 = *(s16 *)(arg0 + 0x1C);

    if (temp_v0 < 8) {
        s32 temp_v1 = temp_v0 << 5;
        if (temp_v1 < *(u8 *)(arg0 + 0x5C)) {
            *(u8 *)(arg0 + 0x5C) = temp_v1;
        }
    }
    return 1;
}

s32 func_150E67D0() {
    return 0;
}
