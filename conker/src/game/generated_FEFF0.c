#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/FEFF0.s. */

extern f32 D_800A08E0;
extern u8 D_800DCD20[];

s32 func_1509BE40();
void func_151467A4(f32 *, f32, f32 *, f32, f32, f32, f32, f32 *);
void func_1515D4D4(s32, s32, s32, s32);

void func_150D1B40(u8 *arg0) {
    f32 *color = (f32 *)(arg0 + 0x28);

    func_151467A4((f32 *)(arg0 + 0x30), 10.0f,
                  (f32 *)(arg0 + 0x2C), 86.0f, 170.0f, 255.0f,
                  D_800A08E0, color);
    func_1515D4D4(*color, D_800DCD20[1], D_800DCD20[2], 0);
}

void func_150D1BD0(u8 *arg0) {
    if (func_1509BE40(1, 0x402C, 6, 0x2000) != 0) {
        *(u32 *) (arg0 + 0x84) |= 0x10;
    } else {
        *(u32 *) (arg0 + 0x84) &= ~0x10;
    }
}
