#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/1A1E50.s. */

extern s32 D_800BE9E4;
extern u8 D_800DD405;
extern u8 D_800DD406;

void func_151749A0(s32 timerLimit, s32 counterLimit) {
    D_800DD406 += D_800BE9E4;
    if (timerLimit < D_800DD406) {
        D_800DD405++;
        if (D_800DD405 >= counterLimit) {
            D_800DD405 = 0;
        }
        D_800DD406 = 0;
    }
}

s32 func_151749F8() {
    return 0;
}

s32 func_15174AA4() {
    return 0;
}

s32 func_15174B48() {
    return 0;
}
