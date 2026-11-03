#include <ultra64.h>

typedef struct {
    u8 retained00[0x48];
    f32 xPosition;
    f32 yPosition;
    f32 zPosition;
    u8 retained54[0xAC];
    f32 xRotation;
    f32 yRotation;
    f32 zRotation;
    f32 uniformScale;
} UniformMatrixState1518A914;

void func_150A8050(f32 matrix[4][4], f32, f32, f32);

/* Recovered function and remaining placeholders for asm/1B7870.s. */

s32 func_1518A3C0() {
    return 0;
}

s32 func_1518A5F4() {
    return 0;
}

/* Build and submit the state's translated, uniformly scaled matrix. */
s32 func_1518A914(Mtx *output, UniformMatrixState1518A914 *state) {
    f32 *rotation;
    f32 matrix[4][4];

    rotation = &state->xRotation;
    func_150A8050(matrix, rotation[0], rotation[1], rotation[2]);
    matrix[3][0] = state->xPosition;
    matrix[3][1] = state->yPosition;
    matrix[3][2] = state->zPosition;
    matrix[0][0] *= rotation[3];
    matrix[0][1] *= rotation[3];
    matrix[0][2] *= rotation[3];
    matrix[1][0] *= rotation[3];
    matrix[1][1] *= rotation[3];
    matrix[1][2] *= rotation[3];
    matrix[2][0] *= rotation[3];
    matrix[2][1] *= rotation[3];
    matrix[2][2] *= rotation[3];
    guMtxF2L(matrix, output);
    return 1;
}
