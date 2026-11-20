#include <ultra64.h>
#include "structs.h"

/* C recoveries and remaining non-matching routines from asm/1AB530.s. */

/* Complete private view; the shared struct162 stops before byte 0x30. */
typedef struct ListRecord1AB530 {
    f32 position[3];
    f32 valueC;
    f32 value10;
    f32 direction[3];
    f32 facingThreshold;
    struct ListRecord1AB530 *next;
    s16 state28;
    u16 sample2A;
    u16 depth2C;
    u8 flags2E;
    u8 first2F;
    u8 second30;
    u8 opaque31[3];
} ListRecord1AB530;

extern ListRecord1AB530 *D_800DDD64;
s32 allocate_memory(s32, s32, s32, s32);

extern s32 D_800BE620, D_800BE624;
extern s32 D_800BE9C4;

/* Append through the captured tail link and initialize only the owned fields. */
struct162 *func_1517E080(s32 first, s32 second) {
    ListRecord1AB530 *node;
    ListRecord1AB530 **link;

    node = D_800DDD64;
    if (node != NULL) {
        while (node->next != NULL) {
            node = node->next;
        }
        link = &node->next;
    } else {
        link = &D_800DDD64;
    }
    node = (ListRecord1AB530 *)allocate_memory(0x34, 1, 0, 1);
    if (node == NULL) {
        return NULL;
    }
    *link = node;
    node->next = NULL;
    node->state28 = 0;
    node->flags2E = 0;
    node->value10 = 0.0f;
    node->valueC = 0.0f;
    node->first2F = first;
    node->second30 = second;
    return (struct162 *)node;
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1AB530/func_1517E134.s")

/* Sample the current RGBA16 image at each in-bounds record position. */
void func_1517E1AC(void) {
    ListRecord1AB530 *node = D_800DDD64;

    while (node != NULL) {
        if (node->valueC >= 0.0f && node->valueC < D_800BE620 &&
            node->value10 >= 0.0f && node->value10 < D_800BE624) {
            node->sample2A = ((u16 *)D_800BE9C4)[(s32)node->valueC + (s32)node->value10 * D_800BE620];
        }
        node = node->next;
    }
}

s32 func_1517E28C() {
    return 0;
}

s32 func_1517E4A8() {
    return 0;
}

Gfx *func_1517EA4C(Gfx *arg0) {
    gDPPipeSync(arg0++);
    gDPSetCombine(arg0++, 0xFFB3FF, 0xFF65FEFF);
    gDPSetOtherMode(arg0++, 0x2C0F, 0x504344);
    return arg0;
}

typedef struct {
    u8 opaque0[0x2F8];
    f32 position[3];
    u8 opaque304[0x7C];
    f32 rotationY;
    u8 opaque384[4];
    f32 rotationX;
    u8 opaque38C[0x260];
    f32 rotationZ;
    u8 opaque5F0[0x3B0];
} ProjectionCamera1AB530;
typedef struct {
    u8 opaque0[0xC];
    f32 scaleX, scaleY;
    u8 opaque14[0x2C];
    Vp viewports[2];
    u8 opaque60[0x120];
} ProjectionView1AB530;
extern ProjectionCamera1AB530 *D_800DBFF0;
extern ProjectionView1AB530 *D_800BE628;
extern s32 D_80082FA4;
void func_15110360(s32, f32 [4][4], f32, f32, f32);
void func_150A7A00(f32 [4][4], f32, f32, f32, f32 *, f32 *, f32 *, f32 *);

/* Project a world point through the active view; reject depths at or below ten. */
s32 func_1517EAAC(f32 x, f32 y, f32 z, f32 *screenX, f32 *screenY) {
    f32 rotationX, rotationY, rotationZ;
    f32 inverse;
    f32 projectedX, projectedY, projectedZ, projectedW;
    f32 matrix[4][4];
    f32 scaleX, scaleY;

    rotationX = -D_800DBFF0[D_80082FA4].rotationX;
    rotationY = -D_800DBFF0[D_80082FA4].rotationY;
    rotationZ = D_800DBFF0[D_80082FA4].rotationZ;
    func_15110360(D_80082FA4, matrix, rotationX, rotationY, rotationZ);
    scaleX = D_800BE628[D_80082FA4].scaleX;
    scaleY = D_800BE628[D_80082FA4].scaleY;
    func_150A7A00(matrix, x, y, z, &projectedX, &projectedY,
                  &projectedZ, &projectedW);
    if (projectedW > 10.0f) {
        inverse = 1.0f / projectedW;
        projectedX = projectedX * scaleX * inverse;
        projectedY = projectedY * scaleY * inverse;
        *screenX = scaleX + projectedX;
        *screenY = scaleY - projectedY;
        return 1;
    }
    *screenX = 0.0f;
    *screenY = 0.0f;
    return 0;
}

typedef struct {
    u32 shift, base;
} PackedDepthRange1AB530;
extern const PackedDepthRange1AB530 D_80089630[8];
extern u8 D_800BE9C0;
f32 sqrtf(f32);
s32 func_1509563C(f32, f32, f32, f32 *, f32 *, f32 *, f32 *, f32);

/* Project the record, apply its optional facing gate, and update depth values. */
s32 func_1517EC1C(ListRecord1AB530 *record, u32 *sampleDepth) {
    f32 dx, dy, dz;
    f32 distance;
    u16 sample;
    PackedDepthRange1AB530 const *range;
    f32 depth, divisor;

    if (func_1509563C(record->position[0], record->position[1], record->position[2],
                      &record->valueC, &record->value10, &depth, &divisor, 4000.0f) == 1) {
        if (record->flags2E & 4) {
            dx = record->position[0] - D_800DBFF0->position[0];
            dy = record->position[1] - D_800DBFF0->position[1];
            dz = record->position[2] - D_800DBFF0->position[2];
            distance = sqrtf((dx * dx + dy * dy) + dz * dz);
            dx = ((dx * record->direction[0] + dy * record->direction[1]) +
                      dz * record->direction[2]) / distance;
            if (dx < record->facingThreshold) {
                return 1;
            }
        }
        sample = record->sample2A;
        /* The immutable range table contains only shift counts zero through six. */
        range = &D_80089630[sample >> 13];
        *sampleDepth = (range->base + (((sample >> 2) & 0x7FFU) << range->shift)) >> 3;
        record->depth2C = (u32)(((depth / divisor) * D_800BE628->viewports[D_800BE9C0].vp.vscale[2] +
                               D_800BE628->viewports[D_800BE9C0].vp.vtrans[2]) * 32.0f);
        return 1;
    }
    return 0;
}
