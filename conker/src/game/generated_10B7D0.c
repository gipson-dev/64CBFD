#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/10B7D0.s. */

extern u8 D_800A0D0B[];
extern u8 D_800A0D2B[];
extern s32 D_80082FA0;
extern f32 D_800BE9A4;

typedef struct {
    u8 pad0[0x388];
    f32 threshold;
    u8 pad38C[0x614];
} Generated10B7D0PlayerRecord;

typedef struct {
    u8 pad0[0x34];
    f32 x;
    f32 y;
    f32 z;
    u8 pad40[0xD0];
    f32 velocityX;
    f32 velocityY;
    f32 velocityZ;
    f32 verticalSpeed;
} Generated10B7D0MotionRecord;

extern Generated10B7D0PlayerRecord *D_800DBFF0;

s32 func_150DEC28();
s32 func_15140410();

void func_150DE320(s32 arg0) {
}

/* Two words preserve the complete eight-byte tables before any helper call. */
typedef struct { u32 words[2]; } RouteBytes10B7D0;
extern RouteBytes10B7D0 D_80088950,D_80088958;
typedef struct {
    s16 origin0;
    s16 origin1;
    s16 origin2;
    s16 radius;
    s16 heightOffset;
    u8 padA[6];
    f32 parameter10;
    u8 disabled;
    u8 flags;
    u8 pad16;
    u8 field17;
    s32 field18;
    s32 field1C;
    u32 field20;
    f32 coefficient0;
    f32 scale;
    f32 coefficient1;
    f32 coefficient2;
} GeneratedCDE80Record;

extern GeneratedCDE80Record *D_800D3098;
s32 func_150A32B4(s32, s32, s32, s32);
u8 *func_151149AC(u8);
void func_150A2864(u32, s32);
/* Query eight snapshotted record IDs and update their actor/resource status. */
void func_150DE32C(s32 x, s32 y, s32 z) {
    RouteBytes10B7D0 indices;
    RouteBytes10B7D0 tags;
    s32 i;
    u8 *entry;
    u8 *object;
    indices = D_80088950;
    tags = D_80088958;
    for (i = 0, entry = (u8 *)&indices; i < 8; i++, entry++) {
        if (func_150A32B4((s32)&D_800D3098[*entry], x, y, z)) {
            if (((u8 *)&tags)[i]) {
                object = func_151149AC(((u8 *)&tags)[i]);
                object[0x73] = (object[0x73] & ~3) | 3;
            } else {
                func_150A2864(*entry, 1);
            }
        }
    }
}



extern s32 D_800BE9E4;
extern s32 D_80090204[];
u32 func_1510D0EC(s32, s32 *, s32, s32);
void func_1510D874(s32, s32, s32, s32, s32);
#ifdef __GNUC__
#define ACTOR_ANGLE_ALIAS __attribute__((__may_alias__))
#else
#define ACTOR_ANGLE_ALIAS
#endif
typedef struct ACTOR_ANGLE_ALIAS {
    f32 angleX,angleY,angleZ;
    u8 reserved0C[4];
    s16 positionX,positionY,positionZ;
    u8 reserved16[0x26];
    s32 verticalAcceleration;
    u8 reserved40[0x14];
    u16 type;
    u8 reserved56[4];
    s16 velocityX,velocityY,velocityZ;
    f32 angularVelocityX,angularVelocityY,angularVelocityZ;
    u8 reserved6C[2];
    u8 remove;
    u8 reserved6F[4];
    u8 flags;
    u8 reserved74[8];
    s32 variant;
    u8 reserved80[10];
    u8 lifetime;
    u8 reserved8B[0x15];
} ActorAngleState10B7D0;

/* Integrate actor spin, position and lifetime; queue its resource pair. */
void func_150DE458(void *object) {
    ActorAngleState10B7D0 *actor = object;
    const f32 upper = 360.0f;
    const f32 lower = 0.0f;
    f32 delta;
    s32 extent;
    s32 first;
    s32 last;
    s32 remaining;
    s32 *resource;
    u32 address;
    if ((actor->flags & 3) == 3) {
        delta = D_800BE9E4;
        actor->angleX += actor->angularVelocityX * delta;
        if (actor->angleX < lower) actor->angleX += upper;
        else if (actor->angleX >= upper) actor->angleX -= upper;
        actor->angleY += actor->angularVelocityY * delta;
        if (actor->angleY < lower) actor->angleY += upper;
        else if (actor->angleY >= upper) actor->angleY -= upper;
        actor->angleZ += actor->angularVelocityZ * delta;
        if (actor->angleZ < lower) actor->angleZ += upper;
        else if (actor->angleZ >= upper) actor->angleZ -= upper;
        remaining = actor->lifetime;
        actor->velocityY -= (u32)actor->verticalAcceleration * (u32)D_800BE9E4;
        actor->positionX += (u32)actor->velocityX * (u32)D_800BE9E4;
        actor->positionY += (u32)actor->velocityY * (u32)D_800BE9E4;
        actor->positionZ += (u32)actor->velocityZ * (u32)D_800BE9E4;
        remaining = (u32)remaining - (u32)D_800BE9E4;
        if (remaining > 0) actor->lifetime = remaining;
        else actor->remove = 1;
    }
    if ((actor->type & ~0x8000) == 12) {
        resource = &D_80090204[actor->variant * 2];
        first = 4;
        for (last = 5; last != 9; last += 2, resource++, first += 2) {
            address = func_1510D0EC(*resource, &extent, 3, 0);
            func_1510D874((s32)actor, address, address + (u32)extent - 0x200u, first, last);
        }
    }
}


typedef struct {
    f32 x,y,z;
    u8 reserved0C[6];
    s16 pitch;
    u8 reserved14[0x68];
    u32 phaseX,phaseY,phaseZ;
} ActorPhaseMotion;
extern f32 D_800A0D48,D_800A0D4C,D_800A0D50,D_800A0D54;
extern s32 D_800BE9E4;
f32 func_15048A40(u8 angle);
/* Update the actor's oscillating pitch/position and advance three phase counters. */
void func_150DE6D8(ActorPhaseMotion *actor) {
    actor->pitch = func_15048A40((u8)((s32)actor->phaseX >> 3)) * D_800A0D48 + D_800A0D4C;
    actor->x = func_15048A40((u8)((s32)actor->phaseY >> 3)) * D_800A0D50;
    actor->z = func_15048A40((u8)((s32)actor->phaseZ >> 3)) * D_800A0D54;
    actor->phaseX += (u32)D_800BE9E4 * 12;
    actor->phaseY += (u32)D_800BE9E4 * 16;
    actor->phaseZ += (u32)D_800BE9E4 * 24;
}

s32 func_150DE7C0() {
    return 0;
}

// Matches retail directly from the explicit timestep pointer.
s32 func_150DEACC(Generated10B7D0MotionRecord *arg0) {
    f32 *timestep = &D_800BE9A4;

    arg0->x += arg0->velocityX * *timestep;
    arg0->y += arg0->velocityY * *timestep;
    arg0->z += arg0->velocityZ * *timestep;
    arg0->verticalSpeed -= *timestep;
    if (arg0->verticalSpeed < 0.0f) {
        return 0;
    }
    return 1;
}

/* Note 529: current-player threshold gate and embedded-record dispatch. */
s32 func_150DEB58(u8 *arg0, s16 arg1) {
    if (D_800DBFF0[D_80082FA0].threshold < 5.0f) {
        return 0;
    }
    return func_15140410(arg0, arg0 + 0x120, arg0 + 0x12C, arg1);
}

void func_150DEBE0(s32 arg0) {
    s32 i = 0;

    do {
        func_150DEC28(i & 0xFF, 1);
        i += 1;
        i = i & 0xFF;
    } while (i < 4);
}

s32 func_150DEC28(arg0, arg1)
u8 arg0;
u8 arg1;
{
    s32 offset = arg0 * 4;

    func_151616D0(D_800A0D0B[offset], 0x22, 0);
    func_151417C4(D_800A0D2B[offset], 0x22);
}
