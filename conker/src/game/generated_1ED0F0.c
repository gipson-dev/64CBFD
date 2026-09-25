#include <ultra64.h>

void func_151D5334(u8 *arg0, f32 arg1, f32 arg2, f32 arg3, s32 arg4, s32 arg5, s32 arg6);
void func_151D5404(u8 *arg0, f32 arg1, f32 arg2, f32 arg3, s32 arg4, s32 arg5, s32 arg6, s32 arg7);

extern u8 D_800AA954[];
extern u8 D_800AA958[][12];

/* Non-matching placeholders for the text-only asm slice asm/1ED0F0.s. */

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1ED0F0/func_151BFC40.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1ED0F0/func_151BFDA0.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1ED0F0/func_151BFE84.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1ED0F0/func_151C0098.s")

s32 func_151C02E4(s32 arg0, s32 arg1, s32 arg2, s32 *arg3) {
    u8 i = 0;

    if (arg2 > 0) {
        do {
            if (arg0 == arg3[i]) {
                return 0;
            }
            i++;
        } while (i < arg2);
    }
    if (arg0 == arg1) {
        return 0;
    }
    if (*(s32 *) arg0 == 0) {
        return 0;
    }
    if (*(u8 *) (arg0 + 4) == 0xFF) {
        return 0;
    }
    return 1;
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1ED0F0/func_151C0360.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1ED0F0/func_151C0418.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1ED0F0/func_151C04F8.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1ED0F0/func_151C05A4.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1ED0F0/func_151C05F0.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1ED0F0/func_151C0644.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1ED0F0/func_151C0698.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1ED0F0/func_151C110C.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1ED0F0/func_151C1180.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1ED0F0/func_151C1570.s")

s32 func_151C15FC(s32 arg0) {
    func_151C1570(arg0);
    func_15132570(arg0);
}

s32 func_151C1628(s32 arg0) {
    func_151C1570(arg0);
    func_1513259C(arg0);
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1ED0F0/func_151C1654.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1ED0F0/func_151C1798.s")

void func_151C1814(u8 *arg0, s32 *arg1, u8 arg2) {
    u8 *temp_v0 = arg0 + 0x170;

    if (arg2 == 0x2D) {
        s32 temp_v1 = arg1[0];
        s32 temp_a2 = *(s32 *) (temp_v0 + 0x6C);

        if (temp_v1 == temp_a2) {
            *(s32 *) (temp_v0 + 0x6C) = arg1[1];
            return;
        }
        if (temp_a2 == arg1[1]) {
            *(s32 *) (temp_v0 + 0x6C) = temp_v1;
        }
    }
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1ED0F0/func_151C1860.s")

void func_151C1940(s32 arg0, s32 arg1, s32 *arg2) {
    func_151C02E4(arg0, arg1, arg2[0], &arg2[1]);
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1ED0F0/func_151C196C.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1ED0F0/func_151C1D5C.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1ED0F0/func_151C1FB8.s")
