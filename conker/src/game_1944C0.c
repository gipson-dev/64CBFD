#include <ultra64.h>

#include "functions.h"
#include "variables.h"


#pragma GLOBAL_ASM("asm/nonmatchings/game_1944C0/func_15167010.s")
// NON-MATCHING: not hugely far away
// void func_15167010(void) {
//     void (*func)(void);
//     s32 i;
//
//     for (i = 0; i < 24; i++)
//     {
//         func = D_8008B4A8[i].unk18;
//         if (func != NULL) {
//             func();
//         }
//     }
// }

#pragma GLOBAL_ASM("asm/nonmatchings/game_1944C0/func_1516706C.s")
#pragma GLOBAL_ASM("asm/nonmatchings/game_1944C0/func_151670C0.s")
#pragma GLOBAL_ASM("asm/nonmatchings/game_1944C0/func_151671E8.s")
#pragma GLOBAL_ASM("asm/nonmatchings/game_1944C0/func_15167310.s")
#pragma GLOBAL_ASM("asm/nonmatchings/game_1944C0/func_151674F8.s")
#pragma GLOBAL_ASM("asm/nonmatchings/game_1944C0/func_15167A68.s")
#pragma GLOBAL_ASM("asm/nonmatchings/game_1944C0/func_15167AD8.s")
#pragma GLOBAL_ASM("asm/nonmatchings/game_1944C0/func_15167B44.s")
#pragma GLOBAL_ASM("asm/nonmatchings/game_1944C0/func_15167C58.s")
#pragma GLOBAL_ASM("asm/nonmatchings/game_1944C0/func_15167D84.s")
#pragma GLOBAL_ASM("asm/nonmatchings/game_1944C0/func_15167E0C.s")
#pragma GLOBAL_ASM("asm/nonmatchings/game_1944C0/func_15168118.s")
#pragma GLOBAL_ASM("asm/nonmatchings/game_1944C0/func_1516865C.s")
#pragma GLOBAL_ASM("asm/nonmatchings/game_1944C0/func_15168800.s")
#pragma GLOBAL_ASM("asm/nonmatchings/game_1944C0/func_15168870.s")
// NON-MATCHING: only differs from us by the jal target address of func_15168B10
// (not yet confirmed byte-matching itself) - this function's own code is verified
// byte-identical otherwise.
void func_15168A2C(s32 arg0) {
    func_15168B10(arg0, 0);
}
#pragma GLOBAL_ASM("asm/nonmatchings/game_1944C0/func_15168A4C.s")
#pragma GLOBAL_ASM("asm/nonmatchings/game_1944C0/func_15168A9C.s")
// void *func_15168A9C(struct12 *arg0) {
//     void *temp_a1;
//     void *temp_v0;
//     void *temp_v0_2;
//
//     temp_a1 = (arg0->unk1 * 0x1A0) + (arg0->unk0 * 4) + 0x800DCE50;
//     if (arg0 == *temp_a1) {
//         *temp_a1 = (void *) arg0->unk8;
//     }
//     temp_v0_2 = arg0->unk8;
//     if (temp_v0_2 != 0) {
//         temp_v0_2->unk4 = (void *) arg0->unk4;
//     }
//     temp_v0 = arg0->unk4;
//     if (temp_v0 != 0) {
//         temp_v0->unk8 = (void *) arg0->unk8;
//     }
//     return temp_v0;
// }


void func_15168B10(s32 arg0, s32 arg1) {
    func_15168A9C(arg0);
    func_15168A4C(arg0, arg1);
}

#pragma GLOBAL_ASM("asm/nonmatchings/game_1944C0/func_15168B44.s")
#pragma GLOBAL_ASM("asm/nonmatchings/game_1944C0/func_15168BAC.s")
#pragma GLOBAL_ASM("asm/nonmatchings/game_1944C0/func_15168BE4.s")
#pragma GLOBAL_ASM("asm/nonmatchings/game_1944C0/func_15168C4C.s")
void func_15168E34(s32 *arg0, s32 arg1) {
    if ((*arg0 & 0xF000000) == 0) {
        *arg0 += arg1;
    }
}
#pragma GLOBAL_ASM("asm/nonmatchings/game_1944C0/func_15168E54.s")
#pragma GLOBAL_ASM("asm/nonmatchings/game_1944C0/func_15168F08.s")
#pragma GLOBAL_ASM("asm/nonmatchings/game_1944C0/func_15168F84.s")
// NON-MATCHING: only differs from us by the jal target address of the still-non-matching
// func_15169070 - this function's own code is verified byte-identical otherwise.
void func_15169040(s32 arg0, u8 arg1) {
    func_15169070(0, 0x68, arg0, arg1);
}
// NON-MATCHING: ported from ects_proto (ECTS ROM build), not yet byte-verified for us
void func_15169070(s32 arg0, s32 arg1, s32 arg2, u8 arg3) {
    s32 col;
    u8 *row;
    u8 *slot;
    struct115 *cur;
    void *node;

    func_15143D18(&arg0, &arg1, 2, 0x68);
    if (arg0 < arg1) {
        col = arg0 * 4;
        cur = &D_8008B4A8[arg0];
        do {
            row = D_800DCE50;
            slot = D_800DCE50 + col;
            do {
                if (cur->unk1C != NULL) {
                    node = *(void **) slot;
                    D_800DD190++;
                    if (node != NULL) {
                        do {
                            D_800DD198[D_800DD190] = *(void **) ((u8 *) node + 8);
                            func_1516968C(node, arg2, arg3);
                            cur->unk1C(node, arg2, arg3);
                            node = D_800DD198[D_800DD190];
                        } while (node != NULL);
                    }
                    D_800DD190--;
                } else {
                    node = *(void **) slot;
                    D_800DD190++;
                    if (node != NULL) {
                        do {
                            D_800DD198[D_800DD190] = *(void **) ((u8 *) node + 8);
                            func_1516968C(node, arg2, arg3);
                            node = D_800DD198[D_800DD190];
                        } while (node != NULL);
                    }
                    D_800DD190--;
                }
                row += 0x1A0;
                slot += 0x1A0;
            } while (row != (u8 *) &D_800DD190);
            col += 4;
            cur += 1;
        } while (col < arg1 * 4);
    }
}
#pragma GLOBAL_ASM("asm/nonmatchings/game_1944C0/func_15169260.s")
#pragma GLOBAL_ASM("asm/nonmatchings/game_1944C0/func_1516944C.s")
#pragma GLOBAL_ASM("asm/nonmatchings/game_1944C0/func_151695F0.s")
#pragma GLOBAL_ASM("asm/nonmatchings/game_1944C0/func_1516962C.s")
s32 func_15169668(s32 arg0, s32 arg1, s32 arg2, s32 arg3) {
    D_800D2DAB = 1;
    return arg0;
}
// NON-MATCHING: ported from ects_proto (ECTS ROM build), not yet byte-verified for us
void func_1516968C(struct102 *arg0, u8 *arg1, s32 arg2) {
    if (((arg2 == 0xF) || (arg2 == 0x10)) && (*arg1 == arg0->unkC)) {
        func_1516972C(arg0);
    }
}
// NON-MATCHING: ported from ects_proto (ECTS ROM build), not yet byte-verified for us
void func_151696DC(void *arg0) {
    s8 i;
    void **slot;

    i = 0;
    if (D_800DD190 > 0) {
        do {
            slot = &D_800DD198[i];
            i++;
            if (arg0 == *slot) {
                *slot = *(void **) ((u8 *) arg0 + 8);
            }
        } while (i < D_800DD190);
    }
}

void func_1516972C(struct102 *arg0) {
    void (*func)(struct102 *arg0);
    func_151696DC(arg0);

    if (arg0->unk0 >= 2) {
        func = D_8008B4D0[arg0->unk0].unk0;
        if (func != NULL) {
            func(arg0);
            return;
        }
        func_15169804(arg0);
    }
}

void func_1516979C(struct102 *arg0) {
    void (*func)(struct102 *arg0);

    func_151696DC(arg0);
    func = D_8008B4D4[arg0->unk0].unk0;
    if (func != NULL) {
        func(arg0);
        return;
    }
    func_15169824(arg0);
}

void func_15169804(struct102 *arg0) {
    func_15168B10(arg0, 1);
}

void func_15169824(struct102 *arg0) {
    func_15168A9C(arg0);
    func_10004074(arg0);
}

#pragma GLOBAL_ASM("asm/nonmatchings/game_1944C0/func_15169850.s")
