#include <ultra64.h>

void func_15142600(Mtx *output, f32 row0, f32 row1, f32 cx, f32 cy, f32 cz,
    f32 sx, f32 sy, f32 sz, f32 ex, f32 ey, f32 ez);

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

s32 func_150B9D14(Mtx *output, u8 *source) {
    func_15142600(output,
                  *(f32 *)(source + 0x18),
                  *(f32 *)(source + 0x1C),
                  *(f32 *)(source + 0x2C),
                  *(f32 *)(source + 0x30),
                  *(f32 *)(source + 0x34),
                  *(f32 *)(source + 0x38),
                  *(f32 *)(source + 0x3C),
                  *(f32 *)(source + 0x40),
                  *(f32 *)(source + 0x20),
                  *(f32 *)(source + 0x24),
                  *(f32 *)(source + 0x28));
    return 1;
}

s32 func_150B9D8C() {
    return 0;
}
