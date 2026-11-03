#include <ultra64.h>
typedef struct {
    u8 retained00[0x18];
    f32 horizontalScale;
    f32 verticalScale;
    u8 retained20[0x18];
    f32 xPosition;
    f32 yPosition;
    f32 zPosition;
    u8 retained44[0x12C];
    f32 zRotation;
} AnisotropicMatrixState151B9310;
typedef struct {
    u32 retained;
    f32 values[4][4];
} MatrixWorkspace151B9310;
void func_150A8050(f32 matrix[4][4], f32, f32, f32);

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

/* Build and submit the state's translated, anisotropically scaled matrix. */
s32 func_151B9310(Mtx *output, AnisotropicMatrixState151B9310 *state) {
    MatrixWorkspace151B9310 workspace;

    func_150A8050(workspace.values, 0.0f, 0.0f, state->zRotation);
    workspace.values[3][0] = state->xPosition;
    workspace.values[3][1] = state->yPosition;
    workspace.values[3][2] = state->zPosition;
    workspace.values[0][0] *= state->horizontalScale;
    workspace.values[0][1] *= state->horizontalScale;
    workspace.values[0][2] *= state->horizontalScale;
    workspace.values[1][0] *= state->verticalScale;
    workspace.values[1][1] *= state->verticalScale;
    workspace.values[1][2] *= state->verticalScale;
    workspace.values[2][0] *= state->horizontalScale;
    workspace.values[2][1] *= state->horizontalScale;
    workspace.values[2][2] *= state->horizontalScale;
    guMtxF2L(workspace.values, output);
    return 1;
}

s32 func_151B9408() {
    return 0;
}

void func_151B9660(u8 *arg0) {
    *(f32 *) (arg0 + 0x188) = 5.0f;
    *(f32 *) (arg0 + 0x18C) = D_800AA56C;
    *(f32 *) (arg0 + 0x190) = D_800AA570;
}
