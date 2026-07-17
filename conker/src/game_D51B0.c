#include <ultra64.h>
#include "functions.h"
#include "variables.h"


// s16 / f32 matrix
void func_150A7D00(s16 *arg0, f32 arg1, f32 arg2, f32 arg3) {
    s32 x = arg1 * 65536.0f;
    s32 y = arg2 * 65536.0f;
    s32 z = arg3 * 65536.0f;

    bzero(arg0, 0x40);
    arg0[0] = 1;
    arg0[5] = 1;
    arg0[10] = 1;
    arg0[15] = 1;
    arg0[12] = x >> 16;
    arg0[13] = y >> 16;
    arg0[14] = z >> 16;
    arg0[28] = x;
    arg0[29] = y;
    arg0[30] = z;
}
