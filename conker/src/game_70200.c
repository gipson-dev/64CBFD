#include <ultra64.h>

#include "functions.h"
#include "variables.h"


void func_15042D50(void) {
    D_800CBD64 = 0;
    func_15043384(0);
}

void func_15042D78(u8 arg0) {
    D_800CBD74 = arg0;
}

void func_15042ECC(s32 arg0, s32 *arg1);

void func_15042D94(s16 arg0, s16 arg1, u8 arg2, s32 arg3,
                   s32 arg4, s32 arg5, s32 arg6, s32 arg7,
                   s32 arg8, s32 arg9, s32 argA, s32 argB,
                   s32 argC, s32 argD, s32 argE, s32 argF,
                   s32 arg10, s32 arg11, s32 arg12, s32 arg13) {
    s32 sp24[16];

    D_800CBD74 = arg2;
    D_800CBD70 = arg0;
    D_800CBD72 = arg1;

    sp24[0] = arg4;
    sp24[1] = arg5;
    sp24[2] = arg6;
    sp24[3] = arg7;
    sp24[4] = arg8;
    sp24[5] = arg9;
    sp24[6] = argA;
    sp24[7] = argB;
    sp24[8] = argC;
    sp24[9] = argD;
    sp24[10] = argE;
    sp24[11] = argF;
    sp24[12] = arg10;
    sp24[13] = arg11;
    sp24[14] = arg12;
    sp24[15] = arg13;
    func_15042ECC(arg3, sp24);
}

void func_15042E3C(s32 arg0,
                   s32 arg1, s32 arg2, s32 arg3, s32 arg4,
                   s32 arg5, s32 arg6, s32 arg7, s32 arg8,
                   s32 arg9, s32 argA, s32 argB, s32 argC,
                   s32 argD, s32 argE, s32 argF, s32 arg10) {
    s32 sp24[16];

    sp24[0] = arg1;
    sp24[1] = arg2;
    sp24[2] = arg3;
    sp24[3] = arg4;
    sp24[4] = arg5;
    sp24[5] = arg6;
    sp24[6] = arg7;
    sp24[7] = arg8;
    sp24[8] = arg9;
    sp24[9] = argA;
    sp24[10] = argB;
    sp24[11] = argC;
    sp24[12] = argD;
    sp24[13] = argE;
    sp24[14] = argF;
    sp24[15] = arg10;
    func_15042ECC(arg0, sp24);
}
#pragma GLOBAL_ASM("asm/nonmatchings/game_70200/func_15042ECC.s")

void func_150432BC(f32 arg0) {
    D_800CBD80 = arg0;
}

void func_150432CC(s32 arg0, s32 arg1) {
    D_800CBD74 = D_800CBD74 | 1;
    D_800CBD74 = D_800CBD74;
    D_800CBD7C = arg1;
    D_800CBD78 = arg0;
}

void func_150432FC(s16 arg0, s16 arg1) {
    D_800CBD70 = arg0;
    D_800CBD72 = arg1;
}

void func_1504332C(u8 arg0, u8 arg1, u8 arg2, u8 arg3) {
    D_800CBD60 = arg0;
    D_800CBD61 = arg1;
    D_800CBD62 = arg2;
    D_800CBD63 = arg3;
}

#pragma GLOBAL_ASM("asm/nonmatchings/game_70200/func_15043384.s")

void func_15043A00(struct105 *arg0, s32 arg1, s32 arg2) {
    if (arg0 != 0) {
        arg0->unk0 = arg1; // are these structs?
        arg0->unk4 = arg2;
        arg0->unkC = 0;
        arg0->unk8 = 0;
    }
}

// something with memcpy
#pragma GLOBAL_ASM("asm/nonmatchings/game_70200/func_15043A20.s")
#pragma GLOBAL_ASM("asm/nonmatchings/game_70200/func_15043AC8.s")

s32 func_15043B70(s32 arg0, s32 arg1, s32 arg2, s32 arg3) {
    s32 tmp;

    while (arg3 != 0) {
        tmp = arg3;
        if (arg1 < arg2 + arg3) {
            tmp = arg1 - arg2;
        }
        arg2 += tmp;
        arg3 -= tmp;
        if (arg2 >= arg1) {
            arg2 = 0;
        }
    }

    return arg2;
}
#pragma GLOBAL_ASM("asm/nonmatchings/game_70200/func_15043BB8.s")

#pragma GLOBAL_ASM("asm/nonmatchings/game_70200/func_15043CA4.s")
