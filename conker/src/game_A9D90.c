#include <ultra64.h>

#include "functions.h"
#include "variables.h"

/* Generated placeholder declarations. */
s32 func_1507C8FC();
s32 func_1507CD64();
s32 func_1507D1D8(s32 arg0);
s32 func_1507D4F8();
s32 func_1507D754();
s32 func_1507DB6C();
s32 func_1507DF10();
s32 func_1507DFE4();
s32 func_1507E114();
s32 func_1507E1D0();
/* End generated placeholder declarations. */

void func_1507C8E0(struct127 *arg0, s32 arg1) {
    arg0->unk31C->unk120 = (u8)2;
    arg0->unk31C->unk124 = arg1;
}

// "goto" hell
/* Non-matching C placeholders for asm/nonmatchings/game_A9D90/func_1507C8FC.s. */
s32 func_1507C8FC() {
    return 0;
}

void func_1507CD0C(struct127 *arg0) {
    s32 temp_lo = ((s32)arg0 - (s32)&D_800CC2D0) / (s32)sizeof(struct127);

    arg0->unk31C->unk120 = 3;

    if (temp_lo <= D_80082FA0) {
        func_15181D70(temp_lo);
    }
}

extern u8 D_800CC40F[];

/* Non-matching C placeholders for asm/nonmatchings/game_A9D90/func_1507CD64.s. */
s32 func_1507CD64() {
    return 0;
}

void func_1507D158(s32 arg0, s32 arg1, s32 arg2, s32 arg3, s32 arg4, s32 arg5) {
    u8 value = D_800CC40F[arg0 * sizeof(struct127)];

    func_1509BFB0(3, value | 0x2000, arg1, arg2, arg3, arg4, arg5);
}
/* Non-matching C placeholders for asm/nonmatchings/game_A9D90/func_1507D1D8.s. */
s32 func_1507D1D8(s32 arg0) {
    return 0;
}

/* Non-matching C placeholders for asm/nonmatchings/game_A9D90/func_1507D4F8.s. */
s32 func_1507D4F8() {
    return 0;
}
// NON-MATCHING: pretty far away!
// void func_1507D4F8(s16 arg0) { // struct126 *
//     // ?32 sp24;
//     struct127 *temp_a0;
//
//     if ((D_8008FDBC & 1) == 0) {
//         func_15085710(arg0, 4, 1);
//     }
//     // sp24 = (?32) arg0;
//     if (func_150859AC(arg0, 3) != 0) {
//         func_15085710(arg0, 5, D_8008726C); //temp_ret =
//         temp_a0 = &D_800CC2D0[arg0];
//         temp_a0->unkB2 = (u16)0;
//         if (D_800BE616 == 0) {
//             D_800D18A8 = (u8)1;
//             if (((D_800D2E4C->unk19 & 4) != 0) || (D_8008FDA8 < 0)) {
//                 func_1501C730(2, D_800BE3DF, D_800BE3E0, 0, 0);
//                 return;
//             }
//             func_1501C730(1, 0x22, 0, 0, 0);
//             return;
//         }
//         if (D_800E0C20 != 0) {
//             temp_a0->unk31C->unk120 = (u8)0xA;
//             return; // temp_ret;
//         }
//         func_1507D1D8(temp_a0);
//         return;
//     }
//     if (D_800BE616 == 0) {
//         D_800D2E43 = (u8)1;
//         func_1509C3A0();
//         D_800D18A8 = (u8)1;
//         func_15085710(arg0, 5, D_8008726C);
//         func_15085710(arg0, 2, D_80087260);
//         func_1501C730(1, 0x18, 0, 0, 0);
//     } else {
//         D_800D18A0 = (u16) (D_800D18A0 | (1 << (s32) arg0));
//     }
//     // temp_a0 = &D_800CC2D0[arg0];
//     if (temp_a0->unk31C->unk84 == 0) {
//         D_8008FD94 -= 1; //(s8) (D_8008FD94 - 1);
//     }
//     temp_a0->unk31C->unk120 = (u8)0xA;
//     D_800BE618 -= 1; //(s8) (D_800BE618 - 1);
//     //return temp_a0_2->unk31C;
// }

/* Non-matching C placeholders for asm/nonmatchings/game_A9D90/func_1507D754.s. */
s32 func_1507D754() {
    return 0;
}

void func_1507DB44(s32 arg0, s32 arg1) {
    func_1503DE70(arg0, arg1, -1);
}

void func_1507DB64(void) {
}

/* Non-matching C placeholders for asm/nonmatchings/game_A9D90/func_1507DB6C.s. */
s32 func_1507DB6C() {
    return 0;
}

void func_1507DE4C(struct127 *arg0) {

    if (arg0->interaction_state == 1) {
        func_150836CC(arg0, 0x44);
        func_150836CC(arg0, 0x23);
        arg0->unk9C |= 0xF000;
        func_150836CC(arg0, 0x44);
        func_150836CC(arg0, 0x23);
        return;
    }

    switch(arg0->id) {
        case 0x9F:
        case 0xa0:
            arg0->unk9C |= 0xF000;
            break;
        case 0x5A:
        case 0x74:
        case 0x7A:
            arg0->unk9C |= 0xFF8;
            break;
    }
}


/* Non-matching C placeholders for asm/nonmatchings/game_A9D90/func_1507DF10.s. */
s32 func_1507DF10() {
    return 0;
}
/* Non-matching C placeholders for asm/nonmatchings/game_A9D90/func_1507DFE4.s. */
s32 func_1507DFE4() {
    return 0;
}
/* Non-matching C placeholders for asm/nonmatchings/game_A9D90/func_1507E114.s. */
s32 func_1507E114() {
    return 0;
}
/* Non-matching C placeholders for asm/nonmatchings/game_A9D90/func_1507E1D0.s. */
s32 func_1507E1D0() {
    return 0;
}
