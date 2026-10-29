#include <ultra64.h>

#include "structs.h"

extern void func_1513CAA0();

typedef struct {
    u8 pad0[0x24];
    struct102 *resource24;
    struct102 *resource28;
    struct102 *resource2C;
    struct102 *resource30;
    struct102 *resource34;
} ActorOwnedResources101148;

extern void func_1513CA6C();

typedef struct {
    u8 pad0[0x110];
    ActorOwnedResources101148 resources;
    u8 pad148[0x58];
    u16 handle1A0;
} ActorResourceOwner101090;

/* Non-matching placeholders for the text-only asm slice asm/12DAB0.s. */

s32 func_15100600() {
    return 0;
}

/* Stop the unsigned handle, retire each owned object, then retire the actor. */
void func_15101090(ActorResourceOwner101090 *volatile actor) {
    extern void func_100111C8(u16 handle);
    extern void func_1516972C(struct102 *resource);
    u16 handle;
    ActorOwnedResources101148 *resources;

    handle = actor->handle1A0;
    if (handle != 0) {
        func_100111C8(handle);
    }
    resources = &actor->resources;
    if (resources->resource28 != NULL) {
        func_1516972C(resources->resource28);
    }
    if (resources->resource2C != NULL) {
        func_1516972C(resources->resource2C);
    }
    if (resources->resource24 != NULL) {
        func_1516972C(resources->resource24);
    }
    if (resources->resource30 != NULL) {
        func_1516972C(resources->resource30);
    }
    if (resources->resource34 != NULL) {
        func_1516972C(resources->resource34);
    }
    func_1513CA6C((struct210 *)actor);
}

/* Release owned objects in retail order, then destroy their actor. */
void func_15101148(struct210 *volatile actor) {
    extern void func_1516979C(struct102 *resource);
    struct102 *resource;
    ActorOwnedResources101148 *resources;

    resource = *(struct102 **)((u8 *)actor + 0x138);
    if (resource != NULL) {
        func_1516979C(resource);
    }
    resources = (ActorOwnedResources101148 *)((u8 *)actor + 0x110);
    if (resources->resource2C != NULL) {
        func_1516979C(resources->resource2C);
    }
    if (resources->resource24 != NULL) {
        func_1516979C(resources->resource24);
    }
    if (resources->resource30 != NULL) {
        func_1516979C(resources->resource30);
    }
    if (resources->resource34 != NULL) {
        func_1516979C(resources->resource34);
    }
    func_1513CAA0(actor);
}

s32 func_151011E8(u8 *arg0) {
    u8 *temp_v0 = *(u8 **)(arg0 + 0x124) + 0x110;

    *(s32 *)(temp_v0 + 0x28) = 0;
    func_1513CA6C(arg0);
}

s32 func_15101210(u8 *arg0) {
    u8 *temp_v0 = *(u8 **)(arg0 + 0x124) + 0x110;

    *(s32 *)(temp_v0 + 0x28) = 0;
    func_1513CAA0(arg0);
}

s32 func_15101238(u8 *arg0) {
    u8 *temp_v0 = *(u8 **)(arg0 + 0x18) + 0x110;

    *(s32 *)(temp_v0 + 0x2C) = 0;
    func_151617C4(arg0);
}

s32 func_15101260(u8 *arg0) {
    u8 *temp_v0 = *(u8 **)(arg0 + 0x18) + 0x110;

    *(s32 *)(temp_v0 + 0x2C) = 0;
    func_151617E4(arg0);
}

s32 func_15101288(u8 *arg0) {
    u8 *temp_v0 = *(u8 **)(arg0 + 0xD0) + 0x110;

    *(s32 *)(temp_v0 + 0x24) = 0;
    func_1513173C(arg0);
}

s32 func_151012B0(u8 *arg0) {
    u8 *temp_v0 = *(u8 **)(arg0 + 0xD0) + 0x110;

    *(s32 *)(temp_v0 + 0x24) = 0;
    func_1513175C(arg0);
}

s32 func_151012D8(u8 *arg0) {
    u8 *temp_v0 = *(u8 **)(arg0 + 0x170) + 0x110;

    *(s32 *)(temp_v0 + 0x30) = 0;
    func_151411A4(arg0);
}

s32 func_15101300(u8 *arg0) {
    u8 *temp_v0 = *(u8 **)(arg0 + 0x170) + 0x110;

    *(s32 *)(temp_v0 + 0x30) = 0;
    func_151411C4(arg0);
}

s32 func_15101328(u8 *arg0) {
    u8 *temp_v0 = *(u8 **)(arg0 + 0xA8) + 0x110;

    *(s32 *)(temp_v0 + 0x34) = 0;
    func_1513173C(arg0);
}

s32 func_15101350(u8 *arg0) {
    u8 *temp_v0 = *(u8 **)(arg0 + 0xA8) + 0x110;

    *(s32 *)(temp_v0 + 0x34) = 0;
    func_1513175C(arg0);
}

s32 func_15101378() {
    return 0;
}

s32 func_151019C4() {
    return 0;
}

s32 func_15101F50() {
    return 0;
}

s32 func_151022AC() {
    return 0;
}

typedef struct {
    f32 valueX;
    f32 valueY;
    f32 baseX;
    f32 baseY;
    f32 amplitudeX;
    f32 amplitudeY;
    f32 phaseX;
    f32 phaseY;
    f32 rateX;
    f32 rateY;
} PairedSineState;
typedef struct {
    u8 pad[0xA8];
    PairedSineState state;
} PairedSineOwner;
extern f32 D_800BE9A4;
f32 sinf(f32);
f32 func_15144B68(f32);

/* Update both sine outputs, advance their phases, then normalize each phase. */
s32 func_151025F4(PairedSineOwner *volatile owner, void *context) {
    /* Preserve the retail frame and first-sine stack slot. */
    struct { f32 y; f32 x; f32 reserved[2]; } sines;
    PairedSineState *state;

    sines.x = sinf(owner->state.phaseX);
    state = (PairedSineState *)owner;
    sines.y = ((PairedSineOwner *)state)->state.phaseY;
    state = (PairedSineState *)((u8 *)state + 0xA8);
    sines.y = sinf(sines.y);
    state->valueX = state->baseX + state->amplitudeX * sines.x;
    state->valueY = state->baseY + state->amplitudeY * sines.y;
    state->phaseX += state->rateX * D_800BE9A4;
    state->phaseY += state->rateY * D_800BE9A4;
    state->phaseX = func_15144B68(state->phaseX);
    state->phaseY = func_15144B68(state->phaseY);
    return 1;
}

s32 func_151026BC() {
    return 0;
}

s32 func_151027E8(u8 *arg0) {
    struct { u8 *ptr; u8 value; } temp;

    temp.ptr = arg0;
    temp.value = *(u8 *)(arg0 + 0x3B);
    func_151403A8(&temp, 0x1A);
}

s32 func_1510281C(u8 *arg0, s16 arg1) {
    u8 *base = *(u8 **)(arg0 + 0xD0);
    u8 *nested;

    base += 0x110;
    if (arg1 == *(u8 *)(base + 0x22)) {
        nested = *(u8 **)base;
        if ((nested == NULL) || (*(u8 *)(*(u8 **)(nested + 0x31C) + 0x197) != 0)) {
            return 0;
        }
    }

    if (!(*(u8 *)(arg0 + 0xD4) & 1)) {
        return 0;
    }
    return 1;
}

s32 func_15102884(u8 *arg0, u8 arg1) {
    if (!(*(arg0 + 0xAC) & 1)) {
        return 0;
    }
    return 1;
}

s32 func_151028AC(u8 *arg0, s16 arg1) {
    u8 *base = *(u8 **)(arg0 + 0x170);
    u8 *nested;

    base += 0x110;
    if (arg1 == *(u8 *)(base + 0x22)) {
        nested = *(u8 **)base;
        if ((nested == NULL) || (*(u8 *)(*(u8 **)(nested + 0x31C) + 0x197) != 0)) {
            return 0;
        }
    }

    if (!(*(u8 *)(arg0 + 0x174) & 1)) {
        return 0;
    }
    return 1;
}
