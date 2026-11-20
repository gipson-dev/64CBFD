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

void func_10004074(void *);

/* Unlink before freeing. Known callers also pass an actor context that retail ignores. */
void func_1517E134(void *target, void *unusedActor) {
    ListRecord1AB530 *node;

    if (target == D_800DDD64) {
        D_800DDD64 = ((ListRecord1AB530 *)target)->next;
    } else {
        node = D_800DDD64;
        while (node != NULL && node->next != target) {
            node = node->next;
        }
        if (node == NULL) {
            return;
        }
        node->next = ((ListRecord1AB530 *)target)->next;
    }
    func_10004074(target);
}

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

typedef struct { u8 values[2]; } ListFlarePair1AB530;
extern const ListFlarePair1AB530 D_8008D004, D_8008D008, D_8008D00C;
extern u8 D_800DDD60, D_800DCDD0, D_800DD2D0;
extern u8 *D_800B0DF0;
extern f32 *D_8008CFFC[2];
s32 func_1517EAAC(f32, f32, f32, f32 *, f32 *);
s32 func_1517EC1C(ListRecord1AB530 *, u32 *);
Gfx *func_1517E4A8(Gfx *, ListRecord1AB530 *, s32, s32, s32, s32, u8 *);

/* Project enabled list records, choose their flare parameters, and submit them. */
Gfx *func_1517E28C(Gfx *commands, s32 unusedCategory) {
    /* Keep the retail carry slots; the depth helper can leave its output untouched. */
    s32 strength;
    s32 skip;
    u32 sampleDepth;
    s32 flags;
    ListRecord1AB530 *node;
    ListFlarePair1AB530 groups = D_8008D004;
    ListFlarePair1AB530 counts = D_8008D008;
    ListFlarePair1AB530 falloffs = D_8008D00C;

    node = D_800DDD64;
    D_800DDD60 = 0;
    while (node != NULL) {
        if (node->second30 != 0) {
            skip = 0;
            flags = node->flags2E;
            if (flags & 1) {
                if (D_800DCDD0 == 0) {
                    skip = 1;
                } else {
                    f32 *position = D_8008CFFC[D_800B0DF0[0x10]];
                    if (func_1517EAAC(position[0], position[1], position[2],
                                      &node->valueC, &node->value10) != 1) {
                        skip = 1;
                    }
                    strength = 255;
                    if (node->sample2A != 0xFFFC) {
                        strength = -1;
                    }
                    flags = node->flags2E;
                }
            } else {
                if (func_1517EC1C(node, &sampleDepth) != 1) {
                    skip = 1;
                }
                strength = -1;
                if ((s32)((u32)node->depth2C - sampleDepth) < 30) {
                    strength = 256;
                }
                flags = node->flags2E;
            }
            {
                u8 *intensity = (flags & 2) ? &D_800DD2D0 : NULL;
                if (skip == 0) {
                    commands = func_1517E4A8(commands, node, groups.values[node->first2F],
                        counts.values[node->first2F], falloffs.values[node->first2F], strength, intensity);
                } else if (intensity != NULL) {
                    *intensity = 0;
                }
            }
        }
        node = node->next;
    }
    return commands;
}

typedef struct {
    u32 unk0;
    u16 unk4, unk6;
    u8 unk8, unk9, unkA, padB;
} FlareDescriptor1AB530;
typedef struct {
    s16 coordinates[3];
    s16 extentX, extentY;
    u8 alpha, animationStep, animationFrame, flipFlags;
    u8 paddingE[2];
    FlareDescriptor1AB530 *descriptor;
} FlareDrawPacket1AB530;
extern FlareDescriptor1AB530 D_800903AC;
extern const u8 D_800A7250[16];
extern s32 D_800BE9E4;
extern f32 D_800380A0, D_800380A4;
extern u8 D_800D2DA8, D_800D2DA9, D_800D2DAA, D_800D2DAB;
f32 fabsf(f32);
#pragma intrinsic (fabsf)
Gfx *func_1517EA4C(Gfx *);
s32 func_150950D4(s32, FlareDescriptor1AB530 *, s32, s32, s32, s32, s32, s32, s32, s32);
Gfx *func_15095A48(Gfx *, FlareDrawPacket1AB530 *, f32, f32);

/* Smooth flare intensity, prepare the sprite state, then submit its palette row. */
Gfx *func_1517E4A8(Gfx *commands, ListRecord1AB530 *record, s32 group,
                    s32 count, s32 falloff, s32 strength, u8 *intensity) {
    f32 centerX = record->valueC - D_800BE620 * 0.5f;
    f32 centerY = record->value10 - D_800BE624 * 0.5f;
    s32 distance;
    s32 desired;
    s32 value;
    s32 index;
    s32 factor;
    const u8 *palette;
    f32 x, y;
    FlareDrawPacket1AB530 packet;

    if (intensity != NULL) {
        if (strength == -1) {
            desired = 0;
        } else {
            distance = ((s32)centerX * (s32)centerX + (s32)centerY * (s32)centerY) * falloff / 10;
            if (distance < 120) {
                desired = (120 - distance) * 176 / 120;
            } else {
                desired = 0;
            }
        }
        value = *intensity;
        if ((desired - value < 0 ? value - desired : desired - value) < (D_800BE9E4 * 5)) {
            value = desired;
        } else if (value < desired) {
            value += (D_800BE9E4 * 5);
        } else {
            value -= (D_800BE9E4 * 5);
        }
        *intensity = value;
    }
    distance = ((s32)centerX * (s32)centerX + (s32)centerY * (s32)centerY) * falloff / 10;
    if (record->valueC < 2.0f || record->valueC >= D_800BE620 - 2 ||
        record->value10 < 0.0f || record->value10 >= D_800BE624) {
        desired = 0;
    } else if (strength == -1) {
        desired = 0;
    } else {
        desired = (1760000 / (distance + 10000) * strength) / 256;
    }
    value = record->state28;
    if ((desired - value < 0 ? value - desired : desired - value) < (D_800BE9E4 * 10)) {
        record->state28 = desired;
    } else if (desired < value) {
        record->state28 = value - (D_800BE9E4 * 10);
    } else {
        record->state28 = value + (D_800BE9E4 * 10);
    }

    if (distance < 200000 && record->state28 > 0 &&
        fabsf(record->valueC) < 2000.0f && fabsf(record->value10) < 2000.0f) {
        D_800D2DA8 = 255;
        D_800D2DA9 = 255;
        D_800D2DAA = 255;
        packet.descriptor = &D_800903AC;
        packet.animationStep = 0;
        packet.animationFrame = 0;
        packet.flipFlags = 0;
        if (D_800DDD60 == 0) {
            commands = func_1517EA4C(commands);
            commands = (Gfx *)(u32)func_150950D4((s32)commands, &D_800903AC, 0, 0, 0, 0, 2, 256, 256, 3);
            D_800DDD60 = 1;
        }
        value = (record->state28 * record->second30) >> 8;
        palette = D_800A7250 + group * 7;
        factor = 2;
        for (index = 0; index < count; index++) {
            x = record->valueC - centerX * (f32)factor / 5.0f;
            y = record->value10 - centerY * (f32)factor / 5.0f;
            desired = palette[index];
            y += desired * 0.015625f;
            packet.alpha = value;
            D_800D2DAB = 0;
            packet.extentX = (s32)((desired << 12) * D_800380A0 / 255.0f);
            packet.extentY = (s32)((desired << 12) * D_800380A4 / 255.0f);
            commands = func_15095A48(commands, &packet, x, y);
            gDPPipeSync(commands++);
            factor += 2;
        }
    }
    return commands;
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
