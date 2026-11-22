#include <ultra64.h>
#include "structs.h"
struct260 *func_15149130(s16, s8, s8, s8, u8, u8, u32, u8, s32);
void *memcpy(void *, const void *, u32);
typedef struct {
    u8 *owner;
    u8 identity, first, second, third, fourth, fifth;
} AttachedEffectPayload1199D0;

void func_1502EA98(u8 *arg0, u8 arg1, u8 arg2, u8 arg3, u8 arg4,
                   s32 arg5, u8 arg6);

/* Recovered routines from asm/1199D0.s; the build preserves retail layout. */

typedef struct { void *source; f32 rate; s16 *gate; f32 accumulator; } ParticleEmitter1199D0;
typedef struct { struct260 header; u8 reserved24[4]; ParticleEmitter1199D0 emitter; } ParticleEmitterRecord1199D0;
typedef struct { f32 x,y,z,parameter; } ParticlePacket1199D0;
typedef struct { f32 top; ParticlePacket1199D0 packet; } ParticleScratch1199D0;
extern f32 D_800A1570,D_800A1574,D_800BE9A4;
u8 func_151464B8(s16 *);
f32 func_150ADA68(void);
u32 func_150ADA20(void);
void func_151432BC(void *,f32 *,f32 *,f32 *,f32 *);

/* Accumulate an emission rate and publish sampled particle packets. */
void func_150EC520(struct260 *record) {
    ParticleEmitter1199D0 *emitter;
    ParticleScratch1199D0 scratch;
    u8 *effect;
    f32 randomValue;
    u32 lifetime;
    if (func_151464B8(((ParticleEmitterRecord1199D0 *)record)->emitter.gate) == 0) {
        emitter=&((ParticleEmitterRecord1199D0 *)record)->emitter;
        randomValue=func_150ADA68();
        emitter->accumulator += (D_800A1570+randomValue*D_800A1574)*emitter->rate*D_800BE9A4;
        if (emitter->accumulator > 1.0f) {
            scratch.packet.parameter=0.0f;
            do {
                func_151432BC(emitter->source,&scratch.packet.x,&scratch.packet.z,&scratch.top,&scratch.packet.y);
                lifetime=func_150ADA20();
                effect=(u8 *)func_15149130((s16)(lifetime%131U+80),-1,90,-1,1,0,sizeof(scratch.packet),((u8 *)record)[0xC],((u8 *)record)[1]);
                if (effect != NULL) memcpy(effect+0x28,&scratch.packet,sizeof(scratch.packet));
                emitter->accumulator -= 1.0f;
            } while (emitter->accumulator > 1.0f);
        }
    }
}


typedef struct { f32 x, y, z; } RandomParticlePoint1199D0;

typedef struct {
    u32 flags00, zero04;
    s16 code08, lifetime;
    u32 zero0C, zero10;
    u8 rgba14[4], rgba18[4];
    u8 value1C, paletteIndex;
    s16 value1E, value20, value22;
    f32 scale, extentX, extentY;
    RandomParticlePoint1199D0 position, velocity, acceleration;
    f32 parameter;
    u32 flags58, reserved5C;
    u8 value60, value61, value62;
    s8 value63, value64, value65;
    u8 reserved66[2];
    s16 reserved68;
    u8 reserved6A[2];
    f32 reserved6C;
} RandomParticleDefinition1199D0;

typedef struct {
    u8 first, second, width, height;
    f32 offsetX, offsetY, depth;
} RandomParticleExtra1199D0;

typedef struct {
    RandomParticlePoint1199D0 position;
    f32 accumulator;
} RandomParticleEmitter1199D0;

typedef struct {
    struct260 header;
    u8 reserved24[4];
    RandomParticleEmitter1199D0 emitter;
} RandomParticleRecord1199D0;

void *func_15130280(RandomParticleDefinition1199D0 *, u8, void *, s32, u8, s32);

/* Accumulate randomized particles and attach the extra packet after allocation. */
void func_150EC6B0(struct260 *record) {
    f32 randomValue;
    RandomParticleDefinition1199D0 definition;
    RandomParticleExtra1199D0 extra;
    register RandomParticleEmitter1199D0 *emitter;
    u8 *effect;
    u32 firstFlag;

    emitter = (RandomParticleEmitter1199D0 *)((u8 *)record + 0x28);
    randomValue = func_150ADA68();
    emitter->accumulator += (1352.0f + randomValue * 1698.0f) * 0.0001f * D_800BE9A4;
    if (emitter->accumulator > 1.0f) {
        extra.first = 0;
        extra.second = 0;
        extra.depth = 0.9704700112f;
        definition.paletteIndex = 0x6C;
        definition.code08 = 0x5103;
        definition.flags00 = 0x200005;
        definition.value1E = 70;
        definition.value20 = 3;
        definition.flags58 = 0x80DE07;
        definition.value60 = 8;
        definition.value61 = 6;
        definition.zero04 = 0;
        definition.zero0C = 0;
        definition.zero10 = 0;
        definition.value62 = 22;
        definition.value63 = -1;
        definition.value64 = -1;
        definition.value65 = 0;
        definition.value22 = 70;
        definition.rgba14[0] = 71;
        definition.rgba14[1] = 194;
        definition.rgba14[2] = 0;
        definition.rgba14[3] = 255;
        definition.rgba18[0] = 192;
        definition.rgba18[1] = 73;
        definition.rgba18[2] = 0;
        definition.value1C = 255;
        definition.scale = 1.021028996f;
        definition.position = emitter->position;
        definition.velocity.x = 0.0f;
        definition.velocity.y = 0.0f;
        definition.velocity.z = 0.0f;
        definition.acceleration.x = 0.0f;
        definition.acceleration.y = 0.0f;
        definition.acceleration.z = 0.0f;
        do {
            extra.width = func_150ADA20() % 5U + 4;
            extra.height = func_150ADA20() % 5U + 4;
            extra.offsetX = func_150ADA68() * 11.0f;
            extra.offsetY = func_150ADA68() * 11.0f;
            definition.parameter = func_150ADA68() * 0.1720000058f + 0.09800000489f;
            definition.flags58 &= ~0xC0U;
            firstFlag = (func_150ADA20() & 1U) ? 0x80 : 0;
            definition.flags58 = (((func_150ADA20() & 1U) ? 0x40 : 0) | firstFlag) | definition.flags58;
            definition.rgba18[3] = func_150ADA20() % 101U + 100;
            definition.lifetime = func_150ADA20() % 51U + 80;
            randomValue = func_150ADA68() * 80.0f + 92.0f;
            definition.extentY = randomValue;
            definition.extentX = randomValue;
            effect = func_15130280(&definition, 0, 0, sizeof(extra), ((u8 *)record)[0xC], ((u8 *)record)[1]);
            if (effect != 0) {
                memcpy(effect + 0xA8, &extra, sizeof(extra));
            }
            emitter->accumulator -= 1.0f;
        } while (emitter->accumulator > 1.0f);
    }
}

/* Capture the owner and effect settings; publish them only after allocation. */
void func_150ECA68(u8 *owner, u8 first, u8 second, u8 third, u8 fourth,
                   u8 fifth, s16 duration, u8 selector, s32 category) {
    AttachedEffectPayload1199D0 payload;
    u8 *effect;
    payload.owner = owner;
    payload.identity = owner[0x3B];
    payload.first = first;
    payload.second = second;
    payload.third = third;
    payload.fourth = fourth;
    payload.fifth = fifth;
    effect = (u8 *)func_15149130(duration == -1 ? 300 : duration, -1, 0x5D, -1,
                                duration == -1 ? 0 : 1, 0x45,
                                sizeof(payload), selector, category);
    if (effect != NULL) {
        memcpy(effect + 0x28, &payload, sizeof(payload));
    }
}

void func_150ECB4C(u8 *arg0, s32 arg1, u8 arg2) {
    func_15169850(arg1, arg2, (s32) (arg0 + 0x28), (s32) (arg0 + 0x2C), (s32) arg0);
}

void func_150ECB8C(u8 *arg0) {
    u8 *sub = arg0 + 0x28;
    u8 *target = *(u8 **) sub;

    if ((*(s32 *) target == 0) || (sub[4] != target[0x3B])) {
        *(s16 *) (arg0 + 0xE) = -1;
        return;
    }
    func_1502EA98(target, sub[5], sub[6], sub[7], sub[8], 0, sub[9]);
}

void func_150ECC00(u8 *arg0, volatile u8 arg1, s32 arg2) {
    func_151C9AC0(arg0, arg1, arg2);
    func_150ECA68(arg0, 0, 0xFF, 0, 0xFF, 4, -1, arg1, arg2);
}

extern f32 D_80088AD0, D_80088AD4, D_80088AD8;
extern f32 D_80088ADC, D_80088AE0, D_80088AE4;
extern f32 D_80088AE8, D_80088AEC, D_80088AF0;
s32 func_1509BE40(s32, ...);
void func_1509BFB0(s32, s32, s32, ...);
void func_150495B0(f32 *, f32, f32 *, f32, f32, f32);

/* Select script-driven view color and range, then smooth and publish RGB. */
void func_150ECC70(struct108 *view) {
    s32 value;
    s32 halfValue;
    s32 range;
    s32 selector;
    s32 radius;
    if (func_1509BE40(1, 0x403B, 6, 0x2000)) {
        func_1509BFB0(0, 0x4031, 1);
        func_1509BFB0(0, 0x4032, 1);
        func_1509BFB0(0, 0x4033, 1);
        view->unk84 |= 0x80021200;
        if (func_1509BE40(1, 0x4038, 6, 0x2000)) {
            D_80088ADC = 128.0f;
            D_80088AE0 = 255.0f;
            D_80088AE4 = 255.0f;
        } else if (func_1509BE40(1, 0x4039, 6, 0x2000)) {
            D_80088ADC = 255.0f;
            D_80088AE0 = 128.0f;
            D_80088AE4 = 255.0f;
        } else if (func_1509BE40(1, 0x403A, 6, 0x2000)) {
            D_80088ADC = 255.0f;
            D_80088AE0 = 255.0f;
            D_80088AE4 = 128.0f;
        } else {
            D_80088ADC = 255.0f;
            D_80088AE0 = 255.0f;
            D_80088AE4 = 255.0f;
        }
        selector = func_1509BE40(0, 0x2007, 0xB7) | 0x2000;
        if (func_1509BE40(1, 0x4010, 6, 0x2000) == 0) {
            view->unk134 = 0;
            view->unk190 = 0.0f;
            return;
        }
        if (selector != 0) {
            view->unk134 = 1;
            value = func_1509BE40(1, selector, 0x9C, 0x2000);
            func_1509BFB0(1, 0x9000, 0x17, value);
            value = func_1509BE40(1, selector, 0x9A, 0x2000);
            halfValue = value >> 1;
            range = value < 900 ? 900 : value >= 1191 ? 1190 : value;
            radius = halfValue < 180 ? 180 : halfValue >= 232 ? 231 : halfValue;
            func_1509BFB0(2, 0x9000, 8, range, radius);
            view->unk190 = 220.0f;
        } else {
            return;
        }
    } else {
        D_80088ADC = 255.0f;
        D_80088AE0 = 255.0f;
        D_80088AE4 = 255.0f;
        func_1509BFB0(0, 0x4031, 0);
        func_1509BFB0(0, 0x4032, 0);
        func_1509BFB0(0, 0x4033, 0);
        view->unk84 &= 0x7FFDEDFF;
        view->unk84 |= 8;
    }
    func_150495B0(&D_80088AD0, D_80088ADC, &D_80088AE8, 4.0f, 6.0f, view->unk7B4);
    func_150495B0(&D_80088AD4, D_80088AE0, &D_80088AEC, 4.0f, 6.0f, view->unk7B4);
    func_150495B0(&D_80088AD8, D_80088AE4, &D_80088AF0, 4.0f, 6.0f, view->unk7B4);
    func_1509BFB0(1, 0x30F3, 0x12, (u8)(u32)D_80088AD0);
    func_1509BFB0(1, 0x30F4, 0x12, (u8)(u32)D_80088AD4);
    func_1509BFB0(1, 0x30F5, 0x12, (u8)(u32)D_80088AD8);
}
