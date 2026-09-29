#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/6C960.s. */

s32 func_1505E0C4(s32 arg0, s32 arg1, u8 *arg2, s32 arg3, s32 arg4,
                  s32 arg5, s32 arg6, f32 arg7, f32 arg8, f32 arg9,
                  f32 arg10, s32 arg11);

s32 func_1503F4B0() {
    return 0;
}

s32 func_1503F5B8(u8 *arg0, s32 arg1, s32 arg2, f32 arg3, f32 arg4,
                  s32 arg5) {
    return func_1505E0C4(0, 0, arg0, 0, arg1, arg2, arg0[0x3F5], arg3,
                         arg4, 0.0f, 0.0f, arg5);
}

s32 func_1503F62C() {
    return 0;
}

void func_1503F7B8(u8 *arg0) {
    func_100043B4(*(s32 *) (arg0 + 0x3E8), 4);
    func_100043B4(*(s32 *) (arg0 + 0x3EC), 4);
    func_10004074(arg0);
}
