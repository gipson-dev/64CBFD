#include <ultra64.h>
#include "structs.h"

/* Non-matching placeholders for the text-only asm slice asm/FF5C0.s. */

void func_150D22D4();
Gfx *func_1517F08C(Gfx *, s32, s32, s32, s32, s32);

extern u8 D_800D9900;

typedef struct {
    u8 active;
    u8 pad1[3];
    f32 phase;
    f32 threshold;
    f32 inactiveDuration;
    f32 period;
    u8 activeColor;
    u8 inactiveColor;
} PhaseCycle;

extern u8 D_800D9900;

struct260 *func_15149130(s16, s8, s8, s8, u8, u8, s32, u8, s32);
void *memcpy(void *, const void *, u32);

/* Spawn a phase cycle and copy its state, retaining the packet's original padding bytes. */
void func_150D2110(s16 lifetime, f32 activeDuration, f32 inactiveDuration,
                   u8 activeColor, u8 inactiveColor, u8 priority, s32 owner) {
    PhaseCycle cycle;
    struct260 *effect;

    D_800D9900++;
    cycle.threshold = activeDuration;
    cycle.inactiveDuration = inactiveDuration;
    cycle.period = activeDuration + inactiveDuration;
    cycle.active = 0;
    cycle.phase = 0.0f;
    cycle.activeColor = activeColor;
    cycle.inactiveColor = inactiveColor;
    effect = func_15149130(lifetime, -1, 0x2F, 2, 1, 0x26, sizeof(PhaseCycle), priority, owner);
    if (effect != NULL) {
        memcpy((u8 *)effect + 0x28, &cycle, sizeof(PhaseCycle));
    }
}

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

extern s32 D_800BE9E4;
s32 func_150ADA20(void);

typedef struct {
    u32 baseDelay;
    u32 delayRange;
    s32 timer;
    s16 baseLifetime;
    s16 lifetimeRange;
    f32 activeDuration;
    f32 inactiveDuration;
    u8 activeColor;
    u8 inactiveColor;
} PeriodicPhaseSpawnFF5C0;

/* Spawn a randomized phase cycle on expiry, then select the next delay. */
void func_150D2374(u8 *owner) {
    PeriodicPhaseSpawnFF5C0 *state = (PeriodicPhaseSpawnFF5C0 *)(owner + 0x28);
    u32 random;

    *(s32 *)(owner + 0x30) = (s32)((u32)*(s32 *)(owner + 0x30) - (u32)D_800BE9E4);
    if (*(s32 *)(owner + 0x30) < 0) {
        random = (u32)func_150ADA20();
        func_150D2110((s16)(random % (state->lifetimeRange + 1) + state->baseLifetime),
                     state->activeDuration, state->inactiveDuration,
                     state->activeColor, state->inactiveColor, owner[0xC], owner[1]);
        random = (u32)func_150ADA20();
        state->timer = (s32)(random % (state->delayRange + 1U) +
                             state->baseDelay);
    }
}
