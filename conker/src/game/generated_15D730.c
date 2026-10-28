#include <ultra64.h>
typedef struct { s32 a, b, c; } ThreeWord15D730;
void func_15169260(void *, s32, s32, u8);
void *func_15130280(void *, u8, void *, s32, u8, s32);
extern u8 D_800A37F0[];
extern void (*D_80089844[])();
extern void (*D_80089814[])();
extern void (*D_80089878[])(u8 *, s32, u8);
extern s32 D_800BE9E4;

/* Non-matching placeholders for the text-only asm slice asm/15D730.s. */

void func_151318E8(f32 *, f32);

void func_15131918(f32 *, f32);
void func_15131958(f32 *, f32);

s32 func_151319C4();


#pragma GLOBAL_ASM("asm/nonmatchings/generated_15D730/func_15130280.s")


void *func_15130374(void *arg0, u8 arg1, s32 arg2, u8 arg3, s32 arg4) {
    return func_15130280(arg0, arg1, 0, arg2, arg3, arg4);
}

void func_151303BC(void *arg0, u8 arg1, s32 arg2) {
    func_15130374(arg0, arg1, arg2, 0xFF, 0);
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

s32 func_15131514() {
    return 0;
}

s32 func_1513164C(s32 arg0, s32 arg1, s32 arg2, s32 arg3, s32 arg4, s32 arg5, s32 arg6, s32 arg7, s32 arg8) {
    func_15131514(arg4, arg5, arg6, arg7, arg8);
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
    func_151319C4(arg0, arg1, arg0 + 0xA8);
}

s32 func_151319C4() {
    return 0;
}

void func_15131AFC(u8 *arg0, s32 arg1) {
    func_15131958((f32 *) (arg0 + 0x58), *(f32 *) (arg0 + 0xA8));
    func_151319C4(arg0, arg1, arg0 + 0xB0);
}

void func_15131B3C(u8 *arg0, s32 arg1) {
    func_15131918((f32 *) (arg0 + 0x58), *(f32 *) (arg0 + 0xA8));
    func_151319C4(arg0, arg1, arg0 + 0xB0);
}

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

s32 func_15131C84() {
    return 0;
}

void func_15131D4C(s32 arg0, u8 arg1) {
    ThreeWord15D730 tmp;

    tmp = *(ThreeWord15D730 *) D_800A37F0;
    func_15169260(&tmp, 3, arg0, arg1);
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_15D730/func_15131D9C.s")

s32 func_15131DEC() {
    return 0;
}

s32 func_15131EE4() {
    return 0;
}
