#include <ultra64.h>

extern f32 D_800A8708;
f32 func_150ADA68(void);
void func_1514373C(f32, f32, f32 *, f32 *);
void func_15137610(u8 *, f32 *, f32 *, f32 *, s32, s32);


void *func_151AF270(u8 *, u8, s32);
#include "structs.h"
s32 func_15136C3C(void *, s32, s32, s32, s32, s32, s32, s32);
void func_15145A50(struct127 *);
s32 func_1507CD64(struct127 *, s32);


extern s8 D_8008FD90;
extern s32 D_800E9D00;
extern u8 D_800BE616;
extern u8 D_800A8210[];
extern u8 D_800A822C[];
extern u8 D_800A8244[];

/* Non-matching placeholders for the text-only asm slice asm/1C1150.s. */

s32 func_15194FF4();
s32 func_1518D1C0(void *, s32, s32, s32, u8, u8, void *);

/* Note 362: original ROM hit effect dispatch. */
#pragma GLOBAL_ASM("asm/nonmatchings/generated_1C1150/func_15193CA0.s")


void func_151942B0(arg0, arg1, arg2)
u8 arg0;
s32 arg1;
u8 arg2;
{
    func_15193CA0(arg1, 0, 0xFF, 1);
}

void func_151942E8(arg0, arg1, arg2)
u8 arg0;
s32 arg1;
u8 arg2;
{
    func_15193CA0(arg1, 1, 0xFF, 1);
}

void func_15194320(s32 arg0, u8 *arg1, s32 arg2) {
    switch (arg1[4]) {
    case 0:
    case 1:
    case 2:
    case 3:
    case 4:
        func_1518D1C0(arg1, 0xA, 0, 1, 0xFF, 1, D_800A8210);
        break;
    }
}

void func_15194394(s32 arg0, u8 *arg1, s32 arg2) {
    switch (arg1[4]) {
    case 0:
    case 1:
    case 2:
    case 3:
    case 4:
        func_1518D1C0(arg1, 0xC, 0, 1, 0xFF, 1, D_800A822C);
        break;
    }
}

s32 func_15194408() {
    return 0;
}

void func_15194588(u8 *arg0, s32 arg1, s32 arg2) {
    func_150C7020(arg0, 0x1F4, 0xFF, 1);
    func_15194408(arg0, arg1);
}

s32 func_151945CC() {
    return 0;
}

void func_15194794(u8 *arg0, u8 *arg1, s32 arg2) {
    func_151B01B8(arg0, arg1);
    func_151B09BC(arg0, arg1, 0x3E8, 0xFF, 0);

    switch (arg1[4]) {
    case 0:
    case 1:
    case 2:
    case 3:
    case 4:
        func_151AF270(arg1, 0xFF, 1);
        break;
    }
}

s32 func_15194810() {
    return 0;
}

void func_151949E0(s32 arg0, s32 arg1, s32 arg2) {
}

void func_151949F4(arg0, arg1)
s32 arg0;
u8 *arg1;
{
    if ((D_8008FD90 == 1) && (arg1[0x127] == 0) && ((D_800E9D00 & 8) != 0) &&
        (*(u16 *)(*(s32 *)(arg1 + 0x31C) + 0x1A0) == 0)) {
        func_15104170(arg0, arg1);
        *(u16 *)(*(s32 *)(arg1 + 0x31C) + 0x1A0) = 0x4B0;
    }
}

void func_15194A68(s32 arg0, u8 *arg1, s32 arg2) {
    func_1507DE4C(arg1);
    func_15138BC0(arg1, 0xFF, 1);
    func_151949F4(0, arg0, arg1);
}

void func_15194AB4(u8 *arg0) {
    u8 state = arg0[4];
    s32 temp;

    *(s32 *)(arg0 + 0x9C) |= 0xFFFE;
    temp = -1;
    switch (state) {
        case 0x75:
            temp = 0x73;
            break;
        case 0x80:
            temp = 0x72;
            break;
    }
    if (temp != -1) {
        func_15083568(arg0, temp, 0x3F800000, 0);
    }
}

void func_15194B1C(u8 *arg0) {
    s32 temp_v0 = func_15134070(arg0);

    if (temp_v0 != 0x63) {
        func_15138120(arg0, temp_v0, 0);
    }
    func_15136C3C(arg0, 1, 1, 1, 1, 1, 0xFF, 1);
    func_15194AB4(arg0);
}

void func_15194B94(s32 arg0, u8 *arg1, s32 arg2) {
    if (arg1[4] == 0x53) {
        func_151942B0(arg0, arg1, arg2);
    } else {
        func_15194B1C(arg1);
        func_151949F4(1, arg0, arg1);
    }
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1C1150/func_15194BF0.s")

void func_15194D80(s32 arg0, s32 arg1, s32 arg2) {
    func_15194FF4(arg0, arg1, 0);
}

void func_15194DA4(s32 arg0, s32 arg1, s32 arg2) {
    func_15194FF4(arg0, arg1, 1);
}

void func_15194DC8(s32 arg0, u8 *arg1, s32 arg2) {
    f32 sp2C[9];

    if (D_800BE616 != 0) {
        func_15194DA4(arg0, arg1, arg2);
    } else {
        func_1518D1C0(arg1, 0xB, 0, 1, 0xFF, 1, D_800A8244);
    }
    func_1504715C(sp2C, arg1);
    func_1514B364(arg1 + 0x14, sp2C, 0xFF, 1);
}

void func_15194E54(s32 arg0, u8 *arg1, s32 arg2) {
    u8 state = arg1[4];

    if ((state == 0x3E) || (state == 0xA6)) {
        func_150B06B0(arg1, arg0, 0xFF, 1);
    }
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1C1150/func_15194EA8.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1C1150/func_15194F48.s")

#pragma GLOBAL_ASM("asm/nonmatchings/game_1C1150/func_15194FF4.s")

s32 func_151951E0() {
    return 0;
}

/* Submit a direction-aligned pair of positions around an actor. */
void func_15195528(u8 *source, u8 *actor, s32 unused) {
    f32 angle;
    f32 start[3];
    f32 end[3];
    f32 direction[3];
    f32 x, z;
    if (source != NULL) angle = *(f32 *)(source + 0x40) - 90.0f;
    else if (actor != NULL) angle = *(f32 *)(actor + 0x40) - 90.0f;
    else angle = func_150ADA68() * 360.0f;
    func_1514373C(angle * D_800A8708, 1.0f, &direction[0], &direction[2]);
    direction[1] = 0.0f;
    x = direction[0] * 20.0f;
    start[0] = *(f32 *)(actor + 0x14) + x;
    start[1] = *(f32 *)(actor + 0x18) + 50.0f;
    z = direction[2] * 20.0f;
    start[2] = *(f32 *)(actor + 0x1C) + z;
    end[0] = *(f32 *)(actor + 0x14) - x;
    end[1] = *(f32 *)(actor + 0x18) + 50.0f;
    end[2] = *(f32 *)(actor + 0x1C) - z;
    func_15137610(actor, start, end, direction, 255, 1);
}

void func_15195650(u8 *arg0, s32 arg1, s32 arg2) {
    func_151B01B8(arg0, arg1);
    func_151B09BC(arg0, arg1, 0x3E8, 0xFF, 0);
}

/* Dispatch zero-health actor updates, then clear the type-0x47 actor. */
void func_15195698(struct127 *other, struct127 *actor, u8 *arg2) {
    if ((actor->health == 0) && (actor->unk127 != 0xFF)) {
        func_15136C3C(actor, 1, 1, 1, 1, 0, 0xFF, 1);
        func_15145A50(actor);
        func_1507CD64(actor, 6);
    }
    if (other->id == 0x47) {
        other->health = 0;
    }
}

void func_15195738(s32 arg0, s32 arg1, s32 arg2) {
    s8 sp18[7];

    sp18[0] = 1;
    *(s16 *)&sp18[2] = (func_150ADA20() % 0xBU) + 0x14;
    sp18[4] = 8;
    sp18[6] = -1;
    sp18[5] = 1;
    func_151D8868(sp18, 0, 0xFF, 0);
}
