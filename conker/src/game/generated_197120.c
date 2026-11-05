#include <ultra64.h>

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

s32 func_1516A648() {
    return 0;
}
