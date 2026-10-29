#include <ultra64.h>

extern f32 D_800AA454, D_800AA458, D_800AA45C, D_800BE9A4;
f32 sinf(f32);
s32 func_15133894(u8 *);


/* Non-matching placeholders for the text-only asm slice asm/1E34C0.s. */

s32 func_151B6010() {
    return 0;
}

/* Advance the owner's phase and apply its sine-modulated scale. */
s32 func_151B6254(u8 *owner) {
    f32 *state = (f32 *)(owner + 0x170);
    f32 period = D_800AA454;
    f32 result;

    *(f32 *)(owner + 0x170) += D_800AA458 * D_800BE9A4;
    while (*state > period) {
        *state -= period;
    }
    result = sinf(*state);
    result = (result * (D_800AA45C * state[1])) + state[1];
    *(f32 *)(owner + 0x18) = *(f32 *)(owner + 0x1C) = result;
    return func_15133894(owner);
}
