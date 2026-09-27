#include <ultra64.h>

extern s32 D_800BE9E4;
extern void func_1516972C(void *arg0);

/* Non-matching placeholders for the text-only asm slice asm/193430.s. */

s32 func_15165F80() {
    return 0;
}

s32 func_15166118() {
    return 0;
}

void func_15166204(u8 *arg0) {
    s32 timer = arg0[0x92];

    *(s16 *)(arg0 + 0x9E) += *(s16 *)(arg0 + 0x96) * D_800BE9E4;
    timer -= D_800BE9E4;
    if (timer <= 0) {
        func_1516972C(arg0);
    } else {
        arg0[0x92] = timer;
    }
}

s32 func_15166268() {
    return 0;
}

s32 func_151668B8() {
    return 0;
}
