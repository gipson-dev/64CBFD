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

typedef struct {
    f32 height; s16 vertices[9]; s16 pad16; u32 metadata;
    u8 flags, state; u16 pad1E; s32 value;
} Surface15194408;
typedef struct { s16 firstAngleBase, firstAngleRange, secondAngleBase, secondAngleRange; } Angles15194408;
typedef struct {
    f32 position[3], timeBase, timeRange, scaleBase, scaleRange, radiusBase, radiusRange;
    s16 countBase, countRange, requestSelectorBase, requestSelectorRange;
    s16 durationBase, durationRange, modeBase, modeRange;
    u8 selector, private35[3]; f32 opaqueChance; s16 firstValue, secondValue; s32 requestValue;
} Trail15194408;
extern f32 D_800A8294, D_800A8298, D_800A829C;
void *func_151AE7B0(u8 *, f32, s16, u8, s32);
void func_1504715C(void *, void *);
void func_15153F18(void *, void *, s32, s32, s32);

/* Submit the surface-aligned angular effect for actor kinds zero through four. */
void func_15194408(u8 *unused, u8 *actor) {
    Trail15194408 trail;
    Angles15194408 angles;
    Surface15194408 surface;

    switch (actor[4]) {
    case 0:
    case 1:
    case 2:
    case 3:
    case 4:
        func_151AE7B0(actor, 0.6f, 90, 255, 1);
        func_1504715C(&surface, actor);
        trail.position[0] = *(f32 *)(actor + 0x14);
        trail.position[1] = *(f32 *)(actor + 0x18) + 50.0f;
        trail.position[2] = *(f32 *)(actor + 0x1C);
        trail.countBase = 12;
        trail.countRange = 5;
        angles.firstAngleBase = 0;
        angles.firstAngleRange = 255;
        angles.secondAngleBase = -63;
        angles.secondAngleRange = 35;
        trail.timeBase = 6.0f;
        trail.timeRange = 3.0f;
        trail.scaleBase = D_800A8294;
        trail.scaleRange = D_800A8298;
        trail.radiusBase = 13.0f;
        trail.radiusRange = 8.0f;
        trail.requestSelectorBase = 3;
        trail.requestSelectorRange = 2;
        trail.durationBase = 30;
        trail.durationRange = 30;
        trail.modeBase = 100;
        trail.modeRange = 100;
        trail.opaqueChance = D_800A829C;
        trail.firstValue = 16;
        trail.secondValue = 15;
        trail.requestValue = 0;
        trail.selector = 0;
        func_15153F18(&angles, &trail, (s32)&surface, 255, 1);
        break;
    }
}

void func_15194588(u8 *arg0, u8 *arg1, s32 arg2) {
    func_150C7020(arg0, 0x1F4, 0xFF, 1);
    func_15194408(arg0, arg1);
}

typedef struct { f32 x,y,z; } TrailPoint151945CC;
typedef struct {
    TrailPoint151945CC position;
    f32 timeBase,timeRange,scaleBase,scaleRange,radiusBase,radiusRange;
    s16 countBase,countRange,requestSelectorBase,requestSelectorRange;
    s16 durationBase,durationRange,modeBase,modeRange;
    u8 selector,private35[3];f32 opaqueChance;s16 firstValue,secondValue;s32 requestValue;
} Trail151945CC;
extern f64 D_800A82A0;
extern f32 D_800A82A8,D_800A82AC,D_800A82B0,D_800A82B4,D_800A82B8;
extern u8 D_800A3FE6[];
s32 func_15134070(u8 *);
void *func_151B4CD0(u8 *,u8,s32);

/* Emit a classified trail from the captured source heading and actor position. */
void func_151945CC(u8 *source,u8 *actor,u8 *unusedContext) {
    TrailPoint151945CC position;
    s16 heading;
    Trail151945CC trail;
    Angles15194408 angles;
    Surface15194408 surface;
    s32 category;

    heading = (*(u16 *)(source + 0x7A) >> 8) - 64;
    position.x = *(f32 *)(actor + 0x14);
    position.y = *(f32 *)(actor + 0x18) + D_800A82A0;
    position.z = *(f32 *)(actor + 0x1C);
    func_1504715C(&surface,actor);
    category = func_15134070(actor);
    if (category != 99) {
        category = D_800A3FE6[category * 16];
        if (category != 2) {
            trail.position = position;
            trail.countBase = 15;
            trail.countRange = 12;
            trail.timeBase = D_800A82A8;
            trail.timeRange = D_800A82AC;
            trail.scaleBase = D_800A82B0;
            trail.scaleRange = 0.0f;
            trail.radiusBase = D_800A82B4;
            trail.radiusRange = D_800A82B8;
            angles.firstAngleBase = heading - 64;
            angles.firstAngleRange = 128;
            angles.secondAngleBase = -160;
            angles.secondAngleRange = 32;
            trail.requestSelectorBase = 3;
            trail.requestSelectorRange = 1;
            trail.durationBase = 31;
            trail.durationRange = 19;
            trail.modeBase = 155;
            trail.modeRange = 100;
            trail.firstValue = 16;
            trail.secondValue = 15;
            trail.requestValue = 0;
            trail.opaqueChance = 0.5f;
            if (category == 1) trail.selector = 1;
            else trail.selector = 0;
            func_15153F18(&angles,&trail,(s32)&surface,255,1);
            func_151B4CD0(actor,255,1);
        }
    }
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
