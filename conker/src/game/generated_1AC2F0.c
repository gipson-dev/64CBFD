#include <ultra64.h>
extern u8 D_800BE616, D_800DDE3C[];
extern f32 D_800A72B4;
extern f32 D_800D9D10[][4][4];
extern f32 D_800A7280, D_800A7284, D_800A7288;
void func_150A7A00(f32 matrix[4][4], f32 x, f32 y, f32 z,
    f32 *outX, f32 *outY, f32 *outZ, f32 *outW);
typedef struct {
    u8 padding00[0xC];
    f32 extentX, extentY;
    u8 padding14[0x10];
    f32 top, bottom, left, right;
    u8 padding34[0x14C];
} OverlayViewport1AC2F0;
extern u8 *D_800BE628;
#define OVERLAY_VIEWS_1AC2F0 ((OverlayViewport1AC2F0 *)D_800BE628)
extern s8 D_800DDDAC[];
extern u8 D_800DDDC0[];
extern u16 D_800DDE10[];
extern s32 D_80082FA0;
extern u8 D_800DDD9C[];
extern u8 D_800DDD90[];
extern s32 D_800BE9E4;
extern u8 D_800DDD8C;
extern u8 D_800DDD8B;
extern u8 D_800DDD8A;
extern u8 D_800DDD89;
extern u8 D_800DDD88;
extern u16 D_800DDE08;
extern s32 D_800DDE28[];
extern s32 D_800DDDB0[];
extern u8 D_800DDDA0[];
extern f32 D_800DDDC8[];
extern f32 D_800DDDD8[];
extern f32 D_800DDDE8[][2];
extern u8 D_800DDE1C[];
extern u8 D_800DDE20[];
extern f32 D_800A72AC;
extern f32 D_800A72B0;

/* Non-matching placeholders for the text-only asm slice asm/1AC2F0.s. */

/* Publish a channel's RGB transition when its mode or active state requires it. */
void func_1517EE40(s32 red, s32 green, s32 blue, s32 duration, s8 mode, s32 channel) {
    u8 *color;

    if (mode != D_800DDDAC[channel] ||
        D_800DDDB0[channel] < D_800DDE28[channel] ||
        D_800DDDC0[channel] != 0) {
        color = &D_800DDDA0[channel * 3];
        color[1] = green;
        color[2] = blue;
        color[0] = red;
        D_800DDE28[channel] = duration;
        D_800DDDB0[channel] = 0;
        D_800DDDAC[channel] = mode;
        D_800DDDC0[channel] = 0;
    }
}

/* Return the channel's signed progress, preserving the 32-bit scaled product. */
s32 func_1517EF00(s32 channel) {
    s32 progress;

    if (D_800DDDC0[channel] != 0) {
        progress = D_800DDDC0[channel];
    } else {
        if (D_800DDE28[channel] != 0) {
            progress = (s32)((u32)D_800DDDB0[channel] * 255U) / D_800DDE28[channel];
            if (progress > 255) {
                progress = 255;
            }
        } else {
            progress = 255;
        }
        if (D_800DDDAC[channel] == 0) {
            progress = (s32)(255U - (u32)progress);
        }
    }
    return progress;
}

s32 func_1517EFAC(s32 arg0) {
    if (func_1517EF00(arg0) == 0xFF) {
        return 1;
    }
    return 0;
}

/* Test whether every live channel has positive progress or float state. */
s32 func_1517EFDC(void) {
    s32 channel;
    s32 active = -1;

    for (channel = 0; channel <= D_80082FA0; channel++) {
        if (func_1517EF00(channel) > 0 || D_800DDDC8[channel] > 0.0f) {
            active++;
        }
    }
    if (active == D_80082FA0) {
        return 1;
    }
    return 0;
}

/* Append the channel's RGBA overlay using the live viewport bounds. */
Gfx *func_1517F08C(Gfx *commands, s32 alpha, s32 red, s32 green, s32 blue, s32 channel) {

    gDPPipeSync(commands++);
    gDPSetCombineMode(commands++, G_CC_PRIMITIVE, G_CC_PRIMITIVE);
    gDPSetPrimColor(commands++, 0, 0, red, green, blue, alpha);
    /* The overlay uses coverage-save with the SDK translucent blender. */
    gDPSetOtherMode(commands++, G_CYC_1CYCLE | G_TP_NONE | G_TF_BILERP |
        G_TC_FILT | G_CD_DISABLE | G_AD_DISABLE | 0xF,
        G_ZS_PRIM | CVG_DST_SAVE | ((G_RM_XLU_SURF | G_RM_XLU_SURF2) & ~CVG_DST_SAVE));
    gDPFillRectangle(commands++,
        (u32)OVERLAY_VIEWS_1AC2F0[channel].left,
        (u32)OVERLAY_VIEWS_1AC2F0[channel].top,
        (u32)OVERLAY_VIEWS_1AC2F0[channel].right,
        (u32)OVERLAY_VIEWS_1AC2F0[channel].bottom);
    return commands;
}

s32 func_1517F3A0(s32 arg0, s32 arg1) {
    s32 mapped = func_1517EF00(arg1);

    if (mapped == 0) {
        return arg0;
    }

    return (s32)func_1517F08C(
        (Gfx *)arg0,
        mapped,
        D_800DDDA0[arg1 * 3],
        D_800DDDA0[arg1 * 3 + 1],
        D_800DDDA0[arg1 * 3 + 2],
        arg1);
}

s32 func_1517F40C(s32 arg0) {
    if (D_800DDDB0[arg0] >= D_800DDE28[arg0]) {
        return 1;
    }
    return 0;
}

// Matched with guarded address-calculation scheduling normalization.
void func_1517F448(s32 arg0) {
    s32 *ptr = &D_800DDDB0[arg0];
    s32 value = *ptr;

    if (D_800DDE28[arg0] != value) {
        *ptr = value + D_800BE9E4;
    }
}

void func_1517F488(s32 arg0, s32 arg1, s32 arg2, s32 arg3, s32 arg4, s32 arg5) {
    u8 *ptr = D_800DDD90 + arg5 * 3;

    ptr[0] = arg0;
    ptr[1] = arg1;
    ptr[2] = arg2;
    D_800DDD9C[arg5] = arg3;
    D_800DDE10[arg5] = arg4;
}

s32 func_1517F4D8(s32 arg0, s32 arg1) {
    u8 *ptr;

    if (D_800DDE10[arg1] == 0) {
        return arg0;
    }

    if (D_800DDD9C[arg1] == 0) {
        return arg0;
    }

    ptr = D_800DDD90 + arg1 * 3;
    return (s32)func_1517F08C((Gfx *)arg0, D_800DDD9C[arg1], ptr[0], ptr[1], ptr[2], arg1);
}

s32 func_1517F564() {
    return 0;
}

void func_1517F720(s32 arg0, s32 arg1, s32 arg2, s32 arg3, s32 arg4) {
    D_800DDE08 = arg1;
    D_800DDD88 = arg2;
    D_800DDD89 = 0;
    D_800DDD8A = arg0;
    D_800DDD8B = arg3;
    D_800DDD8C = arg4;
}

void func_1517F75C(void) {
    s32 i;

    for (i = 0; i <= D_80082FA0; i++) {
        if (D_800BE9E4 < D_800DDE10[i]) {
            D_800DDE10[i] -= D_800BE9E4;
        } else {
            D_800DDE10[i] = 0;
        }
    }
}

// Matched with guarded timer-base register normalization.
void func_1517F7B4(void) {
    if (D_800DDE08 != 0) {
        if (D_800BE9E4 < D_800DDE08) {
            D_800DDE08 -= D_800BE9E4;
        } else {
            D_800DDE08 = 0;
        }
        D_800DDD89 += D_800DDD88 * D_800BE9E4;
    }
}

/* Project or accept screen coordinates, clamp, and publish relative offsets. */
void func_1517F814(s32 screenSpace, f32 x, f32 y, f32 z, s32 view) {
    f32 projectedX;
    f32 projectedY;
    f32 projectedZ;
    f32 divisor;
    f32 lower;
    OverlayViewport1AC2F0 *record;

    if (screenSpace == 0) {
        func_150A7A00((f32 (*)[4])((u8 *)D_800D9D10 + (u32)view * 64U),
            x, y, z, &projectedX, &projectedY, &projectedZ, &divisor);
        if (divisor == 0.0f) {
            divisor = 1.0f;
        }
        record = &OVERLAY_VIEWS_1AC2F0[view];
        projectedX = (record->extentX * projectedX) / divisor;
        projectedY = (record->extentY * projectedY) / divisor;
        projectedX += record->extentX;
        projectedY = record->extentY - projectedY;
        projectedX += record->left;
        projectedY += record->top;
    } else {
        projectedX = x;
        projectedY = y;
        record = &OVERLAY_VIEWS_1AC2F0[view];
    }
    if (10000.0f < projectedX) {
        lower = -10000.0f;
        projectedX = 10000.0f;
    } else {
        lower = -10000.0f;
        if (projectedX < lower) {
            projectedX = lower;
        }
    }
    if (10000.0f < projectedY) {
        projectedY = 10000.0f;
    } else if (projectedY < lower) {
        projectedY = lower;
    }
    D_800DDDE8[view][0] = projectedX - record->extentX;
    D_800DDDE8[view][1] = projectedY - record->extentY;
}

/* Sort and clip signed endpoints, then append one fill rectangle. */
Gfx *func_1517F9F4(Gfx *commands, s32 left, s32 top, s32 right, s32 bottom, s32 view) {
    s32 scratch;
    OverlayViewport1AC2F0 *record;
    s32 clipTop, clipBottom, clipRight;
    s32 clipped;

    if (right < left) {
        scratch = left;
        left = right;
        right = scratch;
    }
    if (bottom < top) {
        scratch = top;
        top = bottom;
        bottom = scratch;
    }
    record = &OVERLAY_VIEWS_1AC2F0[view];
    /* Sorting scratch now holds the left clip bound. */
    scratch = (s32)record->left;
    clipTop = (s32)record->top;
    clipRight = (s32)record->right;
    clipBottom = (s32)record->bottom;
    if (top >= clipBottom || clipTop >= bottom || left >= clipRight || scratch >= right) {
        return commands;
    }
    clipped = left < scratch ? scratch : clipRight < left ? clipRight : left;
    left = clipped;
    clipped = top < clipTop ? clipTop : clipBottom < top ? clipBottom : top;
    top = clipped;
    clipped = right < scratch ? scratch : clipRight < right ? clipRight : right;
    right = clipped;
    clipped = bottom < clipTop ? clipTop : clipBottom < bottom ? clipBottom : bottom;
    bottom = clipped;
    gDPFillRectangle(commands++, left, top, right, bottom);
    return commands;
}

s32 func_1517FB9C() {
    return 0;
}

s32 func_15180580() {
    return 0;
}

s32 func_151814FC() {
    return 0;
}

s32 func_15181CC8(s32 arg0) {
    if (0.0f == D_800DDDC8[arg0]) {
        return 1;
    }
    return 0;
}

void func_15181D00(s32 arg0, s32 arg1) {
    if (arg1 == 0) {
        D_800DDDC8[arg0] = 0.0f;
    } else {
        D_800DDDD8[arg0] = 0.0f;
        D_800DDDC8[arg0] = D_800A72AC;
        D_800DDDE8[arg0][0] = 0.0f;
        D_800DDDE8[arg0][1] = 0.0f;
    }
    D_800DDE1C[arg0] = arg1;
}

void func_15181D70(s32 arg0) {
    D_800DDDD8[arg0] = D_800A72B0;
    D_800DDDC8[arg0] = 0.0f;
    D_800DDDE8[arg0][0] = 0.0f;
    D_800DDDE8[arg0][1] = 0.0f;
    D_800DDE20[arg0] = 1;
}

void func_15181DC8(s32 arg0) {
    D_800DDDD8[arg0] = 0.0f;
    D_800DDDC8[arg0] = 0.0f;
    D_800DDDE8[arg0][0] = 0.0f;
    D_800DDDE8[arg0][1] = 0.0f;
    D_800DDE20[arg0] = 0;
}

/* Reset a channel to its mode-dependent overlay defaults. */
void func_15181E18(s32 channel) {
    u8 *color;
    f32 *projected;

    if (D_800BE616 != 0) {
        color = &D_800DDDA0[channel * 3];
        color[0] = 0;
        color[1] = 0;
        color[2] = 0;
        D_800DDE28[channel] = 25;
        D_800DDDB0[channel] = 0;
        D_800DDDAC[channel] = 0;
        D_800DDDC0[channel] = 0;
        return;
    }
    D_800DDE3C[channel] = 1;
    D_800DDDC8[channel] = 1.0f;
    projected = D_800DDDE8[channel];
    projected[0] = 0.0f;
    projected[1] = 0.0f;
    D_800DDDD8[channel] = D_800A72B4;
}

s32 func_15181EE0() {
    return 0;
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1AC2F0/func_15182670.s")

void func_15182748(u8 *arg0) {
    *(u8 *)(arg0 + 0x2B) = *(s16 *)(arg0 + 0xE) * *(s16 *)(arg0 + 0x2E);
}

s32 func_15182768(s32 arg0, u8 *arg1, s16 arg2) {
    u8 *values = arg1 + 0x28;

    if (arg2 == arg1[0x2C]) {
        arg0 = (s32)func_1517F08C((Gfx *)arg0, values[3], values[0], values[1], values[2], values[4]);
    }
    return arg0;
}
