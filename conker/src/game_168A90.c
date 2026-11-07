#include <ultra64.h>

#include "functions.h"
#include "variables.h"

typedef struct {
    u8 field0, field1, field2, pad3;
    s16 field4;
    u8 pad6[2];
    s32 field8, fieldC, field10, field14, field18, field1C, field20;
    u8 field24, field25, pad26[10];
    s32 field30, field34;
    u8 field38;
} EffectDescriptor1513BAE8;
typedef struct { f32 value0, value4, value8, valueC, value10; } EffectPayload1513BAE8;

void *func_1502B6BC(s32 *, s32, s32 *, s32, ...);
void *func_15167A68(s32, s32, s32, s32, u8, u8);
s32 func_1510CE60(void *, s32, s32, s32, s32 *);

typedef struct { s32 first, count; } TextureVertexRange168A90;
extern f32 D_800A49C0[9][3];
extern TextureVertexRange168A90 D_800A4A2C[9];
extern f32 D_800A4A74, D_800A4A78, D_800A4A7C, D_800A4A80;
f32 *func_15144B34(s32);

/* Generated placeholder declarations. */
s32 func_1513B5E0(EffectDescriptor1513BAE8 *descriptor, u8 mode, s32 extraSize, u8 priority, s32 context);
void func_1513B798(u8 *arg0);
Gfx *func_1513B83C(Gfx *displayList, u8 *resource, s16 view);
s32 func_1513BAE8(void);
s32 func_1513BBFC(u8 *resource, s16 view);
s32 func_1513BEB0();
s32 func_15109064(struct132 *, s32, u8);
void func_151BA468(struct132 *, s32, u8);
/* End generated placeholder declarations. */

extern s32 (*D_80089C18[])(u8 *);
extern s32 (*D_80089C28[])(u8 *, s16);

/* Create two resource buffers per live view, retaining the initial total size. */
s32 func_1513B5E0(EffectDescriptor1513BAE8 *descriptor, u8 mode, s32 extraSize, u8 priority, s32 context) {
    u8 *created;
    u8 *asset;
    u32 bufferBytes;
    u8 *source;
    u8 *cursor;
    s32 lookupSize;
    s32 lookupStatus;
    s32 index;
    u8 *row;
    s32 bytes;
    void *end;

    asset = func_1502B6BC(&lookupSize, 0, &lookupStatus, 2,
                         descriptor->field30, descriptor->field34);
    bytes = (u32)*(u8 **)asset - (u32)asset - 40;
    bufferBytes = ((u32)bytes * 2) * ((u32)D_80082FA0 + 1);
    created = func_15167A68(mode != 0 ? 0x54 : 0x38, context,
                           (u32)extraSize + bufferBytes + 248, 2, priority, 1);
    if (created == NULL) return 0;
    memcpy(created + 16, descriptor, 60);
    *(u8 **)(created + 0x4C) = asset;
    row = created;
    cursor = created + 248;
    source = asset + 40;
    index = 0;
    if ((s32)((u32)D_80082FA0 + 1) > 0) {
        do {
            *(u8 **)(row + 0x58) = cursor;
            *(u8 **)(row + 0x68) = cursor + bytes;
            memcpy(cursor, source, bytes);
            memcpy(*(u8 **)(row + 0x68), source, bytes);
            row += 4;
            cursor += (u32)bytes * 2;
            index = (u32)index + 1;
        } while (index <= D_80082FA0);
    }
    end = *(void **)asset;
    *(void **)(created + 0x54) = end;
    *(u32 *)(created + 0x50) = bufferBytes;
    func_1510CE60(end, 0, 1, 62, 0);
    return (s32)(u32)created;
}
void func_1513B798(u8 *arg0) {
    s32 remove = 0;
    s8 callbackIndex;

    if ((arg0[0x10] & 1) != 0) {
        *(s16 *)(arg0 + 0x14) -= D_800BE9E4;
        if (*(s16 *)(arg0 + 0x14) < 0) {
            remove = 1;
        }
    }

    if (remove == 0) {
        callbackIndex = *(s8 *)(arg0 + 0x11);
        if ((callbackIndex != -1) && (D_80089C18[callbackIndex](arg0) == 0)) {
            remove = 1;
        }
    }

    if (remove != 0) {
        func_1516972C((struct102 *)arg0);
    }
}
/* Submit the resource's three graphics commands after per-view filtering. */
Gfx *func_1513B83C(Gfx *displayList, u8 *resource, s16 view) {
    s8 callbackIndex;

    if ((resource[0x10] & 2) != 0 &&
        (resource[0x49] & (1U << view)) == 0) {
        return displayList;
    }
    callbackIndex = *(s8 *)(resource + 0x12);
    if (callbackIndex != -1 && D_80089C28[callbackIndex](resource, view) == 0) {
        return displayList;
    }
    gSPMatrix(displayList++, (Mtx *)(resource + 0x78 + ((u32)D_800BE9C0 << 6)),
              G_MTX_MODELVIEW | G_MTX_LOAD | G_MTX_NOPUSH);
    gSPSegment(displayList++, 1,
               *(u32 *)(resource + 0x58 + ((u32)D_800BE9C0 << 4) + (s32)view * 4));
    gSPDisplayList(displayList++, *(Gfx **)(resource + 0x54));
    return displayList;
}

s32 func_1513B968(s32 arg0, s16 arg1) {
    // FIXME: &arg0->unk_120[D_800BE9C0]
    func_150A7B80(arg0 + 120 + (D_800BE9C0 << 6));
    return 1;
}

void func_1513B9A8(struct132 *arg0) {
    func_100043B4(arg0->unk4C, 4);
    func_15169804(arg0);
}

void func_1513B9DC(struct132 *arg0) {
    func_100043B4(arg0->unk4C, 4);
    func_15169824(arg0);
}

void func_1513BA10(struct132 *arg0) {
    D_80089C44[arg0->unk48]();
}

void func_1513BA44(struct132 *arg0) {
    D_80089C54[arg0->unk48]();
}

void func_1513BA78(struct132 *arg0, s32 arg1, u8 arg2) {
    switch (arg0->unk48) {
        case 1:
            func_15109064(arg0, arg1, arg2);
            break;
        case 2:
            func_151BA468(arg0, arg1, arg2);
            break;
    }
}

s32 func_1513BAD4(s32 arg0, s32 arg1) {
    return 0;
}

/* Build the fixed effect and preserve its handle even on validation release. */
s32 func_1513BAE8(void) {
    u32 handle;
    EffectDescriptor1513BAE8 descriptor;
    EffectPayload1513BAE8 payload;
    payload.value0 = 0.0f;
    payload.value4 = 0.0f;
    payload.valueC = 0.0f;
    payload.value10 = 0.0f;
    payload.value8 = 0.0f;
    descriptor.field0 = 0;
    descriptor.field1 = 2;
    descriptor.field2 = 5;
    descriptor.field4 = 300;
    descriptor.field30 = 9;
    descriptor.field34 = 430;
    descriptor.field8 = 1;
    descriptor.fieldC = 0x220205;
    descriptor.field10 = 0x40600;
    descriptor.field24 = 0;
    descriptor.field25 = 0;
    descriptor.field14 = 1;
    descriptor.field18 = 54;
    descriptor.field1C = 128;
    descriptor.field20 = 32;
    descriptor.field38 = 3;
    handle = func_1513B5E0(&descriptor, 1, 20, 255, 1);
    if (handle != 0) {
        if (*(s32 *)(handle + 0x50) != 0x1180) {
            func_1516972C((struct102 *)handle);
        } else {
            memcpy((void *)(handle + *(s32 *)(handle + 0x50) + 0xF8), &payload, 20);
        }
    }
    return handle;
}
/* Update texture coordinates for the resource's nine vertex groups. */
s32 func_1513BBFC(u8 *resource, s16 view) {
    f32 *payload;
    f32 *viewer;
    f32 *center;
    TextureVertexRange168A90 *range;
    f32 scaleS, scaleT, wrappedS, wrappedT;
    f32 directionX, directionZ, inverse, horizontal, vertical;
    f32 x, y, z, dx, dy, dz;
    Vtx *vertex;
    s32 index;

    func_1513B968((s32)resource, view);
    payload = (f32 *)(resource + *(u32 *)(resource + 0x50) + 0xF8);
    scaleS = sinf(payload[3]) * D_800A4A74 + D_800A4A78;
    scaleT = sinf(payload[4]) * D_800A4A7C + D_800A4A80;
    viewer = func_15144B34(view);
    wrappedS = payload[0] - (f32)(s32)(payload[0] * (1.0f / 1024.0f)) * 1024.0f;
    wrappedT = payload[1] - (f32)(s32)(payload[1] * (1.0f / 1024.0f)) * 1024.0f;
    center = D_800A49C0[0];
    range = D_800A4A2C;
    do {
        horizontal = center[0] - viewer[0];
        vertical = center[2] - viewer[2];
        if (horizontal != 0.0f || vertical != 0.0f) {
            inverse = 1.0f / sqrtf(horizontal * horizontal + vertical * vertical);
            directionX = vertical * inverse;
            directionZ = -horizontal * inverse;
        } else {
            directionX = 1.0f;
            directionZ = 0.0f;
        }
        for (index = range->first;
             index < range->first + range->count;
             index = (u32)index + 1) {
            vertex = *(Vtx **)(resource + 0x58 + ((u32)D_800BE9C0 << 4) + (s32)view * 4) + index;
            x = vertex->v.ob[0];
            y = vertex->v.ob[1];
            z = vertex->v.ob[2];
            dx = x - center[0];
            dy = y - center[1];
            dz = z - center[2];
            vertex->v.tc[0] = (s32)((dx * directionX + dz * directionZ) * scaleS - wrappedS);
            vertex->v.tc[1] = (s32)(dy * scaleT - wrappedT);
        }
        range++;
        center += 3;
    } while (range != (TextureVertexRange168A90 *)&D_800A4A74);
    return 1;
}
/* Non-matching C placeholders for asm/nonmatchings/game_168A90/func_1513BEB0.s. */
s32 func_1513BEB0() {
    return 0;
}
