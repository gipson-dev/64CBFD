#include <ultra64.h>
#include "functions.h"
#include "variables.h"

void guMtxIdentF(f32 mf[4][4]) {
    volatile f32 *matrix = (volatile f32 *)mf;
    volatile u32 *words = (u32 *)mf;

    words[1] = 0;
    matrix[0] = 1.0f;
    words[2] = 0;
    words[3] = 0;
    words[4] = 0;
    matrix[5] = 1.0f;
    words[6] = 0;
    words[7] = 0;
    words[8] = 0;
    words[9] = 0;
    matrix[10] = 1.0f;
    words[11] = 0;
    words[12] = 0;
    words[13] = 0;
    words[14] = 0;
    matrix[15] = 1.0f;
}
