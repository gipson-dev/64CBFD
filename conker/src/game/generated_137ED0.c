#include <ultra64.h>

extern s32 D_800BE9E4;
extern f32 D_800A26B0, D_800A26B4, D_800A26B8;
f32 cosf(f32);
s32 func_15114D24(u8 *, s32, s32, s16, s16, s32);

/* Recovered routines for the text-only asm slice asm/137ED0.s. */

s32 func_15179008();

void func_1510AA20(s32 arg0) {
    func_15179008(0);
}

extern s32 D_800BE3E4;

/* Advance the clock hands and submit a pending chime when its second changes. */
void func_1510AA44(u8 *state) {
    s32 previousMinute, minute, second;
    f32 hourAngle;

    previousMinute = (*(s32 *)(state + 0x3C) / 3600) % 60;
    if (*(s32 *)(state + 0x84) == 0 && D_800BE3E4 != 0) {
        *(s32 *)(state + 0x84) = 1;
        *(s32 *)(state + 0x3C) = ((u32)D_800BE3E4 * 180U) % 43200U;
        *(s32 *)(state + 0x3C) *= 60;
        previousMinute = (*(s32 *)(state + 0x3C) / 3600) % 60;
    }
    if (previousMinute < 0) previousMinute += 60;
    *(s32 *)(state + 0x3C) = (s32)((u32)*(s32 *)(state + 0x3C) + (u32)D_800BE9E4);
    if (*(s32 *)(state + 0x3C) >= 2592000) {
        *(s32 *)(state + 0x3C) -= 2592000;
    }
    second = *(s32 *)(state + 0x3C) / 60;
    minute = second / 60;
    hourAngle = (f32)(second / 300) * 2.5f;
    if (360.0f < hourAngle) *(s32 *)(state + 0x3C) = *(s32 *)(state + 0x3C) - 2592000;
    minute %= 60;
    if (minute < 0) minute += 60;
    if (previousMinute != minute && minute / 15 != previousMinute / 15) {
        if ((minute / 15 & 3) == 0) {
            *(s32 *)(state + 0x7C) = (s32)(hourAngle / 30.0f);
            if (*(s32 *)(state + 0x7C) == 0) *(s32 *)(state + 0x7C) = 12;
        } else {
            *(s32 *)(state + 0x7C) = 1;
        }
        *(s32 *)(state + 0x80) = -1;
    }
    if (*(s32 *)(state + 0x7C) != 0 && second != *(s32 *)(state + 0x80)) {
        *(s32 *)(state + 0x80) = second;
        *(s32 *)(state + 0x7C) = (s32)((u32)*(s32 *)(state + 0x7C) - 1U);
        func_15114D24(state, 0x4CC, 32767, 200, 1000, 12);
    }
    *(f32 *)(state + 0x68) = 5.0f;
    *(f32 *)(state + 0x108) = 5.0f;
    *(f32 *)(state + 0xA8) = -hourAngle;
    *(f32 *)(state + 8) = -((f32)minute * 6.0f);
}

/* Advance cosine motion and signal the alternating half/full-period crossings. */
void func_1510ADD8(u8 *state) {
    f32 value;
    f32 previous;

    *(f32 *)(state + 0x80) += D_800A26B0 * (f32)D_800BE9E4 / 60.0f;
    value = cosf(*(f32 *)(state + 0x80)) * 10.0f;
    previous = *(f32 *)state - value;
    *(f32 *)state = value;
    *(f32 *)(state + 0x60) = previous;
    if (*(s32 *)(state + 0x7C) == 0) {
        if (D_800A26B4 <= *(f32 *)(state + 0x80)) {
            *(s32 *)(state + 0x7C) = 1;
            func_15114D24(state, 0x4CA, 12000, 200, 1000, 4);
        }
    } else if (D_800A26B8 <= *(f32 *)(state + 0x80)) {
        previous = *(f32 *)(state + 0x80) - D_800A26B8;
        *(s32 *)(state + 0x7C) = 0;
        *(f32 *)(state + 0x80) = previous;
        func_15114D24(state, 0x4CB, 12000, 200, 1000, 4);
    }
}

f32 fabsf(f32);
#pragma intrinsic (fabsf)

/* Reject points outside the supplied depth and scaled projection bounds. */
s32 func_1510AEE0(f32 matrix[4][4], f32 x, f32 y, volatile f32 z,
                  f32 nearPlane, f32 farPlane, f32 xScale, f32 yScale,
                  f32 *xResult, f32 *volatile yResult) {
    f32 depth, horizontal, component; volatile f32 vertical;
    depth = matrix[0][2] * x;
    depth += matrix[1][2] * y;
    depth += matrix[2][2] * z;
    depth = -(matrix[3][2] + depth);
    if (depth < nearPlane) return 1;
    if (farPlane < depth) return 1;
    horizontal = matrix[0][0] * x;
    horizontal += matrix[1][0] * y;
    horizontal += matrix[2][0] * z;
    horizontal = fabsf(matrix[3][0] + horizontal) * xScale;
    if (depth < horizontal) return 1;
    component = matrix[0][1] * x;
    component += matrix[1][1] * y;
    component += matrix[2][1] * z;
    vertical = fabsf(matrix[3][1] + component) * yScale;
    if (depth < vertical) return 1;
    if (xResult != 0) *xResult = 1.0f - horizontal / depth;
    xResult = yResult;
    if (xResult != 0) *xResult = 1.0f - vertical / depth;
    return 0;
}
