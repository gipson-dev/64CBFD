#include <ultra64.h>
extern f32 D_800BE9A4;
typedef struct { s32 a, b, c; } ThreeWord15D730;
void func_15169260(void *, s32, s32, u8);
void *func_15130280(void *, u8, void *, s32, u8, s32);
extern u8 D_800A37F0[];
extern void (*D_80089844[])();
extern void (*D_80089814[])();
extern void (*D_80089878[])(u8 *, s32, u8);
extern s32 D_800BE9E4;

/* Recovered routines and remaining placeholders from asm/15D730.s. */

void func_151318E8(f32 *, f32);

void func_15131918(f32 *, f32);
void func_15131958(f32 *, f32);

#include "structs.h"

typedef struct {
    u8 reserved[0x3C];
    f32 extent;
    f32 position[3];
    u8 reserved4C[0xC];
    f32 velocity[3];
    f32 verticalAcceleration;
    u32 flags;
} BounceRecord15D730;

typedef struct {
    u8 flags;
    s8 kind;
    u8 reserved[2];
    f32 damping;
} BounceResponse15D730;

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
extern f32 D_800A3844;
s32 func_1514672C(struct17 *);
s32 func_15046C80(f32 *, u16, f32, HeightResult71820 *);
extern s32 (*D_80089874[])(BounceRecord15D730 *, void *, f32 *, BounceResponse15D730 *);

s32 func_151319C4(BounceRecord15D730 *, void *, BounceResponse15D730 *);


#pragma GLOBAL_ASM("asm/nonmatchings/generated_15D730/func_15130280.s")


void *func_15130374(void *arg0, u8 arg1, s32 arg2, u8 arg3, s32 arg4) {
    return func_15130280(arg0, arg1, 0, arg2, arg3, arg4);
}

void *func_151303BC(void *arg0, u8 arg1, s32 arg2) {
    return func_15130374(arg0, arg1, arg2, 0xFF, 0);
}

s32 func_151303EC() {
    return 0;
}

s32 func_15130A9C() {
    return 0;
}

s32 func_1513137C() {
    return 0;
}

/* Select the record's color mode and write four halfword output channels. */
void func_15131514(s16 *red, s16 *green, s16 *blue, s16 *alpha, register u8 *record) {
    switch (record[0x71]) {
        case 1:
        case 5:
            *blue = 0;
            *red = *green = *blue;
            *alpha = 0;
            break;
        case 2:
            *red = *green = *blue = record[0x2C];
            *alpha = 0;
            break;
        case 8:
            *blue = 0;
            *red = *green = *blue;
            *alpha = record[0x2B];
            break;
        case 3:
            *red = record[0x24];
            *green = record[0x25];
            *blue = record[0x26];
            *alpha = 0;
            break;
        case 4:
        case 6:
            *red = record[0x28];
            *green = record[0x29];
            *blue = record[0x2A];
            *alpha = record[0x2B];
            break;
        case 7:
            *red = *green = *blue = record[0x2C];
            *alpha = record[0x2B];
            break;
        case 9:
            *red = record[0x24];
            *green = record[0x25];
            *blue = record[0x26];
            *alpha = record[0x2B];
            break;
        default:
            *red = *green = *blue = record[0x2C];
            *alpha = (record[0x2B] * record[0x27]) >> 8;
            break;
    }
}

s32 func_1513164C(s32 arg0, s32 arg1, s32 arg2, s32 arg3, s32 arg4, s32 arg5, s32 arg6, s32 arg7, s32 arg8) {
    func_15131514((s16 *)arg4, (s16 *)arg5, (s16 *)arg6, (s16 *)arg7, (u8 *)arg8);
    return func_1513137C(arg0, arg1, arg2, arg3, arg8);
}

s32 func_151316AC(u8 *arg0, s32 arg1) {
    u8 *temp_a2 = arg0;

    func_151318E8((f32 *)(temp_a2 + 0x58), *(f32 *)(temp_a2 + 0xA8));
    return 1;
}

s32 func_151316DC(u8 *arg0, s32 arg1) {
    u8 *temp_a2 = arg0;

    func_15131918((f32 *) (temp_a2 + 0x58), *(f32 *) (temp_a2 + 0xA8));
    return 1;
}

s32 func_1513170C(u8 *arg0, s32 arg1) {
    u8 *temp_a2 = arg0;

    func_15131958((f32 *) (temp_a2 + 0x58), *(f32 *) (temp_a2 + 0xA8));
    return 1;
}

void func_1513173C() {
    func_15169804();
}

void func_1513175C(u8 *arg0) {
    func_15169824(arg0);
}

s32 func_1513177C(u8 *arg0) {
    s32 idx = (*(u32 *) (arg0 + 0x68) & 0x4000) ? *(arg0 + 0x75) : 0;

    D_80089814[idx]();
}

s32 func_151317C8(u8 *arg0) {
    s32 idx = (*(u32 *) (arg0 + 0x68) & 0x4000) ? *(arg0 + 0x75) : 0;

    D_80089844[idx]();
}

s32 func_15131814(s32 arg0, s32 arg1) {
    return 0;
}

f32 func_151423D8(u8);

/* Write the two phase-driven offsets, then advance the byte phases by the live tick count. */
void func_15131828(u8 *record, f32 *amplitudes, u8 *phases, u8 *rates) {
    f32 sample;

    sample = func_151423D8((u8)(phases[0] - 0x40));
    *(f32 *)(record + 0x4C) = sample * amplitudes[0];
    sample = func_151423D8((u8)(phases[1] - 0x40));
    *(f32 *)(record + 0x54) = sample * amplitudes[1];
    phases[0] += rates[0] * (u32)D_800BE9E4;
    phases[1] += rates[1] * (u32)D_800BE9E4;
}

/* The mixed pointer/float ABI carries arg1's raw bits in a1. */
void func_151318E8(f32 *arg0, f32 arg1) {
    s32 count = D_800BE9E4;

    while (count > 0) {
        arg0[1] *= arg1;
        count--;
    }
}

void func_15131918(f32 *arg0, f32 arg1) {
    s32 count = D_800BE9E4;

    while (count > 0) {
        arg0[0] *= arg1;
        arg0[2] *= arg1;
        count--;
    }
}

void func_15131958(f32 *arg0, f32 arg1) {
    s32 count = D_800BE9E4;

    while (count > 0) {
        arg0[0] *= arg1;
        arg0[1] *= arg1;
        arg0[2] *= arg1;
        count--;
    }
}

void func_151319A4(register u8 *arg0, register s32 arg1) {
    func_151319C4((BounceRecord15D730 *)arg0, (void *)arg1, (BounceResponse15D730 *)(arg0 + 0xA8));
}

/* Probe the response plane and dispatch its live collision callback. */
s32 func_151319C4(BounceRecord15D730 *record, void *surface, BounceResponse15D730 *response) {
    u8 result = 1;
    f32 point[3];
    f32 contact[3];

    if (response->flags & 1) {
        if (response->kind != -1 && D_80089874[response->kind] != NULL &&
            record->position[1] < ((f32 *)surface)[1]) {
            point[0] = record->position[0];
            point[1] = ((f32 *)surface)[1];
            point[2] = record->position[2];
            if (!func_1514672C((struct17 *)point)) {
                return 0;
            }
            if (func_15046C80(point, 0,
                             record->position[1] - record->extent * D_800A3844,
                             (HeightResult71820 *)((u8 *)record + 0x80))) {
                contact[0] = point[0];
                contact[2] = point[2];
                contact[1] = ((HeightResult71820 *)((u8 *)record + 0x80))->height;
                result = D_80089874[response->kind](record, surface, contact, response);
            }
        }
    }
    return result;
}

void func_15131AFC(u8 *arg0, s32 arg1) {
    func_15131958((f32 *) (arg0 + 0x58), *(f32 *) (arg0 + 0xA8));
    func_151319C4((BounceRecord15D730 *)arg0, (void *)arg1, (BounceResponse15D730 *)(arg0 + 0xB0));
}

void func_15131B3C(u8 *arg0, s32 arg1) {
    func_15131918((f32 *) (arg0 + 0x58), *(f32 *) (arg0 + 0xA8));
    func_151319C4((BounceRecord15D730 *)arg0, (void *)arg1, (BounceResponse15D730 *)(arg0 + 0xB0));
}

extern f32 D_800A3848, D_800A384C;
f32 fabsf(f32);
#pragma intrinsic (fabsf)

/* Reflect and damp collision velocity, then settle motion below the threshold. */
s32 func_15131B7C(BounceRecord15D730 *record, void *surface, f32 *point, BounceResponse15D730 *response) {
    record->position[1] = point[1] + record->extent * D_800A3848;
    record->velocity[0] *= response->damping;
    record->velocity[1] *= -response->damping;
    record->velocity[2] *= response->damping;
    if (fabsf(record->velocity[1]) < D_800A384C) {
        record->velocity[0] = 0.0f;
        record->velocity[1] = 0.0f;
        record->velocity[2] = 0.0f;
        record->verticalAcceleration = 0.0f;
        response->flags &= ~1;
        record->flags &= ~6;
    }
    return 1;
}

void func_15131C2C(u8 *arg0, s32 arg1, u8 arg2) {
    void (*callback)(u8 *, s32, u8);

    if ((*(u32 *)(arg0 + 0x68) & 0x4000) != 0) {
        callback = D_80089878[arg0[0x75]];
        if (callback != NULL) {
            callback(arg0, arg1, arg2);
        }
    }
}

/* Advance the byte phases, then write their scaled offsets around the base. */
void func_15131C84(u8 *phases, s8 *rates, f32 base, f32 *amplitudes,
                  f32 *first, f32 *second) {
    f32 sample;

    phases[0] += rates[0] * (u32)D_800BE9E4;
    phases[1] += rates[1] * (u32)D_800BE9E4;
    sample = func_151423D8((u8)(phases[0] - 0x40));
    *first = sample * amplitudes[0] + base;
    sample = func_151423D8((u8)(phases[1] - 0x40));
    *second = sample * amplitudes[1] + base;
}

void func_15131D4C(s32 arg0, u8 arg1) {
    ThreeWord15D730 tmp;

    tmp = *(ThreeWord15D730 *) D_800A37F0;
    func_15169260(&tmp, 3, arg0, arg1);
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_15D730/func_15131D9C.s")

/* Update the paired scale, curve byte, and bounded timer. */
s32 func_15131DEC(u8 *record, s32 event) {
    f32 scale;
    f32 time;

    scale = sqrtf(*(f32 *)(record + 0xA8)) * *(f32 *)(record + 0xB0);
    *(f32 *)(record + 0x3C) = scale;
    *(f32 *)(record + 0x38) = scale;
    time = *(f32 *)(record + 0xA8);
    record[0x2B] = (u32)(*(f32 *)(record + 0xB4) -
                         *(f32 *)(record + 0xB8) * time * time);
    *(f32 *)(record + 0xA8) += D_800BE9A4;
    if (*(f32 *)(record + 0xAC) < *(f32 *)(record + 0xA8)) {
        return 0;
    }
    return 1;
}

s32 func_15131EE4() {
    return 0;
}
