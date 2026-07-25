#include <ultra64.h>
#include "functions.h"
#include "variables.h"

void guMtxXFMF(f32 mf[4][4], f32 x, f32 y, f32 z, f32 *ox, f32 *oy, f32 *oz) {
    *ox = mf[0][0] * x + mf[1][0] * y + mf[2][0] * z + mf[3][0];
    *oy = mf[0][1] * x + mf[1][1] * y + mf[2][1] * z + mf[3][1];
    *oz = mf[0][2] * x + mf[1][2] * y + mf[2][2] * z + mf[3][2];
}

void guMtxCatF(f32 lmf[4][4], f32 rmf[4][4], f32 dst[4][4]) {
	s32 i, j, k;
    f32 sp1C[4][4];

	for(i = 0; i < 4; i++){
		for(j = 0; j < 4; j++){
			sp1C[i][j] = 0.0f;
			for(k = 0; k < 4; k++){
				sp1C[i][j] += lmf[i][k]*rmf[k][j];
			}
		}
	}
	for(i = 0; i < 4; i++){
		for(j = 0; j < 4; j++){
			dst[i][j] = sp1C[i][j];
		}
	}
}
