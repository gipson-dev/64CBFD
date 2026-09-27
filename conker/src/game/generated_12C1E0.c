#include <ultra64.h>
void func_15145740(s32, s32, s32, s32, f32);
s32 func_15081E0C(u8 *, u16, u8);

/* Non-matching placeholders for the text-only asm slice asm/12C1E0.s. */

s32 func_1503195C();
s32 func_151D3E6C();
s32 func_151D5A18();
extern s32 D_8008FC8C;
extern u8 *D_8008FC94;
extern f32 D_800A211C;

#pragma GLOBAL_ASM("asm/nonmatchings/game_12C1E0/func_150FED30.s")


#pragma GLOBAL_ASM("asm/nonmatchings/generated_12C1E0/func_150FEFD0.s")


#pragma GLOBAL_ASM("asm/nonmatchings/game_12C1E0/func_150FF084.s")

void func_150FF288(s32 arg0) {
    func_1503195C(arg0, 0x82, 0);
}

void func_150FF2AC(s32 arg0, s32 arg1, s32 arg2, s32 arg3) {
    func_15145740(arg0, arg1, arg2, arg3, D_800A211C);
}

#pragma GLOBAL_ASM("asm/nonmatchings/game_12C1E0/func_150FF2D4.s")

#pragma GLOBAL_ASM("asm/nonmatchings/game_12C1E0/func_150FF474.s")

s32 func_150FF6B4(u8 *arg0, u8 arg1, u8 arg2) {
    if (*(arg0 + 4) == 0x98) {
        return 0;
    }
    return 1;
}

#pragma GLOBAL_ASM("asm/nonmatchings/game_12C1E0/func_150FF6E0.s")

s32 func_150FF840() {
    return 0;
}

s32 func_150FFB6C() {
    return 0;
}


#pragma GLOBAL_ASM("asm/nonmatchings/generated_12C1E0/func_150FFBDC.s")


s32 func_150FFC3C() {
    return 0;
}

s32 func_150FFCC8(s32 arg0, s32 arg1, s32 arg2, s32 arg3, s32 arg4) {
    func_151D5A18(arg0, arg1, arg2, arg3, arg4, D_8008FC8C, *D_8008FC94);
    return func_151D3E6C(arg0, arg1, arg1, 0x8003A);
}

void func_150FFD2C(s32 arg0, u8 *arg1, s32 arg2) {
    u8 type = arg1[4];

    if ((type == 0x9F || type == 0xA0) &&
        ((*(u32 *)(arg1 + 0x94) & 0x80) == 0)) {
        func_15081E0C(arg1, 4, 0);
    }
}

s32 func_150FFD84() {
    return 0;
}
