#include <ultra64.h>
extern f32 D_800DF70C[];

/* Non-matching placeholders for the text-only asm slice asm/1B5370.s. */

extern u8 D_800DF700[];
extern s32 D_800DF7B4;

s32 func_15187EC0() {
    return 0;
}

s32 func_15187F90(void) {
    bzero(D_800DF700, 0xB4);
    D_800DF7B4 = 0;
}

void func_15187FC0(s32 arg0, s32 *arg1) {
    u8 *temp_v0;

    if (arg0 < D_800DF7B4) {
        if (arg0 >= 0) {
            temp_v0 = &D_800DF700[arg0 * 36];
            arg1[0] = temp_v0[6];
            arg1[1] = temp_v0[7];
            arg1[2] = temp_v0[8];
        }
    }
}

void func_15188010(s32 arg0, f32 *arg1) {
    if (arg0 < D_800DF7B4) {
        if (arg0 >= 0) {
            *arg1 = *(f32 *) ((u8 *) D_800DF70C + arg0 * 36);
        }
    }
}

s32 func_1518804C() {
    return 0;
}

s32 func_151880C0() {
    return 0;
}
