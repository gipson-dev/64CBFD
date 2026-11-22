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

/* Non-matching placeholders for the text-only asm slice asm/1199D0.s. */

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


s32 func_150EC6B0() {
    return 0;
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

s32 func_150ECC70() {
    return 0;
}
