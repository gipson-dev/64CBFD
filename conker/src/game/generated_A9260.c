#include <ultra64.h>

#include "variables.h"

/* Non-matching placeholders for the text-only asm slice asm/A9260.s. */

s32 func_1507BDB0() {
    return 0;
}

s32 func_1507C22C() {
    return 0;
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_A9260/func_1507C324.s")

void func_1507C3E0(struct127 *arg0, u16 *arg1, u16 *arg2, u16 *arg3);

void func_1507C370(void) {
    struct127 *object;
    struct126 *state;
    s32 i;

    object = D_800CC2D0;
    for (i = 0; i < D_8008FD8C; i++, object++) {
        state = object->unk31C;
        if (state != NULL) {
            func_1507C3E0(object, &state->unk114, &state->unk116,
                          &state->unk118);
        }
    }
}

void func_1507C3E0(struct127 *arg0, u16 *arg1, u16 *arg2, u16 *arg3) {
}
