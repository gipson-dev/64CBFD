#include <ultra64.h>
extern f32 D_800BE9A4;

/* Non-matching placeholders for the text-only asm slice asm/1104D0.s. */

s32 func_150E3020() {
    return 0;
}

s32 func_150E3208() {
    return 0;
}

s32 func_150E32D0() {
    return 0;
}

s32 func_150E3340() {
    return 0;
}

s32 func_150E33CC(s32 arg0, s32 arg1, s32 *arg2, s32 arg3) {
    s32 temp_v0 = *arg2;

    if (temp_v0 == 0) {
        return 1;
    }
    func_1000E7A0(2, temp_v0);
    return 0;
}

s32 func_150E3414() {
    return 0;
}

s32 func_150E3514() {
    return 0;
}

s32 func_150E35DC() {
    return 0;
}

s32 func_150E36BC() {
    return 0;
}

s32 func_150E3738() {
    return 0;
}

s32 func_150E4010() {
    return 0;
}

s32 func_150E411C() {
    return 0;
}

s32 func_150E4174(u8 *arg0) {
    *(f32 *) (arg0 + 0x2C) = *(f32 *) (arg0 + 0x4C) * D_800BE9A4 + *(f32 *) (arg0 + 0x2C);
    *(f32 *) (arg0 + 0x30) = *(f32 *) (arg0 + 0x54) * D_800BE9A4 + *(f32 *) (arg0 + 0x30);
    return 1;
}
