#include <ultra64.h>
extern f32 D_800A0894;
f32 func_150ADA68();

/* Non-matching placeholders for the text-only asm slice asm/FDD70.s. */

s32 func_150D08C0() {
    return 0;
}

#include "structs.h"
extern s32 D_80088890,D_80088894,D_80088898,D_8008889C,D_800BE9E4;
extern struct127 D_800CC2D0[];
extern struct131 *D_800DBEF4;
extern u32 *D_800DBF94;
u8 *func_151149AC(u8);
void func_151951E0(u8 *);
s32 func_10010154(u16,void *,u16,s16,u16);
s32 func_15136C3C(void *,s32,s32,s32,s32,s32,s32,s32);
void func_15145A50(struct127 *);
s32 func_1507CD64(struct127 *,s32);

/* Advance stage counters and dispatch four record events for the first actor. */
void func_150D0E90(s32 unused) {
    struct127 *actor = D_800CC2D0;
    s32 i;
    s32 index;
    D_80088890 += D_800BE9E4 * 40;
    D_80088894 += D_800BE9E4 * -66;
    D_80088898 += D_800BE9E4 * -8;
    D_8008889C += D_800BE9E4 * 92;
    if (((u8 *)actor->unk31C)[0x120] == 0) {
        for (i = 0; i != 3; i++) {
            index = (struct131 *)func_151149AC((u8)(250 - i)) - D_800DBEF4;
            if (D_800DBF94[index] & 1) {
                func_151951E0((u8 *)actor);
                func_10010154(0x627,actor,0x7FFF,200,700);
            }
        }
        index = (struct131 *)func_151149AC(251) - D_800DBEF4;
        if (D_800DBF94[index] & 1) {
            func_10010154(0x627,actor,0x7FFF,200,700);
            func_15136C3C(actor,1,1,1,1,0,255,1);
            func_15145A50(actor);
            func_1507CD64(actor,6);
        }
    }
}

extern f32 D_800A0890;
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
} OwnerVariantDescriptorFDD70;

/* Construct an owner-attached effect with a variant-dependent signed offset. */
void *func_150D10E4(u8 *owner, u8 variant) {
    OwnerVariantDescriptorFDD70 packet;
    packet.owner_id = owner[0x3B];
    packet.owner = owner;
    packet.attachmentIndex = 0;
    packet.zero0 = 0.0f;
    packet.zero1 = 0.0f;
    packet.zero2 = 0.0f;
    packet.zero3 = 0.0f;
    packet.value1C = variant != 0 ? -30.0f : 30.0f;
    packet.value20 = 0.0f;
    packet.mode = 2;
    packet.activeFrames = 50;
    packet.restartDelay = 22;
    packet.lifetime = 2000;
    packet.value2C = 0;
    packet.startCallback = 6;
    packet.transformCallback = 7;
    packet.updateCallback = -1;
    packet.rate = D_800A0890;
    packet.flags = 0;
    packet.finishCallback = -1;
    return func_15134DAC((s32)&packet, 0);
}

s32 func_150D11B4(u8 *arg0) {
    *(f32 *) (arg0 + 0x74) = (func_150ADA68() * 150.0f + 350.0f) * D_800A0894;
    return 1;
}

u32 func_150ADA20(void);
extern f32 D_800A0898,D_800A089C,D_800A08A0,D_800A08A4;
void *func_151DB5D0(u8,const struct17 *,const struct17 *,f32,f32,f32,f32,s16,u8,s16,s16,u8,u8,s32);

/* Interpolate a particle origin and velocity, then submit randomized emission. */
void func_150D1204(f32 *first,f32 *second,f32 *firstStep,f32 *secondStep,f32 fraction,struct102 *emitter) {
    struct17 position;
    struct17 other;
    struct17 velocity;
    u32 secondBits,firstBits;
    f32 secondRandom,firstRandom;

    position.unk0 = firstStep[0] * fraction + first[0];
    position.unk4 = firstStep[1] * fraction + first[1];
    position.unk8 = firstStep[2] * fraction + first[2];
    other.unk0 = secondStep[0] * fraction + second[0];
    other.unk4 = secondStep[1] * fraction + second[1];
    other.unk8 = secondStep[2] * fraction + second[2];
    velocity.unk0 = (other.unk0 - position.unk0) * emitter->unk74;
    velocity.unk4 = (other.unk4 - position.unk4) * emitter->unk74;
    velocity.unk8 = (other.unk8 - position.unk8) * emitter->unk74;
    firstRandom = func_150ADA68();
    secondRandom = func_150ADA68();
    firstBits = func_150ADA20();
    secondBits = func_150ADA20();
    func_151DB5D0(0,&position,&velocity,firstRandom * 61.0f + 60.0f,
        D_800A0898,D_800A089C,secondRandom * D_800A08A0 + D_800A08A4,
        (firstBits & 15) + 35,(secondBits % 156U) + 100,30,8,0,
        ((u8 *)emitter)[0xC],((u8 *)emitter)[1]);
}
