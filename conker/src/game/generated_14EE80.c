#include <ultra64.h>
void func_15049688(f32 *, f32, f32 *, f32, f32, f32);
extern f32 D_800A3430;

/* Non-matching placeholders for the text-only asm slice asm/14EE80.s. */

s32 func_151219D0() {
    return 0;
}

void func_15121C00(u8 *arg0, f32 arg1, f32 arg2, f32 arg3, f32 arg4) {
    func_15049688((f32 *) (arg0 + 0x37C), arg1, (f32 *) (arg0 + 0x8C0), arg3, arg4,
                  *(f32 *) (arg0 + 0x7B4));
    *(f32 *) (arg0 + 0x39C) = *(f32 *) (arg0 + 0x37C) * D_800A3430;
}

void func_15121C64(s32 arg0, s32 arg1, s32 arg2, s32 arg3) {
}
