#include <ultra64.h>
#include "structs.h"
extern s16 D_800DC204[];
extern s16 D_800DC206[];
f32 sqrtf(f32);
/* Keep the current provider return declaration; this caller ignores it. */
s32 func_15123A54(struct108 *);
void func_1512C150(struct108 *);


/* Restored functions and remaining placeholders for asm/157840.s. */

s32 func_1512A390() {
    return 0;
}

typedef struct { s16 x, y, width, height; } CoordinatePreset1512ABF8;
extern CoordinatePreset1512ABF8 D_80089590[4], D_800DC200[4][4];
extern u8 D_800DC0C0[];
extern s32 D_80082FA0, D_800BE9F0;

/* Copy and scale the four coordinate presets for each output group. */
void func_1512ABF8(void) {
    s32 players = D_80082FA0;
    s32 mode = D_800BE9F0;
    u8 group, index;
    for (group = 0; group < 4; group++) {
        for (index = 0; index < 4; index++) {
            D_800DC200[group][index] = D_80089590[index];
            if (players > 0 && players < 4) {
                D_800DC200[group][index].x = D_800DC200[group][index].x * 0.5f;
                D_800DC200[group][index].y = D_800DC200[group][index].y * 0.5f;
            }
            if (mode == 27 || mode == 30) {
                D_800DC200[group][index].x = D_800DC200[group][index].x * 0.75f;
                D_800DC200[group][index].y = D_800DC200[group][index].y * 0.75f;
            }
        }
    }
    bzero(D_800DC0C0, 0x130);
}

s32 func_1512AD54() {
    return 0;
}

extern u8 D_800BEAC0;
extern u8 D_800C3671;

/* Request the fixed state unless the actor can use its normal handler. */
void func_1512B100(u8 *actor) {
    s32 type = *(s32 *)(actor + 0x2C);

    if ((type & ~0x100) && !D_800BEAC0 && !D_800C3671) {
        if ((type != 0x40) && (*(s32 *)(actor + 0x84) & 8) &&
            !(*(s32 *)(actor + 0x84) & 0x200) && !actor[0x23C] &&
            !(*(s32 *)(actor + 0x5F0) & 0x80) && !(*(s32 *)(actor + 0x5F0) & 0x40)) {
            func_1512AD54(actor);
        } else {
            *(s16 *)(actor + 0x5F8) = 1;
            *(u16 *)(actor + 0x5FC) = 2;
            *(s16 *)(actor + 0x5FE) = 60;
        }
    }
}

s32 func_1512B1B8() {
    return 0;
}

extern s32 D_800BE628;
/* Reset each active slot marker while the actor's refresh counter is nonzero. */
s32 func_1512B53C(u8 *actor) {
    s32 index;
    u32 offset;

    if (*(s16 *)(actor + 0x5FC) == 0) goto inactive;
    {
        *(s16 *)(actor + 0x5F8) = 1;
        index = 0;
        offset = 0;
        while ((f32)index < *(f32 *)((u32)D_800BE628 + actor[0x23D] * 0x180 + 4)) {
            *(u16 *)(*(u8 **)(actor + 0x8BC) + offset) = 0xFFFC;
            index = (s32)((u32)index + 1);
            offset += 2;
        }
        *(f32 *)(actor + 0x60C) = 0.0f;
        *(s16 *)(actor + 0x5FC) -= 1;
        return 1;
    }
inactive:
    return 0;
}

void func_1512B5FC(u8 *arg0, s32 arg1, s32 arg2) {
    *(arg0 + 2) = *(arg0 + 1);
    if (*(s32 *) (arg0 + 4) < arg1) {
        *(arg0 + 1) = 0;
    } else {
        *(arg0 + 1) = 1;
    }
    *(s32 *) (arg0 + 8) = arg2;
    *(s32 *) (arg0 + 4) = arg1;
}

typedef struct {
    u8 state;
    u8 active;
    u8 previous;
    u8 pad3;
    s32 value;
    s32 threshold;
} ActorThresholdTransition;

/* Update a directional transition from the actor's signed threshold. */
s32 func_1512B630(u8 *actor, ActorThresholdTransition *transition,
                  s32 threshold, s32 value, s32 otherValue, s32 alternate) {
    s32 actorThreshold;

    if (alternate == 0) {
        actorThreshold = *(s16 *)((u8 *)D_800DC204 +
                                  *(s16 *)(actor + 0x1B4) * 8 +
                                  actor[0x23D] * 0x20);
    } else {
        actorThreshold = *(s16 *)((u8 *)D_800DC206 +
                                  *(s16 *)(actor + 0x1B4) * 8 +
                                  actor[0x23D] * 0x20);
    }
    if (*(s32 *)(actor + 0x84) & 0x8000) {
        actorThreshold = (s16)(actorThreshold * 2);
    }
    if ((actorThreshold < threshold) && (value < otherValue)) {
        transition->state = 2;
        func_1512B5FC((u8 *)transition, value, threshold);
        return 1;
    }
    if ((actorThreshold < threshold) && (otherValue < value)) {
        transition->state = 1;
        func_1512B5FC((u8 *)transition, value, threshold);
        return 1;
    }
    transition->active = 0;
    transition->state = 0;
    transition->threshold = 0xFFFC;
    return 0;
}

s32 func_1512B730() {
    return 0;
}

s32 func_1512BB10() {
    return 0;
}

/* Start a near-target angle blend, then advance the current blend. */
void func_1512C068(struct108 *actor) {
    f32 direction;
    f32 x;
    f32 z;
    f32 distance;

    if (actor->unk390 < 180.0f) {
        direction = 2.0f;
    } else {
        direction = -2.0f;
    }
    if (actor->unk2C != 0x80 && actor->unk2C != 0x40) {
        x = actor->unk2F8 - actor->unk2BC;
        z = actor->unk300 - actor->unk2C4;
        distance = sqrtf(x * x + z * z);
        *(f32 *)actor->pad370 = distance;
        if (distance < 42.0f) {
            actor->unk384 = actor->unk37C - 45.0f * direction;
            actor->unk5CC = 0.0f;
            func_15123A54(actor);
            actor->unk240 |= 2;
        }
    }
    func_1512C150(actor);
}

extern f32 D_800A3694, D_800A3698;
f32 func_15048A70(f32 current, f32 target);

/* Advance the angle blend, then mark completion or apply one wrapped delta. */
void func_1512C150(struct108 *actor) {
    f32 delta;

    actor->unk5CC += D_800A3694;
    actor->unk5CC = actor->unk5CC > 1.0f ? 1.0f : actor->unk5CC;
    if (actor->unk5CC == 1.0f) {
        actor->unk384 = D_800A3698;
        actor->unk240 &= ~2;
    } else {
        delta = func_15048A70(actor->unk384, actor->unk37C);
        actor->unk384 += delta * actor->unk5CC;
    }
}

void func_1512C200(s32 arg0) {
}

s32 func_1512C20C() {
    return 0;
}

s32 func_1512C47C(s32 arg0) {
    return 1;
}
