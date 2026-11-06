#include <ultra64.h>
#include "structs.h"

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

s32 func_150DDFAC() {
    return 0;
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
