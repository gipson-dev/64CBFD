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

typedef struct EffectRequest150DB518 {
    u8 kind, reserved01;
    u16 mode;
    s16 duration;
    u8 reserved06[2];
    s32 value;
    u32 flags;
    u8 red, green, blue, alpha;
    u8 reserved14[0x2C];
    u32 allocationFlags;
    u8 first, second, reserved46[0x12];
} EffectRequest150DB518;
typedef struct EffectSources150DB518 {
    u8 reserved[0x110];
    void *first, *second, *third, *fifth, *fourth;
} EffectSources150DB518;
void *func_1513D524(void *, u8, u8, u8, u8, u8, s32, u8, s32);
/* Create a parameter-driven effect and retain its five live source pointers. */
void func_150DB518(void *first, void *second, void *third, void *fourth,
                   void *fifth, s16 duration, u8 channel, s32 context) {
    EffectRequest150DB518 request;
    EffectSources150DB518 *effect;

    if (first && second && third && fourth && fifth && duration) {
        /* Reserved descriptor bytes retain their original stack contents. */
        request.kind = 0x17;
        request.flags = 0x243A;
        request.allocationFlags = 0x401;
        request.first = 255;
        request.value = 0;
        request.duration = duration;
        request.second = 255;
        request.red = request.green = request.blue = 200;
        request.alpha = 200;
        request.mode = 0x401;
        effect = func_1513D524(&request, 0, 10, 0, 8, 0, 20, channel, context);
        if (effect) {
            effect->first = first;
            effect->second = second;
            effect->third = third;
            effect->fifth = fifth;
            effect->fourth = fourth;
        }
    }
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
