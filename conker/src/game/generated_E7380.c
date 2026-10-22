#include <ultra64.h>
extern f32 D_800BE9A4;
extern f32 D_8009FE2C;


/* Partially recovered text-only slice asm/E7380.s. */

s32 func_150B9ED0() {
    return 0;
}

s32 func_150BA35C(u8 *arg0) {
    s16 value = *(s16 *)(arg0 + 0x1C);

    if (value < 0x40) {
        arg0[0x28] = value << 2;
    }
    return 1;
}

/* Apply vertical acceleration and advance five float fields by the live timestep. */
s32 func_150BA37C(u8 *actor) {
    *(f32 *)(actor + 0x114) += D_8009FE2C * D_800BE9A4;
    *(f32 *)(actor + 0x34) += *(f32 *)(actor + 0x110) * D_800BE9A4;
    *(f32 *)(actor + 0x38) += *(f32 *)(actor + 0x114) * D_800BE9A4;
    *(f32 *)(actor + 0x3C) += *(f32 *)(actor + 0x118) * D_800BE9A4;
    *(f32 *)(actor + 0x40) += *(f32 *)(actor + 0x11C) * D_800BE9A4;
    *(f32 *)(actor + 0x44) += *(f32 *)(actor + 0x120) * D_800BE9A4;
    return 1;
}

s32 func_150BA424(u8 *arg0) {
    f32 delta;
    s32 actor_intensity;
    s32 distance_intensity;
    s32 result;

    delta = *(f32 *)(arg0 + 0x38) - *(f32 *)(arg0 + 0x124);
    if (delta < 0.0f) {
        return 0;
    }

    actor_intensity = *(s16 *)(arg0 + 0x1C) << 4;
    if (actor_intensity >= 0x100) {
        actor_intensity = 0xFF;
    }

    distance_intensity = (s32)delta << 2;
    if (distance_intensity >= 0x100) {
        distance_intensity = 0xFF;
    }

    if (distance_intensity < actor_intensity) {
        arg0[0x5C] = distance_intensity;
    } else {
        arg0[0x5C] = actor_intensity;
    }

    result = 1;
    if (arg0[0x5C] < 0) {
        return 0;
    }
    return result;
}
