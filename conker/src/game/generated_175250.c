#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/175250.s. */

s32 func_15147DA0() {
    return 0;
}

s32 func_15147EB8() {
    return 0;
}

s32 func_1514803C() {
    return 0;
}

s32 func_151488C4() {
    return 0;
}

s32 func_15148AF4() {
    return 0;
}

s32 func_15148BA4() {
    return 0;
}

s32 func_15148DE0() {
    return 0;
}

s32 func_15148EF8(u8 *arg0, s32 arg1, s32 arg2, s32 arg3) {
    u8 *temp_v1 = *(u8 **) (arg0 + 0x98);

    temp_v1[0x20] = 4;
    return 1;
}

s32 func_15148F1C() {
    return 0;
}

s32 func_151490C8(u8 *arg0) {
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

s32 func_15149104() {
    return 0;
}
