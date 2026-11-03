#include <ultra64.h>
typedef struct {
    f32 oscillation;
    f32 amplitude;
    f32 phase;
    f32 phaseRate;
    f32 targetAmplitude;
    f32 targetPhaseRate;
    f32 transitionTime;
    f32 amplitudeVelocity;
    f32 phaseRateVelocity;
} TimedOscillationTransition151B9214;
extern f32 D_800BE9A4;
extern f32 D_800AA564;
f32 func_15144B68(f32);
f32 sinf(f32);

extern f32 D_800AA570;
extern f32 D_800AA56C;

/* Non-matching placeholders for the text-only asm slice asm/1E6260.s. */

s32 func_151B8DB0() {
    return 0;
}

/* Advance the oscillation and transition its amplitude and phase rate. */
s32 func_151B9214(u8 *owner) {
    TimedOscillationTransition151B9214 *state =
        (TimedOscillationTransition151B9214 *)(owner + 0x170);
    f32 transitionScale;

    state->phase += state->phaseRate * D_800BE9A4;
    state->phase = func_15144B68(state->phase);
    state->oscillation = sinf(state->phase) * state->amplitude;
    if (0.0f < state->transitionTime) {
        state->transitionTime -= D_800BE9A4;
        state->phaseRate += state->phaseRateVelocity * D_800BE9A4;
        state->amplitude += state->amplitudeVelocity * D_800BE9A4;
    } else {
        transitionScale = D_800AA564;
        state->phaseRate +=
            (state->targetPhaseRate - state->phaseRate) * transitionScale;
        state->amplitude +=
            (state->targetAmplitude - state->amplitude) * transitionScale;
    }
    return 1;
}

s32 func_151B9310() {
    return 0;
}

s32 func_151B9408() {
    return 0;
}

void func_151B9660(u8 *arg0) {
    *(f32 *) (arg0 + 0x188) = 5.0f;
    *(f32 *) (arg0 + 0x18C) = D_800AA56C;
    *(f32 *) (arg0 + 0x190) = D_800AA570;
}
