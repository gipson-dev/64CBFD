#include <ultra64.h>

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

s32 func_151718F0() {
    return 0;
}

s32 func_15171BF4() {
    return 0;
}
