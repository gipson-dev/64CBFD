#include <ultra64.h>
#include "functions.h"
#include "variables.h"

s32 func_1509DD10(s32 arg0) {
    return 1;
}

s32 func_1509DD20(s32 arg0) {
    return 1;
}

s32 func_1509DD30(s32 arg0) {
    return 1;
}

s32 func_1509DD40(s32 arg0) {
    return 1;
}

s32 func_1509DD50(s32 arg0, struct214 *arg1) {
    func_15177F90(arg1->unk7, 0, arg1->unkB, arg1->unkC, arg1->unk10, arg1->unk14, arg1->unk18, 0x7FFF, 0xFF, arg1->unk1C, 0);
    return 1;
}

s32 func_1509DDC4(s32 arg0, u8 arg1) {
    func_15178E14(arg0 & 0xff, arg0);
    return 0;
}

s32 func_15084000(s32);
void func_15178C34(u8, s32, s32, s32, s16);
void func_15178BE4(u8, f32*, s16);
s32 func_15178C9C(u8 arg0, s32 arg1);
/* Position the selected record using an actor reference or explicit coordinates.
 * Preserve the record ID home across the actor resolver and conditional dispatch. */
s32 func_1509DDFC(volatile s32 recordId, s32 mode, struct215 *command) {
    s32 objectIndex;

    switch (mode) {
        case 0:
            objectIndex = func_15084000(command->unk8 & ~0x2000);
            func_15178BE4(recordId & 0xFF,
                &D_800CC2D0[objectIndex].x_position,
                command->unkC.s.unk2);
            return 1;
        case 1:
            func_15178C34(recordId & 0xFF, command->unk8, command->unkC.i.unk0,
                command->unk10, command->unk14);
            return 1;
        default:
            return 0;
    }
}

s32 func_1509DEC4(s32 arg0, s32 arg1, struct215 *arg2) {
    if (arg1 == 0) {
        s32 mask = ~0x2000;
        return func_15178C9C(arg0 & 0xff, func_15084000(arg2->unk8 & mask));
    }
    return 0;
}
