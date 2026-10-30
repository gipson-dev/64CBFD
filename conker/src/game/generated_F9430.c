#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/F9430.s. */

typedef struct {
    s16 threshold;
    u8 pad2[2];
    f32 rate;
} GeneratedF9430MotionRecord;

typedef struct {
    u8 pad0[0x1C];
    s16 value;
    u8 pad1E[0xE];
    f32 accumulator0;
    f32 accumulator1;
    u8 pad34[0x24];
    s32 flags;
    u8 limit;
    u8 pad5D[0xCB];
    GeneratedF9430MotionRecord motion;
} GeneratedF9430MotionObject;

extern f32 D_800BE9A4;

s32 func_150CBF80() {
    return 0;
}

/* Note 527: flag-gated motion threshold and paired accumulator update. */
s32 func_150CC638(GeneratedF9430MotionObject *arg0) {
    s32 scaled;
    s32 value;
    f32 delta;

    if (arg0->flags & 1) {
        GeneratedF9430MotionRecord *record;

        value = arg0->value;
        if (value < 0x20) {
            scaled = value << 3;
            if (scaled < arg0->limit) {
                arg0->limit = scaled;
                value = arg0->value;
            }
        }

        record = &arg0->motion;
        if (record->threshold < value) {
            delta = record->rate * D_800BE9A4;
            arg0->accumulator0 += delta;
            arg0->accumulator1 += delta;
        }
    }
    return 1;
}

s32 func_150CC6B8() {
    return 0;
}

s32 func_150CC8D4() {
    return 0;
}

s32 func_150CCA7C() {
    return 0;
}

typedef struct {
    u8 pad0[0x20];
    f32 rotation[3];
    u8 pad2C[0xC];
    f32 position[3];
    f32 velocity[3];
    f32 angularVelocity[3];
    f32 verticalAcceleration;
} GeneratedF9430KinematicObject;

/* Advance position and rotation, including vertical acceleration over the timestep. */
s32 func_150CCCB4(GeneratedF9430KinematicObject *object) {
    object->position[0] += object->velocity[0] * D_800BE9A4;
    object->position[1] += object->velocity[1] * D_800BE9A4 +
        object->verticalAcceleration * D_800BE9A4 * D_800BE9A4 * 0.5f;
    object->position[2] += object->velocity[2] * D_800BE9A4;
    object->velocity[1] += object->verticalAcceleration * D_800BE9A4;
    object->rotation[0] += object->angularVelocity[0] * D_800BE9A4;
    object->rotation[1] += object->angularVelocity[1] * D_800BE9A4;
    object->rotation[2] += object->angularVelocity[2] * D_800BE9A4;
    return 1;
}
