
#include <ultra64.h>

#include "functions.h"
#include "variables.h"

/* Generated placeholder declarations. */
s32 func_10002718();
/* End generated placeholder declarations. */

s32 func_10002070(s32 arg0, s32 arg1, s32 arg2) {
    return 1;
}
void func_100020D0(s32 (*arg0)(s32, s32, s32), s32 arg1, s32 arg2, s32 *arg3);

void func_10002088(s32 arg0, ...) {
    D_80035500 = 0;
    func_100020D0(func_10002070, 0, arg0, &arg0 + 1);
}

// this is a beast:
/* Non-matching C placeholders for asm/nonmatchings/init_2070/func_100020D0.s. */
void func_100020D0(s32 (*arg0)(s32, s32, s32), s32 arg1, s32 arg2, s32 *arg3) {
}

// contains a jump table
/* Non-matching C placeholders for asm/nonmatchings/init_2070/func_10002718.s. */
s32 func_10002718() {
    return 0;
}
