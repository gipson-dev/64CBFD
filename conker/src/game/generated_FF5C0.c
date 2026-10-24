#include <ultra64.h>
#include "structs.h"

/* Non-matching placeholders for the text-only asm slice asm/FF5C0.s. */

void func_150D22D4();
Gfx *func_1517F08C(Gfx *, s32, s32, s32, s32, s32);

extern u8 D_800D9900;

s32 func_150D2110() {
    return 0;
}

/* The callback receives the common actor header followed by this local state. */
typedef struct {
    u8 active;
    u8 pad1[3];
    f32 phase;
    f32 threshold;
    f32 unused;
    f32 period;
} PhaseCycle;

extern f32 D_800BE9A4;
void func_1515D4D4(s32 red, s32 green, s32 blue, u8 priority);

/* Advance the phase and enable the white override during its threshold window. */
void func_150D21CC(struct260 *owner) {
    PhaseCycle *cycle = (PhaseCycle *)((u8 *)owner + 0x28);

    cycle->phase += D_800BE9A4;
    while (cycle->phase > cycle->period) {
        cycle->phase -= cycle->period;
    }
    if (cycle->phase <= cycle->threshold) {
        cycle->active = 1;
        func_1515D4D4(255, 255, 255, 255);
    } else {
        cycle->active = 0;
    }
}

s32 func_150D227C(s32 arg0) {
    func_150D22D4(arg0);
    func_1514933C(arg0);
}

s32 func_150D22A8(s32 arg0) {
    func_150D22D4(arg0);
    func_15149368(arg0);
}

void func_150D22D4(s32 arg0) {
    D_800D9900--;
}

/* Note 528: mode-selected color arguments and updated-handle return. */
s32 func_150D22F4(s32 arg0, u8 *arg1, s16 arg2) {
    if (arg1[0x28] == 1) {
        arg0 = (s32)func_1517F08C((Gfx *)arg0, arg1[0x3C], 0xFF, 0xFF, 0xFF, arg2);
    } else {
        arg0 = (s32)func_1517F08C((Gfx *)arg0, arg1[0x3D], 0, 0, 0, arg2);
    }
    return arg0;
}

s32 func_150D2374() {
    return 0;
}
