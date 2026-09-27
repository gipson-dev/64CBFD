#include <ultra64.h>

extern f32 D_800A8CD8;

/* Non-matching placeholders for the text-only asm slice asm/1CBE20.s. */

s32 func_1519E970() {
    return 0;
}

s32 func_1519EA04() {
    return 0;
}

s32 func_1519EA78() {
    return 0;
}

s32 func_1519EB8C() {
    return 0;
}

s32 func_1519ED24(u8 *arg0) {
    f32 scale = D_800A8CD8;
    u8 *source = *(u8 **)(arg0 + 0x170);

    *(f32 *)(arg0 + 0x18) = *(f32 *)(source + 0x18) * scale;
    *(f32 *)(arg0 + 0x1C) = *(f32 *)(source + 0x1C) * scale;
    *(f32 *)(arg0 + 0x20) = *(f32 *)(source + 0x0C);
    *(f32 *)(arg0 + 0x24) = *(f32 *)(source + 0x10);
    *(f32 *)(arg0 + 0x28) = *(f32 *)(source + 0x14);
    *(f32 *)(arg0 + 0x38) = *(f32 *)(source + 0x00);
    *(f32 *)(arg0 + 0x3C) = *(f32 *)(source + 0x04);
    *(f32 *)(arg0 + 0x40) = *(f32 *)(source + 0x08);
    return 1;
}

s32 func_1519ED84() {
    return 0;
}

s32 func_1519EF04(u8 *arg0) {
    u8 *source = *(u8 **)(arg0 + 0x110);

    *(f32 *)(arg0 + 0x2C) = *(f32 *)(source + 0x18) * 10.0f;
    *(f32 *)(arg0 + 0x30) = *(f32 *)(source + 0x1C) * 10.0f;
    *(f32 *)(arg0 + 0x40) = *(f32 *)(source + 0x0C);
    *(f32 *)(arg0 + 0x44) = *(f32 *)(source + 0x10);
    *(f32 *)(arg0 + 0x48) = *(f32 *)(source + 0x14);
    *(f32 *)(arg0 + 0x34) = *(f32 *)(source + 0x00);
    *(f32 *)(arg0 + 0x38) = *(f32 *)(source + 0x04);
    *(f32 *)(arg0 + 0x3C) = *(f32 *)(source + 0x08);
    return 1;
}
