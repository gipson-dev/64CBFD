#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/E5E90.s. */

s32 func_150B89E0() {
    return 0;
}

s32 func_150B8F44() {
    return 0;
}

s32 func_150B9560() {
    return 0;
}

s32 func_150B95FC(u8 *arg0) {
    s16 value = *(s16 *)(arg0 + 0x1C);

    if (value < 0x20) {
        arg0[0x5C] = value << 3;
    }
    return 1;
}

s32 func_150B961C(u8 *arg0) {
    s16 value = *(s16 *)(arg0 + 0x1C);

    if (value < 0x40) {
        arg0[0x28] = value << 2;
    }
    return 1;
}

s32 func_150B963C() {
    return 0;
}

s32 func_150B9D14() {
    return 0;
}

s32 func_150B9D8C() {
    return 0;
}
