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

extern struct127 D_800CC2D0[26];
extern struct124 *D_800D1C90[187];
extern u8 D_800C3E90;
s32 func_1502DB20(s32);
typedef struct {
    u8 retained[0x30];
    f32 x, y, z;
    u32 retained3C;
} ExtentPosition15184150;

/* Measure actor-relative matrix positions, falling back to model dimensions.
 * The retail caller ignores the normal-path residual V0; early exits return zero. */
s32 func_15184150(s32 actorIndex, f32 *x, f32 *y, f32 *z) {
    struct127 *actor;
    s32 modelId;
    s32 count;
    s32 i;
    f32 dx, dy, dz;
    ExtentPosition15184150 *positions;

    actor = &D_800CC2D0[actorIndex];
    modelId = actor->id;
    *z = 0.0f;
    *y = 0.0f;
    *x = 0.0f;
    if (actor->unk1D4 == NULL || D_800C3E90 != 0) {
        return 0;
    }
    count = func_1502DB20(modelId);
    for (i = 0; i < count; i++) {
        positions = (ExtentPosition15184150 *)actor->unk1D4;
        dx = positions[i].x;
        dy = positions[i].y;
        dz = positions[i].z;
        dx -= actor->x_position;
        dy -= actor->y_position;
        dz -= actor->z_position;
        if (dx < 0.0f) dx = -dx;
        if (*x < dx) *x = dx;
        if (dy < 0.0f) dy = -dy;
        if (*y < dy) *y = dy;
        if (dz < 0.0f) dz = -dz;
        if (*z < dz) *z = dz;
    }
    if (*x == 0.0f || *y == 0.0f || *z == 0.0f) {
        dx = (f32)D_800D1C90[actor->id]->unk1A;
        dy = actor->xz_scale * dx;
        *z = dy;
        *x = dy;
        dx = (f32)(D_800D1C90[actor->id]->unk1C + D_800D1C90[actor->id]->unk1E);
        *y = actor->y_scale * dx;
    }
}


s32 func_15184368() {
    return 0;
}

extern struct127 D_800CC2D0[26];
extern struct108 *D_800DBFF0;
extern f32 D_800A7378;
s32 func_150AD9A0(s32, s32, s32);

/* Reject distant reference records, then scale and validate the output vector. */
s32 func_15184DF0(s32 actorIndex, s32 recordIndex, f32 *x, f32 *y, f32 *z) {
    f32 actorX, actorY, actorZ;
    s32 distance;
    f32 scale;

    actorX = D_800CC2D0[actorIndex].x_position;
    actorY = D_800CC2D0[actorIndex].y_position;
    actorZ = D_800CC2D0[actorIndex].z_position;
    distance = func_150AD9A0(
        (s32)(actorX - D_800DBFF0[recordIndex].unk2F8),
        (s32)(actorY - D_800DBFF0[recordIndex].unk2FC),
        (s32)(actorZ - D_800DBFF0[recordIndex].unk300));
    if (distance >= 2001) {
        D_800D3688 = 0.0f;
        D_800D368C = D_800D3688;
        return 0;
    }
    func_15184150(actorIndex, x, y, z);
    scale = D_800A7378;
    *x *= scale;
    *y *= scale;
    *z *= scale;
    if (*x == 0.0f || *y == 0.0f || *z == 0.0f) {
        D_800D3688 = 0.0f;
        D_800D368C = D_800D3688;
        return 0;
    }
    return distance;
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

typedef struct {
    u8 retained00[0x10];
    s16 x;
    s16 retained12;
    s16 z;
    u8 retained16[0x39];
    u8 flags;
    u16 width;
    u16 depth;
    u8 retained54[0x1A];
    u8 disabled;
    u8 retained6F[0x31];
} OverlapEntity1B1600;
extern s32 D_800DBEF0;
extern OverlapEntity1B1600 *D_800DBEF4;
extern s16 D_800D37E0[];
extern s32 D_800DBE3C, D_800D3690, D_800DF0E4;
extern s32 D_800DF0E8, D_800DF0EC, D_800DF0F0, D_800DF0F4;
void func_1510F800(s32);
void func_150A44F0(s32, s16 *, s32);
ClipVertex *func_150A5E44(s16 *, ClipVertex *, f32 [4][4], ClipVertex *);

/* Collect entity bounds overlapping the query and append their vertex output. */
s32 func_151873E4(s32 x, s32 z, s32 halfSize, ClipVertex *out,
                 f32 transform[4][4], ClipVertex *limit, s32 outCount) {
    s32 selectedCount;
    s32 index;
    s32 extent;
    OverlapEntity1B1600 *entity;
    ClipVertex *end;

    if (D_800DBEF0 == 0) return outCount;
    func_1510F800(2);
    out += outCount;
    D_800DF0E8 = (s32)((u32)x - (u32)halfSize);
    D_800DF0EC = (s32)((u32)x + (u32)halfSize);
    D_800DF0F0 = (s32)((u32)z - (u32)halfSize);
    D_800DF0F4 = (s32)((u32)z + (u32)halfSize);
    selectedCount = 0;
    for (index = 0; index < D_800DBEF0; index++) {
        entity = &D_800DBEF4[index];
        if (entity->disabled != 0 || (entity->flags & 0x60) != 0) continue;
        extent = entity->depth < entity->width ? entity->width : entity->depth;
        if (D_800DF0EC < (s32)((u32)(s32)entity->x - (u32)extent)) continue;
        if ((s32)((u32)(s32)entity->x + (u32)extent) < D_800DF0E8) continue;
        if (D_800DF0F4 < (s32)((u32)(s32)entity->z - (u32)extent)) continue;
        if ((s32)((u32)(s32)entity->z + (u32)extent) < D_800DF0F0) continue;
        D_800D37E0[selectedCount++] = index;
    }
    if (selectedCount != 0) {
        func_150A44F0(selectedCount, D_800D37E0, 0);
        D_800D3690 = D_800DBE3C;
        D_800DF0E4 = selectedCount;
        end = func_150A5E44(D_800D37E0, out, transform, limit);
        outCount += end - out;
    }
    return outCount;
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
