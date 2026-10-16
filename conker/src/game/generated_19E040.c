#include <ultra64.h>

typedef struct RingColors19E040 {
    u8 values[3];
} RingColors19E040;
extern RingColors19E040 D_8008CC20;
f32 func_15048A40(u8 angle);
f32 func_150489B0(u8 angle);
s32 func_150ADA20(void);
void func_1516D4E8(
    s16 arg0, s16 arg1, s16 arg2, u8 arg3, u8 arg4, u8 arg5,
    u8 arg6, u8 arg7, u8 arg8, u8 arg9, u8 arg10, u8 arg11,
    u8 arg12, u8 arg13, u8 arg14, u8 arg15, u8 arg16, u8 arg17,
    u8 arg18, u8 arg19, u8 arg20, u8 arg21, u8 arg22, s16 arg23,
    s16 arg24, u8 arg25, s16 arg26, s32 arg27, s32 arg28, u8 arg29,
    s32 arg30);

extern s32 D_800BE9F0;

void func_151700D8(f32 *, f32, f32, s32, f32, s32, s32, s32, u8, s32);

/* Non-matching placeholders for the text-only asm slice asm/19E040.s. */

s32 func_15170B90() {
    return 0;
}

void func_15170EC4(u8 *arg0, u8 arg1, s32 arg2) {
    switch (D_800BE9F0) {
        case 2:
            func_15170B90(arg0, 1, 1, 1, arg1, arg2);
            break;
        case 0x10:
            func_15170B90(arg0, 0xA9, 8, 0, arg1, arg2);
            break;
    }
}

s32 func_15170F4C() {
    return 0;
}

void func_151711C4(u8 *arg0) {
    if (*(arg0 + 4) == 0x33) {
        func_150C3D5C(arg0);
    }
    func_15060F28(arg0, 1);
}

s32 func_15171200() {
    return 0;
}

s32 func_15171600() {
    return 0;
}

/* Build a rectangle around signed actor coordinates and emit its perimeter.
 * Guards normalize the compiler's private homes and FP/register schedule. */
void func_151717FC(u8 *actor, f32 halfWidth, f32 halfDepth, f32 offsetX,
                  f32 offsetY, f32 offsetZ, s32 kind, s32 preset,
                  s32 xCount, s32 zCount, f32 scale, u8 flags, s32 context) {
    f32 quad[12];
    f32 frontZ;
    f32 centerY;
    f32 centerX;
    f32 centerZ;
    f32 backZ;
    f32 rightX;
    f32 leftX;

    centerX = (f32)*(s16 *)(actor + 0x10) + offsetX;
    centerY = (f32)*(s16 *)(actor + 0x12) + offsetY;
    centerZ = (f32)*(s16 *)(actor + 0x14) + offsetZ;
    quad[1] = centerY;
    quad[4] = centerY;
    rightX = halfWidth + centerX;
    quad[7] = centerY;
    quad[0] = rightX;
    quad[9] = rightX;
    leftX = centerX - halfWidth;
    backZ = centerZ - halfDepth;
    frontZ = halfDepth + centerZ;
    quad[3] = leftX;
    quad[6] = leftX;
    quad[2] = frontZ;
    quad[5] = frontZ;
    quad[10] = centerY;
    quad[8] = (&backZ)[0];
    quad[11] = (&backZ)[0];
    func_151700D8(quad, centerX, centerZ, preset, scale, kind,
                  xCount, zCount, flags, context);
}

/* Emit randomized radial particles using the staged palette-zero color.
 * Nonzero palette selectors would read beyond the original three-byte object.
 * Guards normalize only eight closed initialization temporary-register words. */
void func_151718F0(f32 x, f32 y, f32 z, f32 radius, s32 lifetime,
                  f32 spread, s32 palette, s32 count, u8 flags, s32 context) {
    u8 *color;
    f32 sine;
    f32 cosine;
    f32 positionZ;
    f32 delay;
    f32 baseLifetime;
    s32 phase;
    s32 index;
    s32 angle;
    s32 zHigh;
    s32 zLow;
    s32 extent;
    s32 fixedX;
    s32 fixedZ;
    s32 tail;
    s32 step;
    s16 height;
    u32 draw;
    RingColors19E040 colors;

    colors = D_8008CC20;
    if (count != 0) {
        phase = 0;
        index = 0;
        if (count > 0) {
            step = 0xFFFF / count;
            height = (s16)(s32)y;
            baseLifetime = (f32)lifetime;
            color = colors.values + palette * 3;
            do {
                angle = (phase >> 8) & 255;
                sine = func_15048A40(angle);
                cosine = func_150489B0(angle);
                positionZ = radius * cosine + z;
                fixedZ = (s32)(200.0f * cosine);
                zHigh = (fixedZ >> 8) & 255;
                zLow = fixedZ & 255;
                draw = (u32)func_150ADA20() & 0xFFFFU;
                delay = (f32)draw * 0.0000152587890625f + 100.0f;
                extent = (s32)((f32)((u32)func_150ADA20() & 0xFFFFU) * spread + baseLifetime);
                tail = func_150ADA20();
                fixedX = (s32)(200.0f * sine);
                func_1516D4E8((s16)(s32)(radius * sine + x), height, (s16)(s32)positionZ,
                    0xD, 0, color[0], color[1], color[2], 0, 0, 0, 0, 2,
                    (fixedX >> 8) & 255, fixedX & 255, zHigh, zLow, 0, 0, 5, 0, 0, 0,
                    (s16)extent, (s16)extent, (tail & 15) + 10, (s32)delay,
                    0, 0, flags, context);
                index += 1;
                phase += step;
            } while (index != count);
        }
    }
}

s32 func_15171BF4() {
    return 0;
}
