#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/61490.s. */

extern u8 D_800CC2D0[];

s32 func_15033FE0() {
    return 0;
}

s32 func_150341BC() {
    return 0;
}

u8 *func_15034340(u8 *arg0, s32 arg1) {
    s8 *record = (s8 *)&D_800CC2D0[arg1 * 0x32C];

    if (record[0x1D1] != 0) {
        *(s16 *)arg0 = 6;
        arg0 += 4;
        *(s16 *)(arg0 - 2) = record[0x1D1] * 200;
    }

    return arg0;
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_61490/func_150343B0.s")

/* Original mounted-gun bone command writer; OGL Note 653. */
#pragma GLOBAL_ASM("asm/nonmatchings/generated_61490/func_15034420.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_61490/func_150344A0.s")

s32 func_1503453C() {
    return 0;
}

s32 func_150345E4() {
    return 0;
}

s32 func_15034728() {
    return 0;
}

s32 func_150347E8() {
    return 0;
}
