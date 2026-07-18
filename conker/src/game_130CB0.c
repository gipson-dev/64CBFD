#include <ultra64.h>

#include "functions.h"
#include "variables.h"

/* Generated placeholder declarations. */
s32 func_15103910();
s32 func_15103AA0();
s32 func_15103C14();
/* End generated placeholder declarations. */

void func_15103800(void) {
    bzero(D_800D9AB0, 8); // bzero
}

void func_15103828(void) {
    u16 temp_v1;
    s32 i;

    for (i = 0; i < 4; i++)
    {
        if (D_800D9AB0[i]) {
            if (D_800D9AB0[i] > D_800BE9E4)
            {
                D_800D9AB0[i] -= D_800BE9E4;
            } else {
              D_800D9AB0[i] = 0;
            }
        }
    }
}

// need to figure out the structs
/* Non-matching C placeholders for asm/nonmatchings/game_130CB0/func_15103910.s. */
s32 func_15103910() {
    return 0;
}
/* Non-matching C placeholders for asm/nonmatchings/game_130CB0/func_15103AA0.s. */
s32 func_15103AA0() {
    return 0;
}
/* Non-matching C placeholders for asm/nonmatchings/game_130CB0/func_15103C14.s. */
s32 func_15103C14() {
    return 0;
}
