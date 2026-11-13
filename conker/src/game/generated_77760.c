#include <ultra64.h>

extern f32 D_800990A0, D_800990A4, D_800990A8;
extern f32 fabsf(f32);
#pragma intrinsic (fabsf)

/* Evaluate the retail exponential approximation with a convergent series. */
f32 func_1504A2B0(f32 x) {
    f32 magnitude = fabsf(x);
    f32 result;
    f32 term;
    f32 previous;
    f32 remainder;
    s32 scale;
    s32 index;
    s32 remaining;

    if (magnitude < 1.1920929e-7f) {
        return 1.0f;
    }
    scale = (s32)(magnitude / D_800990A0);
    remaining = scale;
    if (scale >= 1025) {
        if (x >= 0.0f) {
            return D_800990A4;
        }
        return 0.0f;
    }
    result = 1.0f;
    term = 1.0f;
    index = 1;
    remainder = magnitude - (f32)scale * D_800990A8;
    do {
        previous = result;
        term *= remainder / (f32)index;
        result += term;
        index++;
    } while (result != previous);
    while (remaining != 0) {
        result += result;
        remaining--;
    }
    if (x >= 0.0f) {
        return result;
    }
    return 1.0f / result;
}
