#include <ultra64.h>

#include "functions.h"
#include "variables.h"

/* Generated placeholder declarations. */
s32 func_15049350();
/* End generated placeholder declarations. */

extern f32 D_80099080;
void func_150AAD98(s32 arg0, s32 arg1, s32 arg2, s32 arg3, s32 arg4, s32 arg5, s32 arg6, s32 arg7, s32 arg8);

// wtf?
void func_15049260(s32 arg0, s32 arg1, s32 arg2, s32 arg3, s32 arg4, s32 arg5, s32 arg6, s32 arg7, s32 arg8) {
    func_150AAD98(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8);
}

void func_150492CC(f32 arg0, f32 arg1, f32 arg2) {
    D_800CC220 = arg0;
    D_800CC224 = arg1;
    D_800CC228 = arg2;
    D_800CC22C = arg0 / 2.0f;
    D_800CC230 = arg1 / 2.0f;
    D_800CC234 = arg2 / 2.0f;

    if (arg0 == 0.0f) {
        arg0 = D_80099080;
    }

    D_800CC238 = arg1 / arg0;
    D_800CC23C = arg2 / arg0;
}

// too many temp vars
/* Non-matching C placeholders for asm/nonmatchings/game_76710/func_15049350.s. */
s32 func_15049350() {
    return 0;
}
