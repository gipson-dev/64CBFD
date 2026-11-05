#include <ultra64.h>

/* Partially recovered text-only slice asm/176A00.s. */

extern f32 D_800BE9A4;

s32 func_1514BC08();

s32 func_15149550() {
    return 0;
}

s32 func_15149838() {
    return 0;
}

s32 func_15149A94() {
    return 0;
}

s32 func_15149BF4(u8 *arg0) {
    *(f32 *)(arg0 + 0x2C) -= *(f32 *)(arg0 + 0x2C) * *(f32 *)(arg0 + 0x150);
    *(f32 *)(arg0 + 0x30) -= *(f32 *)(arg0 + 0x30) * *(f32 *)(arg0 + 0x150);

    if (*(f32 *)(arg0 + 0x2C) < 2.0f || *(f32 *)(arg0 + 0x30) < 2.0f) {
        return 0;
    }
    return 1;
}

/* Damp billboard extents, integrate vertical motion and test the active bounds. */
s32 func_15149C58(u8 *actor) {
    *(f32 *)(actor + 0x2C) -= *(f32 *)(actor + 0x2C) * *(f32 *)(actor + 0x150);
    *(f32 *)(actor + 0x30) -= *(f32 *)(actor + 0x30) * *(f32 *)(actor + 0x150);
    *(f32 *)(actor + 0x50) += *(f32 *)(actor + 0x4C) * D_800BE9A4;
    *(f32 *)(actor + 0x38) += *(f32 *)(actor + 0x50) * D_800BE9A4;
    if (*(f32 *)(actor + 0x15C) < *(f32 *)(actor + 0x38)) {
        return 0;
    }
    if (*(f32 *)(actor + 0x2C) < 4.0f || *(f32 *)(actor + 0x30) < 4.0f) {
        return 0;
    }
    return 1;
}

s32 func_15149D18() {
    return 0;
}

typedef struct { f32 x, y, z; } EffectPosition176A00;
typedef struct {
    EffectPosition176A00 position;
    u8 retained0C[10];
    s16 value16, value18, value1A, value1C, value1E, value20;
    s16 value22, value24, value26;
    u8 firstRGB[3], secondRGB[3], alpha, value2F;
    s8 value30;
    u8 flags;
} EffectDescriptor176A00;
s32 func_150ADA20(void);
void func_151429E0(u8, u8 *, u8 *, u8 *);
void func_1518CA80(EffectDescriptor176A00 *, u8);

/* Submit a position snapshot with ordered random fields and two color rows. */
s32 func_15149EC4(u8 *actor) {
    EffectDescriptor176A00 descriptor;

    descriptor.position = *(EffectPosition176A00 *)(actor + 0x34);
    descriptor.value16 = 0;
    descriptor.value18 = 0;
    descriptor.value1A = descriptor.value1C = (u32)func_150ADA20() % 6u + 8;
    descriptor.value1E = 0;
    descriptor.value20 = 0;
    descriptor.value22 = (u32)func_150ADA20() % 201u + 100;
    descriptor.value24 = (u32)func_150ADA20() % 5u + 3;
    descriptor.value26 = 600;
    func_151429E0(3, &descriptor.firstRGB[0], &descriptor.firstRGB[1], &descriptor.firstRGB[2]);
    func_151429E0(4, &descriptor.secondRGB[0], &descriptor.secondRGB[1], &descriptor.secondRGB[2]);
    descriptor.alpha = 255;
    descriptor.value2F = (u32)func_150ADA20() % 65u + 92;
    descriptor.value30 = (u32)func_150ADA20() % 3u + 1;
    descriptor.flags = 0;
    func_1518CA80(&descriptor, 1);
    return 0;
}

s32 func_15149FD0() {
    return 0;
}

s32 func_1514A19C() {
    return 0;
}

s32 func_1514A380() {
    return 0;
}

s32 func_1514A498(u8 *arg0) {
    f32 value0 = *(f32 *)(arg0 + 0x30);
    f32 scale = *(f32 *)(arg0 + 0x144);
    f32 value1 = *(f32 *)(arg0 + 0x2C);
    s32 index = *(s16 *)(arg0 + 0x1C);

    *(f32 *)(arg0 + 0x30) = value0 - (value0 * scale);
    *(f32 *)(arg0 + 0x2C) = value1 - (value1 * scale);
    if (index < *(s16 *)(arg0 + 0x156)) {
        arg0[0x5C] = (u32)index * (u32)*(s16 *)(arg0 + 0x158);
    }
    return 1;
}

/* Snapshot position, damp horizontal velocity and integrate the live timestep. */
s32 func_1514A4EC(u8 *actor) {
    f32 damping = *(f32 *)(actor + 0x140);

    *(u32 *)(actor + 0x40) = *(u32 *)(actor + 0x34);
    *(u32 *)(actor + 0x44) = *(u32 *)(actor + 0x38);
    *(u32 *)(actor + 0x48) = *(u32 *)(actor + 0x3C);
    *(f32 *)(actor + 0x130) *= damping;
    *(f32 *)(actor + 0x134) += *(f32 *)(actor + 0x13C) * D_800BE9A4;
    *(f32 *)(actor + 0x138) *= damping;
    *(f32 *)(actor + 0x34) += *(f32 *)(actor + 0x130) * D_800BE9A4;
    *(f32 *)(actor + 0x38) += *(f32 *)(actor + 0x134) * D_800BE9A4;
    *(f32 *)(actor + 0x3C) += *(f32 *)(actor + 0x138) * D_800BE9A4;
    return 1;
}

s32 func_1514A594() {
    return 0;
}

s32 func_1514A6A0() {
    return 0;
}

s32 func_1514AB5C() {
    return 0;
}

s32 func_1514AD9C() {
    return 0;
}

/* Damp billboard extents and integrate position before advancing vertical velocity. */
s32 func_1514AF74(u8 *actor) {
    *(f32 *)(actor + 0x2C) -= *(f32 *)(actor + 0x2C) * *(f32 *)(actor + 0x150);
    *(f32 *)(actor + 0x30) -= *(f32 *)(actor + 0x30) * *(f32 *)(actor + 0x150);
    *(f32 *)(actor + 0x38) += *(f32 *)(actor + 0x50) * D_800BE9A4 +
        0.5f * *(f32 *)(actor + 0x4C) * D_800BE9A4 * D_800BE9A4;
    *(f32 *)(actor + 0x50) += *(f32 *)(actor + 0x4C) * D_800BE9A4;
    if (*(f32 *)(actor + 0x2C) < 10.0f || *(f32 *)(actor + 0x30) < 10.0f) {
        return 0;
    }
    return 1;
}

s32 func_1514B034() {
    return 0;
}

s32 func_1514B364() {
    return 0;
}

s32 func_1514B844(u8 *arg0) {
    u8 *temp_v0 = *(u8 **) (arg0 + 0x98);
    s32 temp_v1 = *(s16 *) (arg0 + 0x1C);

    if (temp_v1 < 0x10) {
        s32 shifted = temp_v1 << 4;

        if (shifted < *(temp_v0 + 0x1B)) {
            *(temp_v0 + 0x1B) = shifted;
        }
    }
    return 1;
}

s32 func_1514B87C(f32 *arg0) {
    f32 delta = arg0[0x4C / 4] * D_800BE9A4;

    arg0[0x2C / 4] += delta;
    arg0[0x30 / 4] += delta;
    return 1;
}

s32 func_1514B8B0(u8 *arg0) {
    s32 temp_v0 = *(s16 *)(arg0 + 0x1C);

    if (temp_v0 < 0x10) {
        s32 temp_v1 = temp_v0 << 4;
        if (temp_v1 < *(u8 *)(arg0 + 0x5C)) {
            *(u8 *)(arg0 + 0x5C) = temp_v1;
        }
    }
    return 1;
}

s32 func_1514B8E4() {
    return 0;
}

s32 func_1514BC08() {
    return 0;
}

void func_1514BE00(register u8 *arg0) {
    func_1514BC08(arg0, arg0 + 0x110);
}

s32 func_1514BE20() {
    return 0;
}

void func_1514BF50(u8 *arg0) {
    *(f32 *) (arg0 + 0x40) = *(f32 *) (arg0 + 0x34);
    *(f32 *) (arg0 + 0x44) = *(f32 *) (arg0 + 0x38) + 100.0f;
    *(f32 *) (arg0 + 0x48) = *(f32 *) (arg0 + 0x3C);
}

void func_1514BF7C(register u8 *arg0) {
    func_1514BC08(arg0, arg0 + 0x110);
}

s32 func_1514BF9C() {
    return 0;
}

s32 func_1514C258(s32 arg0) {
    func_1514BF9C(arg0);
    func_1514BE20(arg0);
    return 1;
}

s32 func_1514C288(s32 arg0) {
    func_1514BF9C(arg0);
    func_1514BF50(arg0);
    return 1;
}

s32 func_1514C2B8(u8 *arg0) {
    *(arg0 + 0x72) = 0;
    *(arg0 + 0x71) = 0x24;
    *(s16 *) (arg0 + 0x1C) = *(s16 *) (arg0 + 0x164);
    *(u32 *) (arg0 + 0x58) |= 0x8000000;
    *(f32 *) (arg0 + 0x154) = *(f32 *) (arg0 + 0x160);
    return 1;
}

s32 func_1514C2F0() {
    return 0;
}

s32 func_1514C470() {
    return 0;
}

/* Note 313: original ROM implementation, retained as assembly until C conversion. */
#pragma GLOBAL_ASM("asm/nonmatchings/generated_176A00/func_1514C678.s")

s32 func_1514C858() {
    return 0;
}
