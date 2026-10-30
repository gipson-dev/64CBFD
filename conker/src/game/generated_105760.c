#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/105760.s. */

void func_150D82B0(s32 arg0) {
}

s32 func_150D82BC() {
    return 0;
}

s32 func_150D83D8() {
    return 0;
}

u8 *func_150D8590(u16 *arg0, s32 arg1) {
    arg0[0] = 0x42;
    arg0[1] = 0;
    return (u8 *)(arg0 + 2);
}

s32 func_150D85AC() {
    return 0;
}

s32 func_150D88AC(u8 *arg0) {
    if (*(u8 *) (*(u8 **) (arg0 + 0x18) + 0x6F) != 0) {
        *(u8 *) (*(u8 **) (arg0 + 0x14) + 9) = 0;
    } else {
        *(u8 *) (*(u8 **) (arg0 + 0x14) + 9) = 1;
    }
    return 1;
}

s32 func_150D88E0() {
    return 0;
}

s32 func_150D8A20(s32 arg0, s32 arg1) {
    return 8;
}

extern f32 D_800A0B30;
extern f32 D_800A0B34;
s32 func_151875E0(f32, f32, f32, s32, s32, s32, f32, f32);
s32 func_15165F80(s32, s32, s32, s32, s32, s32, s32, u8, s32);

/* Use the callback selector byte to emit both coordinate effects. */
/* Keep the complete three-word callback ABI, including the unused third word. */
void func_150D8A34(u8 *owner, s32 selector, s32 unused) {
    f32 position[3];

    if (*(s32 *)(owner + 0x1D4) != 0) {
        func_150D88E0(position, owner, (u8)selector);
        func_151875E0(position[0], position[1], position[2], 30, 15, 7,
                     D_800A0B30, D_800A0B34);
        func_15165F80(-1, (s32)position[0],
                     (s32)(*(f32 *)(owner + 0x180) + 4.0f),
                     (s32)position[2], 4, 50, 0, 255, 0);
    }
}
