#include <ultra64.h>

#include "functions.h"
#include "variables.h"

/* Generated placeholder declarations. */
s32 func_15006234();
/* End generated placeholder declarations. */

void func_150061B0(void) {
    osCreateMesgQueue(&D_800BE900, &D_800BE2D0, 8);
    osSetEventMesg(OS_EVENT_SI, &D_800BE900, D_800BE9E0);
    D_800BE730.unk0 = &D_800BE748;
    D_800BE730.unk4 = &D_800BE74E;
    D_800BE730.unk8 = &D_800BE754;
    D_800BE730.unkC = &D_800BE75A;
    func_15007644();
}

/* Non-matching C placeholders for asm/nonmatchings/game_33660/func_15006234.s. */
s32 func_15006234() {
    return 0;
}
