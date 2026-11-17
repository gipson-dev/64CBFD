#include <ultra64.h>
#include "structs.h"
extern f32 D_800A8FEC;
void func_151AA264(u8 *, f32 *);
extern f32 D_800A8F7C;
u16 func_10010FFC(s32, s32, u16, s16, u8, void *);
extern f32 D_800A8F90;

extern f32 D_800A8F8C;

extern f32 D_800A8F74;
s32 func_15045800(f32 *, u16, f32, void *);
void func_151ABE40(f32 *, void *, s32, u8, s32);

void func_1516972C(struct102 *);

typedef struct { u8 *owner; u8 identity; u8 opaque5[3]; } PayloadOwnerLink;
typedef struct { u8 *before; u8 *after; u8 before_identity; u8 after_identity; u8 opaqueA[2]; } PayloadOwnerLinkEvent;

/* Non-matching placeholders for the text-only asm slice asm/1D6E80.s. */

s32 func_1519F400();

/* Probe below the attached actor and submit a height-aligned effect on a hit. */
void func_151A99D0(u8 *input) {
    u8 *owner = input;
    f32 position[3];
    u8 *actor;

    actor = *(u8 **)(owner + 0x18);
    position[0] = *(f32 *)(actor + 0x14);
    if (D_800A8F74 < *(f32 *)(actor + 0x118)) {
        position[1] = *(f32 *)(actor + 0x118) + 100.0f;
    } else {
        position[1] = *(f32 *)(actor + 0x18) + 150.0f;
    }
    position[2] = *(f32 *)(actor + 0x1C);
    if (func_15045800(position, 0, position[1] - 300.0f, owner + 0x34)) {
        position[1] = *(f32 *)(owner + 0x34);
        func_151ABE40(position, owner + 0x34, 3, owner[0xC], owner[1]);
    }
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1D6E80/func_151A9AA4.s")

/* Probe below the attached actor, submit an effect, and start its hit sound. */
void func_151A9BA0(u8 *input) {
    u8 *owner = input;
    f32 position[3];
    u8 *actor;

    actor = *(u8 **)(owner + 0x18);
    position[0] = *(f32 *)(actor + 0x14);
    if (D_800A8F7C < *(f32 *)(actor + 0x118)) {
        position[1] = *(f32 *)(actor + 0x118) + 100.0f;
    } else {
        position[1] = *(f32 *)(actor + 0x18) + 150.0f;
    }
    position[2] = *(f32 *)(actor + 0x1C);
    if (func_15045800(position, 0, position[1] - 300.0f, owner + 0x34)) {
        position[1] = *(f32 *)(owner + 0x34);
        func_151ABE40(position, owner + 0x34, 1, owner[0xC], owner[1]);
        func_10010FFC(0, 0x11, 0x5208, 0, 0, actor);
    }
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1D6E80/func_151A9CA0.s")

/* Note 313: original ROM implementation, retained as assembly until C conversion. */
#pragma GLOBAL_ASM("asm/nonmatchings/generated_1D6E80/func_151A9DC0.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1D6E80/func_151A9EC0.s")

/* Probe below the attached actor and submit a height-aligned kind-four effect on a hit. */
void func_151A9FC8(u8 *input) {
    u8 *owner = input;
    f32 position[3];
    u8 *actor;

    actor = *(u8 **)(owner + 0x18);
    position[0] = *(f32 *)(actor + 0x14);
    if (D_800A8F8C < *(f32 *)(actor + 0x118)) {
        position[1] = *(f32 *)(actor + 0x118) + 100.0f;
    } else {
        position[1] = *(f32 *)(actor + 0x18) + 150.0f;
    }
    position[2] = *(f32 *)(actor + 0x1C);
    if (func_15045800(position, 0, position[1] - 300.0f, owner + 0x34)) {
        position[1] = *(f32 *)(owner + 0x34);
        func_151ABE40(position, owner + 0x34, 4, owner[0xC], owner[1]);
    }
}

/* Probe below the attached actor and submit a height-aligned kind-four effect on a hit. */
void func_151AA09C(u8 *input) {
    u8 *owner = input;
    f32 position[3];
    u8 *actor;

    actor = *(u8 **)(owner + 0x18);
    position[0] = *(f32 *)(actor + 0x14);
    if (D_800A8F90 < *(f32 *)(actor + 0x118)) {
        position[1] = *(f32 *)(actor + 0x118) + 100.0f;
    } else {
        position[1] = *(f32 *)(actor + 0x18) + 150.0f;
    }
    position[2] = *(f32 *)(actor + 0x1C);
    if (func_15045800(position, 0, position[1] - 300.0f, owner + 0x34)) {
        position[1] = *(f32 *)(owner + 0x34);
        func_151ABE40(position, owner + 0x34, 4, owner[0xC], owner[1]);
    }
}

void func_151AA170(s32 arg0) {
}

void func_151AA17C(u8 *arg0) {
    void *volatile rec_ptr;
    struct {
        u8 *target;
        u8 code;
    } rec;

    rec.target = *(u8 **) (arg0 + 0x18);
    rec.code = arg0[0x1C];
    rec_ptr = &rec;
    func_15147D64(&rec, 0xA);
    func_151494E0(rec_ptr, 0xA);
    func_1519F3B8(arg0);
}

void func_151AA1D0(u8 *arg0) {
    func_1519F400(arg0);
}

void func_151AA1F0(u8 *arg0) {
    func_1519F400(arg0);
}

void func_151AA210(u8 *arg0) {
    void *volatile rec_ptr;
    struct {
        u8 *target;
        u8 code;
    } rec;

    rec.target = *(u8 **) (arg0 + 0x18);
    rec.code = arg0[0x1C];
    rec_ptr = &rec;
    func_15147D64(&rec, 0xA);
    func_151494E0(rec_ptr, 0xA);
    func_1519F3B8(arg0);
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1D6E80/func_151AA264.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1D6E80/func_151AA30C.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1D6E80/func_151AA48C.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1D6E80/func_151AA5A4.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1D6E80/func_151AA6D8.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1D6E80/func_151AAA4C.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1D6E80/func_151AAABC.s")

s32 func_151AAB50(u8 *arg0) {
    u8 *temp_v0 = *(u8 **)(arg0 + 0x80) + 0x58;

    *(s32 *)(temp_v0 + 0x14) = 0;
    func_151352EC(arg0);
}

s32 func_151AAB78(u8 *arg0) {
    u8 *temp_v0 = *(u8 **)(arg0 + 0x80) + 0x58;

    *(s32 *)(temp_v0 + 0x14) = 0;
    func_1513530C(arg0);
}

s32 func_151AABA0(u8 *arg0) {
    s32 result = 1;

    if (*(u8 *)(arg0 + 0x84) == 0) {
        result = 0;
    }
    *(u8 *)(arg0 + 0x84) = 0;
    return result;
}

typedef struct { f32 xyz[3]; } BoneHitPosition151AABC4;
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
typedef struct HeightActor71820 HeightActor71820;
typedef struct {
    BoneHitPosition151AABC4 position;
    f32 timeBase;
    f32 timeRange;
    f32 scaleBase;
    f32 scaleRange;
    f32 radiusBase;
    f32 radiusRange;
    s16 countBase;
    s16 countRange;
    s16 requestSelectorBase;
    s16 requestSelectorRange;
    s16 durationBase;
    s16 durationRange;
    s16 modeBase;
    s16 modeRange;
    u8 selector;
    u8 private35[3];
    f32 opaqueChance;
    s16 firstValue;
    s16 secondValue;
    s32 requestValue;
} BoneHitTrail151AABC4;
typedef struct { s16 firstAngleBase, firstAngleRange, secondAngleBase, secondAngleRange; } BoneHitAngles151AABC4;
extern u8 D_800A8F70[];
extern f32 D_800A8FCC, D_800A8FD0, D_800A8FD4, D_800A8FD8, D_800A8FDC;
u8 func_151D8E20(void);
void func_15142314(u8 *, s32, f32 *);
void func_1504715C(HeightResult71820 *, HeightActor71820 *);
s32 func_1504697C(f32 *, u16, f32, HeightResult71820 *);
void func_151DBCBC(u8, f32, s16, s32, void *, u8, s32);
void func_15153F18(void *, void *, s32, s32, s32);

/* Query the selected actor bone, then emit the hit and its angular trails. */
void func_151AABC4(u8 *actor, u8 bone) {
    BoneHitPosition151AABC4 bonePosition;
    HeightResult71820 surface;
    f32 upper;
    BoneHitPosition151AABC4 query;
    u8 selector;
    BoneHitPosition151AABC4 position;
    BoneHitTrail151AABC4 trail;
    BoneHitAngles151AABC4 angles;

    if (actor != NULL && *(u8 **)(actor + 0x1D4) != NULL) {
        selector = func_151D8E20();
        func_15142314(*(u8 **)(actor + 0x1D4), D_800A8F70[bone], bonePosition.xyz);
        func_1504715C(&surface, (HeightActor71820 *)actor);
        query.xyz[0] = bonePosition.xyz[0];
        upper = bonePosition.xyz[1] + 50.0f;
        query.xyz[1] = upper;
        query.xyz[2] = bonePosition.xyz[2];
        if (func_1504697C(query.xyz, 0, upper - 100.0f, &surface)) {
            position.xyz[0] = bonePosition.xyz[0];
            position.xyz[1] = surface.height;
            position.xyz[2] = bonePosition.xyz[2];
            func_151DBCBC(selector, 40.0f, 150, (s32)surface.vertices, &position, 255, 1);
            /* The first emitter may update the exposed hit position. */
            trail.position = position;
            trail.countBase = 3;
            trail.countRange = 3;
            angles.firstAngleBase = 0;
            angles.firstAngleRange = 255;
            angles.secondAngleBase = -64;
            angles.secondAngleRange = 26;
            trail.requestSelectorBase = 3;
            trail.timeBase = 2.5f;
            trail.timeRange = D_800A8FCC;
            trail.scaleBase = D_800A8FD0;
            trail.scaleRange = D_800A8FD4;
            trail.radiusBase = D_800A8FD8;
            trail.radiusRange = D_800A8FDC;
            trail.requestSelectorRange = 1;
            trail.durationBase = 30;
            trail.durationRange = 20;
            trail.modeBase = 155;
            trail.modeRange = 100;
            trail.selector = selector;
            trail.opaqueChance = 0.0f;
            trail.firstValue = 16;
            trail.secondValue = 15;
            trail.requestValue = 0;
            func_15153F18(&angles, &trail, (s32)&surface, 255, 1);
        }
    }
}

s32 func_151AADBC(u8 *arg0) {
    u8 *temp_v0 = *(u8 **) (arg0 + 0x98);
    s32 temp_v1 = *(s16 *) (arg0 + 0x1C) << 4;

    if (temp_v1 >= 0x100) {
        temp_v1 = 0xFF;
    }
    if (temp_v1 < *(temp_v0 + 0x1B)) {
        *(temp_v0 + 0x1B) = temp_v1;
    }
    return 1;
}

typedef struct {
    u8 *owner;
    u8 enabled, pad05[3];
    f32 base, range, zero;
    s16 zero14, count0, count1;
    u8 pad1a[2];
    f32 rate;
} GroundLinkPayload151AADF8;
typedef struct {
    u32 flags;
    s16 duration;
    u8 kind, pad07;
    u32 zero08;
    s32 angle;
    u8 opacity, alpha, red, green, blue, alpha2, zero16, mode;
    u32 flags18;
    u8 untouched1c[12];
} GroundLinkDescriptor151AADF8;
extern f32 D_800A8FE0, D_800A8FE4, D_800A8FE8;
extern u8 D_800AB414[];
f32 func_150ADA68(void);
s32 func_150ADA20(void);
u8 *func_1513C73C(s32, u8, u8, s32, f32, f32, f32, f32, f32, u8, u8, s32, u8, s32);
void *memcpy(void *, const void *, u32);
typedef struct { u8 opaque0[0x18]; u8 *effect; } GroundLinkSlot151AADF8;

/* Notify the existing ground effect, or create it and attach its oscillator. */
void func_151AADF8(u8 *owner) {
    u8 *actor;
    GroundLinkSlot151AADF8 *links;
    u8 *oscillator;
    f32 position[3];
    GroundLinkDescriptor151AADF8 descriptor;
    GroundLinkPayload151AADF8 payload;
    f32 scale;
    u8 selector;
    u32 second;
    u32 first;

    actor = *(u8 **)(owner + 0x18);
    if (*(u32 *)(owner + 0x70) != 0) {
        oscillator = *(u8 **)(owner + 0x70) + 0xB0;
        oscillator[4] = 1;
    } else {
        position[0] = *(f32 *)(actor + 0x14);
        if (D_800A8FE0 < *(f32 *)(actor + 0x118)) {
            position[1] = *(f32 *)(actor + 0x118) + 100.0f;
        } else {
            position[1] = *(f32 *)(actor + 0x18) + 150.0f;
        }
        position[2] = *(f32 *)(actor + 0x1C);
        if (func_15045800(position, 0, position[1] - 300.0f, owner + 0x34)) {
            selector = func_151D8E20();
            position[1] = *(f32 *)(owner + 0x34);
            scale = func_150ADA68() * 30.0f + 50.0f;
            payload.owner = owner;
            payload.enabled = 1;
            payload.base = D_800A8FE4;
            payload.range = 32768.0f;
            payload.zero = 0.0f;
            payload.zero14 = 0;
            payload.count0 = 10;
            payload.count1 = 10;
            payload.rate = D_800A8FE8;
            descriptor.flags = 0x60300;
            descriptor.duration = 300;
            descriptor.kind = 0x38;
            descriptor.zero08 = 0;
            descriptor.angle = (s32)(payload.range * 0.5f + payload.base);
            descriptor.opacity = 150;
            descriptor.alpha = 255;
            actor = D_800AB414 + selector * 3;
            descriptor.red = actor[0];
            descriptor.green = actor[1];
            descriptor.blue = actor[2];
            descriptor.alpha2 = 255;
            descriptor.zero16 = 0;
            descriptor.mode = 6;
            descriptor.flags18 = 0x440001;
            first = (u32)func_150ADA20();
            second = (u32)func_150ADA20();
            links = (GroundLinkSlot151AADF8 *)(owner + 0x58);
            links->effect = func_1513C73C((s32)&descriptor, 7, 1, (s32)(owner + 0x38),
                position[0], position[1], position[2], scale, scale,
                first & 255, (((u32)func_150ADA20() & 1) << 1) + (second & 1),
                32, 255, 1);
            if (links->effect != NULL) memcpy(links->effect + 0xB0, &payload, 32);
        }
    }
}

typedef struct {
    u32 opaque0;
    u8 notification;
    u8 opaque5[3];
    f32 base;
    f32 amplitude;
    f32 target;
    s16 remaining;
    s16 minimum;
    s16 range;
    u16 opaque1A;
    f32 gain;
} EmbeddedIntegerOscillator;
extern s32 D_800BE9E4;
s32 func_150ADA20(void);
f32 func_150ADA68(void);
/* Capture and clear notification, renew expired timing, then blend the signed rate. */
s32 func_151AB090(u8 *input) {
    EmbeddedIntegerOscillator *oscillator;
    s8 notified;
    oscillator = (EmbeddedIntegerOscillator *)(input + 0xB0);
    notified = 1;
    if (oscillator->notification == 0) notified = 0;
    oscillator->notification = 0;
    oscillator->remaining -= (u32)D_800BE9E4;
    if (oscillator->remaining < 0) {
        u32 randomValue;
        randomValue = (u32)func_150ADA20();
        oscillator->remaining = randomValue % (oscillator->range + 1) + oscillator->minimum;
        oscillator->target = func_150ADA68();
        oscillator->target = oscillator->target * oscillator->amplitude + oscillator->base;
    }
    *(s32 *)(input + 0x24) = (u32)(s32)((oscillator->target - (f32)*(s32 *)(input + 0x24)) * oscillator->gain) + (u32)*(s32 *)(input + 0x24);
    return notified;
}

// Retail retains the otherwise dead temp_v0 + 0x58 update before the call.
#pragma GLOBAL_ASM("asm/nonmatchings/generated_1D6E80/func_151AB180.s")

/* Probe below the attached actor, submit the hit effect and sound, then finalize it. */
void func_151AB1C4(u8 *owner) {
    u8 *actor;
    f32 position[3];

    actor = *(u8 **)(owner + 0x18);
    position[0] = *(f32 *)(actor + 0x14);
    if (D_800A8FEC < *(f32 *)(actor + 0x118)) {
        position[1] = *(f32 *)(actor + 0x118) + 100.0f;
    } else {
        position[1] = *(f32 *)(actor + 0x18) + 150.0f;
    }
    position[2] = *(f32 *)(actor + 0x1C);
    if (func_15045800(position, 0, position[1] - 300.0f, owner + 0x34)) {
        position[1] = *(f32 *)(owner + 0x34);
        func_151ABE40(position, owner + 0x34, 3, owner[0xC], owner[1]);
        func_10010FFC(0, 0x11, 0x5208, 0, 0, actor);
    }
    func_151AA264(actor, (f32 *)(owner + 0x34));
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1D6E80/func_151AB2C4.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1D6E80/func_151AB3A4.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1D6E80/func_151AB6B8.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1D6E80/func_151AB788.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1D6E80/func_151AB7D8.s")

void func_151AB828(u8 *arg0) {
    func_15141DA4(*(s32 *) (arg0 + 0x18), 0, 4);
}

void *func_15190770(struct185 *, s32, u8, s32);

/* Submit an effect for supported actor types and reset the attached timer. */
void func_151AB854(u8 *record) {
    u8 *actor = *(u8 **)(record + 0x18);
    struct185 packet;

    if (actor[4] == 0 || actor[4] == 1 || actor[4] == 2 || actor[4] == 3 || actor[4] == 4 || actor[4] == 150) {
        packet.unk0 = (struct127 *)actor;
        packet.unk4 = actor[0x3B];
        packet.unk6 = 300;
        packet.unk8 = 0;
        packet.unk9 = 0;
        if (actor[4] == 150) {
            packet.unkA = 3;
        } else {
            packet.unkA = 0;
        }
        if (actor[0x127] != 255) {
            *(s16 *)(*(u8 **)(actor + 0x31C) + 0x66) = 500;
        }
        func_15190770(&packet, 0, record[0xC], record[1]);
    }
}

void func_151AB920(s32 arg0, s32 arg1) {
}

/* Snapshot actor fields, then copy the packet if allocation succeeds. */
void func_151AB930(u8 *actor) {
    extern f32 D_800A9014;
    extern u8 func_151D8E20(void);
    extern void *func_151491F4(s16, s8, s8, u8, u8, s32, u8, s32);
    extern void *memcpy(void *, const void *, u32);
    u8 *created;
    struct {
        u8 *actor;
        u8 slot;
        u32 value;
        f32 time, scale, lifetime;
        u8 selector;
    } packet;

    packet.actor = actor;
    packet.slot = actor[0x3B];
    packet.value = *(u16 *)(actor + 0x84);
    packet.time = 0.0f;
    packet.scale = D_800A9014;
    packet.lifetime = 3.0f;
    packet.selector = func_151D8E20();
    created = func_151491F4(0x3C, -1, 0xE, 1, 9, 0x1C, 0xFF, 0);
    if (created != NULL) {
        memcpy(created + 0x28, &packet, 0x1C);
    }
}

typedef struct {
    u8 *actor;
    u8 identity;
    u8 padding5[3];
    u32 value;
    f32 time, rateBase, rateRange;
    u8 selector;
    u8 padding19[3];
} ActorAccumulator151AB9C8;
extern f32 D_800BE9A4, D_800A9018, D_800A901C;
f32 func_151423D8(u8);
void *func_151D9014(void *, f32 *, u8, f32, s16, u8, f32, u8,
                  f32, f32, u8, s32, u8, u8, u8, s32);

/* Emit accumulated actor particles while the captured actor snapshot is valid. */
void func_151AB9C8(u8 *record) {
    s8 invalid;
    HeightResult71820 surface;
    f32 position[3];
    f32 velocity[3];
    ActorAccumulator151AB9C8 *state;
    s16 yaw;
    s16 pitch;
    f32 pitchValue;
    f32 pitchQuarter;
    f32 yawValue;
    f32 yawQuarter;
    f32 speed;
    f32 sample;
    f32 bias;
    u32 lifetime;
    u32 opacity;

    invalid = 0;
    state = (ActorAccumulator151AB9C8 *)(record + 0x28);
    if (*(u32 *)state->actor == 0) {
        invalid = 1;
    } else if (state->identity != state->actor[0x3B]) {
        invalid = 1;
    } else if (state->value != *(u16 *)(state->actor + 0x84)) {
        invalid = 1;
    }
    if (invalid == 0) {
        state = (ActorAccumulator151AB9C8 *)(record + 0x28);
        sample = func_150ADA68();
        state->time = state->time + (state->rateBase + sample * state->rateRange) * D_800BE9A4;
        if (state->time > 1.0f) {
            func_1504715C(&surface, (HeightActor71820 *)state->actor);
            do {
                yaw = (u32)func_150ADA20() & 255;
                pitch = (u32)func_150ADA20() % 46u - 63;
                pitchValue = func_151423D8((u8)pitch);
                pitchQuarter = func_151423D8((u8)(pitch - 64));
                yawValue = func_151423D8((u8)yaw);
                yawQuarter = func_151423D8((u8)(yaw - 64));
                sample = func_150ADA68();
                position[0] = *(f32 *)(state->actor + 0x14) + (30.0f * pitchValue) * yawQuarter;
                position[1] = *(f32 *)(state->actor + 0x18) - 75.0f * pitchQuarter;
                position[2] = *(f32 *)(state->actor + 0x1C) + (30.0f * pitchValue) * yawValue;
                speed = (sample * D_800A9018 + 500.0f) * D_800A901C;
                velocity[0] = (speed * pitchValue) * yawQuarter;
                velocity[1] = -speed * pitchQuarter;
                velocity[2] = (speed * pitchValue) * yawValue;
                bias = func_150ADA68();
                lifetime = (u32)func_150ADA20();
                opacity = (u32)func_150ADA20();
                sample = func_150ADA68();
                lifetime = lifetime % 26u + 32;
                opacity = opacity % 101u + 100;
                func_151D9014(position, velocity, state->selector,
                              bias * 0.5f + -1.0f, lifetime,
                              opacity, sample * 34.0f + 52.0f,
                              1, 1.0f, 1.0f, 1, (s32)&surface, 1, 0,
                              record[0x0C], record[1]);
                state->time -= 1.0f;
            } while (state->time > 1.0f);
        }
    }
    if (invalid != 0) {
        *(s16 *)(record + 0x0E) = -1;
    }
}

/* Retarget the payload owner link or release its matching actor. */
void func_151ABD54(struct260 *owner, s32 eventAddress, u8 command) {
    PayloadOwnerLink *link = (PayloadOwnerLink *)((u8 *)owner + 0x28);
    PayloadOwnerLinkEvent *event = (PayloadOwnerLinkEvent *)eventAddress;

    if (command == 0) {
        if (link->owner == event->before || link->identity == ((u8 *)event)[4]) {
            func_1516972C((struct102 *)owner);
        }
    } else if (command == 0x2D) {
        u8 *current = link->owner;
        if (current == event->before) {
            link->owner = event->after;
            link->identity = event->after_identity;
        } else if (current == event->after) {
            link->owner = event->before;
            link->identity = event->before_identity;
        }
    }
}

void func_151ABE00(u8 *arg0) {
    struct {
        u8 *target;
        u8 code;
    } rec;

    rec.target = arg0;
    rec.code = *(arg0 + 0x3B);
    func_1516944C(0x20, &rec, 0xC);
}
