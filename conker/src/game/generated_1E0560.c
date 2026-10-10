#include <ultra64.h>

extern f32 D_800AA390;
void *func_15167A68(s32, s32, s32, s32, u8, u8);
void *memcpy(void *, const void *, u32);

extern s32 D_800BE9E4;
extern s32 (*D_8008FAF0[])(u8 *, void *, s32);
extern s32 (*D_8008FAF8[])(u8 *);
void func_1516972C(u8 *);

typedef struct { f32 x, y, z; } OwnerRibbonPosition32C8;
extern u8 *D_800DBFF0;
extern u8 D_80090DE8[];
extern u32 D_800D2C9C, D_800A4AC8[];
void func_151D5D60(void *, s16, s32, Vtx **, u8 *);
Gfx *func_15142B7C(Gfx *, u32, u32);
Gfx *func_15142E24(Gfx *, void *, s32, s32, s32, s32, s32, u8, u8 *, u8 *, s32);
Gfx *func_15142C10(Gfx *, s32, s32, s32, s32, u8 *);
Gfx *func_15142CF0(Gfx *, s32, s32, s32, s32, s32, s32, u8 *);
Gfx *func_1513F4E4(Gfx *, u8, u8 *);
Gfx *func_15142FBC(Gfx *, u32, u32, u8 *);
extern s32 (*D_8008FB10[])(u8 *, s32 *, s32 *, s32 *, s32 *, s32 *,
    s32 *, s32 *, s32 *, s32 *, s32 *, s32 *, u8 *, u8 *);


typedef struct { OwnerRibbonPosition32C8 position, velocity; } OwnerPointRecord3A7C;
typedef struct {
    u8 header[0x10];
    u8 flags;
    u8 gap11[3];
    OwnerRibbonPosition32C8 start, end;
    u8 metadata[0x1C];
    OwnerPointRecord3A7C points[10];
} OwnerPoints3A7C;
extern f32 D_800AA394, D_800AA398, D_800AA39C;

extern f32 D_800AA3A0, D_800AA3A4, D_800AA3A8;
f32 func_150484A0(f32, f32);
f32 sinf(f32), cosf(f32), sqrtf(f32), fabsf(f32);
#pragma intrinsic (fabsf)
typedef struct {
    f32 x;
    volatile f32 y;
    f32 z;
} OwnerArcDeltaY;

typedef struct { u8 *actor; u8 epoch; } OwnerPositionLink3F28;
extern f32 D_800AA3AC;

typedef struct {
    u8 *first;
    u8 firstEpoch, firstMatrix, padding06[2];
    f32 firstPosition[3];
    u8 *second;
    u8 secondEpoch, secondMatrix, padding1A[2];
    f32 secondPosition[3];
} OwnerMatrixLink47D8;
void func_15143134(f32 *, f32 *, u8 *);

extern f32 D_800AA3C4;

extern f32 D_800AA3C8;

void func_1502EC34(u8 *, s32 *, s32 *, s32 *, s32 *);
s32 func_151B498C(u8 *owner, s32 *mode1, s32 *mode2, s32 *envR, s32 *envG,
                  s32 *envB, s32 *alpha, s32 *primR, s32 *primG, s32 *primB,
                  s32 *primA, s32 *renderMode, u8 *bank, u8 *combine);

/* Non-matching placeholders for the text-only asm slice asm/1E0560.s. */

extern void (*D_8008FB68[])(u8 *, s32, u8);
extern void (*D_8008FB70[])(u8 *);

s32 func_151D5E30();

u8 *func_151B30B0(void *request, f32 parameter, s32 extraBytes, u8 slot, s32 context) {
    u8 *created;
    f32 distance;
    f32 scaled;

    created = func_15167A68(0x33, context, extraBytes + 0x150, 1, slot, 1);
    if (created == NULL) {
        return NULL;
    }
    memcpy(created + 0x10, request, 56);
    distance = *(f32 *)(created + 0x38);
    created[0x10] |= 0xE;
    scaled = distance * distance / D_800AA390;
    *(f32 *)(created + 0x138) = scaled + scaled;
    *(s32 *)(created + 0x13C) = (s32)(distance * parameter * 4096.0f);
    bzero(created + 0x140, 16);
    return created;
}

void func_151B3184(u8 *actor) {
    s32 selector;
    u8 remove;

    remove = 0;
    if (actor[0x10] & 1) {
        *(s16 *)(actor + 0x12) -= D_800BE9E4;
        if (*(s16 *)(actor + 0x12) < 0) {
            remove = 1;
        }
    }
    if (!remove) {
        selector = (s8)actor[0x2C];
        if (selector != -1) {
            if (!D_8008FAF0[selector](actor, actor + 0x14, 1)) {
                remove = 1;
            }
        }
        selector = (s8)actor[0x2D];
        if (selector != -1) {
            if (!D_8008FAF0[selector](actor, actor + 0x20, 0)) {
                remove = 1;
            }
        }
        if ((actor[0x10] & 4) || (actor[0x10] & 8)) {
            actor[0x10] |= 2;
        } else if ((s8)actor[0x34] != -1) {
            if (!D_8008FAF8[(s8)actor[0x34]](actor)) {
                remove = 1;
            }
        }
    }
    if (remove) {
        func_1516972C(actor);
    }
}

Gfx *func_151B32C8(Gfx *output, u8 *actor, s16 view) {
    u32 textureT;
    Vtx *cursor;
    OwnerRibbonPosition32C8 first, second;
    s32 offset;
    OwnerRibbonPosition32C8 *origin;
    f32 rx, ry, rz;
    f32 dx, dy, dz;
    f32 nx, ny, nz;
    f32 ox, oy, oz;
    u8 sync;
    s32 mode1, mode2, envR, envG, envB, alpha, primR, primG, primB, primA, renderMode;
    u8 bank, combine;
    f32 squaredZ;
    u8 *points;
    f32 length, squared;

    if (actor[0x10] & 4) {
        return output;
    }
    if (actor[0x10] & 8) {
        return output;
    }
    if (actor[0x10] & 2) {
        return output;
    }
    func_151D5D60(actor + 0x140, view, 0x190, &cursor, NULL);
    if (cursor != NULL) {
        origin = (OwnerRibbonPosition32C8 *)(D_800DBFF0 + view * 0x9A0 + 0x2F8);
        sync = 1;
        if (!D_8008FB10[actor[0x2E]](actor, &mode1, &mode2, &envR, &envG, &envB,
                &alpha, &primR, &primG, &primB, &primA, &renderMode, &bank, &combine)) {
            return output;
        }
        output = func_15142B7C(output, mode1, mode2);
        output = func_15142C10(output, primR, primG, primB, primA, &sync);
        output = func_15142CF0(output, 0, 0, envR, envG, envB, alpha, &sync);
        output = func_1513F4E4(output, combine, &sync);
        output = func_15142E24(output, D_80090DE8, 0, 0, 0, 0, 54, 0, NULL, &sync, 3);
        points = actor + 0x48;
        output = func_15142FBC(output, renderMode | 0x80000 | D_800D2C9C | 0x2CA0,
            D_800A4AC8[bank * 2 + 1] | D_800A4AC8[bank * 2], &sync);
        first = *(OwnerRibbonPosition32C8 *)points;
        second = *(OwnerRibbonPosition32C8 *)(points + 0x18);
        dx = second.x - first.x;
        dy = second.y - first.y;
        dz = second.z - first.z;
        rx = first.x - origin->x;
        ry = first.y - origin->y;
        rz = first.z - origin->z;
        nx = dy * rz - ry * dz;
        ny = dz * rx - rz * dx;
        nz = dx * ry - rx * dy;
        squaredZ = nz * nz;
        squared = (nx * nx) + (ny * ny) + squaredZ;
        if (squared == 0.0f) {
            ox = 0.0f; oy = 0.0f; oz = 0.0f;
        } else {
            length = sqrtf(squared);
            dz = *(f32 *)(actor + 0x30) / length;
            ox = nx * dz;
            oy = ny * dz;
            oz = nz * dz;
        }
        cursor->v.ob[0] = (s32)(first.x + ox);
        cursor->v.ob[1] = (s32)(first.y + oy);
        cursor->v.ob[2] = (s32)(first.z + oz);
        cursor->v.tc[0] = 0;
        cursor->v.tc[1] = 0;
        cursor->v.cn[0] = 255;
        cursor->v.cn[1] = 100;
        cursor->v.cn[2] = 100;
        cursor->v.cn[3] = 255;
        cursor++;
        cursor->v.ob[0] = (s32)(first.x - ox);
        cursor->v.ob[1] = (s32)(first.y - oy);
        cursor->v.ob[2] = (s32)(first.z - oz);
        cursor->v.tc[0] = 0x3C0;
        cursor->v.tc[1] = 0;
        cursor->v.cn[0] = 255;
        cursor->v.cn[1] = 100;
        cursor->v.cn[2] = 100;
        cursor->v.cn[3] = 255;
        cursor++;
        textureT = *(s32 *)(actor + 0x13C);
        for (offset = 0x18; offset != 0xF0; offset += 0x18) {
            first = *(OwnerRibbonPosition32C8 *)(points + offset - 0x18);
            second = *(OwnerRibbonPosition32C8 *)(points + offset);
            dx = second.x - first.x;
            dy = second.y - first.y;
            dz = second.z - first.z;
            rx = second.x - origin->x;
            ry = second.y - origin->y;
            rz = second.z - origin->z;
            nx = dy * rz - ry * dz;
            ny = dz * rx - rz * dx;
            nz = dx * ry - rx * dy;
            squaredZ = nz * nz;
            squared = (nx * nx) + (ny * ny) + squaredZ;
            if (squared == 0.0f) {
                ox = 0.0f; oy = 0.0f; oz = 0.0f;
            } else {
                length = sqrtf(squared);
                dz = *(f32 *)(actor + 0x30) / length;
                ox = nx * dz;
                oy = ny * dz;
                oz = nz * dz;
            }
            cursor->v.ob[0] = (s32)(second.x + ox);
            cursor->v.ob[1] = (s32)(second.y + oy);
            cursor->v.ob[2] = (s32)(second.z + oz);
            cursor->v.tc[0] = 0;
            cursor->v.tc[1] = textureT;
            cursor->v.cn[0] = 255;
            cursor->v.cn[1] = 100;
            cursor->v.cn[2] = 100;
            cursor->v.cn[3] = 255;
            cursor++;
            cursor->v.ob[0] = (s32)(second.x - ox);
            cursor->v.ob[1] = (s32)(second.y - oy);
            cursor->v.ob[2] = (s32)(second.z - oz);
            cursor->v.tc[0] = 0x3C0;
            cursor->v.tc[1] = textureT;
            cursor->v.cn[0] = 255;
            cursor->v.cn[1] = 100;
            cursor->v.cn[2] = 100;
            cursor->v.cn[3] = 255;
            cursor++;

            textureT += *(s32 *)(actor + 0x13C);
            gSPVertex(output++, cursor - 4, 4, 0);
            gSP1Triangle(output++, 0, 1, 2, 0);
            gSP1Triangle(output++, 1, 3, 2, 0);
        }
    }
    return output;
}

void func_151B3A34(u8 *arg0, s32 arg1, u8 arg2) {
    void (*callback)(u8 *, s32, u8) = D_8008FB68[arg0[0x44]];

    if (callback != NULL) {
        callback(arg0, arg1, arg2);
    }
}

s32 func_151B3A7C(u8 *actor) {
    OwnerPoints3A7C *owner = (OwnerPoints3A7C *)actor;
    OwnerRibbonPosition32C8 delta, position, step;
    s32 i, count;
    OwnerPointRecord3A7C *points;

    points = owner->points;
    delta.x = owner->end.x - owner->start.x;
    delta.y = owner->end.y - owner->start.y;
    delta.z = owner->end.z - owner->start.z;
    position = owner->start;
        points[0].position = position;
        *(f32 *)(actor + 0x5C + (0) * 24) = 0.0f;
        *(f32 *)(actor + 0x58 + (0) * 24) = 0.0f;
        *(f32 *)(actor + 0x54 + (0) * 24) = 0.0f;
        step.x = delta.x * D_800AA394;
        position.x += step.x;
        step.y = delta.y * D_800AA398;
        position.y += step.y;
        step.z = delta.z * D_800AA39C;
        position.z += step.z;
        points[1].position = position;
        *(f32 *)(actor + 0x5C + (1) * 24) = 0.0f;
        *(f32 *)(actor + 0x58 + (1) * 24) = 0.0f;
        *(f32 *)(actor + 0x54 + (1) * 24) = 0.0f;
        position.x += step.x;
        position.y += step.y;
        position.z += step.z;
    count = 10;
    for (i = 2; i < count; i += 4) {
        points[i + 0].position = position;
        *(f32 *)(actor + 0x5C + (i + 0) * 24) = 0.0f;
        *(f32 *)(actor + 0x58 + (i + 0) * 24) = 0.0f;
        *(f32 *)(actor + 0x54 + (i + 0) * 24) = 0.0f;
        position.x += step.x;
        position.y += step.y;
        position.z += step.z;
        points[i + 1].position = position;
        *(f32 *)(actor + 0x5C + (i + 1) * 24) = 0.0f;
        *(f32 *)(actor + 0x58 + (i + 1) * 24) = 0.0f;
        *(f32 *)(actor + 0x54 + (i + 1) * 24) = 0.0f;
        position.x += step.x;
        position.y += step.y;
        position.z += step.z;
        points[i + 2].position = position;
        *(f32 *)(actor + 0x5C + (i + 2) * 24) = 0.0f;
        *(f32 *)(actor + 0x58 + (i + 2) * 24) = 0.0f;
        *(f32 *)(actor + 0x54 + (i + 2) * 24) = 0.0f;
        position.x += step.x;
        position.y += step.y;
        position.z += step.z;
        points[i + 3].position = position;
        *(f32 *)(actor + 0x5C + (i + 3) * 24) = 0.0f;
        *(f32 *)(actor + 0x58 + (i + 3) * 24) = 0.0f;
        *(f32 *)(actor + 0x54 + (i + 3) * 24) = 0.0f;
        position.x += step.x;
        position.y += step.y;
        position.z += step.z;
    }
    owner->flags &= ~2;
    return 1;
}

s32 func_151B3CF0(u8 *actor) {
    OwnerArcDeltaY delta;
    OwnerRibbonPosition32C8 midpoint;
    volatile OwnerRibbonPosition32C8 first, last;
    f32 inverse, nx, nz;
    f32 vertical, angle, radius, angleStep;
    f32 sine, along;
    s32 offset;
    OwnerRibbonPosition32C8 *cursor;

    nz = *(f32 *)(actor + 0x20);
    along = *(f32 *)(actor + 0x14);
    nx = *(f32 *)(actor + 0x24);
    angle = *(f32 *)(actor + 0x18);
    angleStep = *(f32 *)(actor + 0x28);
    sine = *(f32 *)(actor + 0x1C);
    delta.x = nz - along;
    delta.y = nx - angle;
    delta.z = angleStep - sine;
    if (D_800AA3A0 < fabsf(delta.x) || D_800AA3A0 < fabsf(delta.z)) {
        midpoint.x = along + delta.x * 0.5f;
        first.x = along - midpoint.x;
        last.x = nz - midpoint.x;
        midpoint.y = angle + delta.y * 0.5f;
        first.y = angle - midpoint.y;
        last.y = nx - midpoint.y;
        midpoint.z = sine + delta.z * 0.5f;
        first.z = sine - midpoint.z;
        last.z = angleStep - midpoint.z;
        inverse = 1.0f / sqrtf(delta.x * delta.x + delta.z * delta.z);
        nz = delta.z * inverse;
        nx = delta.x * inverse;
        angleStep = (last.z * nz + last.x * nx) - (first.z * nz + first.x * nx);
        vertical = last.y - first.y;
        angle = func_150484A0(vertical, angleStep);
        radius = sqrtf(angleStep * angleStep + vertical * vertical) * 0.5f;
        angle -= D_800AA3A4;
        angleStep = D_800AA3A8;
        cursor = (OwnerRibbonPosition32C8 *)(actor + 0x48);
        for (offset = 0; offset != 0xF0; offset += 0x18) {
            actor = (u8 *)cursor;
            sine = sinf(angle);
            along = radius * cosf(angle);
            ((OwnerRibbonPosition32C8 *)actor)->x = along * nx + midpoint.x;
            ((OwnerRibbonPosition32C8 *)actor)->y = radius * sine + midpoint.y;
            ((OwnerRibbonPosition32C8 *)actor)->z = along * nz + midpoint.z;
            angle += angleStep;
            cursor = (OwnerRibbonPosition32C8 *)((u8 *)cursor + 0x18);
        }
    }
    return 1;
}

s32 func_151B3F28(u8 *actor, f32 *output, u8 enabled) {
    OwnerPositionLink3F28 *link;
    s32 result;
    f32 y;

    result = 1;
    if (enabled) {
        link = (OwnerPositionLink3F28 *)(actor + 0x150);
        if (*(s32 *)link->actor != 0 && link->epoch == link->actor[0x3B]) {
            output[0] = *(f32 *)(link->actor + 0x14);
            output[1] = *(f32 *)(link->actor + 0x18);
            output[2] = *(f32 *)(link->actor + 0x1C);
            actor[0x10] &= ~4;
        } else {
            result = 0;
            actor[0x10] |= 0xC;
        }
    } else {
        output[0] = 0.0f;
        y = D_800AA3AC;
        output[2] = 0.0f;
        output[1] = y;
        actor[0x10] &= ~8;
    }
    return result;
}

s32 func_151B3FDC() {
    return 0;
}

s32 func_151B42A4() {
    return 0;
}

s32 func_151B47D8(u8 *actor, OwnerMatrixLink47D8 *link,
    f32 *destination, u8 firstEndpoint) {
    u8 *first;
    u8 *second;
    f32 *point;
    union { s32 mask; u8 *matrix; } selected;

    first = link->first;
    second = link->second;
    if (*(u8 **)(first + 0x1D4) == NULL || *(u8 **)(second + 0x1D4) == NULL) {
        actor[0x10] |= 0xC;
        return 1;
    }
    if (*(s32 *)first == 0 || link->firstEpoch != first[0x3B] ||
        *(s32 *)second == 0 || link->secondEpoch != second[0x3B]) {
        return 0;
    }
    selected.mask = firstEndpoint ? 4 : 8;
    actor[0x10] &= ~selected.mask;
    point = firstEndpoint ? link->firstPosition : link->secondPosition;
    if (firstEndpoint) {
        selected.matrix = *(u8 **)(first + 0x1D4) + (link->firstMatrix << 6);
    } else {
        selected.matrix = *(u8 **)(second + 0x1D4) + (link->secondMatrix << 6);
    }
    func_15143134(point, destination, selected.matrix);
    return 1;
}

s32 func_151B48DC(OwnerPoints3A7C *owner) {
    f32 start, step, x;
    s32 i;

    start = owner->start.x;
    step = -(start - owner->end.x);
    owner->points[0].position.x = start;
    owner->points[0].position.y = 0.0f;
    owner->points[0].position.z = 0.0f;
    step *= D_800AA3C4;
    x = start + step;
    for (i = 1; i < 10; i++) {
        owner->points[i].position.x = x;
        owner->points[i].position.y = 0.0f;
        owner->points[i].position.z = 0.0f;
        x += step;
    }
    owner->flags &= ~2;
    return 1;
}

s32 func_151B498C(u8 *arg0, s32 *arg1, s32 *arg2, s32 *arg3, s32 *arg4,
                  s32 *arg5, s32 *arg6, s32 *arg7, s32 *arg8, s32 *arg9,
                  s32 *arg10, s32 *arg11, u8 *arg12, u8 *arg13) {
    *arg1 = 0x220005;
    *arg2 = 0x40600;
    *arg3 = 0xFF;
    *arg4 = 0xFF;
    *arg5 = 0xFF;
    *arg6 = 0xFF;
    *arg7 = 0xFF;
    *arg8 = 0xFF;
    *arg9 = 0xFF;
    *arg10 = 0xFF;
    *arg11 = 0;
    *arg12 = 5;
    *arg13 = 0x2B;
    return 1;
}

s32 func_151B4A14(u8 *owner, s32 *mode1, s32 *mode2, s32 *envR, s32 *envG,
                  s32 *envB, s32 *alpha, s32 *primR, s32 *primG, s32 *primB,
                  s32 *primA, s32 *renderMode, u8 *bank, u8 *combine) {
    u8 result;
    /* Retain retail scratch allocation; reserved words are never accessed. */
    s32 reserved1, reserved2;
    u8 *object;
    s32 red, green, blue, opacity;
    s32 reserved3;

    result = 1;
    object = *(u8 **)(owner + 0x150);
    func_1502EC34(object, &red, &green, &blue, &opacity);
    if (object[0xA4] & 1) {
        *mode1 = 0x200005;
        *mode2 = 0x60600;
        *envR = red;
        *envG = green;
        *envB = blue;
        *alpha = 0xFF;
        *primB = opacity;
        *primG = opacity;
        *primR = opacity;
        *primA = 0xFF;
        *renderMode = 0x100000;
        *bank = 5;
        *combine = 0x2F;
    } else {
        result = func_151B498C(owner, mode1, mode2, envR, envG, envB, alpha,
            primR, primG, primB, primA, renderMode, bank, combine);
    }
    return result;
}

s32 func_151B4B78(OwnerPoints3A7C *owner) {
    f32 x, step;
    s32 i;

    x = -1000.0f;
    step = D_800AA3C8;
    for (i = 0; i < 10; i++) {
        owner->points[i].position.x = x;
        owner->points[i].position.y = 0.0f;
        owner->points[i].position.z = 0.0f;
        x += step;
    }
    owner->flags &= ~2;
    return 1;
}

void func_151B4C1C(u8 *arg0) {
    void (*callback)(u8 *);

    func_151D5E30(arg0 + 0x140);
    callback = D_8008FB70[arg0[0x44]];
    if (callback != NULL) {
        callback(arg0);
    }
}

void func_151B4C6C(u8 *arg0) {
    func_151B4C1C(arg0);
    func_15169824(arg0);
}

void func_151B4C98(u8 *arg0) {
    func_151B4C1C(arg0);
    func_15169824(arg0);
}
