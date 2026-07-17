#include <ultra64.h>

#include "functions.h"
#include "variables.h"

f32 func_1514182C(void *arg0, void *arg1, s32 arg2, f32 arg3, f32 arg4, f32 arg5);


#pragma GLOBAL_ASM("asm/nonmatchings/game_16DC80/func_151407D0.s")

#pragma GLOBAL_ASM("asm/nonmatchings/game_16DC80/func_151408A4.s")

void func_151411A4(struct210 *arg0) {
    func_1513CA6C(arg0);
}

void func_151411C4(struct210 *arg0) {
    func_1513CAA0(arg0);
}

#pragma GLOBAL_ASM("asm/nonmatchings/game_16DC80/func_151411E4.s")

#pragma GLOBAL_ASM("asm/nonmatchings/game_16DC80/func_15141250.s")

#pragma GLOBAL_ASM("asm/nonmatchings/game_16DC80/func_151412BC.s")

// NON-MATCHING: ported from ects_proto (ECTS ROM build), not yet byte-verified for us
// NON-MATCHING (logic verified): retail materializes base = arg0+0x110 inside the
// if-body and reaches the vertex pointer as +0x44 off it (so unk154 likely sits at
// +0x44 of a sub-struct at 0x110), and evaluates each store's LHS pointer before its
// RHS value. Every rewrite tried (block/function-scope pointer local, u8*/s32 casts,
// struct224 member access) gets constant-folded by IDO back to direct 340(a0) loads.
void func_1514143C(struct210 *arg0) {
    if (arg0->unk154 != NULL) {
        arg0->unk154->x = arg0->unk34;
        arg0->unk154->y = arg0->unk38;
        arg0->unk154->z = arg0->unk3C;
    }
}

#pragma GLOBAL_ASM("asm/nonmatchings/game_16DC80/func_15141478.s")

#pragma GLOBAL_ASM("asm/nonmatchings/game_16DC80/func_15141564.s")

#pragma GLOBAL_ASM("asm/nonmatchings/game_16DC80/func_151415D4.s")

#pragma GLOBAL_ASM("asm/nonmatchings/game_16DC80/func_151416E8.s")

void func_151417C4(s32 arg0, u8 arg1) {
    s32 tmp[2];
    u8 byte;

    tmp[0] = D_8008A074[0];
    tmp[1] = D_8008A074[1];
    byte = arg0;
    func_15169260((s32) tmp, 2, (s32) &byte, arg1);
}

s32 func_15141818(s32 arg0, s32 arg1) {
    return 0;
}

#pragma GLOBAL_ASM("asm/nonmatchings/game_16DC80/func_1514182C.s")
// f32 func_1514182C(void *arg0, void *arg1, s32 arg2, f32 arg3, s32 arg4, s32 arg5) {
//     f32 sp6C;
//     f32 sp68;
//     f32 sp64;
//     ? sp34;
//     f32 temp_f0;
//     f32 temp_f12;
//     f32 temp_f2;
//
//     func_150A8050(&sp34, arg4, 0, arg5);
//     sp64 = arg1->unk0;
//     sp68 = arg1->unk4;
//     sp6C = arg1->unk8;
//     func_150A7960(&sp34, 0, arg2, 0, arg0 + 0x34, arg0 + 0x38, arg0 + 0x3C);
//     temp_f0 = arg0->unk34;
//     temp_f2 = arg0->unk38;
//     temp_f12 = arg0->unk3C;
//     arg0->unk40 = (f32) (temp_f0 + ((temp_f0 - arg1->unk0) * arg3 * 500.0f));
//     arg0->unk44 = (f32) (temp_f2 + ((temp_f2 - arg1->unk4) * arg3 * 500.0f));
//     arg0->unk48 = (f32) (temp_f12 + ((temp_f12 - arg1->unk8) * arg3 * 500.0f));
//     return temp_f0;
// }

s32 func_15141928(void *arg0) {
    void *temp_v0 = *(void **) ((u8 *) arg0 + 0x178);

    func_1514182C(arg0, (u8 *) arg0 + 0x17C, *(s32 *) ((u8 *) arg0 + 0x170), *(f32 *) ((u8 *) arg0 + 0x174), *(f32 *) temp_v0, *(f32 *) ((u8 *) temp_v0 + 8));
    return 1;
}
