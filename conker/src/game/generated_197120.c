#include <ultra64.h>

extern s32 D_800BE9E4;
void func_1516F864(u8 *);
s32 func_1510F8D8(s16, s16, s16, s32);
void func_1516F94C(u8 *, s32);


/* Non-matching placeholders for the text-only asm slice asm/197120.s. */

s32 func_15169C70() {
    return 0;
}

typedef struct {
    u32 tag;
    s16 zero, extent, x, y, z, size1, size2;
    u8 flag, padding, type, alpha;
} ContactEffect1516A3F4;
extern u32 D_8008CADC;
extern f32 D_800A6CC8;
void func_1510F800(s32);
void func_15167AD8(void *, u8, s32);

/* Refresh the floor height and emit the contact effect, or damp motion. */
void func_1516A3F4(u8 *record) {
    s32 height;
    s32 threshold;
    s32 value;
    ContactEffect1516A3F4 effect;
    u8 alpha;
    threshold = *(s16 *)(record + 0x2A) + *(s16 *)(record + 0x22);
    height = *(s32 *)(record + 0x14);
    if (height >= threshold) {
        func_1510F800(0);
        height = func_1510F8D8(*(s16 *)(record + 0x20), *(s16 *)(record + 0x22), *(s16 *)(record + 0x24), 0);
        *(s32 *)(record + 0x14) = height;
    }
    if (height >= threshold) {
        *(s16 *)(record + 0x38) = 0;
        if ((s32)((u32)threshold - (u32)height) < 50) {
            effect.zero = 0;
            effect.extent = 256;
            effect.tag = D_8008CADC;
            effect.x = *(s16 *)(record + 0x20);
            effect.y = (s32)((u32)*(s32 *)(record + 0x14) + 10u);
            effect.z = *(s16 *)(record + 0x24);
            alpha = record[0x3B];
            effect.flag = 0;
            effect.type = 3;
            value = ((s32)alpha << 12) / 5100 + 204;
            effect.size1 = value;
            effect.size2 = value;
            effect.alpha = alpha;
            func_15167AD8(&effect, record[0x0C], record[1]);
        }
    } else {
        height = (s32)((f32)*(s16 *)(record + 0x26) * D_800A6CC8);
        threshold = (s32)((f32)*(s16 *)(record + 0x28) * D_800A6CC8);
        *(s16 *)(record + 0x26) = height;
        *(s16 *)(record + 0x28) = threshold;
    }
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
