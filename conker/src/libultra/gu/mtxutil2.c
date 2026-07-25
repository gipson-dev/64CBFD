#include <ultra64.h>
#include "functions.h"
#include "variables.h"

void guMtxF2L2(f32 mf[4][4], Mtx *m) {
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

void func_151EFE00(f32 mf[4][4]) {
    s32 i;
    s32 j;

    for (i = 0; i < 4; i++) {
        for (j = 0; j < 4; j++) {
            if (i == j) {
                mf[i][j] = 1.0f;
            } else {
                mf[i][j] = 0.0f;
            }
        }
    }
}

void func_151EFE88(Mtx *m) {
    f32 mf[4][4];

    func_151EFE00(mf);
    guMtxF2L2(mf, m);
}

void guMtxL2F(float mf[4][4], Mtx *m)
{
	int		i, j;
	unsigned int	e1,e2;
	unsigned int	*ai,*af;
	int		q1,q2;

	ai=(unsigned int *) &m->m[0][0];
	af=(unsigned int *) &m->m[2][0];

	for (i=0; i<4; i++)
	for (j=0; j<2; j++) {
		e1 = (*ai & 0xffff0000) | ((*af >> 16) & 0xffff);
		e2 = ((*(ai++) << 16) & 0xffff0000) | (*(af++) & 0xffff);
		q1 = *((int *)&e1);
		q2 = *((int *)&e2);

		mf[i][j*2] = (f32)q1/65536.0f;
		mf[i][j*2+1] = (f32)q2/65536.0f;
	}
}
