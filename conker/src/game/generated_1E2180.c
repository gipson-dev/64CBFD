#include <ultra64.h>
extern f32 D_800AA3D4,D_800AA3D8,D_800AA3DC;
s32 func_150ADA20(void);
f32 func_150ADA68(void);
void *func_151D9014(f32 *,f32 *,u8,f32,s16,u8,f32,u8,f32,f32,u8,s32,u8,u8,u8,s32);

/* Non-matching placeholders for the text-only asm slice asm/1E2180.s. */

s32 func_151B4CD0() {
    return 0;
}

void func_151B4EA4(f32 *, f32, f32, f32, u8, u8);

void func_151B4E4C(f32 arg0, f32 arg1, f32 arg2, f32 arg3, f32 arg4,
                   f32 arg5, u8 *arg6) {
    f32 position[3];

    position[0] = arg0;
    position[1] = arg1;
    position[2] = arg2;
    func_151B4EA4(position, arg3, arg4, arg5, arg6[0x58], arg6[0xC]);
}

/* Spawn an effect from a reversed direction and five ordered random draws. */
void func_151B4EA4(f32 *position, f32 x, f32 y, f32 z, u8 selector, u8 mode) {
    f32 size;
    f32 velocity[3];
    f32 scale = D_800AA3D4;
    f32 second;
    u32 alpha, duration;
    f32 first;
    u32 variant;
    velocity[0] = -x * scale;
    velocity[1] = -y * scale;
    velocity[2] = -z * scale;
    first = func_150ADA68();
    duration = (u32)func_150ADA20();
    alpha = (u32)func_150ADA20();
    second = func_150ADA68();
    variant = (u32)func_150ADA20();
    size = D_800AA3D8;
    func_151D9014(position, velocity, selector, first * D_800AA3DC + -1.0f,
                        duration % 31 + 20, alpha % 101 + 155,
                        second * 152.0f + 109.0f, variant & 1,
                        size, size, 0, 0, 1, 0, mode, 1);
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
