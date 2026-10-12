#include <ultra64.h>
extern f32 D_80098AFC;
extern f32 D_80098B00;
extern f32 D_80098B04;
extern f32 D_80098B08;
extern f32 D_80098B0C;

/* Non-matching placeholders for the text-only asm slice asm/6E770.s. */

extern u8 D_800848D0[];
extern u8 D_80084930[];

s32 func_15041480(u8 arg0);
Gfx *func_15041508(Gfx *, s32, s32, s32);

Gfx *func_150412C0(Gfx *displayList) {
    gSPTexture(displayList++, 0xFFFF, 0xFFFF, 0, G_TX_RENDERTILE, G_ON);
    gDPPipeSync(displayList++);
    gDPSetCombineMode(displayList++, G_CC_DECALRGBA, G_CC_DECALRGBA);
    gDPSetOtherMode(displayList++, G_TF_BILERP | G_TC_FILT | 0xF, 0x55204C);
    gDPSetTextureImage(displayList++, G_IM_FMT_I, G_IM_SIZ_16b, 64, D_80084930);
    gDPLoadTextureBlock_4b(displayList++, D_80084930, G_IM_FMT_I, 64, 128,
        0, G_TX_WRAP, G_TX_WRAP, 0, 0, G_TX_NOLOD, G_TX_NOLOD);
    return displayList;
}

Gfx *func_150413FC(Gfx *displayList, s32 x, s32 y, u8 *text) {
    Gfx *result;
    s32 value;
    u8 *commands;
    u32 xCursor;

    result = displayList;
    value = y;
    commands = text;
    xCursor = x;

    while (*commands != 0) {
        result = func_15041508(result, xCursor, value, func_15041480(*commands));
        commands++;
        xCursor += 8;
    }
    return result;
}

s32 func_15041480(u8 arg0) {
    s32 i;

    for (i = 0; i != 0x50; i += 4) {
        if (arg0 == D_800848D0[i]) {
            return i;
        }
        if (arg0 == D_800848D0[i + 1]) {
            return i + 1;
        }
        if (arg0 == D_800848D0[i + 2]) {
            return i + 2;
        }
        if (arg0 == D_800848D0[i + 3]) {
            return i + 3;
        }
    }
    return i;
}

Gfx *func_15041508(Gfx *displayList, s32 x, s32 y, s32 glyph) {
    gSPTextureRectangle(displayList++,
        (u32)x << 2, (u32)y << 2, ((u32)x + 8) << 2, ((u32)y + 12) << 2,
        G_TX_RENDERTILE, ((u32)(glyph % 8) * 8) << 5,
        ((u32)((glyph - (glyph % 8)) / 8) * 12) << 5, 0x400, 0x400);
    return displayList;
}

void func_150415E0(s32 code, s32 *width, s32 *height, f32 *scale,
    s32 *mode, f32 *factor) {
    if (code >= 0xA8 && code < 0x100) {
        *factor = 1.0f;
        switch (code) {
            case 0xA8:
            case 0xA9:
                *width = 32;
                *height = 18;
                *scale = D_80098AFC;
                *mode = 1;
                return;
            case 0xAA:
            case 0xAB:
            case 0xAC:
            case 0xAD:
                *width = 32;
                *height = 27;
                *scale = 2.0f;
                *mode = 1;
                *factor = D_80098B00;
                return;
            case 0xAE:
                *width = 16;
                *height = 17;
                *scale = D_80098B04;
                *mode = 1;
                return;
            case 0xAF:
            case 0xB0:
                *width = 46;
                *height = 16;
                *scale = 2.0f;
                *mode = 1;
                return;
            case 0xB6:
            case 0xB7:
            case 0xB8:
            case 0xB9:
                *width = 16;
                *height = 12;
                *scale = 2.0f;
                *mode = 0;
                return;
            case 0xBA:
                *mode = 0;
                *scale = D_80098B08;
                *width = 55;
                *height = 12;
                return;
            case 0xB1:
                *width = 38;
                *height = 24;
                *scale = 2.0f;
                *mode = 1;
                *factor = D_80098B0C;
                return;
            default:
                *width = 12;
                *height = 16;
                *scale = 2.0f;
                *mode = 0;
                return;
        }
    }
    *scale = 0.0f;
    *width = 0;
    *height = 0;
}

s32 func_150417AC() {
    return 0;
}

s32 func_150428D4() {
    return 0;
}

s32 func_15042C40() {
    return 0;
}
