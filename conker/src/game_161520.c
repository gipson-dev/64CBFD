#include <ultra64.h>
#include "functions.h"
#include "variables.h"

/* Generated placeholder declarations. */
s32 func_15134070();
s32 func_1513418C();
s32 func_151342BC();
s32 func_151347CC();
s32 func_15134908();
s32 func_151349D0();
s32 func_15134CEC();
s32 func_15134DAC();
s32 func_15134E48();
s32 func_15135480();
s32 func_151356D4();
s32 func_15135BF8();
s32 func_15135DD0();
s32 func_15136404();
s32 func_15136698();
s32 func_15136918();
s32 func_15136A50();
s32 func_15136AE4();
s32 func_15136C3C();
s32 func_15136F50();
s32 func_15137610();
s32 func_1513783C();
s32 func_15137C64();
s32 func_15137E60();
s32 func_15137F30();
s32 func_15138120();
s32 func_151382E0();
s32 func_15138424();
s32 func_151389A8();
s32 func_15138BC0();
s32 func_15138C80();
s32 func_15138E98();
s32 func_15139578();
s32 func_15139768();
s32 func_15139D74();
s32 func_1513A24C();
s32 func_1513A48C();
s32 func_1513A5E0(s32 arg0, s32 arg1, s32 arg2);
s32 func_1513A6E0();
s32 func_1513ABB8();
s32 func_1513B0F8();
/* End generated placeholder declarations. */

void func_151BC5A4(struct102 *arg0, s32 arg1, u8 arg2);
void func_15143134(f32 *arg0, s32 arg1, s32 arg2);
extern f32 D_800A3FD8[];

// requires jump table
/* Non-matching C placeholders for asm/nonmatchings/game_161520/func_15134070.s. */
s32 func_15134070() {
    return 0;
}
s32 func_1513416C(struct102 *arg0) {
    s16 temp_v0 = arg0->unk1C;
    if (temp_v0 < 32) {
        arg0->unk28 = temp_v0 * 8;
    }
    return 1;
}
/* Non-matching C placeholders for asm/nonmatchings/game_161520/func_1513418C.s. */
s32 func_1513418C() {
    return 0;
}
// void *func_1513418C(s32 arg0, s32 arg1 /* size/offset */, u8 arg2, s32 arg3) {
//     void *sp24;
//     s32 temp_v1;
//     u8 temp_a0;
//     void *temp_ret;
//     void *temp_v0;
//     struct127 *temp_v0_2;
//
//     temp_ret = func_15167A68(0x28, arg3, arg1 + 0x58, 1, arg2, 1);
//     temp_v0 = temp_ret;
//     if (temp_v0 == 0) {
//         return NULL;
//     }
//     sp24 = temp_v0;
//     memcpy(&temp_v0->unk10, arg0, 0x30); //, temp_v0);
//     temp_a0 = temp_v0->unk3A;
//     if ((temp_a0 & 2) != 0) {
//         temp_v0_2 = temp_v0->unk1C;
//         if ((temp_v0_2->unk0 == 0) || (temp_v0->unk18 != temp_v0_2->unk3B)) {
//             func_1516972C(temp_v0);
//             return NULL;
//         }
//         temp_v1 = temp_v0_2->unk1D4;
//         if ((temp_v1 != 0) && ((temp_v0_2->unk74 & 0xF) != 0xF)) {
//             sp24 = temp_v0;
//             func_15143134(temp_v0->unk24, temp_v0->unk40, temp_v1 + (temp_v0->unk20 << 6), temp_v0);
//         } else {
//             temp_v0->unk3A = (u8) (temp_a0 | 8);
//         }
//     } else {
//         temp_v0->unk3A = (u8) (temp_a0 | 0x18);
//     }
//     temp_ret->unk50 = 0.0f;
//     temp_ret->unk4C = (f32) (1.0f / (2.0f * temp_ret->unk30));
//     return temp_ret;
// }
/* Non-matching C placeholders for asm/nonmatchings/game_161520/func_151342BC.s. */
s32 func_151342BC() {
    return 0;
}
s32 func_151346D0(s32 arg0, struct102 *arg1, s32 arg2) {
    arg1->unk3A &= 0xFFEF;
    return arg0;
}

void func_151346EC(struct102 *arg0) {
    func_15169804(arg0);
}

void func_1513470C(struct102 *arg0) {
    func_15169824(arg0);
}

void func_1513472C(struct102 *arg0) {
    s32 idx = arg0->unk3D;
    if (idx < 0) {
        idx = 0;
    }
    if (idx >= 10) {
        idx = 0;
    }
    D_80089AAC[idx]();
}

void func_1513477C(struct102 *arg0) {
  s32 idx = arg0->unk3D;
  if (idx < 0) {
      idx = 0;
  }
  if (idx >= 10) {
      idx = 0;
  }
    D_80089AD4[idx]();
}
/* Non-matching C placeholders for asm/nonmatchings/game_161520/func_151347CC.s. */
s32 func_151347CC() {
    return 0;
}
void func_151348F0(f32 arg0, f32 arg1, s32 arg2, s32 arg3) {
}
/* Non-matching C placeholders for asm/nonmatchings/game_161520/func_15134908.s. */
s32 func_15134908() {
    return 0;
}/* Non-matching C placeholders for asm/nonmatchings/game_161520/func_151349D0.s. */
s32 func_151349D0() {
    return 0;
}
void func_15134C98(struct102 *arg0, s32 arg1, u8 arg2) {
    if (arg0->unk28 == 1) {
        func_151BC5A4(arg0, arg1, arg2);
    }
}

void func_15134CD4(f32 arg0, f32 arg1, s32 arg2, s32 arg3) {
}
/* Non-matching C placeholders for asm/nonmatchings/game_161520/func_15134CEC.s. */
s32 func_15134CEC() {
    return 0;
}/* Non-matching C placeholders for asm/nonmatchings/game_161520/func_15134DAC.s. */
s32 func_15134DAC() {
    return 0;
}/* Non-matching C placeholders for asm/nonmatchings/game_161520/func_15134E48.s. */
s32 func_15134E48() {
    return 0;
}
// NON-MATCHING: only differs from us by the jal target address of the still-unmatched
// func_15169804 - this function's own code is verified byte-identical otherwise.
void func_151352EC(struct102 *arg0) {
    func_15169804(arg0);
}

// NON-MATCHING: only differs from us by the jal target address of the still-unmatched
// func_15169824 - this function's own code is verified byte-identical otherwise.
void func_1513530C(struct102 *arg0) {
    func_15169824(arg0);
}

void func_1513532C(u8 *arg0) {
    u8 idx = arg0[0x50];
    u16 handle;

    if (idx >= 6) {
        idx = 0;
    }
    handle = *(u16 *)(arg0 + 0x44);
    if (handle != 0) {
        func_100111C8(handle);
        *(u16 *)(arg0 + 0x44) = 0;
    }
    D_80089B70[idx](arg0);
}

void func_151353A8(u8 *arg0) {
    u8 idx = arg0[0x50];
    u16 handle;

    if (idx >= 6) {
        idx = 0;
    }
    handle = *(u16 *)(arg0 + 0x44);
    if (handle != 0) {
        func_100111C8(handle);
        *(u16 *)(arg0 + 0x44) = 0;
    }
    D_80089B88[idx](arg0);
}

void func_15135424(s32 arg0, s32 arg1, s32 arg2, s32 arg3, s32 arg4) {
    s32 sp20[2];
    s32 sp18[2];

    sp20[0] = arg1;
    sp20[1] = arg2;
    sp18[0] = arg3;
    sp18[1] = arg4;
    func_15145EA4(sp20, sp18, arg0, 2);
}
/* Non-matching C placeholders for asm/nonmatchings/game_161520/func_15135480.s. */
s32 func_15135480() {
    return 0;
}
void func_1513555C(struct102 *arg0, u8 *arg1, u8 arg2) {
    if ((arg2 == 0) || (arg2 == 0x12)) {
        if ((*(s32 *)&arg1[0] == arg0->unk1C) || (arg1[4] == arg0->unk18)) {
            func_1516972C(arg0);
        }
    }
}

void func_151355B8(struct102 *arg0, u8 *arg1, u8 arg2) {
    if (arg2 == 0) {
        if ((*(s32 *)&arg1[0] == arg0->unk1C) || (arg1[4] == arg0->unk18)) {
            func_1516972C(arg0);
        }
    } else if (arg2 == 3) {
        if ((*(s32 *)&arg1[0] == arg0->unk1C) || (arg1[4] == arg0->unk18)) {
            *(s32 *)((u8 *)arg0 + 0x10) &= ~1;
        }
    }
}

s32 func_15135658(struct102 *arg0) {
    arg0->unk74 = 1.0f;
    return 1;
}

f32 func_15135670(s32 arg0) {
    // "power", "../Effects/Blood/blood.c"
    return func_151422DC(0, &D_800A3FB4, 0, 2000, 1000, &D_800A3FBC, 2938) * D_800A45B4;
}
/* Non-matching C placeholders for asm/nonmatchings/game_161520/func_151356D4.s. */
s32 func_151356D4() {
    return 0;
}/* Non-matching C placeholders for asm/nonmatchings/game_161520/func_15135BF8.s. */
s32 func_15135BF8() {
    return 0;
}/* Non-matching C placeholders for asm/nonmatchings/game_161520/func_15135DD0.s. */
s32 func_15135DD0() {
    return 0;
}/* Non-matching C placeholders for asm/nonmatchings/game_161520/func_15136404.s. */
s32 func_15136404() {
    return 0;
}/* Non-matching C placeholders for asm/nonmatchings/game_161520/func_15136698.s. */
s32 func_15136698() {
    return 0;
}
s32 func_151368A8(struct102 *arg0) {
    f32 *step;
    s16 idx = arg0->unk1C;
    u8 *bytes = (u8 *)arg0;

    if (idx < 32) {
        u8 value = idx * 8;
        if (value < bytes[0x5C]) {
            bytes[0x5C] = value;
        }
    }

    step = (f32 *)(bytes + 0x128);
    *(f32 *)(bytes + 0x2C) += *step * D_800BE9A4;
    *(f32 *)(bytes + 0x30) += *step * D_800BE9A4;
    return 1;
}
/* Non-matching C placeholders for asm/nonmatchings/game_161520/func_15136918.s. */
s32 func_15136918() {
    return 0;
}
s32 func_15136A1C(struct102 *arg0) {
    s16 temp_v0 = arg0->unk1C;
    s32 temp_v1;
    if (temp_v0 < 32) {
        temp_v1 = temp_v0 * 8;
        if (temp_v1 < arg0->unk28) {
            arg0->unk28 = temp_v1;
        }
    }
    return 1;
}
/* Non-matching C placeholders for asm/nonmatchings/game_161520/func_15136A50.s. */
s32 func_15136A50() {
    return 0;
}/* Non-matching C placeholders for asm/nonmatchings/game_161520/func_15136AE4.s. */
s32 func_15136AE4() {
    return 0;
}/* Non-matching C placeholders for asm/nonmatchings/game_161520/func_15136C3C.s. */
s32 func_15136C3C() {
    return 0;
}/* Non-matching C placeholders for asm/nonmatchings/game_161520/func_15136F50.s. */
s32 func_15136F50() {
    return 0;
}/* Non-matching C placeholders for asm/nonmatchings/game_161520/func_15137610.s. */
s32 func_15137610() {
    return 0;
}/* Non-matching C placeholders for asm/nonmatchings/game_161520/func_1513783C.s. */
s32 func_1513783C() {
    return 0;
}/* Non-matching C placeholders for asm/nonmatchings/game_161520/func_15137C64.s. */
s32 func_15137C64() {
    return 0;
}
s32 func_15137E10(struct102 *arg0) {
    arg0->unk74 = ((func_150ADA68() * 50.0f) + 580.0f) * D_800A4828;
    return 1;
}
/* Non-matching C placeholders for asm/nonmatchings/game_161520/func_15137E60.s. */
s32 func_15137E60() {
    return 0;
}/* Non-matching C placeholders for asm/nonmatchings/game_161520/func_15137F30.s. */
s32 func_15137F30() {
    return 0;
}
s32 func_151380B4(u8 *arg0, s32 arg1, s32 arg2) {
    u8 *ptr = *(u8 **)(arg0 + 0x1D4);

    if (ptr == NULL) {
        return 0;
    }
    if ((arg0[0x74] & 0xF) == 0xF) {
        return 0;
    }
    func_15143134(&D_800A3FD8[arg1 * 4], arg2, (s32)(ptr + 0x300));
    return 1;
}
/* Non-matching C placeholders for asm/nonmatchings/game_161520/func_15138120.s. */
s32 func_15138120() {
    return 0;
}/* Non-matching C placeholders for asm/nonmatchings/game_161520/func_151382E0.s. */
s32 func_151382E0() {
    return 0;
}/* Non-matching C placeholders for asm/nonmatchings/game_161520/func_15138424.s. */
s32 func_15138424() {
    return 0;
}/* Non-matching C placeholders for asm/nonmatchings/game_161520/func_151389A8.s. */
s32 func_151389A8() {
    return 0;
}/* Non-matching C placeholders for asm/nonmatchings/game_161520/func_15138BC0.s. */
s32 func_15138BC0() {
    return 0;
}/* Non-matching C placeholders for asm/nonmatchings/game_161520/func_15138C80.s. */
s32 func_15138C80() {
    return 0;
}/* Non-matching C placeholders for asm/nonmatchings/game_161520/func_15138E98.s. */
s32 func_15138E98() {
    return 0;
}/* Non-matching C placeholders for asm/nonmatchings/game_161520/func_15139578.s. */
s32 func_15139578() {
    return 0;
}/* Non-matching C placeholders for asm/nonmatchings/game_161520/func_15139768.s. */
s32 func_15139768() {
    return 0;
}/* Non-matching C placeholders for asm/nonmatchings/game_161520/func_15139D74.s. */
s32 func_15139D74() {
    return 0;
}/* Non-matching C placeholders for asm/nonmatchings/game_161520/func_1513A24C.s. */
s32 func_1513A24C() {
    return 0;
}/* Non-matching C placeholders for asm/nonmatchings/game_161520/func_1513A48C.s. */
s32 func_1513A48C() {
    return 0;
}
void func_1513A594(struct127 *arg0, s32 arg1, s32 arg2, u8 arg3, s32 arg4) {
    func_1513A5E0(arg1, arg3, arg4);
}
/* Non-matching C placeholders for asm/nonmatchings/game_161520/func_1513A5E0.s. */
s32 func_1513A5E0(s32 arg0, s32 arg1, s32 arg2) {
    return 0;
}/* Non-matching C placeholders for asm/nonmatchings/game_161520/func_1513A6E0.s. */
s32 func_1513A6E0() {
    return 0;
}/* Non-matching C placeholders for asm/nonmatchings/game_161520/func_1513ABB8.s. */
s32 func_1513ABB8() {
    return 0;
}
void func_1513B0B8(void *arg0, s32 arg1, u8 arg2) {
    s32 *counter;

    if (arg2 == 0x45) {
        counter = (s32 *) ((u8 *) arg0 + 0x170);
        *counter -= 1;
        if (*counter < 0) {
            *(s32 *) ((u8 *) arg0 + 0x60) |= 0x80;
        }
    }
}
/* Non-matching C placeholders for asm/nonmatchings/game_161520/func_1513B0F8.s. */
s32 func_1513B0F8() {
    return 0;
}
