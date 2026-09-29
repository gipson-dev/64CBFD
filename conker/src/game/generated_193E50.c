#include <ultra64.h>
extern u8 D_80089470[];
extern u8 D_8009054C[];
extern s32 D_800DD220;
extern s32 D_800DD224;
extern u8 *D_800DD228;
extern u8 D_800DD230[];

s32 func_15094F70(s32, u8 *, s32, u8 *, s32, s32, s32, s32, s32);

/* Non-matching placeholders for the text-only asm slice asm/193E50.s. */

s32 func_151669A0() {
    return 0;
}

s32 func_15166B50() {
    return 0;
}

s32 func_15166D68() {
    return 0;
}

void func_15166F6C(s32 arg0, s32 arg1, s32 arg2, s32 arg3) {
    D_800DD228 = D_8009054C;
    func_15094F70(arg0, D_800DD228, D_800DD220, D_800DD230, 0, 0, 0, D_800DD224, 3);
}

/* Note 319: guarded expansion preserves retail's display-list cursor schedule. */
Gfx *func_15166FD8(Gfx *arg0, u8 arg1, u8 arg2) {
    Gfx *g = arg0++;

    g->words.w0 = 0xDA380003;
    g->words.w1 = (u32) D_80089470;
    return arg0;
}
