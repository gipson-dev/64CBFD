#include <ultra64.h>
void func_100111C8(u16 arg0);
void func_151A5D2C();

/* Non-matching placeholders for the text-only asm slice asm/1D2B10.s. */

s32 func_151A5660() {
    return 0;
}

void func_151A5CAC(u8 *arg0) {
    if (*(volatile u16 *) (arg0 + 0x6C) != 0) {
        func_151A5D2C(*(volatile u16 *) (arg0 + 0x6C));
    }
    func_1514933C(arg0);
}

void func_151A5CEC(u8 *arg0) {
    if (*(volatile u16 *) (arg0 + 0x6C) != 0) {
        func_151A5D2C(*(volatile u16 *) (arg0 + 0x6C));
    }
    func_15149368(arg0);
}

void func_151A5D2C(arg0)
u16 arg0;
{
    func_100111C8(arg0);
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1D2B10/func_151A5D58.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1D2B10/func_151A5F70.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1D2B10/func_151A6068.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1D2B10/func_151A6350.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1D2B10/func_151A6600.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1D2B10/func_151A6AB8.s")

s32 func_151A6B10(s32 arg0) {
    func_151A6AB8(arg0);
    func_1513CA6C(arg0);
}

s32 func_151A6B3C(s32 arg0) {
    func_151A6AB8(arg0);
    func_1513CAA0(arg0);
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1D2B10/func_151A6B68.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1D2B10/func_151A6BD8.s")

s32 func_151A6C90() {
    return 0;
}
