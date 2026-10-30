#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/108320.s. */

s32 func_150DAE70() {
    return 0;
}

s32 func_150DB114() {
    return 0;
}

s32 func_150DB2D8() {
    return 0;
}

s32 func_150DB518() {
    return 0;
}

/* Clamp the sampled actor parameter to its unsigned byte range. */
s32 func_150DB630(u8 *actor) {
    f32 value;

    /* Preserve the retail reload of the parameter pointer on the lower path. */
    if (**(f32 * volatile *)(actor + 0x120) > 255.0f) {
        actor[0x5C] = 255;
    } else {
        value = **(f32 **)(actor + 0x120);
        if (value < 0.0f) {
            actor[0x5C] = 0;
        } else {
            actor[0x5C] = (u32)value;
        }
    }
    return 1;
}

s32 func_150DB714() {
    return 0;
}
