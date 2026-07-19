#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/1B8F40.s. */

s32 func_1518BA90() {
    return 0;
}

s32 func_1518BBF4() {
    return 0;
}

s32 func_1518BCD0() {
    return 0;
}

s32 func_1518BD60() {
    return 0;
}

s32 func_1518C0B8() {
    return 0;
}

s32 func_1518C540(u8 *arg0) {
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

s32 func_1518C57C() {
    return 0;
}

s32 func_1518C69C() {
    return 0;
}

s32 func_1518C850() {
    return 0;
}
