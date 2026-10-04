#include <ultra64.h>

#include "variables.h"

extern f32 D_8009B688;
extern u8 D_800B85A4[];
extern s32 func_150229E4(struct127 *actor);
extern f32 func_1506AD30(struct127 *actor, f32 frame, s32 mode);
extern u8 D_800BEA0C;
extern u8 D_800C365E[];

typedef struct {
    void (*callback)(void);
    u16 flags;
    u8 pad6[2];
    f32 frame;
    f32 padC;
    f32 rate;
    f32 pad14;
    f32 end;
    f32 pad1C;
    f32 start;
    f32 pad24;
    s32 sequence;
    u8 pad2C[0xE];
    s16 decrement;
    s16 timer;
    u8 pad3E[2];
} AnimationTimelineA9260;

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

void func_1507BDB0(struct197 *input, f32 step, struct127 *actor, s32 mode) {
    AnimationTimelineA9260 *state = (AnimationTimelineA9260 *)input;
    f32 frame;
    f32 result;
    u32 flags;
    s32 sequence;
    u8 changed = 0;

    if (state->sequence == 0) {
        return;
    }
    if (actor != NULL) {
        if (D_800C35EA == 0) {
            if (D_800BE9A4 < 2.0f) {
                step = D_800BE9A4 * step;
            } else {
                step += step;
            }
        } else {
            step = D_800BE9A4;
        }
    }
    if (D_800BEA0C != 0) {
        step = 0.0f;
    }
    frame = state->rate * step;
    if (state->end < frame) {
        frame = state->end + state->frame;
    } else {
        frame += state->frame;
    }
    flags = state->flags & 0x8000;
    if (actor != NULL) {
        actor->unk1FC &= ~4;
        D_800C3E78 = ((s32)actor - (s32)D_800CC2D0) / 0x32C;
        flags |= actor->unkF4 & 0xE;
        D_800D154C = actor;
        if (((&D_800C35EA)[mode] != 1) || (D_800C365E[mode] != 0)) {
            result = func_1506AD30(D_800D154C, frame, 0);
            if (result != 0.0f) {
                frame = result;
            }
        }
    }
    if (0.0f <= state->rate) {
        if (((state->end - 1.0f) <= frame) &&
            (state->frame < (state->end - 1.0f)) && (state->callback != NULL)) {
            sequence = state->sequence;
            if ((actor != NULL) && (actor->unkF4 & 8)) {
                actor->unk10C = 0;
                *(s32 *)((u8 *)actor + 0x1C4) = 0;
                state->rate = 0.0f;
            }
            if (D_800C35EA == 0) {
                state->callback();
            }
            if (sequence != state->sequence) {
                frame = state->frame;
                changed = 1;
            }
        }
        if ((actor != NULL) && (actor->unk1FD != 0) &&
            ((state->end - 1.0f) <= frame)) {
            actor->unk76 += actor->unk1FD << 8;
            actor->unk7A = actor->unk76;
            actor->unk78 = actor->unk76;
            state->frame = state->start;
            if (actor->unkF4 & 4) {
                actor->unk21C = 0;
            }
        } else if ((flags == 0) && (state->end <= frame)) {
            state->frame = (frame - state->end) + state->start;
            changed = 1;
            if (actor != NULL) {
                actor->unk1FC |= 4;
            }
        } else if ((flags != 0) && ((state->end - 1.0f) <= frame)) {
            if (((actor != NULL) && (actor->unkF4 & 0xA)) || (state->flags & 0x8000)) {
                state->frame = state->end - 1.0f;
            } else if (state->frame < (state->end - 1.0f)) {
                state->frame = state->end - 1.0f;
                if ((actor != NULL) && (actor->unkF4 & 4)) {
                    actor->unk21C = 0;
                }
            } else {
                state->frame = state->start;
                if (actor != NULL) {
                    actor->unk138 = 0;
                    actor->unk1FC |= 2;
                }
            }
            if ((actor != NULL) && (actor->unkF4 & 8)) {
                actor->unk10C = 0;
                *(s32 *)((u8 *)actor + 0x1C4) = 0;
                state->rate = 0.0f;
            }
            if (state->frame < 0.0f) {
                state->frame = 0.0f;
            }
        } else {
            state->frame = frame;
        }
    } else {
        if (frame < state->start) {
            state->frame = (frame - state->start) + state->end;
        } else {
            state->frame = frame;
        }
    }
    if (state->timer > 0) {
        state->timer = (u32)(s32)state->timer - (u32)(s32)state->decrement * (u32)D_800BE9E4;
    }
    if (actor != NULL) {
        if (changed != 0) {
            func_1506AD30(D_800D154C, state->frame, 0);
        }
        /* The final event helper can replace the frame before publication. */
        *(f32 *)&actor->padB4 = state->frame;
    }
}

void func_1507C22C(s32 mode) {
    struct127 *actor = D_800CC2D0;
    struct127 *end = (struct127 *)&D_800D121C;

    do {
        if ((actor->interaction_state != 0) && !(actor->unk25C & 0x200) &&
            ((mode == 0) || (actor->unk5 == 4))) {
            /* Retail tests the first byte, not the word-declared global's value. */
            if ((D_800C3638 == 0) || (*(u8 *)&D_800C3654 != 0) ||
                (func_150229E4(actor) != 0)) {
                if ((actor->unk2D0 != NULL) && (actor->unk2FA != 0)) {
                    func_1507BDB0(actor->unk2D0, actor->unk48, actor, mode);
                }
            }
        }
        actor++;
    } while (actor != end);
}

void func_1507C324(struct127 *destination, struct127 *source) {
    struct197 *destinationState = destination->unk2D0;
    struct197 *sourceState = source->unk2D0;
    volatile f32 *output;
    f32 value;
    f32 limit;

    if ((destinationState != NULL) && (sourceState != NULL)) {
        output = &destinationState->unk8;
        value = sourceState->unk8;
        limit = destinationState->unk18;
        *output = value;
        if ((limit - 1.0f) <= *output) {
            *output = limit - 1.0f;
        }
    }
}

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
