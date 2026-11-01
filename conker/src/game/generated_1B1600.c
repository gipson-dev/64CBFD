#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/1B1600.s. */

extern f32 D_800D3688;
extern f32 D_800D368C;

s32 func_15184150() {
    return 0;
}

s32 func_15184368() {
    return 0;
}

s32 func_15184DF0() {
    return 0;
}

s32 func_15184FA4() {
    return 0;
}

s32 func_15185454() {
    return 0;
}

s32 func_15185554(f32 *arg0) {
    return arg0[2] < arg0[1];
}

s32 func_1518557C() {
    return 0;
}

s32 func_1518567C(f32 *arg0) {
    return arg0[0] < -arg0[2];
}

s32 func_151856A8() {
    return 0;
}

s32 func_151857B0(f32 *arg0) {
    return arg0[1] < -arg0[2];
}

s32 func_151857DC() {
    return 0;
}

s32 func_151858D4(f32 *arg0) {
    return arg0[2] < arg0[0];
}

s32 func_151858FC() {
    return 0;
}

s32 func_151859FC(f32 *arg0) {
    return D_800D3688 < arg0[2];
}

s32 func_15185A28() {
    return 0;
}

s32 func_15185B28(f32 *arg0) {
    return arg0[2] < D_800D368C;
}

typedef struct {
    f32 x, y, z;
    s16 first, second, third;
    u8 retained[2];
} ClipVertex;

/* Interpolate the X=0 crossing and advance the output vertex cursor. */
ClipVertex *func_15185B54(ClipVertex *a, ClipVertex *b, ClipVertex *out) {
    f32 ratio;
    ratio = a->x / (a->x - b->x);
    out->x = 0.0f;
    out->y = a->y + (b->y - a->y) * ratio;
    out->z = a->z + (b->z - a->z) * ratio;
    out->first = a->first + (b->first - a->first) * ratio;
    out->second = a->second + (b->second - a->second) * ratio;
    out->third = a->third + (b->third - a->third) * ratio;
    return out + 1;
}

s32 func_15185C44(f32 *arg0) {
    return arg0[0] <= 0.0f;
}

/* Interpolate the Y=0 crossing and advance the output vertex cursor. */
ClipVertex *func_15185C6C(ClipVertex *a, ClipVertex *b, ClipVertex *out) {
    f32 ratio;
    ratio = a->y / (a->y - b->y);
    out->y = 0.0f;
    out->x = a->x + (b->x - a->x) * ratio;
    out->z = a->z + (b->z - a->z) * ratio;
    out->first = a->first + (b->first - a->first) * ratio;
    out->second = a->second + (b->second - a->second) * ratio;
    out->third = a->third + (b->third - a->third) * ratio;
    return out + 1;
}

s32 func_15185D5C(f32 *arg0) {
    return arg0[1] <= 0.0f;
}

s32 func_15185D84(f32 *arg0) {
    return arg0[0] > 0.0f;
}

s32 func_15185DAC(f32 *arg0) {
    return arg0[1] > 0.0f;
}

s32 func_15185DD4() {
    return 0;
}

s32 func_15185F24() {
    return 0;
}

s32 func_1518652C() {
    return 0;
}

s32 func_15186794() {
    return 0;
}

s32 func_151872B0() {
    return 0;
}

s32 func_151873E4() {
    return 0;
}

s32 func_151875E0() {
    return 0;
}

s32 func_15187978() {
    return 0;
}

s32 func_15187A98() {
    return 0;
}

s32 func_15187D6C() {
    return 0;
}
