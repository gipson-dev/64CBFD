#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/E7380.s. */

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

s32 func_150BA37C() {
    return 0;
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
