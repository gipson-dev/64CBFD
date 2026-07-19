#include <ultra64.h>
f32 func_150484A0(f32, f32);
extern f32 D_800A0838;

/* Non-matching placeholders for the text-only asm slice asm/FC410.s. */

s32 func_150CEF60() {
    return 0;
}

f32 func_150CF040(s32 arg0, s32 arg1) {
    arg0 += 1;
    arg1 -= 0x2C;
    return func_150484A0(arg0, arg1) * D_800A0838;
}

void func_150CF080(u8 *arg0) {
    *(u32 *)(arg0 + 0x84) |= 0x4000;
}
