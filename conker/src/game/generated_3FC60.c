#include <ultra64.h>
extern u8 D_800DF9B3[];
extern u8 D_800DF7D3[];
extern u8 D_800DF7D2;
extern u8 D_800DF7D1;
extern u8 D_800DF7D0;

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
    u8 *end = D_800DF9B3;
    u8 *ptr = D_800DF7D3;

    D_800DF7D0 = 0;
    D_800DF7D1 = 0;
    D_800DF7D2 = 0;
    do {
        ptr += 4;
        ptr[-3] = 0;
        ptr[-2] = 0;
        ptr[-1] = 0;
        ptr[-4] = 0;
    } while (ptr != end);
}
