#include <ultra64.h>
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

s32 func_1517F08C(s32 arg0, s32 arg1, s32 arg2, s32 arg3, s32 arg4, s32 arg5) {
    return 0;
}

s32 func_1517F3A0(s32 arg0, s32 arg1) {
    s32 mapped = func_1517EF00(arg1);

    if (mapped == 0) {
        return arg0;
    }

    return func_1517F08C(
        arg0,
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
    return func_1517F08C(arg0, D_800DDD9C[arg1], ptr[0], ptr[1], ptr[2], arg1);
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

s32 func_1517F814() {
    return 0;
}

s32 func_1517F9F4() {
    return 0;
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

s32 func_15181E18() {
    return 0;
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
        arg0 = func_1517F08C(arg0, values[3], values[0], values[1], values[2], values[4]);
    }
    return arg0;
}
