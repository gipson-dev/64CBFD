#include <ultra64.h>

/* Build an N64 fixed-point scale matrix from three floating-point factors. */
void func_150A7C10(volatile s16 *matrix, f32 x, f32 y, f32 z) {
    s32 fixedX = x * 65536.0f;
    s32 fixedY = y * 65536.0f;
    s32 fixedZ = z * 65536.0f;
    u64 *words = (u64 *)matrix;

    words[0] = 0;
    words[1] = 0;
    words[2] = 0;
    words[3] = 0;
    words[4] = 0;
    words[5] = 0;
    words[6] = 0;
    words[7] = 0;
    matrix[0] = 1;
    matrix[5] = 1;
    matrix[10] = 1;
    matrix[15] = 1;
    matrix[0] = fixedX >> 16;
    matrix[5] = fixedY >> 16;
    matrix[10] = fixedZ >> 16;
    matrix[16] = fixedX;
    matrix[21] = fixedY;
    matrix[26] = fixedZ;
}
