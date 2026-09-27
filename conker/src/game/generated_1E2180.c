#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/1E2180.s. */

s32 func_151B4CD0() {
    return 0;
}

s32 func_151B4EA4(f32 *, f32, f32, f32, u8, u8);

void func_151B4E4C(f32 arg0, f32 arg1, f32 arg2, f32 arg3, f32 arg4,
                   f32 arg5, u8 *arg6) {
    f32 position[3];

    position[0] = arg0;
    position[1] = arg1;
    position[2] = arg2;
    func_151B4EA4(position, arg3, arg4, arg5, arg6[0x58], arg6[0xC]);
}

s32 func_151B4EA4(f32 *arg0, f32 arg1, f32 arg2, f32 arg3, u8 arg4, u8 arg5) {
    return 0;
}

/* Note 454: original carried actor attachment/effect. */
#pragma GLOBAL_ASM("asm/nonmatchings/generated_1E2180/func_151B4FE0.s")

s32 func_151B50F4(f32 *, f32, f32, f32, u8);

void func_151B50A4(f32 arg0, f32 arg1, f32 arg2, f32 arg3, f32 arg4,
                   f32 arg5, u8 *arg6) {
    f32 position[3];

    position[0] = arg0;
    position[1] = arg1;
    position[2] = arg2;
    func_151B50F4(position, arg3, arg4, arg5, arg6[0xC]);
}

s32 func_151B50F4(f32 *arg0, f32 arg1, f32 arg2, f32 arg3, u8 arg4) {
    return 0;
}
