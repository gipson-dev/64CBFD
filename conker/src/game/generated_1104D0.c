#include <ultra64.h>

s32 func_150AD9A0(s32, s32, s32);
s32 func_150E3020(s32, s32, s32, s32, s32, s32, s32, f32,
                 s32, f32, f32, f32, s32, s16);

#include "structs.h"
extern f32 D_800BE9A4;
extern f32 D_800A1054;

typedef struct {
    u8 type;
    u8 pad1[0xF];
    f32 x;
    f32 y;
    f32 z;
} Generated1104D0Actor;

extern Generated1104D0Actor *D_800D99D0[8];

void func_151C3B0C(void *, f32, f32, f32, f32, s32, s32, s32);

/* Non-matching placeholders for the text-only asm slice asm/1104D0.s. */

s32 func_150E3020(s32 arg0, s32 arg1, s32 arg2, s32 arg3, s32 arg4, s32 arg5,
                  s32 arg6, f32 arg7, s32 arg8, f32 arg9, f32 arg10,
                  f32 arg11, s32 arg12, s16 arg13) {
    return 0;
}

/* Create a distance-scaled effect and return its one-based slot handle. */
s32 func_150E3208(s32 x, s32 y, s32 z, s32 targetX, s32 targetY,
                  s32 targetZ, s32 kind, s32 duration) {
    u8 *effect;
    f32 step;

    step = (f32)func_150AD9A0((s32)((u32)x - (u32)targetX),
                            (s32)((u32)y - (u32)targetY),
                            (s32)((u32)z - (u32)targetZ)) / (f32)duration;
    effect = (u8 *)func_150E3020(x, y, z, targetX, targetY, targetZ,
                               kind, step, 0, 0.0f, 0.0f, 0.0f, 0, -99);
    if (effect != NULL) {
        return effect[0x48] + 1;
    }
    return 0;
}

s32 func_150E32D0(s32 arg0, s32 arg1, s32 arg2, s32 arg3, s32 arg4, f32 arg5) {
    s32 temp_v0;

    temp_v0 = func_150E3020(arg0, arg1, arg2, 0, 0, 0, arg4, arg5, arg3,
                            0.0f, 0.0f, 0.0f, 0, -99);
    if (temp_v0 != 0) {
        return *(u8 *) (temp_v0 + 0x48) + 1;
    }
    return 0;
}

void func_150E3340(f32 *arg0, s32 *arg1, s32 arg2, s16 arg3) {
    func_150E3020(arg1[0], arg1[1], arg1[2], arg1[0], arg1[1], arg1[2],
                  0x1A, 10.0f, 0, arg0[0], arg0[1], arg0[2], arg2, arg3);
}

s32 func_150E33CC(s32 arg0, s32 arg1, s32 *arg2, s32 arg3) {
    s32 temp_v0 = *arg2;

    if (temp_v0 == 0) {
        return 1;
    }
    func_1000E7A0(2, temp_v0);
    return 0;
}

s32 func_150E3414() {
    return 0;
}

void func_100111C8(u16 handle);
u16 func_10010F88(s32, u16, s16, u8, s32, s16, s16, s16, s16, s16);
void func_1516972C(struct102 *actor);

/* Clear the matching actor slot, replace an active sound, then release the actor. */
void func_150E3514(u8 *actor) {
    s32 slot;
    slot = *(u8 *)(actor + 0x48);
    if (slot >= 0 && (u8 *)D_800D99D0[slot] == actor) {
        D_800D99D0[slot] = NULL;
    }
    if (*(u16 *)(actor + 0x4A) != 0) {
        func_100111C8(*(u16 *)(actor + 0x4A));
        *(u16 *)(actor + 0x4A) = 0;
        func_10010F88(0x2D7, 0x5DC0, 0, 0, 0,
                     (s32)*(f32 *)(actor + 0x28),
                     (s32)*(f32 *)(actor + 0x2C),
                     (s32)*(f32 *)(actor + 0x30), 1000, 6000);
    }
    func_1516972C((struct102 *)actor);
}

s32 func_150E35DC() {
    return 0;
}

void func_150E36BC(s32 arg0, s32 *arg1, s32 *arg2, s32 *arg3) {
    Generated1104D0Actor *actor;

    arg0--;
    if ((arg0 >= 0) && (arg0 < 8)) {
        actor = D_800D99D0[arg0];
        if ((actor != NULL) && (actor->type == 0x27)) {
            *arg1 = actor->x;
            *arg2 = actor->y;
            *arg3 = actor->z;
        }
    }
}

s32 func_150E3738() {
    return 0;
}

s32 func_150E4010() {
    return 0;
}

void func_150E411C(void *arg0) {
    func_151C3B0C(arg0, 0.352000028f, 0.701000035f, 0.566000044f, D_800A1054,
                  0xFF, 0xFF, 0xFF);
}

s32 func_150E4174(u8 *arg0) {
    *(f32 *) (arg0 + 0x2C) = *(f32 *) (arg0 + 0x4C) * D_800BE9A4 + *(f32 *) (arg0 + 0x2C);
    *(f32 *) (arg0 + 0x30) = *(f32 *) (arg0 + 0x54) * D_800BE9A4 + *(f32 *) (arg0 + 0x30);
    return 1;
}
