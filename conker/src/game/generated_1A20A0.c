#include <ultra64.h>

#include "structs.h"
typedef struct {
    u8 retained00[0x90];
    u8 slot, retained91;
    s16 flags;
    void *model;
    f32 position[3];
    s16 lifetime, mode;
    f32 tilt, heading, fieldB0, fieldB4, angularRate, fieldBC, scale;
    u32 retainedC4;
    f32 groundHeight;
    u8 retainedCC[0x1C];
    u32 surfaceFlags;
    u8 surfaceKind, variant;
    u16 sound;
    u8 stateF0, stateF1, retainedF2[6];
} Particle15174BF0;
typedef struct { void *model; u32 retained04[4]; } Model15174BF0;
extern u8 *D_800DBFF0;
extern u8 *D_800DBE3C;
extern u32 *D_800DBE5C;
extern Model15174BF0 D_800DDE88[];
extern u8 D_800A7170[];
extern f32 D_800A7174;
f32 func_15048FC8(struct17 *relative);
void *func_15167A68(s32, s32, s32, s32, u8, u8);
u32 func_150ADA20(void);
u16 func_10010E78(s32, s32, s32, s32, s32, s32, s32, s32, s32, s32, s32); /* Full call-site words; narrowing occurs in the callee. */
s32 func_1510F8D8(s32, s32, s32, u8 **);

typedef struct {
    u8 retained00[0x90];
    u8 slot, state91;
    s16 flags;
    void *model;
    f32 position[3];
    s16 lifetime, mode;
    f32 tilt, heading, fieldB0, fieldB4, fieldB8, fieldBC, scale;
    u32 retainedC4;
    f32 groundHeight, fieldCC;
    s16 fieldD0, retainedD2, fieldD4, fieldD6;
    u32 retainedD8;
    s16 fieldDC;
    u16 retainedDE;
    f32 fieldE0, fieldE4;
    u32 surfaceFlags;
    u8 surfaceKind, variant;
    u16 retainedEE;
    u8 stateF0, stateF1, retainedF2[6];
} Particle15174FA4;
typedef struct { s32 fixedHeight; u32 retained04[3]; } Height15174FA4;
extern Height15174FA4 D_800D3300[];
extern void *D_800DDF14;
void func_1510F800(s32 context);
s32 func_150A3A70(s32 x, s32 z);
void func_1516979C(struct102 *record);

/* Recovered routine and remaining placeholders for asm/1A20A0.s. */

/* Create jittered particles with one initial sound and optional ground classification. */
void func_15174BF0(s32 count, s32 slot, s32 x, s32 y, s32 z, s32 view,
                   f32 baseScale, f32 scaleRange, s32 flags) {
    struct17 relative;
    u8 *surface; /* An early query failure leaves the retail stack word untouched. */
    f32 rateScale;
    s32 heading;
    s32 spawnX;
    s32 spawnZ;
    s32 turn;
    s32 angle;
    s32 i;
    s32 grounded;
    u32 material;
    s32 variant;
    Particle15174BF0 *particle;

    relative.unk0 = (f32)x - *(f32 *)(D_800DBFF0 + (u32)view * 0x9A0 + 0x2F8);
    relative.unk4 = (f32)y - *(f32 *)(D_800DBFF0 + (u32)view * 0x9A0 + 0x2FC);
    relative.unk8 = (f32)z - *(f32 *)(D_800DBFF0 + (u32)view * 0x9A0 + 0x300);
    heading = (s32)func_15048FC8(&relative);
    i = 0;
    if (count > 0) {
        rateScale = D_800A7174;
again:
        particle = func_15167A68(10, 0, 0xF8, 1, 0xFF, 1);
        if (particle != NULL) {
            grounded = flags & 1;
            spawnX = (u32)x + (func_150ADA20() & 0x7F) - 0x3F;
            spawnZ = (u32)z + (func_150ADA20() & 0x7F) - 0x3F;
            particle->flags = 3;
            particle->position[1] = (f32)y;
            particle->position[0] = (f32)spawnX;
            particle->slot = slot;
            particle->position[2] = (f32)spawnZ;
            particle->lifetime = (func_150ADA20() % 15U) + 10;
            particle->mode = 1;
            turn = (u32)heading + (func_150ADA20() & 0x1F) - 15;
            angle = turn;
            if (turn < 0) {
                angle = turn + 360;
            } else if (turn >= 360) {
                angle = turn - 360;
            }
            particle->tilt = (f32)((s32)(func_150ADA20() & 0x1F) - 15);
            particle->fieldB0 = 0.0f;
            particle->fieldB4 = -1.0f;
            particle->heading = (f32)angle;
            particle->angularRate = (f32)((s32)(func_150ADA20() & 0xFF) - 128) * rateScale;
            particle->fieldBC = 0.0f;
            particle->scale = ((f32)(s32)(func_150ADA20() & 0xFFFF) * 0.000030517578125f * scaleRange) + baseScale;
            variant = func_150ADA20() & 1;
            particle->variant = variant;
            particle->model = D_800DDE88[variant].model;
            if (i == 0) {
                particle->sound = func_10010E78(0, 0xA2, 0x7D00, 0, 0, 0, spawnX, y, spawnZ, 1000, 4000);
            } else {
                particle->sound = 0;
            }
            particle->surfaceFlags = 0;
            if (grounded) {
                particle->flags |= 0x80;
                particle->groundHeight = (f32)func_1510F8D8(spawnX, y, spawnZ, &surface);
                material = 0;
                if (surface != NULL) {
                    material = D_800DBE5C[(s32)((u32)surface - (u32)D_800DBE3C) / 12];
                }
                particle->surfaceFlags = material;
                particle->surfaceKind = D_800A7170[(material >> 5) & 3];
            } else {
                particle->surfaceKind = 0;
            }
            particle->stateF0 = 0;
            particle->stateF1 = 0;
            i++;
            if (i != count) {
                goto again;
            }
        }
    }
}

/* Create type-19 particles using the lowest returned fixed-point height. */
void func_15174FA4(s32 count, s32 slot, s32 x, s32 y, s32 z, s32 width,
                   s32 unusedView, s32 elevated, f32 baseScale, f32 scaleRange) {
    s32 centerX = x;
    s32 centerY = y;
    s32 i;
    s32 spawnX;
    s32 spawnZ;
    s32 halfWidth;
    s32 hits;
    s32 lowest;
    s32 j;
    Particle15174FA4 *particle;

    if (elevated == 0) {
        func_1510F800(0);
    }
    i = 0;
    if (count > 0) {
        do {
            particle = func_15167A68(19, 0, 0xF8, 1, 0xFF, 1);
            if (particle == NULL) {
                break;
            }
            halfWidth = width >> 1;
            spawnX = (u32)centerX + func_150ADA20() % (u32)width - halfWidth;
            spawnZ = (u32)z + func_150ADA20() % (u32)width - halfWidth;
            particle->slot = slot;
            particle->position[0] = (f32)spawnX;
            particle->position[1] = (f32)centerY;
            particle->position[2] = (f32)spawnZ;
            particle->lifetime = func_150ADA20() % 3U + 4;
            particle->mode = 0;
            particle->tilt = (f32)((s32)(func_150ADA20() & 31) - 15);
            particle->heading = (f32)(func_150ADA20() % 360U);
            particle->fieldB0 = (f32)((s32)(func_150ADA20() & 31) - 15);
            particle->fieldB4 = 0.0f;
            particle->fieldBC = 0.0f;
            particle->fieldB8 = 3.0f;
            particle->scale = ((f32)(s32)(func_150ADA20() & 65535) * 0.000030517578125f * scaleRange) + baseScale;
            particle->model = D_800DDF14;
            particle->variant = 7;
            hits = func_150A3A70(spawnX, spawnZ);
            if (hits == 0) {
                func_1516979C((struct102 *)particle);
            } else {
                lowest = D_800D3300[0].fixedHeight;
                for (j = 1; j < hits; j++) {
                    if (D_800D3300[j].fixedHeight < lowest) {
                        lowest = D_800D3300[j].fixedHeight;
                    }
                }
                lowest >>= 8;
                particle->groundHeight = (f32)lowest;
                if (elevated == 0) {
                    particle->state91 = 0;
                    particle->position[1] = (f32)(lowest + 10);
                    particle->flags = 1;
                } else {
                    particle->state91 = 2;
                    particle->flags = 4;
                    particle->fieldE4 = (f32)(s32)((func_150ADA20() & 127) + (u32)lowest + 300);
                    particle->position[1] = (f32)(s32)((func_150ADA20() & 127) + (u32)lowest + 300);
                }
                particle->fieldCC = 0;
                particle->fieldD0 = centerX;
                particle->fieldD4 = z;
                particle->fieldD6 = halfWidth;
                particle->fieldE0 = 0;
                particle->fieldDC = 0;
                particle->surfaceFlags = 0;
                particle->surfaceKind = 0;
                particle->stateF0 = 0;
                particle->stateF1 = 0;
            }
            i++;
        } while (i != count);
    }
}

s32 func_15175390() {
    return 0;
}

s32 func_15175958() {
    return 0;
}

s32 func_1517685C() {
    return 0;
}

s32 func_15176B84() {
    return 0;
}

s32 func_15176DF0() {
    return 0;
}

s32 func_151770C8() {
    return 0;
}

s32 func_1517725C() {
    return 0;
}
