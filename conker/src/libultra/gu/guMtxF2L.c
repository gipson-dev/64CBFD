#include <ultra64.h>
#include "functions.h"
#include "variables.h"

void guMtxF2L(f32 mf[4][4], Mtx *m) {
    s32 i;
    s32 j;
    s32 e1;
    s32 e2;
    s32 *ai;
    s32 *af;

    ai = (s32 *)&m->m[0][0];
    af = (s32 *)&m->m[2][0];

    for (i = 0; i < 4; i++) {
        for (j = 0; j < 2; j++) {
            e1 = FTOFIX32(mf[i][j * 2]);
            e2 = FTOFIX32(mf[i][j * 2 + 1]);
            *ai++ = (e1 & 0xFFFF0000) | ((e2 >> 16) & 0xFFFF);
            *af++ = ((e1 << 16) & 0xFFFF0000) | (e2 & 0xFFFF);
        }
    }
}
