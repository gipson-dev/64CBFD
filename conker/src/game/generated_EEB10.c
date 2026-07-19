#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/EEB10.s. */

s32 func_150C1660() {
    return 0;
}

s32 func_150C16C0() {
    return 0;
}

s32 func_150C1978(u8 *arg0) {
    u8 *temp_v0 = *(u8 **) (arg0 + 0x98);
    s32 temp_v1 = *(s16 *) (arg0 + 0x1C) << 3;

    if (temp_v1 >= 0x100) {
        temp_v1 = 0xFF;
    }
    *(temp_v0 + 0x1B) = temp_v1;
    if ((temp_v1 & 0xFF) < 0) {
        return 0;
    }
    return 1;
}
