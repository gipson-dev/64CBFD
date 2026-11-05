#include <ultra64.h>

extern s32 D_800BE9E4;
extern f32 D_800A26B0, D_800A26B4, D_800A26B8;
f32 cosf(f32);
s32 func_15114D24(u8 *, s32, s32, s16, s16, s32);

/* Non-matching placeholders for the text-only asm slice asm/137ED0.s. */

s32 func_15179008();

void func_1510AA20(s32 arg0) {
    func_15179008(0);
}

s32 func_1510AA44() {
    return 0;
}

/* Advance cosine motion and signal the alternating half/full-period crossings. */
void func_1510ADD8(u8 *state) {
    f32 value;
    f32 previous;

    *(f32 *)(state + 0x80) += D_800A26B0 * (f32)D_800BE9E4 / 60.0f;
    value = cosf(*(f32 *)(state + 0x80)) * 10.0f;
    previous = *(f32 *)state - value;
    *(f32 *)state = value;
    *(f32 *)(state + 0x60) = previous;
    if (*(s32 *)(state + 0x7C) == 0) {
        if (D_800A26B4 <= *(f32 *)(state + 0x80)) {
            *(s32 *)(state + 0x7C) = 1;
            func_15114D24(state, 0x4CA, 12000, 200, 1000, 4);
        }
    } else if (D_800A26B8 <= *(f32 *)(state + 0x80)) {
        previous = *(f32 *)(state + 0x80) - D_800A26B8;
        *(s32 *)(state + 0x7C) = 0;
        *(f32 *)(state + 0x80) = previous;
        func_15114D24(state, 0x4CB, 12000, 200, 1000, 4);
    }
}

s32 func_1510AEE0() {
    return 0;
}
