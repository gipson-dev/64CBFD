#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/770F0.s. */

void func_15049C40(f32 *arg0, f32 *arg1) {
    f32 dot = arg0[0] * arg1[0] + arg0[1] * arg1[1] +
              arg0[2] * arg1[2] + arg0[3] * arg1[3];

    if (dot < 0.0f) {
        arg1[0] = -arg1[0];
        arg1[1] = -arg1[1];
        arg1[2] = -arg1[2];
        arg1[3] = -arg1[3];
    }
}

s32 func_15049CB8() {
    return 0;
}

s32 func_15049EDC() {
    return 0;
}

/* Write a scalar-first quaternion's rotation while preserving translation. */
void func_1504A140(f32 *quaternion, f32 *matrix) {
    f32 scale = 2.0f / (((quaternion[0] * quaternion[0] +
        quaternion[1] * quaternion[1]) + quaternion[2] * quaternion[2]) +
        quaternion[3] * quaternion[3]);
    f32 scaledX = quaternion[1] * scale;
    f32 scaledY = quaternion[2] * scale;
    f32 scaledZ = quaternion[3] * scale;
    f32 wx = quaternion[0] * scaledX;
    f32 wy = quaternion[0] * scaledY;
    f32 wz = quaternion[0] * scaledZ;
    f32 xx = quaternion[1] * scaledX;
    f32 xy = quaternion[1] * scaledY;
    f32 xz = quaternion[1] * scaledZ;
    f32 yy = quaternion[2] * scaledY;
    f32 yz = quaternion[2] * scaledZ;
    f32 zz = quaternion[3] * scaledZ;

    matrix[0] = 1.0f - (yy + zz);
    matrix[1] = xy + wz;
    matrix[2] = xz - wy;
    matrix[4] = xy - wz;
    matrix[5] = 1.0f - (xx + zz);
    matrix[6] = yz + wx;
    matrix[8] = xz + wy;
    matrix[9] = yz - wx;
    matrix[10] = 1.0f - (xx + yy);
    matrix[3] = 0.0f;
    matrix[7] = 0.0f;
    matrix[11] = 0.0f;
    matrix[15] = 1.0f;
}
