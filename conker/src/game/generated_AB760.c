#include <ultra64.h>
extern u8 D_8009D910[];

/* Non-matching placeholders for the text-only asm slice asm/AB760.s. */

void func_1507EB4C();

#pragma GLOBAL_ASM("asm/nonmatchings/generated_AB760/func_1507E2B0.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_AB760/func_1507E3C0.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_AB760/func_1507E500.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_AB760/func_1507E5C8.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_AB760/func_1507E6B8.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_AB760/func_1507E73C.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_AB760/func_1507E7E4.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_AB760/func_1507E908.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_AB760/func_1507E968.s")

void func_1507E9E8(s32 arg0, s32 arg1) {
}

u8 *func_1507E9F8(u8 *arg0, s32 *arg1) {
    if (func_150849A0(arg0) == 0) {
        if (arg1 != 0) {
            *arg1 = 5;
        }
        return D_8009D910;
    }
    if (arg1 != 0) {
        *arg1 = 0;
    }
    return 0;
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_AB760/func_1507EA44.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_AB760/func_1507EABC.s")

void func_1507EB2C(register s32 arg0) {
    func_1507EB4C(arg0, 0);
}

void func_1507EB4C(u8 *arg0, s32 arg1) {
    if (arg1 != *(arg0 + 0x70)) {
        *(arg0 + 0x70) = arg1;
        func_1507EABC(arg0);
    }
}
