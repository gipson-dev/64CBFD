#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/1368C0.s. */

s32 func_15109410() {
    return 0;
}

s32 func_151094FC() {
    return 0;
}

s32 func_15109848() {
    return 0;
}

s32 func_15109C20() {
    return 0;
}

s32 func_15109ED4() {
    return 0;
}

s32 func_15109FB8() {
    return 0;
}

s32 func_1510A344() {
    return 0;
}

s32 func_1510A40C() {
    return 0;
}

// Matched with guarded commutative branch operand normalization.
void func_1510A870(u8 *arg0, u8 *arg1, u8 arg2) {
    u8 *temp_v0 = arg0 + 0x28;

    if (arg2 == 0x2D) {
        s32 temp_v1 = *(s32 *)arg1;
        s32 temp_a2 = *(s32 *)temp_v0;

        if (temp_v1 == temp_a2) {
            *(s32 *)temp_v0 = *(s32 *)(arg1 + 4);
            temp_v0[4] = arg1[9];
        } else {
            if (temp_a2 != *(s32 *)(arg1 + 4)) {
                return;
            }
            *(s32 *)temp_v0 = temp_v1;
            temp_v0[4] = arg1[8];
        }
    }
}

s32 func_1510A8CC() {
    return 0;
}
