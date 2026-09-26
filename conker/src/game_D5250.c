#include <ultra64.h>
#include "functions.h"
#include "variables.h"


// setting W values in identity matrix
void func_150A7DA0(f32 arg0[4][4], u32 arg1, u32 arg2, u32 arg3) {
    /* Preserve IDO's retail interleaved-store schedule. */
    if (0) {
    }
    ((u32 *) arg0)[1] = 0;
    arg0[0][0] = 1.0f;
first_diagonal_stored:
    ((u32 *) arg0)[2] = 0;
    ((u32 *) arg0)[3] = 0;
    ((u32 *) arg0)[4] = 0;
    arg0[1][1] = 1.0f;
    ((u32 *) arg0)[6] = 0;
    ((u32 *) arg0)[7] = 0;
    ((u32 *) arg0)[8] = 0;
    ((u32 *) arg0)[9] = 0;
    arg0[2][2] = 1.0f;
    ((u32 *) arg0)[11] = 0;
    ((u32 *) arg0)[12] = arg1;
    ((u32 *) arg0)[13] = arg2;
    ((u32 *) arg0)[14] = arg3;
    arg0[3][3] = 1.0f;
}
