#include <ultra64.h>
extern f32 D_800BE9A4;
f32 func_15144B68(f32);
#include "structs.h"

void func_151C329C(struct17 *arg0, s32 arg1, s32 arg2);
void func_150A8050(f32 mtx[4][4], f32 arg1, f32 arg2, f32 arg3);
extern u8 D_800BE9C0;
void func_150A7960(f32 matrix[4][4], f32 x, f32 y, f32 z, f32 *outX, f32 *outY, f32 *outZ);

extern f32 D_800A1920[3];
void func_15143134(f32 *point, f32 *output, u8 *matrix);


/* Non-matching placeholders for the text-only asm slice asm/11F780.s. */

/* Transform the selector's indexed actor record into the output point. */
s32 func_150F22D0(struct17 *output, u8 *actor, u8 selector) {
    s32 index;

    switch (selector) {
        case 3: index = 0x29; break;
        case 4: index = 0x2D; break;
        case 5: index = 0x31; break;
        case 6: index = 0x35; break;
        case 7: index = 0x39; break;
        case 8: index = 0x3D; break;
        default: return 0;
    }
    func_15143134(D_800A1920, (f32 *)output,
                 *(u8 **)(actor + 0x1D4) + (index << 6));
    return 1;
}

s32 func_150F237C(s32 arg0, s32 arg1) {
    return 0xE;
}

void func_150F2390(u8 *arg0, s32 arg1, s32 arg2) {
    struct17 value;

    if (*(s32 *)(arg0 + 0x1D4) != 0) {
        func_150F22D0(&value, arg0, (u8)arg1);
        func_151C329C(&value, 0xFF, 0);
    }
}

/* Update actor offsets from fixed sine state, then advance both phases. */
s32 func_150F23E0(u8 *actor) {
    f32 *state = (f32 *)(actor + 0x170);

    *(f32 *)(actor + 0x20) = state[4] * sinf(state[0]);
    *(f32 *)(actor + 0x28) = state[5] * sinf(state[1]);
    state[0] = func_15144B68(state[2] * D_800BE9A4 + state[0]);
    state[1] = func_15144B68(state[3] * D_800BE9A4 + state[1]);
    return 1;
}

/* Update sine outputs, then advance and wrap both phases. */
s32 func_150F2480(u8 *actor) {
    f32 *state;

    state = (f32 *)(actor + *(s32 *)(actor + 0x50) + 0xF8);
    state[9] = state[4] * sinf(state[0]);
    state[10] = state[5] * sinf(state[1]);
    state[0] = func_15144B68(state[2] * D_800BE9A4 + state[0]);
    state[1] = func_15144B68(state[3] * D_800BE9A4 + state[1]);
    return 1;
}

s32 func_150F2518(u8 *arg0, s32 arg1) {
    f32 matrix[4][4];
    u8 *entry;

    entry = arg0 + *(s32 *)(arg0 + 0x50) + 0xF8;
    func_150A8050(matrix, *(f32 *)(entry + 0x24), 0.0f,
                   *(f32 *)(entry + 0x28));
    matrix[3][0] = *(f32 *)(entry + 0x18);
    matrix[3][1] = *(f32 *)(entry + 0x1C);
    matrix[3][2] = *(f32 *)(entry + 0x20);
    guMtxF2L(matrix, (Mtx *)(arg0 + (D_800BE9C0 << 6) + 0x78));
    return 1;
}

/* Transform the owner-relative point into the destination's signed halfwords. */
s32 func_150F25A0(u8 *record) {
    u8 **owner = (u8 **)(record + 0x18);
    f32 point[3];
    f32 matrix[4][4];

    func_150A8050(matrix, *(f32 *)(*owner + 0x20) * 3.0f, 0.0f,
                 *(f32 *)(*owner + 0x28) * 3.0f);
    matrix[3][0] = *(f32 *)(*owner + 0x38);
    matrix[3][1] = *(f32 *)(*owner + 0x3C);
    matrix[3][2] = *(f32 *)(*owner + 0x40);
    func_150A7960(matrix, 0.0f, -495.0f, 0.0f, &point[0], &point[1], &point[2]);
    *(s16 *)(*(u8 **)(record + 0x14) + 0x0E) = (s32)point[0];
    *(s16 *)(*(u8 **)(record + 0x14) + 0x10) = (s32)point[1];
    *(s16 *)(*(u8 **)(record + 0x14) + 0x12) = (s32)point[2];
    return 1;
}

s32 func_150F26A0() {
    return 0;
}

s32 func_150F2994() {
    return 0;
}
