#include <ultra64.h>

#include "functions.h"
#include "variables.h"

/* Three points passed by value through the original 36-byte aggregate ABI. */
typedef struct { f32 a[3], b[3], c[3]; } PlanePoints;

extern f32 D_80099080;
typedef struct {
    s32 words[9];
} struct_15049260_arg;
void func_150AAD98(struct_15049260_arg arg0);

void func_15049260(struct_15049260_arg arg0) {
    func_150AAD98(arg0);
}

void func_150492CC(f32 arg0, f32 arg1, f32 arg2) {
    D_800CC220 = arg0;
    D_800CC224 = arg1;
    D_800CC228 = arg2;
    D_800CC22C = arg0 / 2.0f;
    D_800CC230 = arg1 / 2.0f;
    D_800CC234 = arg2 / 2.0f;

    if (arg0 == 0.0f) {
        arg0 = D_80099080;
    }

    D_800CC238 = arg1 / arg0;
    D_800CC23C = arg2 / arg0;
}

/* Publish the unnormalized plane normal and its dot product with point A. */
void func_15049350(PlanePoints points) {
    f32 abx, aby, abz, acx, acy, acz;
    f32 nx, ny, nz;
    abx = points.a[0] - points.b[0];
    aby = points.a[1] - points.b[1];
    abz = points.a[2] - points.b[2];
    acx = points.a[0] - points.c[0];
    acy = points.a[1] - points.c[1];
    acz = points.a[2] - points.c[2];
    nx = aby * acz - abz * acy;
    D_800CC210 = nx;
    ny = -abx * acz + abz * acx;
    D_800CC214 = ny;
    nz = abx * acy - aby * acx;
    D_800CC218 = nz;
    D_800CC21C = nx * points.a[0] + ny * points.a[1] + nz * points.a[2];
}
