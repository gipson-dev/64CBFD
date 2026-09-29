#include <ultra64.h>

s32 func_15142600(s32, s32, s32, s32, f32, f32, f32, f32, f32, f32, f32, f32);

/* Non-matching placeholders for the text-only asm slice asm/E5E90.s. */

s32 func_150B89E0() {
    return 0;
}

s32 func_150B8F44() {
    return 0;
}

s32 func_150B9560() {
    return 0;
}

s32 func_150B95FC(u8 *arg0) {
    s16 value = *(s16 *)(arg0 + 0x1C);

    if (value < 0x20) {
        arg0[0x5C] = value << 3;
    }
    return 1;
}

s32 func_150B961C(u8 *arg0) {
    s16 value = *(s16 *)(arg0 + 0x1C);

    if (value < 0x40) {
        arg0[0x28] = value << 2;
    }
    return 1;
}

s32 func_150B963C() {
    return 0;
}

s32 func_150B9D14(s32 arg0, u8 *arg1) {
    func_15142600(arg0, *(s32 *) (arg1 + 0x18), *(s32 *) (arg1 + 0x1C),
                   *(s32 *) (arg1 + 0x2C), *(f32 *) (arg1 + 0x30),
                   *(f32 *) (arg1 + 0x34), *(f32 *) (arg1 + 0x38),
                   *(f32 *) (arg1 + 0x3C), *(f32 *) (arg1 + 0x40),
                   *(f32 *) (arg1 + 0x20), *(f32 *) (arg1 + 0x24),
                   *(f32 *) (arg1 + 0x28));
    return 1;
}

s32 func_150B9D8C() {
    return 0;
}
