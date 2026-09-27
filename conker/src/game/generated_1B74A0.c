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

// Matched with guarded commutative branch operand normalization.
void func_1518A360(u8 *arg0, u8 *arg1, u8 arg2) {
    u8 *temp_v0 = arg0 + 0x170;

    if (arg2 == 0x2D) {
        s32 temp_v1 = *(s32 *)arg1;
        s32 temp_a2 = *(s32 *)(temp_v0 + 0x18);

        if (temp_v1 == temp_a2) {
            *(s32 *)(temp_v0 + 0x18) = *(s32 *)(arg1 + 4);
            temp_v0[0x1D] = arg1[9];
        } else if (*(s32 *)(arg1 + 4) == temp_a2) {
            *(s32 *)(temp_v0 + 0x18) = temp_v1;
            temp_v0[0x1D] = arg1[8];
        }
    }
}
