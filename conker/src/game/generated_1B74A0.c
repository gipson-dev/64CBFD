#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/1B74A0.s. */

s32 func_15189FF0() {
    return 0;
}

s32 func_1518A094() {
    return 0;
}

s32 func_1518A214() {
    return 0;
}

s32 func_1518A2E8(u8 *arg0, u8 *arg1) {
    if (*(*(u8 **) (arg0 + 0x188) + 0x6A) != 0) {
        *(u32 *) (arg0 + 0x58) &= ~2;
        *arg1 = 0;
    } else {
        *arg1 = 1;
    }
    return 1;
}

s32 func_1518A324(u8 *arg0, u8 *arg1) {
    if (*(*(u8 **) (arg0 + 0x188) + 0x6F) == 0) {
        *(u32 *) (arg0 + 0x58) &= ~2;
        *arg1 = 0;
    } else {
        *arg1 = 1;
    }
    return 1;
}

s32 func_1518A360() {
    return 0;
}
