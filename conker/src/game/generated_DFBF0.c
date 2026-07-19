#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/DFBF0.s. */

s32 func_150B2740() {
    return 0;
}

s32 func_150B2EB4() {
    return 0;
}

s32 func_150B3188() {
    return 0;
}

s32 func_150B36AC() {
    return 0;
}

s32 func_150B378C(u8 *arg0) {
    s32 value = *(s16 *) (arg0 + 0x1C) << 4;
    u8 *target = *(u8 **) (arg0 + 0x98);

    if (value >= 0x100) {
        value = 0xFF;
    }
    if (value < target[0x1B]) {
        target[0x1B] = value;
    }
    return 1;
}

s32 func_150B37C8() {
    return 0;
}
