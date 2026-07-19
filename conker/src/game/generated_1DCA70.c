#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/1DCA70.s. */

s32 func_151AF5C0() {
    return 0;
}

s32 func_151AF6C0(s32 arg0, s32 arg1) {
    return 0xC;
}

s32 func_151AF6D4() {
    return 0;
}

s32 func_151AFBD4(u8 *arg0) {
    s32 temp_v0 = *(s16 *)(arg0 + 0x1C);

    if (temp_v0 < 0x20) {
        s32 temp_v1 = temp_v0 << 3;
        if (temp_v1 < *(u8 *)(arg0 + 0x28)) {
            *(u8 *)(arg0 + 0x28) = temp_v1;
        }
    }
    return 1;
}

s32 func_151AFC08() {
    return 0;
}

s32 func_151AFC88() {
    return 0;
}

s32 func_151AFEA4() {
    return 0;
}
