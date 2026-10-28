#include <ultra64.h>
#include "structs.h"

/* Non-matching placeholders for the text-only asm slice asm/133190.s. */

extern void (*D_80088C18[])(u8 *);
extern void (*D_80088C28[])(u8 *, s32, u8);
extern void (* volatile D_80088C38[])(u8 *, s32, u8);

#pragma GLOBAL_ASM("asm/nonmatchings/generated_133190/func_15105CE0.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_133190/func_1510608C.s")

s32 func_151061E0(s32 arg0) {
    return arg0 + 0x88;
}

// Matched with guarded commutative-add normalization.
u8 *func_151061EC(u8 *arg0) {
    s32 temp_v1 = *(s32 *) (arg0 + 0x48);

    return arg0 + temp_v1 * 0x34 + 0x88;
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_133190/func_15106214.s")

f32 func_151064B4(f32 arg0) {
    f32 temp = 1.0f - arg0;

    return temp * temp * temp;
}

f32 func_151064DC(f32 arg0) {
    f32 temp = 1.0f - arg0;

    return 3.0f * arg0 * temp * temp;
}

f32 func_15106510(f32 arg0) {
    return 3.0f * arg0 * arg0 * (1.0f - arg0);
}

f32 func_15106540(register f32 arg0) {
    return arg0 * arg0 * arg0;
}

f32 func_15106558(f32 arg0) {
    f32 temp = 1.0f - arg0;

    return -3.0f * temp * temp;
}

f32 func_15106584(f32 arg0) {
    return 9.0f * arg0 * arg0 - 12.0f * arg0 + 3.0f;
}

f32 func_151065BC(f32 arg0) {
    return -9.0f * arg0 * arg0 + 6.0f * arg0;
}

f32 func_151065EC(f32 arg0) {
    return 3.0f * arg0 * arg0;
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_133190/func_15106610.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_133190/func_151067B8.s")

void func_15106E78(u8 *arg0) {
    void (*callback)(u8 *) = D_80088C18[arg0[0x5C]];

    if (callback != NULL) {
        callback(arg0);
    }
    if (*(u8 **)(arg0 + 0x6C) != NULL) {
        func_1516972C(*(u8 **)(arg0 + 0x6C));
    }
    if (*(u8 **)(arg0 + 0x70) != NULL) {
        func_1516972C(*(u8 **)(arg0 + 0x70));
    }
    func_151D5E30(arg0 + 0x74);
}

void func_15106EF8(u8 *arg0) {
    func_15106E78(arg0);
    func_15169804(arg0);
}

void func_15106F24(u8 *arg0) {
    func_15106E78(arg0);
    func_15169824(arg0);
}

void func_15106F50(u8 *arg0, s32 arg1, u8 arg2) {
    void (*callback)(u8 *, s32, u8) = D_80088C28[arg0[0x5C]];

    if (callback != NULL) {
        callback(arg0, arg1, arg2);
    }
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_133190/func_15106F98.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_133190/func_151070F8.s")

s32 func_151072BC() {
    return 0;
}

void func_15107604(u8 *arg0) {
    u8 *temp_v0 = *(u8 **)(arg0 + 0x60);
    u8 *temp_v1 = *(u8 **)temp_v0 + 0x28;

    *(s32 *)(temp_v1 + 8) = 0;
}

s32 func_1510761C(u8 *arg0) {
    u8 *temp_a1 = arg0;

    if (*(s32 volatile *)(temp_a1 + 0x30) != 0) {
        func_1516972C(*(s32 volatile *)(temp_a1 + 0x30));
    }
}

s32 func_1510764C(s32 arg0) {
    func_1510761C(arg0);
    func_1514933C(arg0);
}

s32 func_15107678(s32 arg0) {
    func_1510761C(arg0);
    func_15149368(arg0);
}

void func_151076A4(u8 *arg0, s32 arg1, u8 arg2) {
    void (* volatile *callbacks)(u8 *, s32, u8) = D_80088C38;

    if (callbacks[*(volatile u8 *)(arg0 + 0x68)] != NULL) {
        callbacks[*(volatile u8 *)(arg0 + 0x68)](arg0, arg1, arg2);
    }
}

s32 func_15107700() {
    return 0;
}

void func_151078E4(u8 *arg0, s32 arg1, u8 arg2) {
    u8 *target = *(u8 **) (arg0 + 0x60);

    func_15169850(arg1, arg2, (s32) target, (s32) (target + 4), (s32) arg0);
}

s32 func_15107924() {
    return 0;
}

void func_1515C244(struct127 *, struct17 *, f32 *, f32 *);
void func_15143794(s16, s16, f32, vertex *);

/* Apply the actor-scaled direction to its queried origin and optionally return that origin. */
void func_15107A20(struct127 *actor, s16 yaw, s16 pitch, vertex *point, struct17 *originOut) {
    struct17 origin;
    f32 radius;
    f32 otherScale;

    func_1515C244(actor, &origin, &radius, &otherScale);
    func_15143794(yaw, pitch, radius, point);
    point->y *= actor->unkF0;
    point->x += origin.unk0;
    point->y += origin.unk4;
    point->z += origin.unk8;
    if (originOut != NULL) {
        *originOut = origin;
    }
}

/* Write two fractional points, retaining the original deltas across stores. */
void func_15107AE0(const f32 start[3], const f32 end[3], f32 first[3], f32 second[3]) {
    f32 firstFraction = 0.333f;
    f32 secondFraction = 0.6667f;
    f32 dx = end[0] - start[0];
    f32 dy = end[1] - start[1];
    f32 dz = end[2] - start[2];

    first[0] = start[0] + dx * firstFraction;
    first[1] = start[1] + dy * firstFraction;
    first[2] = start[2] + dz * firstFraction;
    second[0] = start[0] + dx * secondFraction;
    second[1] = start[1] + dy * secondFraction;
    second[2] = start[2] + dz * secondFraction;
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_133190/func_15107B78.s")

s32 func_15107C1C() {
    return 0;
}

s32 func_15107E48() {
    return 0;
}

void func_15107F54(u8 *arg0, u8 arg1, u8 *arg2, u8 *arg3) {
    func_15143134(arg2, arg3, *(u32 *) (arg0 + 0x1D4) + (arg1 << 6));
}

void func_15107F98(u8 *arg0, s32 arg1, u8 arg2) {
    func_15169850(arg1, arg2, *(u8 **) (arg0 + 0x60), *(u8 **) (arg0 + 0x60) + 4, arg0);
}
