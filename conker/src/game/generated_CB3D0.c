#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/CB3D0.s. */

extern s32 D_800D3840;
extern f32 D_800D2FC0[];
extern f32 D_800D2FD8[];
extern u8 D_800D2FEC[];

void func_1509DF20(s32 arg0, s32 *arg1) {
    if ((arg1[1] == 1) && (D_800D3840 == 3)) {
        D_800D2FC0[arg1[2]] = arg1[3] * 0.0000152587890625f;
        D_800D2FD8[arg1[2]] = arg1[3] * 0.0000152587890625f;
        D_800D2FEC[arg1[2]] = 1;
    }
}

void func_1509DFB4(s32 arg0, s32 arg1) {
}

s32 func_1509DFC4() {
    return 0;
}

s32 func_1509E3DC() {
    return 0;
}
