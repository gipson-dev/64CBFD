#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/1EF500.s. */

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1EF500/func_151C2050.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1EF500/func_151C229C.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1EF500/func_151C2734.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1EF500/func_151C2AD0.s")

s32 func_151C2E4C(u8 *arg0, u8 *arg1) {
    if (arg0 == arg1) {
        return 0;
    }
    if (*(s32 *) arg0 == 0) {
        return 0;
    }
    if (*(arg0 + 4) == 0xFF) {
        return 0;
    }
    return 1;
}

s32 func_151C2E94() {
    return 0;
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1EF500/func_151C2EF0.s")

/* Note 364: original projectile impact callback. */
#pragma GLOBAL_ASM("asm/nonmatchings/generated_1EF500/func_151C2F48.s")

/* Note 362: original ROM hit effect dispatch. */
#pragma GLOBAL_ASM("asm/nonmatchings/generated_1EF500/func_151C329C.s")


#pragma GLOBAL_ASM("asm/nonmatchings/generated_1EF500/func_151C36D8.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1EF500/func_151C3B0C.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1EF500/func_151C436C.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1EF500/func_151C43E0.s")

void func_151C4510(u8 *arg0, f32 *arg1, f32 arg2) {
    *(f32 *) (arg0 + 0x34) = *(f32 *) (arg0 + 0x34) + arg1[1] * arg2;
    *(f32 *) (arg0 + 0x38) = *(f32 *) (arg0 + 0x38) + arg1[2] * arg2;
    *(f32 *) (arg0 + 0x3C) = *(f32 *) (arg0 + 0x3C) + arg1[3] * arg2;
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1EF500/func_151C455C.s")

s32 func_151C4644() {
    return 0;
}

s32 func_151C4820() {
    return 0;
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1EF500/func_151C4AB0.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1EF500/func_151C4B0C.s")
