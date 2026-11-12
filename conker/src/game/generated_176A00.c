#include <ultra64.h>
#include "structs.h"

typedef s32 (*RadialCallback176A00)(s32, s16, f32, f32, f32, f32, f32, f32, u8, u8, f32, s32, f32, s32, u8);
extern RadialCallback176A00 D_8008AA00[];
f32 func_151423D8(u8);

extern f32 D_800A57A0, D_800A57A4, D_800A57A8, D_800A57AC;
void func_1513F680(struct171 *, u8, u8, u8, u8);

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

/* Approach both target extents, then select the settled update callback. */
s32 func_1514A380(u8 *owner) {
    s32 complete = 1;
    u8 *payload = owner + 0x110;

    if ((owner[0x74] & 2) == 0) {
        *(f32 *)(owner + 0x2C) +=
            (*(f32 *)(payload + 8) - *(f32 *)(owner + 0x2C)) * D_800A57A0;
        if (*(f32 *)(payload + 8) * D_800A57A4 < *(f32 *)(owner + 0x2C)) {
            owner[0x74] |= 2;
        } else {
            complete = 0;
        }
    }
    if ((owner[0x74] & 8) == 0) {
        *(f32 *)(owner + 0x30) +=
            (*(f32 *)(payload + 0x18) - *(f32 *)(owner + 0x30)) * D_800A57A8;
        if (*(f32 *)(payload + 0x18) * D_800A57AC < *(f32 *)(owner + 0x30)) {
            owner[0x74] |= 8;
        } else {
            complete = 0;
        }
    }
    if (complete) {
        func_1513F680((struct171 *)owner, owner[0x70], 4, owner[0x72], owner[0x73]);
    }
    return 1;
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

/* Integrate two points, then blend the second toward the first. */
s32 func_1514A594(u8 *owner) {
    f32 *record = (f32 *)owner;
    f32 dx, yComponent, zComponent;
    f32 weight;
    f32 firstX;

    *(f32 *)(owner + 0x130) *= *(f32 *)(owner + 0x140);
    *(f32 *)(owner + 0x134) += *(f32 *)(owner + 0x13C) * D_800BE9A4;
    *(f32 *)(owner + 0x138) *= *(f32 *)(owner + 0x140);
    dx = record[0x130 / 4] * D_800BE9A4;
    yComponent = record[0x134 / 4] * D_800BE9A4;
    zComponent = record[0x138 / 4] * D_800BE9A4;
    record[0x34 / 4] += dx;
    record[0x38 / 4] += yComponent;
    record[0x3C / 4] += zComponent;
    record[0x40 / 4] += dx;
    record[0x44 / 4] += yComponent;
    record[0x48 / 4] += zComponent;
    firstX = record[0x34 / 4];
    weight = record[0x54 / 4];
    /* The finished Y/Z steps can now hold the first-point coordinates. */
    yComponent = record[0x38 / 4];
    zComponent = record[0x3C / 4];
    record[0x40 / 4] = firstX + (record[0x40 / 4] - firstX) * weight;
    record[0x44 / 4] = yComponent + (record[0x44 / 4] - yComponent) * weight;
    record[0x48 / 4] = zComponent + (record[0x48 / 4] - zComponent) * weight;
    return 1;
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

s32 func_15145128(struct17 *, struct17 *, f32 *, f32 *);

/* Reposition the secondary point on a 100-unit radius around the actor. */
s32 func_1514BE20(u8 *actor) {
    s32 normalized;
    struct17 target, interpolated, direction;
    f32 length, reciprocal;
    f32 fraction = *(f32 *)(actor + 0x15C);
    target.unk0 = *(f32 *)(actor + 0x34);
    target.unk4 = *(f32 *)(actor + 0x38) + 100.0f;
    target.unk8 = *(f32 *)(actor + 0x3C);
    interpolated.unk0 = *(f32 *)(actor + 0x40) + (target.unk0 - *(f32 *)(actor + 0x40)) * fraction;
    interpolated.unk4 = *(f32 *)(actor + 0x44) + (target.unk4 - *(f32 *)(actor + 0x44)) * fraction;
    interpolated.unk8 = *(f32 *)(actor + 0x48) + (target.unk8 - *(f32 *)(actor + 0x48)) * fraction;
    direction.unk0 = interpolated.unk0 - target.unk0;
    direction.unk4 = interpolated.unk4 - *(f32 *)(actor + 0x38);
    direction.unk8 = interpolated.unk8 - target.unk8;
    normalized = func_15145128(&direction, &direction, &length, &reciprocal);
    if (normalized) {
        *(f32 *)(actor + 0x40) = *(f32 *)(actor + 0x34) + direction.unk0 * 100.0f;
        *(f32 *)(actor + 0x44) = *(f32 *)(actor + 0x38) + direction.unk4 * 100.0f;
        *(f32 *)(actor + 0x48) = *(f32 *)(actor + 0x3C) + direction.unk8 * 100.0f;
    } else {
        *(struct17 *)(actor + 0x40) = *(struct17 *)(actor + 0x34);
    }
    return normalized;
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
    func_1514BE20((u8 *)arg0);
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

/* Dispatch radial samples until the selected callback stops the loop. */
void func_1514C2F0(f32 x, f32 y, f32 z, f32 radius, u8 start, s8 step, s16 count, u8 selector, s32 arg8, f32 arg9, s32 arg10, u8 arg11) {
    s16 i;
    u8 angle = start;
    f32 quarter;
    f32 sample;
    f32 pointZ;
    RadialCallback176A00 callback;

    i = 0;
    while (i < count) {
        quarter = func_151423D8((u8)(angle - 64));
        sample = func_151423D8(angle);
        pointZ = radius * sample + z;
        callback = D_8008AA00[selector];
        if (callback != 0) {
            if (!callback(1, i, x + radius * quarter, y, pointZ,
                          x, y, z, angle, start, radius, arg8, arg9, arg10, arg11)) {
                return;
            }
        }
        angle += step;
        i++;
    }
}

s32 func_1514C470() {
    return 0;
}

/* Note 313: original ROM implementation, retained as assembly until C conversion. */
#pragma GLOBAL_ASM("asm/nonmatchings/generated_176A00/func_1514C678.s")

s32 func_1514C858() {
    return 0;
}
