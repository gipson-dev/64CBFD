#include <ultra64.h>
#include "functions.h"
#include "variables.h"


// setting W values in identity matrix
void func_150A7DA0(u32 *arg0, u32 arg1, u32 arg2, u32 arg3) {
    arg0[1] = 0;
    arg0[0] = 0x3F800000;
    arg0[2] = 0;
    arg0[3] = 0;
    arg0[4] = 0;
    arg0[5] = 0x3F800000;
    arg0[6] = 0;
    arg0[7] = 0;
    arg0[8] = 0;
    arg0[9] = 0;
    arg0[10] = 0x3F800000;
    arg0[11] = 0;
    arg0[12] = arg1;
    arg0[13] = arg2;
    arg0[14] = arg3;
    arg0[15] = 0x3F800000;
}
// NON-MATCHING: same issues as other matrix funcs
// void func_150A7DA0(f32 arg0[4][4], s32 arg1, s32 arg2, s32 arg3) {
//     if (0) {};
//     ((s32)arg0[0][1]) = 0;
//     (arg0[0][0]) = 1.0f;
//     dummy_label_418035: ;
//     ((s32)arg0[0][2]) = 0;
//     ((s32)arg0[0][3]) = 0;
//     ((s32)arg0[1][0]) = 0;
//     (arg0[1][1]) = 1.0f;
//     ((s32)arg0[1][2]) = 0;
//     ((s32)arg0[1][3]) = 0;
//     ((s32)arg0[2][0]) = 0;
//     ((s32)arg0[2][1]) = 0;
//     (arg0[2][2]) = 1.0f;
//     ((s32)arg0[2][3]) = 0;
//     ((s32)arg0[3][0]) = arg1;
//     ((s32)arg0[3][1]) = arg2;
//     ((s32)arg0[3][2]) = arg3;
//     (arg0[3][3]) = 1.0f;
// }
