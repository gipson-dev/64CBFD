#include <ultra64.h>

extern s32 D_800BE9E4;
void func_1516F864(u8 *);
s32 func_1510F8D8(s16, s16, s16, s32);
void func_1516F94C(u8 *, s32);


/* Non-matching placeholders for the text-only asm slice asm/197120.s. */

s32 func_15169C70() {
    return 0;
}

s32 func_1516A3F4() {
    return 0;
}

s32 func_150ADA20(void);
void func_15171D4C(f32, f32, f32, s16, u16, u8, f32, s32, s32, s32, s32, s32, u8, s32);

/* Submit the randomized effect once the signed record value reaches 0x300. */
void func_1516A538(u8 *record) {
    u32 variant;
    s32 scale;
    u32 angle;

    if (*(s16 *)(record + 0x14) >= 0x300) {
        variant = (u32)func_150ADA20() % 3u;
        scale = record[0x25];
        angle = (u32)func_150ADA20() % 360u;
        func_15171D4C((f32)*(s16 *)(record + 0x18),
                     (f32)(*(s16 *)(record + 0x1A) - 10),
                     (f32)*(s16 *)(record + 0x1C),
                     100, 0, variant + 32,
                     (f32)angle,
                     0, scale * 25 / 255 + 25, 0, 256, 0,
                     record[0x0C], record[1]);
    }
}

/* Advance the packed record fade, motion and contact response. */
s32 func_1516A648(u8 *record) {
    s32 alpha = record[0x1F];
    s32 state = record[0x24];
    s32 level;
    if (state != 0) {
        if (alpha != 255) {
            alpha = (s32)((u32)alpha + ((u32)D_800BE9E4 << 4));
            if (alpha >= 256) alpha = 255;
            record[0x1F] = alpha;
            state = ((volatile u8 *)record)[0x24];
        }
    } else {
        if (alpha != 0) {
            alpha = (s32)((u32)alpha - ((u32)D_800BE9E4 << 2));
            if (alpha < 0) alpha = 0;
            record[0x1F] = alpha;
            state = ((volatile u8 *)record)[0x24];
        }
    }
    if (state == 0 && alpha == 0) return 1;
    *(s16 *)(record + 0x18) -= 300;
    func_1516F864(record);
    level = (s32)((u32)func_1510F8D8(*(s16 *)(record + 0x0E), *(s16 *)(record + 0x10), *(s16 *)(record + 0x12), 0) + 10u);
    record[0x2C] = level >> 8;
    record[0x2D] = level;
    if (*(s16 *)(record + 0x10) < level) {
        *(s16 *)(record + 0x10) = level;
        *(s16 *)(record + 0x18) = (s32)((f32)*(s16 *)(record + 0x18) * -0.5f);
        func_1516F94C(record, 230);
    }
    return 0;
}
