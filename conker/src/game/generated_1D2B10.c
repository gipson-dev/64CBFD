#include <ultra64.h>
void func_100111C8(u16 arg0);
void func_151A5D2C();

/* Non-matching placeholders for the text-only asm slice asm/1D2B10.s. */

typedef struct {
    f32 height;
    s16 vertices[9], reserved16;
    u32 metadata;
    u8 flags, state;
    u16 reserved1E;
    s32 value;
} RegionHeight151A5660;
typedef struct { f32 x, y, z; } RegionPosition151A5660;
/* Partial source view: the producer also reads flags/index through +0x1B. */
typedef struct {
    s16 x, y, z, radius, height, secondRadius;
    u8 reserved0C[4];
    f32 angle;
    u8 disabled, mode, reserved16[2];
} RegionSource151A5660;
typedef struct {
    RegionSource151A5660 *source;
    f32 rate, scale, accumulator, value10;
    f32 horizontalBase, horizontalRange, verticalBase, verticalRange;
    s16 lifetimeBase, lifetimeRange;
    f32 value28, range2C, value30, range34, value38, range3C;
    u8 queryHeight, byteBase, byteRange, reserved43;
    u8 reserved44[4];
    RegionHeight151A5660 heightResult;
    s16 *viewMask;
} RegionState151A5660;
typedef struct {
    RegionPosition151A5660 position;
    f32 value0C, value10, value14, value18, value1C;
    u16 field20, field22;
    s16 lifetime;
    u8 field26, field27, field28, field29;
    s16 field2A;
    u8 value2C, field2D, field2E, field2F;
    u32 field30;
    u8 field34, reserved35[3];
    f32 value38, value3C, value40, value44;
} RegionPacket151A5660;
extern f32 D_800BE9A4, D_800A8D80, D_800A8D84, D_800A8D88;
extern f32 D_800A8D8C, D_800A8D90, D_800A8D94;
u8 func_151464B8(s16 *);
s32 func_150ADA20(void);
f32 func_150ADA68(void);
f32 func_151423D8(u8);
s32 func_15046C80(RegionPosition151A5660 *, u16, f32, RegionHeight151A5660 *);
void *func_15149550(RegionPacket151A5660 *, u8, u8, s32, u8, s32);

/* Sample a region and emit repeatedly while its accumulator exceeds one. */
void func_151A5660(u8 *owner) {
    u8 heightAccepted;
    RegionPacket151A5660 packet;
    RegionState151A5660 *state = (RegionState151A5660 *)(owner + 0x28);
    f32 lower, upper, cosine2, sine2, firstOffset2, secondOffset;
    f32 cosine0, sine0, radius0, cosine1, sine1, radius1;
    f32 horizontal, vertical;
    u8 angle;
    s32 mode;
    RegionPosition151A5660 query;

    if (state->source == NULL) {
        *(s16 *)(owner + 0xE) = -1;
        return;
    }
    if (state->source->disabled == 1) return;
    if (state->viewMask != NULL && func_151464B8(state->viewMask)) return;
    state->accumulator += (state->scale * state->rate) * D_800BE9A4;
    if (1.0f < state->accumulator) {
        packet.field20 = 0x6231;
        packet.field22 = 0x1A4D;
        packet.field26 = 0;
        packet.field27 = 0;
        packet.field28 = 0;
        packet.field29 = 255;
        packet.field2A = 1;
        packet.field2D = 255;
        packet.field30 = 0;
        packet.field2E = 0;
        packet.field2F = 0;
        packet.field34 = 16;
        packet.value3C = state->value10;
        do {
            mode = state->source->mode & 3;
            switch (mode) {
            case 2:
                angle = (u8)(u32)(state->source->angle * D_800A8D80);
                cosine2 = func_151423D8((u8)(angle - 64));
                sine2 = func_151423D8((u8)angle);
                firstOffset2 = func_150ADA68();
                firstOffset2 = firstOffset2 * ((f32)state->source->radius + (f32)state->source->radius) + (f32)-state->source->radius;
                secondOffset = func_150ADA68();
                secondOffset = secondOffset * ((f32)state->source->secondRadius + (f32)state->source->secondRadius) + (f32)-state->source->secondRadius;
                packet.position.x = (f32)state->source->x + (firstOffset2 * sine2 + secondOffset * cosine2);
                packet.position.z = (f32)state->source->z + (secondOffset * sine2 - firstOffset2 * cosine2);
                upper = (f32)(state->source->y + state->source->height);
                lower = (f32)(state->source->y - state->source->height);
                mode = state->queryHeight;
                goto sampledQuery;
            case 0:
                angle = (u32)func_150ADA20();
                cosine0 = func_151423D8((u8)(angle - 64));
                sine0 = func_151423D8((u8)angle);
                radius0 = func_150ADA68() * (f32)state->source->radius;
                packet.position.x = (f32)state->source->x + radius0 * sine0;
                packet.position.z = (f32)state->source->z - radius0 * cosine0;
                lower = (f32)state->source->y;
                upper = (f32)(state->source->y + state->source->height);
                mode = state->queryHeight;
                goto sampledQuery;
            case 1:
                angle = (u32)func_150ADA20();
                cosine1 = func_151423D8((u8)(angle - 64));
                sine1 = func_151423D8((u8)angle);
                radius1 = func_150ADA68() * (f32)state->source->radius;
                packet.position.x = (f32)state->source->x + radius1 * sine1;
                packet.position.z = (f32)state->source->z - radius1 * cosine1;
                upper = (f32)(state->source->y + state->source->height);
                lower = (f32)(state->source->y - state->source->height);
                break;
            default:
                packet.position.x = (f32)state->source->x;
                packet.position.z = (f32)state->source->z;
                lower = (f32)(state->source->y - state->source->height);
                upper = (f32)(state->source->y + state->source->height);
                break;
            }
            mode = state->queryHeight;
        sampledQuery:
            if (mode) {
                query.x = packet.position.x;
                query.y = upper;
                query.z = packet.position.z;
                heightAccepted = func_15046C80(&query, 0, lower, &state->heightResult);
                if (heightAccepted) {
                    packet.position.y = state->heightResult.height;
                } else {
                    packet.position.y = lower;
                }
            } else {
                packet.position.y = lower;
            }
            horizontal = func_150ADA68() * state->horizontalRange + state->horizontalBase;
            vertical = func_150ADA68() * state->verticalRange + state->verticalBase;
            packet.value0C = D_800A8D84 * horizontal;
            packet.value14 = D_800A8D88 * horizontal;
            packet.value10 = D_800A8D8C * vertical;
            packet.value18 = D_800A8D90 * vertical;
            packet.value1C = D_800A8D94 * vertical;
            /* The completed selector now holds the full random word. */
            mode = func_150ADA20();
            packet.lifetime = (u32)mode % (state->lifetimeRange + 1) + state->lifetimeBase;
            packet.value38 = func_150ADA68() * state->range2C + state->value28;
            packet.value40 = func_150ADA68() * state->range34 + state->value30;
            packet.value44 = func_150ADA68() * state->range3C + state->value38;
            mode = func_150ADA20();
            packet.value2C = (u32)mode % (state->byteRange + 1) + state->byteBase;
            func_15149550(&packet, 10, 0, 0, owner[0xC], owner[1]);
            state->accumulator -= 1.0f;
        } while (1.0f < state->accumulator);
    }
}


void func_151A5CAC(u8 *arg0) {
    if (*(volatile u16 *) (arg0 + 0x6C) != 0) {
        func_151A5D2C(*(volatile u16 *) (arg0 + 0x6C));
    }
    func_1514933C(arg0);
}

void func_151A5CEC(u8 *arg0) {
    if (*(volatile u16 *) (arg0 + 0x6C) != 0) {
        func_151A5D2C(*(volatile u16 *) (arg0 + 0x6C));
    }
    func_15149368(arg0);
}

void func_151A5D2C(arg0)
u16 arg0;
{
    func_100111C8(arg0);
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1D2B10/func_151A5D58.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1D2B10/func_151A5F70.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1D2B10/func_151A6068.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1D2B10/func_151A6350.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1D2B10/func_151A6600.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1D2B10/func_151A6AB8.s")

s32 func_151A6B10(s32 arg0) {
    func_151A6AB8(arg0);
    func_1513CA6C(arg0);
}

s32 func_151A6B3C(s32 arg0) {
    func_151A6AB8(arg0);
    func_1513CAA0(arg0);
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1D2B10/func_151A6B68.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1D2B10/func_151A6BD8.s")

typedef struct { f32 x, y, z; } BurstPosition1A6C90;
typedef struct {
    s16 count;
    u8 pad2[2];
    BurstPosition1A6C90 position;
    s16 duration;
    u8 pad12[2];
    f32 radius;
    s16 angle0, range0, angle1, range1;
    f32 speed, speedRange;
    f32 unk28, unk2C;
    f32 direction[3];
    f32 scale, scaleRange;
    f32 unk44, unk48, unk4C, unk50;
    u8 unk54, unk55;
    s16 unk56, unk58;
    u8 pad5A[2];
} ActorBurstPacket1A6C90;

extern f32 D_800A8DB0;
void func_151A6F00(ActorBurstPacket1A6C90 *, u8, u8, s32);
void func_151D5334(BurstPosition1A6C90 *, f32, f32, f32, s32, s32, s32);
void func_151D3FF4(BurstPosition1A6C90 *, u8, s32);
void func_151D5514(BurstPosition1A6C90 *, u8, s32);
void *func_151541B8(BurstPosition1A6C90 *, f32, f32, f32, f32, u8, s32);
void func_151D5404(BurstPosition1A6C90 *, f32, f32, f32, s32, s32, s32, s32);

/* Snapshot the actor position and submit the complete burst effect sequence. */
void func_151A6C90(u8 *actor, u8 slot, s32 context) {
    BurstPosition1A6C90 position;
    ActorBurstPacket1A6C90 packet;
    u32 random;
    f32 sample;

    /* Retail snapshots these coordinates before its later null branch. */
    position.x = *(f32 *)(actor + 0x14);
    position.y = *(f32 *)(actor + 0x18);
    position.z = *(f32 *)(actor + 0x1C);
    if (actor != NULL) {
        packet.count = ((u32)func_150ADA20() & 3) + 6;
        packet.position = position;
        packet.duration = 80;
        packet.radius = 60.0f;
        packet.angle0 = 0;
        packet.range0 = 255;
        packet.angle1 = -63;
        packet.range1 = 80;
        packet.speed = 0;
        packet.speedRange = 35.0f;
        packet.unk28 = 10.0f;
        packet.unk2C = 40.0f;
        packet.direction[0] = 0.0f;
        packet.direction[1] = 0.0f;
        packet.direction[2] = 0.0f;
        packet.scale = D_800A8DB0;
        packet.scaleRange = 0.5f;
        packet.unk44 = -1.0f;
        packet.unk48 = -1.0f;
        packet.unk4C = -2.0f;
        packet.unk50 = 4.0f;
        packet.unk54 = 0;
        packet.unk55 = 0;
        packet.unk56 = 50;
        packet.unk58 = 25;
        func_151A6F00(&packet, 0, slot, context);
        func_151D5334(&position, 506.0f, 1013.0f, 0.000987166888f, 5, slot, context);
        func_151D3FF4(&position, slot, context);
        func_151D5514(&position, slot, context);
        sample = func_150ADA68();
        random = func_150ADA20();
        func_151541B8(&position, sample * 4.0f + 12.0f, 1.64099991f,
            (f32)(random % 56 + 200), 0.0f, slot, context);
        func_151D5404(&position, 1502.0f, 3000.0f, 0.00033333333f, 12, 15, 255, 0);
    }
}

