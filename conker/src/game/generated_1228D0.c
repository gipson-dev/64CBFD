#include <ultra64.h>

extern f32 D_800A1B70;
void *func_15134DAC(s32, s32);
typedef struct {
    u8 owner_id;
    u8 pad1[3];
    u8 *owner;
    u8 attachmentIndex;
    u8 pad9[3];
    f32 zero0;
    f32 zero1;
    f32 zero2;
    f32 zero3;
    f32 value1C;
    f32 value20;
    u8 mode;
    u8 pad25;
    s16 activeFrames;
    s16 restartDelay;
    s16 lifetime;
    s16 value2C;
    s8 startCallback;
    s8 transformCallback;
    s8 updateCallback;
    u8 pad31[3];
    f32 rate;
    u8 flags;
    s8 finishCallback;
} OwnerLifetimeDescriptor1228D0;

#include "functions.h"

/* Non-matching placeholders for the text-only asm slice asm/1228D0.s. */

void func_150F55C8(u8 *record);

s32 func_15179008();

typedef struct {
    u8 *owner;
    u8 owner_id;
    u8 pad5[3];
    f32 value;
} Func150F5C08Payload;

extern u8 D_800917F8[], D_80091930[], D_8009193C[], D_80091948[];
void *func_15169968(void *);
typedef struct {
    u8 *asset; u32 retained04; u32 packedFirstSecond, packedThirdSum; s32 field10;
    s16 sum, field16, field18; u8 retained1A[2]; f32 field1C, field20;
    s16 field24, field26, field28, field2A, field2C, field2E;
    u8 field30, field31, field32, field33, field34, field35, field36, field37;
    u8 retained38, field39, retained3A[2];
} ModeDescriptor150F5420;
/* Construct a mode-specific descriptor and submit it for allocation. */
void *func_150F5420(u32 first, u32 second, u32 third, s32 mode) {
    ModeDescriptor150F5420 descriptor;
    u32 sum;
    if (mode != 0) {
        if (mode == 2) {
            descriptor.field2C = 240;
            descriptor.field2E = 186;
            descriptor.asset = D_80091948;
        } else {
            descriptor.field2C = 270;
            descriptor.field2E = 124;
            if (mode == 1) descriptor.asset = D_80091930;
            else descriptor.asset = D_8009193C;
        }
        descriptor.field30 = 9;
        descriptor.field39 = 16;
        descriptor.field28 = 0;
        descriptor.field2A = 0;
        descriptor.field36 = 8;
    } else {
        descriptor.asset = D_800917F8;
        descriptor.field30 = 10;
        descriptor.field2C = 160;
        descriptor.field2E = 192;
        descriptor.field39 = 32;
        descriptor.field28 = 0x1000;
        descriptor.field2A = 0x1000;
        descriptor.field36 = 24;
    }
    descriptor.packedFirstSecond = (first << 16) | second;
    sum = first + second + third;
    descriptor.packedThirdSum = (third << 16) | sum;
    descriptor.field10 = 10000;
    descriptor.sum = sum;
    descriptor.field18 = 0;
    descriptor.field24 = 0;
    descriptor.field26 = 0;
    descriptor.field31 = 1;
    descriptor.field32 = 255;
    descriptor.field33 = 255;
    descriptor.field34 = 255;
    descriptor.field37 = 17;
    descriptor.field35 = 0;
    descriptor.field16 = 0;
    descriptor.field1C = 146.0f;
    descriptor.field20 = 100.0f;
    return func_15169968(&descriptor);
}

void func_150F5590(u8 *arg0) {
    s32 val = 0x1000 - (*(s16 *) (arg0 + 0x24) << 2);

    *(s16 *) (arg0 + 0x38) = val;
    *(s16 *) (arg0 + 0x3A) = *(s16 *) (arg0 + 0x38);
    func_150F55C8(arg0);
}

/* Apply the record opacity envelope to its remaining lifetime. */
void func_150F55C8(u8 *record) {
    s32 duration = *(s32 *)(record + 0x1C) & 0xFFFF;
    s32 fadeIn = *(s32 *)(record + 0x18) >> 16;
    s32 hold = *(s32 *)(record + 0x18) & 0xFFFF;
    s32 fadeOut = *(s32 *)(record + 0x1C) >> 16;
    s32 boundary = duration - fadeIn;
    s32 remaining = *(s16 *)(record + 0x24);

    if (boundary < remaining) {
        record[0x45] = ((duration - remaining) * 255) / fadeIn;
    } else if (boundary - hold < remaining) {
        record[0x45] = 255;
    } else {
        record[0x45] = (remaining * 255) / fadeOut;
    }
}

void func_150F568C(s32 arg0) {
    func_15179008(0);
}

s32 func_150F56B0() {
    return 0;
}

s32 func_150F5A54() {
    return 0;
}

void func_150F5C08(u8 *arg0, s16 arg1, u8 arg2, s32 arg3) {
    Func150F5C08Payload payload;
    struct260 *object;

    payload.owner = arg0;
    payload.owner_id = arg0[0x3B];
    payload.value = 0.0f;

    object = func_15149130(arg1, -1, 0x51, -1, 1, 0x3E,
                           (struct37 *)sizeof(payload), arg2, arg3);
    if (object != NULL) {
        memcpy((u8 *)object + 0x28, &payload, sizeof(payload));
    }
}

s32 func_150F5C98() {
    return 0;
}

void func_150F6138(u8 *arg0, s32 arg1, u8 arg2) {
    func_15149514(arg1, arg2, (s32) (arg0 + 0x28), (s32) (arg0 + 0x2C), (s32) arg0);
}

s32 func_150F6178() {
    return 0;
}

void func_150F631C(u8 *arg0) {
    u8 *owner = arg0;

    if (*(struct102 * volatile *) (owner + 0x30) != NULL) {
        func_1516972C(*(struct102 * volatile *) (owner + 0x30));
    }
    if (*(struct102 **) (owner + 0x34) != NULL) {
        func_1516972C(*(struct102 **) (owner + 0x34));
    }
}

s32 func_150F6368(s32 arg0) {
    func_150F631C(arg0);
    func_1514933C(arg0);
}

s32 func_150F6394(s32 arg0) {
    func_150F631C(arg0);
    func_15149368(arg0);
}

void func_150F63C0(u8 *arg0, s32 arg1, u8 arg2) {
    func_15169850(arg1, arg2, (s32) (arg0 + 0x28), (s32) (arg0 + 0x2C), (s32) arg0);
}

void func_150F6400(u8 *arg0) {
    u8 *temp_v0;

    if (*(u8 * volatile *)(arg0 + 0x160) != NULL) {
        temp_v0 = *(u8 * volatile *)(arg0 + 0x160) + 0x28;
        *(s32 *)(temp_v0 + 8) = 0;
    }
}

s32 func_150F6420(s32 arg0) {
    func_150F6400(arg0);
    func_1513CA6C(arg0);
}

s32 func_150F644C(s32 arg0) {
    func_150F6400(arg0);
    func_1513CAA0(arg0);
}

void func_150F6478(s32 arg0) {
}

s32 func_150F6484(s32 arg0) {
    func_150F6478(arg0);
    func_151411A4(arg0);
}

s32 func_150F64B0(s32 arg0) {
    func_150F6478(arg0);
    func_151411C4(arg0);
}

s32 func_150F64DC() {
    return 0;
}

void func_150F6850(u8 *arg0, s32 arg1, u8 arg2) {
    func_15169850(arg1, arg2, (s32) (arg0 + 0x28), (s32) (arg0 + 0x2C), (s32) arg0);
}

/* Construct an owner-attached effect with a signed lifetime.
 * The two -1 callback indices disable those optional callbacks.
 * The original four-argument ABI retains the unused selector and context. */
void *func_150F6890(u8 *owner, s16 lifetime, s32 unusedSelector, s32 unusedContext) {
    OwnerLifetimeDescriptor1228D0 packet;
    packet.owner_id = owner[0x3B];
    packet.owner = owner;
    packet.attachmentIndex = 3;
    packet.zero0 = 0.0f;
    packet.zero1 = 0.0f;
    packet.zero2 = 0.0f;
    packet.zero3 = 0.0f;
    packet.value1C = D_800A1B70;
    packet.value20 = 8.5f;
    packet.mode = 2;
    packet.activeFrames = 40;
    packet.restartDelay = 16;
    packet.lifetime = lifetime;
    packet.startCallback = 5;
    packet.transformCallback = 8;
    packet.updateCallback = -1;
    packet.rate = 1.0f;
    packet.flags = 0;
    packet.finishCallback = -1;
    packet.value2C = 0;
    return func_15134DAC((s32)&packet, 0);
}

typedef struct HeightActor71820 HeightActor71820;
typedef struct HeightResult71820 {
    f32 height;
    s16 vertices[9];
    s16 pad16;
    u32 metadata;
    u8 flags;
    u8 state;
    u16 pad1E;
    s32 value;
} HeightResult71820;

typedef struct {
    u8 retained00;
    u8 context;
    u8 retained02[10];
    u8 group;
    u8 retained0D[15];
    HeightActor71820 *actor;
    u8 retained20[0x54];
    f32 derivativeScale;
} Emitter1228D0;

extern f32 D_800A1B74, D_800A1B78, D_800A1B7C;
void func_15137F30(f32 *, f32 *, f32 *, f32 *, f32, void *,
    f32 *, f32 *, f32 *, f32 *, s16 *, u8 *, f32 *);
void func_1504715C(HeightResult71820 *, HeightActor71820 *);
/* Assembly API: argument 12 carries a surface address as an O32 word. */
void *func_151D9014(void *, f32 *, u8, f32, s16, u8, f32, u8,
    f32, f32, u8, s32, u8, u8, u8, s32);

/* Interpolate an emitter sample and submit a randomized surface-aware effect. */
void func_150F695C(f32 *position, f32 *direction, f32 *positionStep,
                  f32 *directionStep, f32 time, Emitter1228D0 *emitter) {
    f32 interpolatedPosition[3];
    f32 interpolatedDirection[3];
    f32 velocity[3];
    f32 angle;
    s16 lifetime;
    u8 alpha;
    f32 scale;
    HeightResult71820 surface;
    u8 useSurface;
    s32 alternate;

    func_15137F30(position, direction, positionStep, directionStep, time,
        emitter, interpolatedPosition, interpolatedDirection, velocity,
        &angle, &lifetime, &alpha, &scale);
    scale *= 1.0f + func_150ADA68() * 2.0f;
    useSurface = func_150ADA68() < D_800A1B74;
    if (useSurface) {
        func_1504715C(&surface, emitter->actor);
    } else {
        surface.metadata = 0;
        surface.flags = 0;
        surface.state = 0;
        surface.value = 0;
        surface.height = D_800A1B78;
    }
    if (useSurface) alternate = func_150ADA68() < 0.5f ? 1 : 0;
    else alternate = 0;
    func_151D9014(interpolatedPosition, velocity, 1, angle, lifetime, alpha,
        scale, useSurface, D_800A1B7C, D_800A1B7C, 1, (s32)&surface, 1,
        alternate, emitter->group, emitter->context);
}
