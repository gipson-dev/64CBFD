#include <ultra64.h>

void func_151EFE00(f32 mf[4][4]);
void guMtxF2L2(f32 mf[4][4], Mtx *m);

void func_151EF800(float mf[4][4], float l, float r, float b, float t, float n, float f, float scale)
{
	int	i, j;

	func_151EFE00(mf);

	mf[0][0] = 2/(r-l);
	mf[1][1] = 2/(t-b);
	mf[2][2] = -2/(f-n);
	mf[3][0] = -(r+l)/(r-l);
	mf[3][1] = -(t+b)/(t-b);
	mf[3][2] = -(f+n)/(f-n);
	mf[3][3] = 1;

	for (i=0; i<4; i++)
	    for (j=0; j<4; j++)
		mf[i][j] *= scale;
}

void func_151EF954(Mtx *m, float l, float r, float b, float t, float n, float f, float scale)
{
	float	mf[4][4];

	func_151EF800(mf, l, r, b, t, n, f, scale);

	guMtxF2L2(mf, m);
}
