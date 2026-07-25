#include <ultra64.h>
extern u8 D_800DF9B3[];
extern u8 D_800DF7D3[];
extern u8 D_800DF7D0[];

/* Non-matching placeholders for the text-only asm slice asm/3FC60.s. */

s32 func_150127B0() {
    return 0;
}

s32 func_15012C84() {
    return 0;
}

s32 func_15012ED8() {
    return 0;
}

void func_15012F90(void) {
    s32 i;

    for (i = 0; i < 0x1E3; i++) {
        D_800DF7D0[i] = 0;
    }
}
