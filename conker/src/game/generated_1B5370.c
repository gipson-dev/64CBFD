#include <ultra64.h>
extern f32 D_800DF70C[];

/* Non-matching placeholders for the text-only asm slice asm/1B5370.s. */

typedef struct ColorEffectRecord15187EC0 {
    u8 startRed;
    u8 startGreen;
    u8 startBlue;
    u8 targetRed;
    u8 targetGreen;
    u8 targetBlue;
    u8 currentRed;
    u8 currentGreen;
    u8 currentBlue;
    u8 padding[3];
    f32 blend;
    s32 mode;
    f32 rate;
    u8 state[12];
} ColorEffectRecord15187EC0;

extern u8 D_800DF700[];
extern s32 D_800DF7B4;

/* Append a color-effect record to the five-entry pool; return its index or -1. */
s32 func_15187EC0(s32 mode, f32 rate, u8 startRed, u8 startGreen,
                  u8 startBlue, u8 targetRed, u8 targetGreen, u8 targetBlue) {
    ColorEffectRecord15187EC0 *record;

    if (D_800DF7B4 < 5) {
        record = (ColorEffectRecord15187EC0 *)(D_800DF700 + D_800DF7B4 * 36);
        record->rate = rate;
        record->currentRed = startRed;
        record->startRed = startRed;
        record->currentGreen = startGreen;
        record->startGreen = startGreen;
        record->currentBlue = startBlue;
        record->startBlue = startBlue;
        record->targetRed = targetRed;
        record->targetGreen = targetGreen;
        record->targetBlue = targetBlue;
        record->mode = mode;
        bzero(record->state, 12);
        return ++D_800DF7B4 - 1;
    }
    return -1;
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

void func_1518804C(s32 arg0, f32 arg1) {
    if (arg0 < D_800DF7B4) {
        if (arg0 >= 0) {
            if (arg1 > 1.0f) {
                arg1 = 1.0f;
            } else if (arg1 < 0.0f) {
                arg1 = 0.0f;
            }
            *(f32 *)((u8 *)D_800DF70C + arg0 * 36) = arg1;
        }
    }
}

s32 func_151880C0() {
    return 0;
}
