#include <ultra64.h>
#include "structs.h"

void func_151C329C(struct17 *arg0, s32 arg1, s32 arg2);
void func_150A8050(f32 mtx[4][4], f32 arg1, f32 arg2, f32 arg3);
extern u8 D_800BE9C0;

/* Non-matching placeholders for the text-only asm slice asm/11F780.s. */

s32 func_150F22D0() {
    return 0;
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

s32 func_150F23E0() {
    return 0;
}

s32 func_150F2480() {
    return 0;
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

s32 func_150F25A0() {
    return 0;
}

s32 func_150F26A0() {
    return 0;
}

s32 func_150F2994() {
    return 0;
}
