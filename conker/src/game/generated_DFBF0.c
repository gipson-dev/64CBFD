#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/DFBF0.s. */

s32 func_150B2740() {
    return 0;
}

s32 func_150B2EB4() {
    return 0;
}

s32 func_150B3188() {
    return 0;
}

/* Reset motion above the threshold; otherwise scale its six components. */
s32 func_150B36AC(u8 *record, s32 unused1, s32 unused2, s32 unused3, f32 offset, void *unused6) {
    f32 vertical = *(f32 *)(record + 0x48);
    f32 scale;
    (void)unused1;
    (void)unused2;
    (void)unused3;
    (void)unused6;

    *(f32 *)(record + 0x3C) = *(f32 *)(record + 0x10) + offset;
    if (*(f32 *)(record + 0x170) < vertical) {
        *(u32 *)(record + 0x60) = *(u32 *)(record + 0x60) & ~7u;
        *(u32 *)(record + 0x60) = *(u32 *)(record + 0x60) & ~8u;
        *(u32 *)(record + 0x60) = *(u32 *)(record + 0x60) & ~0x40u;
        *(u32 *)(record + 0x60) = *(u32 *)(record + 0x60) & ~0x20u;
        *(f32 *)(record + 0x44) = 0.0f;
        *(f32 *)(record + 0x48) = 0.0f;
        *(f32 *)(record + 0x4C) = 0.0f;
        if (*(s16 *)(record + 0x64) >= 33) {
            *(s16 *)(record + 0x64) = 32;
        }
    } else {
        scale = *(f32 *)(record + 0x14);
        *(f32 *)(record + 0x44) *= scale;
        *(f32 *)(record + 0x48) = -vertical * scale;
        *(f32 *)(record + 0x4C) *= scale;
        *(f32 *)(record + 0x50) *= scale;
        *(f32 *)(record + 0x54) *= scale;
        *(f32 *)(record + 0x58) *= scale;
    }
    return 1;
}

s32 func_150B378C(u8 *arg0) {
    u8 *temp_v0 = *(u8 **) (arg0 + 0x98);
    s32 temp_v1 = *(s16 *) (arg0 + 0x1C) << 4;

    if (temp_v1 >= 0x100) {
        temp_v1 = 0xFF;
    }
    if (temp_v1 < *(temp_v0 + 0x1B)) {
        *(temp_v0 + 0x1B) = temp_v1;
    }
    return 1;
}

s32 func_150B37C8() {
    return 0;
}
