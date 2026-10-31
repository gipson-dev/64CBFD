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

s32 func_150DE32C() {
    return 0;
}

s32 func_150DE458() {
    return 0;
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
