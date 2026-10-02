#include <ultra64.h>
#include "functions.h"

/* Non-matching placeholders for the text-only asm slice asm/121A20.s. */

typedef struct {
    u8 pad0[0x24];
    u8 flags;
} Func150F4CFCState;

typedef struct {
    u8 *owner;
    f32 value;
    s8 selector;
    u8 variant;
    u8 padA[2];
} Func150F4D5CPayload;

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

void func_150F4D5C(u8 *arg0, s8 arg1, u8 arg2, u8 arg3, s32 arg4) {
    Func150F4D5CPayload payload;
    struct260 *object;

    payload.owner = arg0;
    payload.value = 0.0f;
    payload.selector = arg1;
    payload.variant = arg2;

    object = func_15149130(0x12C, -1, 0x56, -1, 0, 0,
                           (struct37 *)sizeof(payload), arg3, arg4);
    if (object != NULL) {
        memcpy((u8 *)object + 0x28, &payload, sizeof(payload));
    }
}

s32 func_150F4DEC() {
    return 0;
}
