#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/E7380.s. */

s32 func_150B9ED0() {
    return 0;
}

s32 func_150BA35C(u8 *arg0) {
    s16 value = *(s16 *)(arg0 + 0x1C);

    if (value < 0x40) {
        arg0[0x28] = value << 2;
    }
    return 1;
}

s32 func_150BA37C() {
    return 0;
}

s32 func_150BA424() {
    return 0;
}
