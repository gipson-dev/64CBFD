#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/E8C10.s. */

s32 func_150BB760() {
    return 0;
}

s32 func_150BBB5C() {
    return 0;
}

s32 func_150BC488() {
    return 0;
}

s32 func_150BCBBC() {
    return 0;
}

typedef struct {
    u8 reserved[0x10];
    f32 extent;
    f32 damping;
    u8 reserved18[0x24];
    f32 height;
    f32 reserved40;
    f32 velocity[3];
    f32 rotationVelocity[3];
    f32 reserved5C;
    u32 flags;
} ReboundRecordE8C10;
extern f32 D_8009FEF8;

/* Set the ground height, then stop or reflect and damp the record's motion. */
s32 func_150BCFB8(ReboundRecordE8C10 *record, f32 x, f32 y, f32 z,
                 f32 groundHeight, f32 *normal) {
    record->height = record->extent * D_8009FEF8 + groundHeight;
    if (record->velocity[1] > -2.0f) {
        record->velocity[0] = 0.0f;
        record->flags &= 0xFFFFFF90U;
        record->velocity[1] = 0.0f;
        record->velocity[2] = 0.0f;
    } else {
        f32 damping = record->damping;
        record->velocity[0] *= damping;
        record->velocity[1] = -record->velocity[1] * damping;
        record->velocity[2] *= damping;
        record->rotationVelocity[0] *= damping;
        record->rotationVelocity[1] *= damping;
        record->rotationVelocity[2] *= damping;
    }
    return 1;
}

s32 func_150BD070() {
    return 0;
}

s32 func_150BD740() {
    return 0;
}

s32 func_150BD954() {
    return 0;
}

// Matched with guarded scalar-temporary register normalization.
s32 func_150BDB3C(u8 *arg0) {
    u8 *temp_v0 = *(u8 **) (arg0 + 0x98);
    s32 temp_v1 = *(s16 *) (arg0 + 0x1C);
    {
        s32 shifted = temp_v1 << 3;

        if (shifted < *(temp_v0 + 0x1B)) {
            *(temp_v0 + 0x1B) = shifted;
        }
    }
    return 1;
}
