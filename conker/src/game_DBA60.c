#include <ultra64.h>

#include "functions.h"
#include "variables.h"

/* Generated placeholder declarations. */
s32 func_150AE790();
s32 func_150AEB9C();
s32 func_150AEDF8();
/* End generated placeholder declarations. */

void func_150AE5B0(struct108 *arg0) {
    if ((D_800D2E4C->unk4 & 0x80) == 0) {
        if (func_1509BE40(0, 0x2000, 0xBB) != -1) {
            if (func_15123934(arg0, arg0->unk2C, 0, arg0->unk134, 8) != 0) {
                arg0->unk84 |= 0x1000000;
                func_151254F4(arg0, D_800CC335 - 1);
            }
        } else if (func_151239CC(arg0, 8) != 0) {
            func_151254F4(arg0, 0);
        }
    }
    arg0->unk84 &= -0x4001;
    if ((D_800D2E4C->unk1 & 4) == 0) {
        if (func_1509BE40(1, 0x2000, 0x95, func_1509BE40(0, 0x2014, 0xB7) | 0x2000) != 0) {
            arg0->unk84 |= 0x1000000;
            if (((arg0->unk2C & 1) != 0) && (func_15123934(arg0, arg0->unk2C, 0, arg0->unk134, 0) != 0)) {
                arg0->unk1B4 = 3;
                arg0->unk84 &= -5;
                func_15124B18(arg0);
            }
        } else if (func_151239CC(arg0, 0) != 0) {
            func_15124B18(arg0);
            arg0->unk84 &= 0xFEFFFFFF;
        }
    }
    if (func_1509BE40(1, 0x4082, 6, 0x9000) != 0) {
        arg0->unk84 |= 0x10000;
    } else {
        arg0->unk84 &= 0xFFFEFFFF;
    }
}


/* Non-matching C placeholders for asm/nonmatchings/game_DBA60/func_150AE790.s. */
s32 func_150AE790() {
    return 0;
}
// some funky xor going on
/* Non-matching C placeholders for asm/nonmatchings/game_DBA60/func_150AEB9C.s. */
s32 func_150AEB9C() {
    return 0;
}

void func_150AECCC(struct42 *arg0) {
    arg0->unk96 = arg0->unk96 + (arg0->unk94 * D_800BE9E4);
    if (arg0->unk96 >= 0x1401) {
        arg0->unk96 = 0x1400;
    }
    arg0->unk9E = arg0->unk9E - ((s32) arg0->unk96 >> 8);
    arg0->unkA4 = arg0->unkA4 + D_800BE9E4;
    if (arg0->unkA4 >= 0x1A) {
        arg0->unkA4 = 0x19;
    }
}

void func_150AED4C(struct114 *arg0) {
    arg0->unk34 += arg0->unk14 * D_800BE9E4;
    if (arg0->unk2A < arg0->unk34) {
        arg0->unk3A = 70;
        arg0->unk34 = arg0->unk2A;
    }
    arg0->unk36 = arg0->unk34;
}

// NON-MATCHING: ported from ects_proto (ECTS ROM build), not yet byte-verified for us
s32 func_150AED9C(struct202 *arg0) {
    u8 *p;
    s32 val;

    p = (u8 *) arg0->unk98;
    val = arg0->unk1C * 8;
    if (val >= 0x100) {
        val = 0xFF;
    }
    p[0x1B] = val;
    if ((u8) val < 0) {
        return 0;
    }
    return 1;
}

s32 func_150AEDD8(struct202 *arg0) {
    if (arg0->unk1C < 0x20) {
        arg0->unk28 = arg0->unk1C * 8;
    }
    return 1;
}

/* Non-matching C placeholders for asm/nonmatchings/game_DBA60/func_150AEDF8.s. */
s32 func_150AEDF8() {
    return 0;
}
// void func_150AEDF8(void *arg0, void *arg1, s32 arg2) {
//     s32 temp_a0;
//     s32 temp_t6;
//     s32 temp_v1;
//     void *temp_v0;
//     void *temp_v0_2;
//
//     temp_t6 = arg2 & 0xFF;
//     if (temp_t6 == 0x2D) {
//         temp_v0 = arg0->unk28;
//         temp_a0 = temp_v0->unk0;
//         temp_v1 = arg1->unk0;
//         if (temp_v1 == temp_a0) {
//             temp_v0->unk0 = (s32) arg1->unk4;
//             temp_v0->unk4 = (u8) arg1->unk9;
//             return;
//         }
//         if (arg1->unk4 == temp_a0) {
//             temp_v0->unk0 = temp_v1;
//             temp_v0->unk4 = (u8) arg1->unk8;
//             return;
//         }
//     } else {
//         temp_v0 = arg0->unk28;
//         if (temp_t6 == 0) {
//             if ((arg1->unk0 == temp_v0->unk0) || ((temp_v0->unk4 == (u8) arg1->unk4))) {
//                 func_1516972C(arg0, temp_t6, arg0);
//             }
//         }
//     }
// }
