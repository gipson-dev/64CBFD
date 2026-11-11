#include <ultra64.h>
#include "structs.h"

typedef struct {
    s32 flags;
    s16 lifetime;
    u8 kind;
    u8 pad7;
    s32 value8, valueC;
    u8 value10, value11, value12, value13, value14, value15;
    u8 pad16[2];
    s32 resource;
    u8 pad1C[12];
} EffectDescriptor108E90;
typedef struct { f32 x, y, z; u8 padC[8]; } EffectPosition108E90;
f32 func_150ADA68(void);
s32 func_150ADA20(void);
struct210 *func_1513C73C(s32, u8, u8, s32, f32, f32, f32, f32, f32, u8, u8, s32, u8, s32);


u8 *func_151491F4(s16, s8, s8, u8, u8, s32, u8, s32);
void func_1516972C(u8 *record);


/* Non-matching placeholders for the text-only asm slice asm/108E90.s. */

s32 func_150DB9E0() {
    return 0;
}

typedef struct { f32 x, y, z; } OrientedEffectPosition;
typedef struct {
    OrientedEffectPosition position;
    f32 fieldCBase, field10Range, field14Base, field18Range, speedBase, speedRange;
    s16 countBase, countRange, firstAngleBase, firstAngleRange;
    s16 secondAngleBase, secondAngleRange, byteBase, byteRange, shortBase, shortRange;
    u8 fixed38, fixed39, private3A[2];
    s32 argument3C, argument40, argument44, argument48, argument4C, argument50;
    u8 fixed54, fixed55, privateTail56[2];
} OrientedEffectInput;
extern f32 D_800A0C24, D_800A0C28, D_800A0C2C, D_800A0C30;
void func_15152F70(OrientedEffectInput *, u8);
/* Submit the original oriented-effect descriptor with the owner's byte mode. */
void func_150DBC60(struct260 *owner) {
    OrientedEffectInput input;
    input.position.x = D_800A0C24;
    input.position.y = D_800A0C28;
    input.position.z = D_800A0C2C;
    input.speedBase = 7.0f;
    input.speedRange = 5.0f;
    input.field14Base = D_800A0C30;
    input.field18Range = 0.0f;
    input.countBase = 1;
    input.countRange = 2;
    input.firstAngleBase = -75;
    input.secondAngleBase = -38;
    input.firstAngleRange = 22;
    input.secondAngleRange = 35;
    input.byteBase = 3;
    input.byteRange = 2;
    input.shortBase = 41;
    input.shortRange = 0;
    input.fieldCBase = 2.0f;
    input.field10Range = 2.0f;
    input.fixed38 = 10;
    input.fixed39 = 40;
    input.argument3C = 1;
    input.argument40 = 0;
    input.argument44 = 0;
    input.argument48 = 0;
    input.argument4C = 0;
    input.argument50 = 0;
    input.fixed54 = 255;
    input.fixed55 = 255;
    func_15152F70(&input, ((u8 *)owner)[0x0C]);
}

s32 func_150DBD70() {
    return 0;
}

s32 func_150DC558() {
    return 0;
}

s32 func_150DCEA0() {
    return 0;
}

s32 func_150DD640() {
    return 0;
}

/* Create a short-lived record, then select its byte mode from the owner's subtype. */
void func_150DDED0(u8 *owner) {
    u8 *record;

    record = func_151491F4(100, 2, -1, 1, 0, 1, 255, 0);
    if (record != NULL) {
        switch (owner[0x72]) {
            case 0xFB: record[0x28] = 1; break;
            case 0xFC: record[0x28] = 2; break;
            case 0xFD: record[0x28] = 4; break;
            case 0xFE: record[0x28] = 3; break;
            default: func_1516972C(record); break;
        }
    }
}

void func_150DDF88(u8 *arg0) {
    func_150DBD70(*(u8 *)(arg0 + 0x28), arg0);
}

/* Build and submit an effect for the selected actor position. */
s32 func_150DDFAC(u8 *actor, f32 previousX, f32 previousY, f32 previousZ, f32 height, void *parameter) {
    u8 *payload = *(u8 **)(actor + 0x98);
    EffectPosition108E90 *positions = *(EffectPosition108E90 **)(actor + 0x94);
    EffectDescriptor108E90 descriptor;
    f32 range = func_150ADA68() * 70.0f + 10.0f;
    s32 third, second, first;

    payload[0x20] = 4;
    switch (func_150ADA20() & 1) {
        case 0: descriptor.kind = 29; break;
        case 1: descriptor.kind = 30; break;
    }
    descriptor.value8 = 0;
    descriptor.valueC = 0;
    descriptor.flags = 17;
    descriptor.lifetime = 100;
    descriptor.value10 = 255;
    descriptor.value11 = 255;
    descriptor.value12 = 0;
    descriptor.value13 = 0;
    descriptor.value14 = 0;
    descriptor.value15 = 255;
    descriptor.resource = 0x30002;
    first = func_150ADA20();
    second = func_150ADA20();
    third = func_150ADA20();
    func_1513C73C((s32)&descriptor, 5, 0, (s32)parameter,
                 positions[*(s8 *)(actor + 0x2D)].x, height,
                 positions[*(s8 *)(actor + 0x2D)].z, range, range,
                 first & 255, (third & 1) + (second & 1), 0,
                 actor[0x0C], actor[1]);
    return 1;
}

s32 func_150DE12C() {
    return 0;
}

s32 func_150DE2A4(u8 *arg0) {
    s16 value = *(s16 *)(arg0 + 0x1C);

    if (value < 0x20) {
        arg0[0x28] = value << 3;
    }
    return 1;
}

void func_150DE2C4(u8 *arg0) {
    *(s16 *) (arg0 + 0x34) = *(s16 *) (arg0 + 0x34) - 0x1A;
    *(s16 *) (arg0 + 0x36) = *(s16 *) (arg0 + 0x36) - 0x1A;
    if ((*(s16 *) (arg0 + 0x34) < 0xA) || (*(s16 *) (arg0 + 0x36) < 0xA)) {
        *(s16 *) (arg0 + 0x38) = 0;
    }
}
