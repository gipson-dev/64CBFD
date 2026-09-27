#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/EEB10.s. */

s32 func_1514C2F0(f32, f32, f32, f32, u8, s8, s16, u8, s32, f32, s32, u8);

void func_150C1660(f32 arg0, f32 arg1, f32 arg2, u8 arg3) {
    func_1514C2F0(arg0, arg1, arg2, 80.0f, 0, 3, 0x19, 2, 0, 0.0f, 0, arg3);
}

s32 func_150C16C0() {
    return 0;
}

s32 func_150C1978(u8 *arg0) {
    u8 *temp_v0 = *(u8 **) (arg0 + 0x98);
    s32 temp_v1 = *(s16 *) (arg0 + 0x1C) << 3;

    if (temp_v1 >= 0x100) {
        temp_v1 = 0xFF;
    }
    *(temp_v0 + 0x1B) = temp_v1;
    if ((temp_v1 & 0xFF) < 0) {
        return 0;
    }
    return 1;
}
