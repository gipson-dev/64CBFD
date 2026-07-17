#include <ultra64.h>


void func_150A7CB0(u32 *arg0, u32 arg1, u32 arg2, u32 arg3) {
    arg0[0] = arg1;
    arg0[1] = 0;
    arg0[2] = 0;
    arg0[3] = 0;
    arg0[4] = 0;
    arg0[5] = arg2;
    arg0[6] = 0;
    arg0[7] = 0;
    arg0[8] = 0;
    arg0[9] = 0;
    arg0[10] = arg3;
    arg0[11] = 0;
    arg0[12] = 0;
    arg0[13] = 0;
    arg0[15] = 0x3F800000;
    arg0[14] = 0;
}
// NON-MATCHING: sw/jr in wrong order
// void func_150A7CB0(f32 mtx[4][4], s32 x, s32 y, s32 z) {
//     ((s32)mtx[0][0]) = x;
//     ((s32)mtx[0][1]) = 0;
//     ((s32)mtx[0][2]) = 0;
//     ((s32)mtx[0][3]) = 0;
//     ((s32)mtx[1][0]) = 0;
//     ((s32)mtx[1][1]) = y;
//     ((s32)mtx[1][2]) = 0;
//     ((s32)mtx[1][3]) = 0;
//     ((s32)mtx[2][0]) = 0;
//     ((s32)mtx[2][1]) = 0;
//     ((s32)mtx[2][2]) = z;
//     ((s32)mtx[2][3]) = 0;
//     ((s32)mtx[3][0]) = 0;
//     ((s32)mtx[3][1]) = 0;
//     mtx[3][3] = 1.0f;
//     // fakematch to "help"...
//     dummy_label_123:;
//     ((s32)mtx[3][2]) = 0;
// }
