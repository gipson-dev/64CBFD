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
    u8 *temp_v0 = *(u8 **) (arg0 + 0x98);
    s32 temp_v1 = *(s16 *) (arg0 + 0x1C) << 4;

    if (temp_v1 >= 0x100) {
        temp_v1 = 0xFF;
    }
    if (temp_v1 < *(temp_v0 + 0x1B)) {
        *(temp_v0 + 0x1B) = temp_v1;
    }
    return 1;
}

s32 func_150B37C8() {
    return 0;
}
