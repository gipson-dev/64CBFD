#include <ultra64.h>
extern f32 D_800AA434, D_800AA438, D_800AA43C, D_800AA440, D_800BE9A4;
f32 sinf(f32);
s32 func_15133894(u8 *);
u16 func_10010F88(s32, u16, s16, u8, s32, s16, s16, s16, s16, s16);


void func_100111C8(u16 arg0);

/* Non-matching placeholders for the text-only asm slice asm/1E30A0.s. */

s32 func_151B5BF0() {
    return 0;
}

/* Advance the sound phase, apply its scale pulse and forward the update status. */
s32 func_151B5E94(u8 *owner) {
    f32 *state = (f32 *)(owner + 0x170);
    f32 result;

    *(f32 *)(owner + 0x170) += D_800AA434 * D_800BE9A4;
    if (*(f32 *)(owner + 0x170) > D_800AA438) {
        *(f32 *)(owner + 0x170) = 0.0f;
        func_10010F88(0x502, 24000, 0, 0, -1,
                      (s32)*(f32 *)(owner + 0x38),
                      (s32)*(f32 *)(owner + 0x3C),
                      (s32)*(f32 *)(owner + 0x40), 100, 500);
    }
    if (state[0] < D_800AA43C) {
        result = sinf(state[0]);
        result = (result * (D_800AA440 * state[1])) + state[1];
        *(f32 *)(owner + 0x18) = *(f32 *)(owner + 0x1C) = result;
    } else {
        *(f32 *)(owner + 0x18) = *(f32 *)(owner + 0x1C) = state[1];
    }
    return func_15133894(owner);
}

void func_151B5FCC(u8 *arg0) {
    s32 temp_v0 = *(s32 *) (arg0 + 0x88);

    if (temp_v0 != 0) {
        func_100111C8(temp_v0);
        *(s32 *) (arg0 + 0x88) = 0;
    }
}
