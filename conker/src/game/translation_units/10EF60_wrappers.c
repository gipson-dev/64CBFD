#include <ultra64.h>

/* Isolate the recovered caller ABI from the factory placeholder definition. */
void func_150E1AB0(s32 arg0, f32 arg1, f32 arg2, f32 arg3, f32 arg4,
    f32 arg5, f32 arg6, f32 arg7, f32 arg8, f32 arg9, f32 arg10,
    s16 arg11, u16 arg12, s8 arg13, s16 arg14, s16 arg15, void *arg16,
    u8 arg17, u8 arg18, s32 arg19, u8 arg20, u8 arg21,
    f32 arg22, f32 arg23, f32 arg24, f32 arg25, f32 arg26, f32 arg27);

/* Forward the preset inputs to the 0x27 factory with its 40/400 defaults. */
void func_150E2DB4(void *arg0, u8 arg1, s16 arg2, s32 arg3, f32 arg4, f32 arg5, f32 arg6, f32 arg7, f32 arg8, f32 arg9, s16 arg10, s16 arg11, u16 arg12, u8 arg13) {
    func_150E1AB0(0, 0.0f, 0.0f, 0.0f, 0.0f, 0.0f, 0.0f, 0.0f, 0.0f, 40.0f, 400.0f, (s16) (s32) arg12, 0x27U, 1, (s16) (s32) arg10, (s16) (s32) arg11, arg0, (u8) (s32) arg1, (u8) (s32) arg2, arg3, 0U, (u8) (s32) arg13, arg4, arg5, arg6, arg7, arg8, arg9);
}

/* Forward the configurable ranges and scalar to the 0x27 factory. */
void func_150E2EA4(void *arg0, u8 arg1, s16 arg2, s32 arg3, f32 arg4, f32 arg5, f32 arg6, f32 arg7, f32 arg8, f32 arg9, s16 arg10, s16 arg11, u16 arg12, f32 arg13, f32 arg14, u8 arg15, f32 arg16) {
    func_150E1AB0(0, 0.0f, 0.0f, 0.0f, 0.0f, 0.0f, 0.0f, arg16, 0.0f, arg13, arg14, (s16) (s32) arg12, 0x27U, 1, (s16) (s32) arg10, (s16) (s32) arg11, arg0, (u8) (s32) arg1, (u8) (s32) arg2, arg3, 0U, (u8) (s32) arg15, arg4, arg5, arg6, arg7, arg8, arg9);
}
