#include <ultra64.h>
#include "structs.h"

/* Animated quad records and remaining functions from asm/19F150.s. */

typedef struct {
    u8 opaque0[0x10];
    Vtx vertices[4];
    s16 lifetime;
    s16 frame;
    s16 frameStep;
    u16 color;
    u8 imageIndex;
    u8 flags;
    u8 opaque5A[6];
} QuadEffect19F150;

void *func_15167A68(s32, s32, s32, s32, u8, u8);

/* Allocate an animated quad and initialize its metadata and vertex flags. */
void *func_15171CA0(s16 lifetime, u16 color, u8 imageIndex, s32 flags,
                    s32 frameStep, s32 alternate, u8 slot, s32 context) {
    QuadEffect19F150 *record;

    record = func_15167A68(alternate == 0 ? 0xF : 0x43, context,
                          sizeof(QuadEffect19F150), 1, slot, 1);
    if (record == NULL) {
        return NULL;
    }
    record->lifetime = lifetime;
    record->frame = 0;
    record->frameStep = frameStep;
    record->color = color;
    record->imageIndex = imageIndex;
    record->flags = flags;
    record->vertices[0].v.flag = 0;
    record->vertices[1].v.flag = 0;
    record->vertices[2].v.flag = 0;
    record->vertices[3].v.flag = 0;
    return record;
}

s32 func_15171D4C() {
    return 0;
}

extern s32 D_800BE9E4;
extern u8 *D_8008CA4C[];
s32 func_151725FC(Vtx *, void *, f32, f32, f32, f32, s32, u8);
void func_1516972C(struct102 *);

/* Allocate an animated quad, build its vertices, and release it if geometry setup fails. */
void func_15171F04(f32 x, f32 y, f32 z, void *indirectVertices,
                   s16 lifetime, u16 color, u8 imageIndex, s32 scale,
                   s32 flags, s32 frameStep, s32 alternate, u8 slot, s32 context) {
    QuadEffect19F150 *record;

    record = func_15171CA0(lifetime, color, imageIndex, flags,
                          frameStep, alternate, slot, context);
    if (record != NULL) {
        if (func_151725FC(record->vertices, indirectVertices, x, y, z, 0.0f,
                         scale, *(u16 *)(D_8008CA4C[record->imageIndex] + 6)) == 0) {
            func_1516972C((struct102 *)record);
        }
    }
}

/* Advance an animated quad's lifetime and 8.8 fixed-point image frame. */
void func_15171FC0(QuadEffect19F150 *record) {
    s32 frameCount;

    if (record->lifetime < -1) {
        record->lifetime++;
        if (record->lifetime == -1) {
            func_1516972C((struct102 *)record);
        }
    } else if (record->lifetime == 0) {
        record->lifetime = -3;
    } else if (record->lifetime != -1) {
        if ((record->flags & 4) == 0) {
            if (record->lifetime > D_800BE9E4) {
                record->lifetime = (s32)((u32)record->lifetime -
                                         (u32)D_800BE9E4);
            } else {
                record->lifetime = 0;
            }
        }
        record->frame += record->frameStep;
        frameCount = D_8008CA4C[record->imageIndex][4];
        if (record->frame / 256 >= frameCount) {
            if (record->flags & 4) {
                record->lifetime = -3;
            } else {
                record->frame = (frameCount << 8) - 256;
            }
        }
    }
}

s32 func_151720C4() {
    return 0;
}

s32 func_151725FC(Vtx *vertices, void *indirectVertices, f32 x, f32 y, f32 z,
                   f32 rotation, s32 scale, u8 imageControl) {
    return 0;
}

extern f32 D_800A7154, D_800A7158;
f32 cosf(f32);
f32 sinf(f32);
void func_1510E82C(s32, s32, s32, s32, s32, s32,
                   f32, f32, f32, f32, u16, s32);

/* Place a quad at a projected ground contact, if one exists. */
s32 func_15172B20(Vtx *vertices, f32 x, f32 y, f32 z, f32 angle,
                  s32 radius, s32 scale, u8 imageControl) {
    s32 hit, surface;
    f32 height;
    f32 radians = (angle - 90.0f) * D_800A7154;
    f32 c = cosf(radians);
    f32 s = sinf(radians);
    x += (f32)radius * s;
    z += (f32)radius * c;
    func_1510E82C((s32)&hit, 0, (s32)&height, 0, (s32)&surface, 0,
                  x, y, z, y, 0, 0);
    if (hit == 0 || height == D_800A7158) return 0;
    return func_151725FC(vertices, (void *)hit, x, height, z, angle, scale, imageControl);
}
