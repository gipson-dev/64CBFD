#include <ultra64.h>
#include "structs.h"
extern f32 D_8008D578;
void func_151EFE00(f32 [4][4]);
typedef struct {
    u8 retained[0x8C];
    f32 baseIncrement;
    f32 accumulated;
    s16 elapsed;
    s16 duration;
    u8 tail[8];
} DampedEffectRecord1B1600;
typedef struct {
    u8 retained[0xA4];
    DampedEffectRecord1B1600 *records;
    s16 age;
    s16 lifetime;
} TimedDampedEffect1B1600;
extern s32 D_800BE9E4;
void func_10004074(void *);
void func_1516972C(struct102 *);


typedef struct {
    f32 x, y, z;
    s16 first, second, third;
    u8 retained[2];
} ClipVertex;

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

/* Interpolate the Y=Z crossing and advance the output vertex cursor. */
ClipVertex *func_15185454(ClipVertex *a, ClipVertex *b, ClipVertex *out) {
    f32 ratio;
    ratio = (a->z - a->y) / ((b->y - a->y) - (b->z - a->z));
    out->x = a->x + (b->x - a->x) * ratio;
    out->y = out->z = a->y + (b->y - a->y) * ratio;
    out->first = a->first + (b->first - a->first) * ratio;
    out->second = a->second + (b->second - a->second) * ratio;
    out->third = a->third + (b->third - a->third) * ratio;
    return out + 1;
}

s32 func_15185554(f32 *arg0) {
    return arg0[2] < arg0[1];
}

/* Interpolate the X=-Z crossing and advance the output vertex cursor. */
ClipVertex *func_1518557C(ClipVertex *a, ClipVertex *b, ClipVertex *out) {
    f32 ratio;
    ratio = (a->z + a->x) / ((a->x - b->x) + (a->z - b->z));
    out->x = a->x + (b->x - a->x) * ratio;
    out->y = a->y + (b->y - a->y) * ratio;
    out->z = -out->x;
    out->first = a->first + (b->first - a->first) * ratio;
    out->second = a->second + (b->second - a->second) * ratio;
    out->third = a->third + (b->third - a->third) * ratio;
    return out + 1;
}

s32 func_1518567C(f32 *arg0) {
    return arg0[0] < -arg0[2];
}

/* Interpolate the Y=-Z crossing and advance the output vertex cursor. */
ClipVertex *func_151856A8(ClipVertex *a, ClipVertex *b, ClipVertex *out) {
    f32 ratio;
    ratio = (a->z + a->y) / ((a->y - b->y) + (a->z - b->z));
    out->x = a->x + (b->x - a->x) * ratio;
    out->y = a->y + (b->y - a->y) * ratio;
    out->z = -out->y;
    out->first = a->first + (b->first - a->first) * ratio;
    out->second = a->second + (b->second - a->second) * ratio;
    out->third = a->third + (b->third - a->third) * ratio;
    return out + 1;
}

s32 func_151857B0(f32 *arg0) {
    return arg0[1] < -arg0[2];
}

/* Interpolate the X=Z crossing and advance the output vertex cursor. */
ClipVertex *func_151857DC(ClipVertex *a, ClipVertex *b, ClipVertex *out) {
    f32 ratio;
    ratio = (a->z - a->x) / ((b->x - a->x) - (b->z - a->z));
    out->x = a->x + (b->x - a->x) * ratio;
    out->y = a->y + (b->y - a->y) * ratio;
    out->z = out->x;
    out->first = a->first + (b->first - a->first) * ratio;
    out->second = a->second + (b->second - a->second) * ratio;
    out->third = a->third + (b->third - a->third) * ratio;
    return out + 1;
}

s32 func_151858D4(f32 *arg0) {
    return arg0[2] < arg0[0];
}

/* Interpolate the depth-plane crossing and advance the output vertex cursor. */
ClipVertex *func_151858FC(ClipVertex *a, ClipVertex *b, ClipVertex *out) {
    f32 ratio;
    ratio = (D_800D3688 - a->z) / (b->z - a->z);
    out->x = a->x + (b->x - a->x) * ratio;
    out->y = a->y + (b->y - a->y) * ratio;
    out->z = D_800D3688;
    out->first = a->first + (b->first - a->first) * ratio;
    out->second = a->second + (b->second - a->second) * ratio;
    out->third = a->third + (b->third - a->third) * ratio;
    return out + 1;
}

s32 func_151859FC(f32 *arg0) {
    return D_800D3688 < arg0[2];
}

/* Interpolate the depth-plane crossing and advance the output vertex cursor. */
ClipVertex *func_15185A28(ClipVertex *a, ClipVertex *b, ClipVertex *out) {
    f32 ratio;
    ratio = (D_800D368C - a->z) / (b->z - a->z);
    out->x = a->x + (b->x - a->x) * ratio;
    out->y = a->y + (b->y - a->y) * ratio;
    out->z = D_800D368C;
    out->first = a->first + (b->first - a->first) * ratio;
    out->second = a->second + (b->second - a->second) * ratio;
    out->third = a->third + (b->third - a->third) * ratio;
    return out + 1;
}

s32 func_15185B28(f32 *arg0) {
    return arg0[2] < D_800D368C;
}


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

typedef ClipVertex *(*ClipInterpolate)(ClipVertex *, ClipVertex *, ClipVertex *);
typedef s32 (*ClipClassify)(ClipVertex *);
extern ClipInterpolate D_8008D498[];
extern ClipClassify D_8008D4C0[];

/* Clip a closed polygon against the selected plane and return the output cursor. */
ClipVertex *func_15185DD4(ClipVertex *vertices, s32 count, u32 plane, ClipVertex *out) {
    ClipVertex *current;
    /* Preserve the guest's word-address calculation even when count is nonpositive. */
    ClipVertex *previous = (ClipVertex *)((u32)count * sizeof(ClipVertex) + (u32)vertices - sizeof(ClipVertex));
    ClipInterpolate interpolate = D_8008D498[plane];
    ClipClassify classify = D_8008D4C0[plane];
    s32 i;
    current = vertices;

    for (i = 0; i < count; i++) {
        if (classify(current)) {
            if (classify(previous)) {
                *out++ = *current;
            } else {
                out = interpolate(previous, current, out);
                *out++ = *current;
            }
        } else if (classify(previous)) {
            out = interpolate(previous, current, out);
        }
        previous = current;
        current++;
    }
    return out;
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

extern s32 D_800DE01C,D_800DE020,D_800DE024,D_800DE030,D_800DE034,D_800DE038;
extern f32 D_800DE03C;
extern u8 D_800DE040,D_800DE041;
/* Set parameter defaults before applying the selected variant's overrides. */
void func_151872B0(s32 variant) {
    D_800DE01C = 600;
    D_800DE020 = 180;
    D_800DE024 = 90;
    D_800DE030 = 1016;
    D_800DE034 = 0;
    D_800DE038 = 1;
    D_800DE03C = 1.0f;
    D_800DE040 = 1;
    D_800DE041 = 1;
    switch (variant) {
        case 0x21:
            D_800DE01C = 4800;
            D_800DE020 = D_800DE01C - 1;
            D_800DE024 = D_800DE01C - 2;
            D_800DE030 = 1010;
            D_800DE034 = 1;
            D_800DE038 = 4;
            D_800DE040 = 0;
            break;
        case 0x22:
            D_800DE01C = 2400;
            D_800DE020 = D_800DE01C - 1;
            D_800DE024 = D_800DE01C - 2;
            D_800DE038 = 4;
            D_800DE040 = 0;
            break;
        case 0x14:
            D_800DE041 = 0;
            break;
        case 0x29:
            D_800DE01C = 1200;
            D_800DE020 = 600;
            D_800DE024 = 300;
            break;
    }
}

s32 func_151873E4() {
    return 0;
}

s32 func_151875E0() {
    return 0;
}

/* Advance twelve damped records; release the buffer and actor after expiry. */
void func_15187978(struct102 *input) {
    TimedDampedEffect1B1600 *effect = (TimedDampedEffect1B1600 *)input;
    DampedEffectRecord1B1600 *record;
    s32 offset;

    if (effect->age < 0) {
        func_10004074(effect->records);
        func_1516972C(input);
    } else {
        effect->age += (u32)D_800BE9E4;
        if (effect->age > effect->lifetime) {
            effect->age = -10;
        } else if (effect->age >= 0) {
            for (offset = 0; offset < 0x780; offset += 0xA0) {
                record = (DampedEffectRecord1B1600 *)((u8 *)effect->records + offset);
                if (record->elapsed < record->duration) {
                    record->elapsed += (u32)D_800BE9E4;
                    record = (DampedEffectRecord1B1600 *)((u8 *)effect->records + offset);
                    if (record->elapsed > record->duration) {
                        record->elapsed = record->duration;
                        record = (DampedEffectRecord1B1600 *)((u8 *)effect->records + offset);
                    }
                    record->accumulated += record->baseIncrement -
                        (record->baseIncrement / 3.0f) * record->elapsed / record->duration;
                }
            }
        }
    }
}

s32 func_15187A98() {
    return 0;
}

/* Construct the alternate Euler rotation matrix. */
void func_15187D6C(f32 m[4][4], f32 x, f32 y, f32 z) {
    f32 sx, cx, sy, sz, cy, cz, t;
    x *= D_8008D578; y *= D_8008D578; z *= D_8008D578;
    sx = sinf(x); cx = cosf(x);
    sy = sinf(y); cy = cosf(y);
    sz = sinf(z); cz = cosf(z);
    func_151EFE00(m);
    t = sx * sy;
    m[1][2] = sx;
    m[0][0] = cy * cz - t * sz;
    m[0][1] = cy * sz + t * cz;
    m[0][2] = -sy * cx;
    m[1][0] = -cx * sz;
    m[1][1] = cx * cz;
    t = sx * cy;
    m[2][0] = sy * cz + t * sz;
    m[2][1] = sy * sz - t * cz;
    m[2][2] = cx * cy;
}
