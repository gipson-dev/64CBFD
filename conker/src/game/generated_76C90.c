#include <ultra64.h>

/* Route interpolation; the derivative helper below remains unfinished. */

/* Evaluate the four-point cubic route segment at the supplied fraction. */
f32 func_150497E0(f32 *points, s32 index, f32 fraction) {
    f32 half = -0.5f * points[index];
    f32 linear;
    f32 quadratic;
    f32 cubic;
    f32 value;

    cubic = points[index + 3] * 0.5f +
        ((half + 1.5f * points[index + 1]) + -1.5f * points[index + 2]);
    quadratic = points[index + 3] * -0.5f +
        ((points[index] + -2.5f * points[index + 1]) + (points[index + 2] + points[index + 2]));
    linear = points[index + 2] * 0.5f + half;
    value = ((cubic * fraction + quadratic) * fraction + linear) * fraction + points[index + 1];
    return value;
}

s32 func_150498A4() {
    return 0;
}
