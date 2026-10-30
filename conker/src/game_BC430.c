#include <ultra64.h>

#include "functions.h"
#include "variables.h"

extern f32 D_8009DC80;

/* Generated placeholder declarations. */
void func_1508EF80(f32 *, f32 *, f32, f32 *);
/* End generated placeholder declarations. */

/* Rotate X/Z about the pivot, preserving the output Y coordinate. */
void func_1508EF80(f32 *point, f32 *pivot, f32 degrees, f32 *output) {
    f32 dx, dz, radians, providerValue, z, x, cachedValue;
    dx = point[0] - pivot[0];
    radians = degrees * D_8009DC80;
    dz = point[2] - pivot[2];
    cachedValue = cosf(radians);
    providerValue = sinf(radians);
    x = providerValue * dz + cachedValue * dx;
    x += pivot[0];
    cachedValue = sinf(radians);
    providerValue = cosf(radians);
    z = providerValue * dz + (-cachedValue) * dx;
    z += pivot[2];
    output[0] = x;
    output[2] = z;
}
