#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/121A20.s. */

typedef struct {
    u8 pad0[0x24];
    u8 flags;
} Func150F4CFCState;

s32 func_150F4570() {
    return 0;
}

s32 func_150F48D0() {
    return 0;
}

s32 func_150F4A38() {
    return 0;
}

void func_150F4CFC(u8 *arg0, s32 arg1, u8 arg2) {
    Func150F4CFCState *state = (Func150F4CFCState *) (arg0 + 0x170);

    if (arg2 == 0x4E) {
        arg0[0x71] = 0;
        state->flags |= 5;
    } else if (arg2 == 0x4F) {
        func_1516972C(arg0);
    }
}

s32 func_150F4D5C() {
    return 0;
}

s32 func_150F4DEC() {
    return 0;
}
