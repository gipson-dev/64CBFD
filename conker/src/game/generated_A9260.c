#include <ultra64.h>

#include "variables.h"

extern f32 D_8009B688;
extern u8 D_800B85A4[];

typedef struct {
    u8 pad0[4];
    s32 unk4;
    u8 pad8[0xF];
    u8 unk17;
    u8 pad18[0x36];
    u8 unk4E;
    u8 unk4F;
    u8 pad50[0x147];
    u8 unk197;
    u8 pad198[0xE];
    u16 unk1A6;
    u8 pad1A8[0xB];
    u8 unk1B3;
} DimensionStateA9260;

typedef struct {
    u8 pad0[0x73C];
    s16 unk73C;
    u8 pad73E[0x21E];
    f32 unk95C;
    f32 unk960;
} DimensionCameraA9260;

/* Non-matching placeholders for the text-only asm slice asm/A9260.s. */

s32 func_1507BDB0() {
    return 0;
}

s32 func_1507C22C() {
    return 0;
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_A9260/func_1507C324.s")

void func_1507C3E0(struct127 *arg0, u16 *arg1, u16 *arg2, u16 *arg3);

void func_1507C370(void) {
    struct127 *object;
    struct126 *state;
    s32 i;

    object = D_800CC2D0;
    for (i = 0; i < D_8008FD8C; i++, object++) {
        state = object->unk31C;
        if (state != NULL) {
            func_1507C3E0(object, &state->unk114, &state->unk116,
                          &state->unk118);
        }
    }
}

void func_1507C3E0(struct127 *arg0, u16 *arg1, u16 *arg2, u16 *arg3) {
    DimensionStateA9260 *state;
    DimensionCameraA9260 *camera;
    f32 height;
    f32 baseRadius;
    f32 radius;
    s32 scaled;
    u32 subtype;

    if (arg0->interaction_state == 0) {
        height = 180.0f;
        radius = baseRadius = 60.0f;
        goto publish;
    }
    if (arg0->interaction_state == 0x2D) {
        camera = (DimensionCameraA9260 *)arg0->camera;
        height = camera->unk960;
        radius = baseRadius = camera->unk95C;
        goto publish;
    }
    if (arg0->interaction_state == 4) {
        height = (f32)arg0->unkE6 * 6.0f;
        radius = baseRadius = (f32)arg0->unkE4 * 3.0f;
        goto publish;
    }
    if (arg0->interaction_state == 0x2C) {
        height = 160.0f;
        radius = baseRadius = 80.0f;
        goto publish;
    }
    if (arg0->unk5 == 5) {
        height = (f32)arg0->unkE6 + (f32)arg0->unkE6;
        radius = baseRadius = (f32)arg0->unkE4;
        goto publish;
    }

    subtype = arg0->id;
    scaled = 1;
    if ((subtype <= 4) || (subtype == 0x3B) || (subtype == 0x75) ||
        (subtype == 0x80) || (subtype == 0x82) || (subtype == 0x88) ||
        (subtype == 0x90) || (subtype == 0x96) || (subtype == 0x98) ||
        (subtype == 0x9C) || (subtype == 0x9D) || (subtype == 0x9F) ||
        (subtype == 0xA0) || (subtype == 0xB0) || (subtype == 0xB1) ||
        (subtype == 0xB2) || (subtype == 0xB4)) {
        state = (DimensionStateA9260 *)arg0->unk31C;
        if ((state != NULL) && (state->unk4 != 0)) {
            radius = baseRadius = 60.0f;
            height = 80.0f;
        } else if ((state != NULL) && (state->unk17 != 0)) {
            radius = baseRadius = 70.0f;
            height = 300.0f;
        } else if (arg0->in_water != 0) {
            radius = baseRadius = 90.0f;
            height = 180.0f;
        } else {
            radius = baseRadius = 60.0f;
            height = 180.0f;
            if (state != NULL) {
                camera = (DimensionCameraA9260 *)arg0->camera;
                if (((camera != NULL) && (camera->unk73C != 0)) ||
                    (state->unk197 != 0) || (state->unk1B3 != 0)) {
                    radius = baseRadius = 120.0f;
                }
                height += (f32)state->unk1A6;
            }
        }
        if ((state != NULL) && ((state->unk4E & 0xF) == 1) &&
            (state->unk4F == 0) && (arg0->xz_velocity < 40.0f)) {
            radius = baseRadius = 110.0f;
            height = 500.0f;
        }
    } else if ((subtype == 0x25) || (subtype == 0x2E)) {
        radius = baseRadius = 90.0f;
        height = 70.0f;
    } else if (subtype == 0x36) {
        radius = baseRadius = 90.0f;
        height = D_8009B688;
    } else if (subtype == 0x9A) {
        radius = baseRadius = 45.0f;
        height = 60.0f;
        scaled = 0;
    } else if (subtype == 0xAC) {
        radius = baseRadius = 30.0f;
        height = 90.0f;
        scaled = 0;
    } else if ((subtype == 0x89) || (subtype == 0xBA)) {
        radius = baseRadius = 30.0f;
        height = 60.0f;
        scaled = 0;
    } else if (subtype == 0x53) {
        if (D_800BE616 != 0) {
            radius = baseRadius = 150.0f;
            height = 300.0f;
        } else {
            radius = baseRadius = 90.0f;
            height = 250.0f;
        }
    } else {
        height = (f32)arg0->unkE6 + (f32)arg0->unkE6;
        radius = baseRadius = (f32)arg0->unkE4;
        scaled = 0;
    }

    if ((arg0->unk13C >= 101) &&
        (D_800B85A4[arg0->unk13C * 0x32C] == 0x13)) {
        radius += 120.0f * arg0->xz_scale;
        height += 100.0f * arg0->y_scale;
    }
    if (scaled) {
        height *= arg0->y_scale;
        baseRadius *= arg0->xz_scale;
        radius *= arg0->xz_scale;
    }

publish:
    if (arg1 != NULL) {
        *arg1 = (u16)(s32)height;
    }
    if (arg2 != NULL) {
        *arg2 = (u16)(s32)baseRadius;
    }
    if (arg3 != NULL) {
        *arg3 = (u16)(s32)radius;
    }
}
