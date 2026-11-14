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

typedef struct { f32 timer, x, y, z, phase, rate, width, depth, scale; } TimedMotion150F48D0;
extern f32 D_800BE9A4;
void func_1514373C(f32, f32, f32 *, f32 *);
/* Advance the timed motion and return its embedded state address while active. */
s32 func_150F48D0(f32 *actor) {
    TimedMotion150F48D0 *state = (TimedMotion150F48D0 *)((u8 *)actor + 0x170);
    f32 b, a;
    state->timer -= D_800BE9A4;
    if (state->timer <= 0.0f) {
        return 0;
    }
    func_1514373C(state->phase, state->scale, &a, &b);
    state->phase += state->rate * D_800BE9A4;
    state->x += actor[0x44 / 4] * D_800BE9A4;
    state->y += actor[0x48 / 4] * D_800BE9A4;
    state->z += actor[0x4C / 4] * D_800BE9A4;
    actor[0x38 / 4] = state->x + a * state->width;
    actor[0x3C / 4] = state->y + b;
    actor[0x40 / 4] = state->z - a * state->depth;
    actor[0x20 / 4] += actor[0x50 / 4] * D_800BE9A4;
    actor[0x24 / 4] += actor[0x54 / 4] * D_800BE9A4;
    actor[0x28 / 4] += actor[0x58 / 4] * D_800BE9A4;
    return (s32)state;
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
