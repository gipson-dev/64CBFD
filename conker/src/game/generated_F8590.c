#include <ultra64.h>
#include "variables.h"

typedef struct HeightResult71820 HeightResult71820;
typedef struct HeightActor71820 HeightActor71820;
extern f32 D_800A05E0[];
extern f32 D_800A05EC[];
void func_15143134(f32 *, f32 *, u8 *);
void func_1504715C(HeightResult71820 *, HeightActor71820 *);
s32 func_15046C80(f32 *, u16, f32, HeightResult71820 *);

/* Non-matching placeholders for the text-only asm slice asm/F8590.s. */

/* Transform the selected actor offset and optionally query its height interval. */
s32 func_150CB0E0(f32 *position, u8 *actor, HeightResult71820 *result, u8 mode) {
    f32 start[3];
    f32 *point;
    u8 *matrix;

    if (mode != 1 && mode != 2) {
        return 0;
    }
    if (mode == 1) {
        point = D_800A05EC;
    } else {
        point = D_800A05E0;
    }
    if (mode == 1) {
        matrix = *(u8 **)(actor + 0x1D4) + 0xA00;
    } else {
        matrix = *(u8 **)(actor + 0x1D4) + 0xBC0;
    }
    func_15143134(point, position, matrix);
    if (result == NULL) {
        return 1;
    }
    start[0] = position[0];
    start[1] = position[1] + 100.0f;
    start[2] = position[2];
    func_1504715C(result, (HeightActor71820 *)actor);
    return func_15046C80(start, 0, position[1] - 500.0f, result);
}

s32 func_150CB1E0(s32 arg0, s32 arg1) {
    return 0xB;
}

s32 func_150CB1F4() {
    return 0;
}

s32 func_150CB7CC(u8 *arg0) {
    s32 temp_v0 = *(s16 *)(arg0 + 0x1C);

    if (temp_v0 < 0x20) {
        s32 temp_v1 = temp_v0 << 3;
        if (temp_v1 < *(u8 *)(arg0 + 0x28)) {
            *(u8 *)(arg0 + 0x28) = temp_v1;
        }
    }
    return 1;
}

s32 func_150CB800() {
    return 0;
}

s32 func_150CBA30(u8 *arg0) {
    s32 value;
    f32 delta;

    *(s16 *)(arg0 + 0x128) -= D_800BE9E4;
    if (*(s16 *)(arg0 + 0x128) > 0) {
        delta = *(f32 *)(arg0 + 0x12C) * D_800BE9A4;
        *(f32 *)(arg0 + 0x2C) += delta;
        *(f32 *)(arg0 + 0x30) += delta;
    }

    if ((*(u32 *)(arg0 + 0x58) & 1) != 0) {
        value = *(s16 *)(arg0 + 0x1C);
        if ((value < 0x20) && ((value << 3) < *(u8 *)(arg0 + 0x5C))) {
            *(u8 *)(arg0 + 0x5C) = value << 3;
        }
    }

    return 1;
}

s32 func_150CBABC() {
    return 0;
}

extern s32 D_800BE9E4;
typedef struct { u8 pad00[0x58]; f32 x, pad5C, z; u8 pad64[0x44]; f32 damping; } DampingState150CBCE0;
/* Apply one damping step for each elapsed tick. */
s32 func_150CBCE0(DampingState150CBCE0 *state, s32 unused) {
    u32 ticks;
    f32 *factor = &state->damping;
    for (ticks = (u32)D_800BE9E4; ticks != 0; ticks--) {
        state->x *= *factor;
        state->z *= *factor;
    }
    return 1;
}

/* Integrate position and angles, retaining the original single-precision grouping. */
s32 func_150CBE88(u8 *record) {
    f32 acceleration = *(f32 *)(record + 0x5C);
    f32 verticalVelocity = *(f32 *)(record + 0x48);
    *(f32 *)(record + 0x38) += *(f32 *)(record + 0x44) * D_800BE9A4;
    *(f32 *)(record + 0x3C) += verticalVelocity * D_800BE9A4
        + acceleration * D_800BE9A4 * D_800BE9A4 * 0.5f;
    *(f32 *)(record + 0x40) += *(f32 *)(record + 0x4C) * D_800BE9A4;
    {
        f32 delta = acceleration * D_800BE9A4;

        *(f32 *)(record + 0x48) = verticalVelocity + delta;
    }
    *(f32 *)(record + 0x20) += *(f32 *)(record + 0x50) * D_800BE9A4;
    *(f32 *)(record + 0x24) += *(f32 *)(record + 0x54) * D_800BE9A4;
    *(f32 *)(record + 0x28) += *(f32 *)(record + 0x58) * D_800BE9A4;
    return 1;
}

void func_150CBF5C(u8 *arg0) {
    *(u32 *)(arg0 + 0x58) |= 1;
    *(s16 *)(arg0 + 0x1C) = 0x20;
}
