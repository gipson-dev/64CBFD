#include <ultra64.h>
f32 func_150484A0(f32, f32);
extern f32 D_800A0838;

/* Non-matching placeholders for the text-only asm slice asm/FC410.s. */

u8 *func_151149AC(u8);
f32 func_150AD78C(f32);
f32 func_150AD780(f32);
void func_150A3444(s32, s16, s16, s16);
void func_151749A0(s32, s32);
extern f32 D_800A0830, D_800A0834;

/* Rotate the marker around its fixed origin and advance the phase counter. */
void func_150CEF60(s32 unused) {
    f32 second;
    f32 radians;
    f32 originX, originY, pointX, pointY, dx, dy;
    f32 first;
    (void)unused;
    radians = *(f32 *)(func_151149AC(4) + 8) * D_800A0830;
    first = func_150AD78C(radians);
    second = func_150AD780(radians);
    originX = -1.0f;
    originY = 44.0f;
    pointX = 76.0f;
    pointY = 241.0f;
    dx = pointX - originX;
    dy = pointY - originY;
    func_150A3444(2, (s16)(dx * second - dy * first + originX),
        (s16)(dx * first + dy * second + originY), (s16)D_800A0834);
    func_151749A0(5, 3);
}

f32 func_150CF040(s32 arg0, s32 arg1) {
    arg0 += 1;
    arg1 -= 0x2C;
    return func_150484A0(arg0, arg1) * D_800A0838;
}

void func_150CF080(u8 *arg0) {
    *(u32 *)(arg0 + 0x84) |= 0x4000;
}
