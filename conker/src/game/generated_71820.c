#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/71820.s. */

extern s32 D_800CBD9C;
extern u8 D_800C35EA;
extern u8 D_800CC2D0[];

typedef struct PositionScaleRecord71820 {
    struct PositionScaleRecord71820 *next;
    s16 lifetime;
    s16 x;
    s16 y;
    s16 z;
    u8 type;
    u8 selector;
    u8 state;
    u8 padF;
    s16 scaleX;
    s16 scaleY;
    s16 scaleZ;
    u8 flags;
    u8 pad17;
    s16 *position;
    s16 *scale;
} PositionScaleRecord71820;

typedef struct QueryVertex71820 {
    s16 x;
    s16 y;
    s16 z;
    u8 pad6[10];
} QueryVertex71820;

typedef struct QueryTriangle71820 {
    QueryVertex71820 *vertices[3];
} QueryTriangle71820;

typedef struct HeightCandidate71820 {
    s32 fixedHeight;
    QueryTriangle71820 *triangle;
    s32 vertexIndex;
    s32 padC;
} HeightCandidate71820;

typedef struct HeightResult71820 {
    f32 height;
    s16 vertices[9];
    s16 pad16;
    u32 metadata;
    u8 flags;
    u8 state;
    u16 pad1E;
    s32 value;
} HeightResult71820;

typedef struct HeightEntity71820 {
    u8 pad0[0x40];
    u32 metadata;
    u32 *metadataTable;
    u8 pad48[0x10];
    u16 firstTriangle;
    u8 pad5A[0x15];
    u8 flags;
    u8 pad70[0x30];
} HeightEntity71820;

extern HeightCandidate71820 D_800D3300[];
extern QueryTriangle71820 *D_800DBE3C;
extern u32 *D_800DBE5C;
extern f32 D_800DBE68, D_800DBE6C, D_800DBE70, D_800DBE74;
extern f32 D_80098D44;
extern f32 D_80098D48;
extern f32 D_80098D4C;
extern f32 D_80098D50;
extern f32 D_80098D54;
extern f32 D_80098D5C;
extern u8 D_800D3830[];
extern u8 D_800D37E0[];
extern HeightEntity71820 *D_800DBEF4;
s32 func_150A3A70(s32 x, s32 z);
s32 func_150A4FA0(s32 x, s32 z);
void func_150A44F0(s32 value, void *scratch, s32 mode);
s32 func_150A43E0(s32 x, s32 z, s32 value, void *scratch);
s32 func_150A6500(s32 x, s32 z, s32 *secondaryCount, s32 selector);
s32 func_150A3FC4(f32 x, f32 z, QueryTriangle71820 *triangle, s16 *vertices, f32 *height);
s32 func_15045F8C(f32 *position, f32 threshold, s32 *input, HeightResult71820 *result);

extern PositionScaleRecord71820 *D_800CBE00;
extern s32 D_800BE9E4;
extern s32 (*D_80085E80[])(PositionScaleRecord71820 *record);
extern void (*D_80085E8C[])(void);
s32 allocate_memory(s32 size, s32 mode, s32 arg2, s32 arg3);
void func_100043B4(s32 *record, u32 mode);
f32 func_15048A40(u8 angle);
f32 func_150489B0(u8 angle);
f32 fabsf(f32 value);
#pragma intrinsic (fabsf)

void func_15047390(f32 mf[4][4], f32 xEye, f32 yEye, f32 zEye,
                   f32 xAt, f32 yAt, f32 zAt, f32 xUp, f32 yUp, f32 zUp);
void func_15047700(f32 mf[4][4], LookAt *l, f32 xEye, f32 yEye, f32 zEye,
                   f32 xAt, f32 yAt, f32 zAt, f32 xUp, f32 yUp, f32 zUp);
void func_1505D1C4(f32 arg0, f32 arg1, f32 arg2, s32 arg3, s32 arg4,
                   u16 arg5, s32 arg6, s32 arg7);
s32 func_1504697C(f32 *position, u16 selector, f32 threshold, HeightResult71820 *result);
s32 func_15046D00(f32 *position, u16 selector, f32 threshold, HeightResult71820 *result);
s32 func_15047004(f32 *position, f32 threshold, HeightResult71820 *result);
s32 func_150470B0(f32 *position, f32 threshold, HeightResult71820 *result);
s32 func_15044ED0(f32 *position, f32 threshold, HeightResult71820 *result);
s32 func_150466F8(f32 *position, u16 selector, f32 threshold, HeightResult71820 *result);
PositionScaleRecord71820 *func_15044964(s32 size, s32 type, s32 arg2, s32 arg3,
                                       s32 arg4, s32 x, s32 y, s32 z);

void func_15044370() {
    D_800CBD9C = 0;
}

s32 func_15044380() {
    return 0;
}

s32 func_1504452C() {
    return 0;
}

void func_15044658() {
}

s32 func_15044660() {
    return 0;
}

PositionScaleRecord71820 *func_150448D0(s32 arg0, s32 arg1, s32 arg2, s32 arg3,
                                       s32 arg4, s32 arg5, s32 arg6,
                                       s16 *arg7, s16 *arg8) {
    PositionScaleRecord71820 *record;

    record = func_15044964(0x20, 1, arg0, arg1, arg2, 0, 0, 0);
    if (record == NULL) {
        return NULL;
    }
    record->scaleX = arg3;
    record->scaleY = arg4;
    record->scaleZ = arg5;
    record->flags = arg6;
    record->position = arg7;
    record->scale = arg8;
    return record;
}

PositionScaleRecord71820 *func_15044964(s32 size, s32 type, s32 arg2, s32 arg3,
                                       s32 arg4, s32 x, s32 y, s32 z) {
    PositionScaleRecord71820 *record;
    PositionScaleRecord71820 *head;
    PositionScaleRecord71820 *current;
    PositionScaleRecord71820 *next;

    record = (PositionScaleRecord71820 *)allocate_memory(size, 1, 0, 0);
    if (record == NULL) {
        return NULL;
    }
    record->next = NULL;
    record->lifetime = arg2;
    record->type = type;
    record->selector = arg4;
    record->state = arg3;
    record->x = x;
    record->y = y;
    record->z = z;
    head = D_800CBE00;
    if (head == NULL) {
        D_800CBE00 = record;
    } else {
        next = head->next;
        current = head;
        while (next != NULL) {
            current = next;
            next = next->next;
        }
        current->next = record;
    }
    return record;
}

void func_15044A28(void) {
    PositionScaleRecord71820 *record = D_800CBE00;
    PositionScaleRecord71820 *previous = NULL;
    PositionScaleRecord71820 *next;
    s32 value;
    s32 state;
    s32 type;

    while (record != NULL) {
        state = record->state;
        type = record->type;
        next = record->next;
        if (state == 0) {
            if (D_80085E80[type](record) != 0) {
                D_80085E8C[record->selector]();
            }
        } else {
            value = (s32)((u32)state - (u32)D_800BE9E4);
            if (value < 0) {
                value = 0;
            }
            record->state = value;
        }
        value = record->lifetime;
        if (value != -1) {
            value = (s32)((u32)value - (u32)D_800BE9E4);
            if (value <= 0) {
                if (previous == NULL) {
                    D_800CBE00 = record->next;
                } else {
                    previous->next = record->next;
                }
                func_100043B4((s32 *)record, 2);
            } else {
                record->lifetime = value;
                previous = record;
            }
        } else {
            previous = record;
        }
        record = next;
    }
}

s32 func_15044B78(PositionScaleRecord71820 *record) {
    u8 *player = D_800CC2D0;
    f32 first;
    f32 second;
    f32 x;
    f32 y;
    f32 z;
    f32 rotatedX;
    u8 *dimensions = *(u8 **)(player + 0x31C);
    s32 halfHeight = *(s16 *)(dimensions + 0x114) >> 1;
    s32 extentZ = *(s16 *)(dimensions + 0x116);
    s32 extentX = *(s16 *)(dimensions + 0x118);

    x = *(f32 *)(player + 0x14) - record->x;
    y = (*(f32 *)(player + 0x18) - record->y) + halfHeight;
    z = *(f32 *)(player + 0x1C) - record->z;
    first = func_15048A40(record->flags);
    second = func_150489B0(record->flags);
    rotatedX = z * second + x * first;
    x = x * second - z * first;

    if (fabsf(y) < (f32)(record->scaleZ + halfHeight) &&
        fabsf(x) < (f32)(record->scaleY + extentZ) &&
        fabsf(rotatedX) < (f32)(record->scaleX + extentX)) {
        return 1;
    }
    return 0;
}

s32 func_15044CE4(PositionScaleRecord71820 *arg0) {
    s32 value;
    s16 *position = arg0->position;
    s16 *scale = arg0->scale;

    arg0->x = position[0];
    arg0->y = position[1];
    arg0->z = position[2];
    value = scale[0] / 32;
    arg0->scaleX = value;
    arg0->scaleY = value;
    arg0->scaleZ = value;
    return func_15044B78(arg0);
}

s32 func_15044D40(PositionScaleRecord71820 *arg0) {
    func_1505D1C4(arg0->x, arg0->y, arg0->z, arg0->scaleX, 0xFF, 0, 0, 0);
    return 0;
}

void func_15044DA0() {
    if ((D_800CC2D0[0x104] == 0) && (D_800CC2D0[0x125] == 0)) {
        func_1505D024(D_800CC2D0, 5, *(u16 *) (D_800CC2D0 + 0x7A), -1);
    }
}

void func_15044DE8() {
    if ((D_800CC2D0[0x104] == 0) && (D_800CC2D0[0x125] == 0) &&
            (D_800C35EA != 1)) {
        func_1505D024(D_800CC2D0, 4, *(u16 *) (D_800CC2D0 + 0x7A), -1);
    }
}

void func_15044E40() {
    if ((D_800CC2D0[0x104] == 0) && (D_800CC2D0[0x125] == 0)) {
        func_1505D024(D_800CC2D0, 0x40, *(u16 *) (D_800CC2D0 + 0x7A), -1);
    }
}

void func_15044E88() {
    if ((D_800CC2D0[0x104] == 0) && (D_800CC2D0[0x125] == 0)) {
        func_1505D024(D_800CC2D0, 1, *(u16 *) (D_800CC2D0 + 0x7A), -1);
    }
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_71820/func_15044ED0.s")

s32 func_150450CC(f32 *position, f32 threshold, HeightResult71820 *result) {
    s32 selected = -1;
    s32 count;
    s32 i;
    f32 height;
    HeightCandidate71820 *candidate;
    QueryVertex71820 *vertex;
    QueryVertex71820 **vertexPointers;
    s32 vertexIndex;

    if (position[1] < threshold) {
        result->flags &= ~2;
        return 0;
    }
    result->height = D_80098D44;
    func_1510F800(0);
    D_800DBE68 = position[0];
    D_800DBE6C = position[1];
    D_800DBE70 = position[2];
    D_800DBE74 = threshold;
    count = func_150A3A70((s32)position[0], (s32)position[2]);
    for (i = 0; i < count; i++) {
        height = D_800D3300[i].fixedHeight * (1.0f / 256.0f);
        if (height <= position[1] && result->height < height) {
            selected = i;
            result->height = height;
        }
    }
    if (selected != -1) {
        candidate = &D_800D3300[selected];
        vertexPointers = candidate->triangle->vertices;
        vertexIndex = candidate->vertexIndex;
        for (i = 0; i != 3; i++) {
            vertex = &vertexPointers[i][vertexIndex];
            result->vertices[i * 3] = vertex->x;
            result->vertices[i * 3 + 1] = vertex->y;
            result->vertices[i * 3 + 2] = vertex->z;
        }
        if (D_800DBE5C != NULL) {
            result->metadata = D_800DBE5C[candidate->triangle - D_800DBE3C];
        } else {
            result->metadata = 0;
        }
        result->state = 1;
        result->flags |= 7;
        result->value = 0;
        if (threshold <= result->height) {
            result->flags |= 2;
            return 1;
        }
        return 0;
    }
    result->flags &= ~2;
    return 0;
}

s32 func_1504530C(f32 *arg0, f32 arg1, HeightResult71820 *arg2) {
    switch (func_150470B0(arg0, arg1, arg2)) {
        case 0:
            return func_15044ED0(arg0, arg1, arg2);
        case 1:
            return 0;
        case 2:
            return 1;
    }
}

s32 func_15045384(f32 *position, f32 threshold, HeightResult71820 *result) {
    s32 selected;
    s32 count;
    s32 i;
    f32 height;
    HeightCandidate71820 *candidate;
    QueryVertex71820 *vertex;
    QueryVertex71820 **vertexPointers;
    s32 vertexOffset;

    if (threshold < position[1]) {
        result->flags &= ~2;
        return 0;
    }
    result->height = D_80098D48;
    selected = -1;
    func_1510F800(3);
    count = func_150A4FA0((s32)position[0], (s32)position[2]);
    for (i = 0; i < count; i++) {
        height = D_800D3300[i].fixedHeight * (1.0f / 256.0f);
        if (position[1] <= height && height < result->height) {
            selected = i;
            result->height = height;
        }
    }
    if (selected != -1) {
        candidate = &D_800D3300[selected];
        vertexPointers = candidate->triangle->vertices;
        vertexOffset = candidate->vertexIndex;
        /* Context 3 supplies a byte offset, unlike the indexed context 0 query. */
        for (i = 0; i != 3; i++) {
            vertex = (QueryVertex71820 *)((u8 *)vertexPointers[i] + vertexOffset);
            result->vertices[i * 3] = vertex->x;
            result->vertices[i * 3 + 1] = vertex->y;
            result->vertices[i * 3 + 2] = vertex->z;
        }
        result->metadata = 0;
        result->flags |= 6;
        result->state = 4;
        result->value = 0;
        if (result->height <= threshold) {
            result->flags |= 2;
            return 1;
        }
        return 0;
    }
    result->flags &= ~2;
    return 0;
}

s32 func_1504554C(f32 *position, f32 threshold, HeightResult71820 *result) {
    s32 selected;
    s32 count;
    s32 i;
    f32 height;
    HeightCandidate71820 *candidate;
    QueryVertex71820 *vertex;
    QueryVertex71820 **vertexPointers;
    s32 vertexOffset;

    if (position[1] < threshold) {
        result->flags &= ~2;
        return 0;
    }
    result->height = D_80098D4C;
    selected = -1;
    func_1510F800(3);
    count = func_150A4FA0((s32)position[0], (s32)position[2]);
    for (i = 0; i < count; i++) {
        height = D_800D3300[i].fixedHeight * (1.0f / 256.0f);
        if (height <= position[1] && result->height < height) {
            selected = i;
            result->height = height;
        }
    }
    if (selected != -1) {
        candidate = &D_800D3300[selected];
        vertexPointers = candidate->triangle->vertices;
        vertexOffset = candidate->vertexIndex;
        /* Context 3 supplies a byte offset, unlike the indexed context 0 query. */
        for (i = 0; i != 3; i++) {
            vertex = (QueryVertex71820 *)((u8 *)vertexPointers[i] + vertexOffset);
            result->vertices[i * 3] = vertex->x;
            result->vertices[i * 3 + 1] = vertex->y;
            result->vertices[i * 3 + 2] = vertex->z;
        }
        result->metadata = 0;
        result->flags |= 6;
        result->state = 4;
        result->value = 0;
        if (threshold <= result->height) {
            result->flags |= 2;
            return 1;
        }
        return 0;
    }
    result->flags &= ~2;
    return 0;
}

void func_15045714(f32 *position, u16 selector, s32 *result, s32 *secondaryCount) {
    func_1510F800(2);
    *result = func_150A6500((s16)position[0], (s16)position[2], secondaryCount, selector);
}

s32 func_15045780(f32 *position, u16 selector, f32 threshold, HeightResult71820 *result) {
    s32 counts[2];

    if (position[1] < threshold) {
        result->flags &= ~2;
        return 0;
    }
    func_15045714(position, selector, &counts[1], &counts[0]);
    return func_15045F8C(position, threshold, counts, result);
}

s32 func_15045800(f32 *position, u16 selector, f32 threshold, HeightResult71820 *result) {
    switch (func_15047004(position, threshold, result)) {
        case 0:
            return func_15045780(position, selector, threshold, result);
        case 1:
            return 0;
        case 2:
            return 1;
    }
}

s32 func_15045880(f32 *position, f32 threshold, s32 *input, HeightResult71820 *result) {
    s32 selected;
    s32 count;
    s32 i;
    f32 height;
    HeightCandidate71820 *candidate;
    QueryTriangle71820 *triangle;
    QueryVertex71820 *vertex;
    QueryVertex71820 **vertexPointers;
    s32 vertexOffset;
    HeightEntity71820 *entity;
    u32 *metadataTable;
    s32 metadataIndex;

    result->height = D_80098D50;
    selected = -1;
    func_150A44F0(input[0], D_800D37E0, 0);
    count = func_150A43E0((s32)position[0], (s32)position[2], input[0], D_800D37E0);
    for (i = 0; i < count; i++) {
        height = D_800D3300[i].fixedHeight * (1.0f / 256.0f);
        if (position[1] <= height && height < result->height) {
            selected = i;
            result->height = height;
        }
    }
    if (selected != -1) {
        candidate = &D_800D3300[selected];
        triangle = candidate->triangle;
        vertexPointers = triangle->vertices;
        vertexOffset = candidate->vertexIndex;
        for (i = 0; i != 3; i++) {
            vertex = (QueryVertex71820 *)((u8 *)vertexPointers[i] + vertexOffset);
            result->vertices[i * 3] = vertex->x;
            result->vertices[i * 3 + 1] = vertex->y;
            result->vertices[i * 3 + 2] = vertex->z;
        }
        entity = &D_800DBEF4[candidate->padC];
        result->value = (s32)entity;
        metadataTable = entity->metadataTable;
        if (metadataTable != NULL) {
            metadataIndex = (s32)((u32)(triangle - D_800DBE3C) - entity->firstTriangle);
            result->metadata = metadataTable[metadataIndex];
        } else {
            result->metadata = entity->metadata;
        }
        result->flags |= 6;
        /* Retail reloads both entity operands after the result publications. */
        if ((D_800DBEF4[candidate->padC].flags & 0x80) == 0x80) {
            result->flags |= 1;
        }
        result->state = 2;
        if (result->height <= threshold) {
            result->flags |= 2;
            return 1;
        }
        return 0;
    }
    result->flags &= ~2;
    return 0;
}

s32 func_15045AE4(f32 *position, f32 threshold, s32 *input, HeightResult71820 *result) {
    s32 selected;
    s32 count;
    s32 i;
    f32 height;
    HeightCandidate71820 *candidate;
    QueryTriangle71820 *triangle;
    QueryVertex71820 *vertex;
    QueryVertex71820 **vertexPointers;
    s32 vertexOffset;
    HeightEntity71820 *entity;
    u32 *metadataTable;
    s32 metadataIndex;

    result->height = D_80098D54;
    selected = -1;
    func_150A44F0(input[0], D_800D37E0, 0);
    count = func_150A43E0((s32)position[0], (s32)position[2], input[0], D_800D37E0);
    for (i = 0; i < count; i++) {
        height = D_800D3300[i].fixedHeight * (1.0f / 256.0f);
        if (height <= position[1] && result->height < height) {
            selected = i;
            result->height = height;
        }
    }
    if (selected != -1) {
        candidate = &D_800D3300[selected];
        triangle = candidate->triangle;
        vertexPointers = triangle->vertices;
        vertexOffset = candidate->vertexIndex;
        for (i = 0; i != 3; i++) {
            vertex = (QueryVertex71820 *)((u8 *)vertexPointers[i] + vertexOffset);
            result->vertices[i * 3] = vertex->x;
            result->vertices[i * 3 + 1] = vertex->y;
            result->vertices[i * 3 + 2] = vertex->z;
        }
        entity = &D_800DBEF4[candidate->padC];
        result->value = (s32)entity;
        metadataTable = entity->metadataTable;
        if (metadataTable != NULL) {
            metadataIndex = (s32)((u32)(triangle - D_800DBE3C) - entity->firstTriangle);
            result->metadata = metadataTable[metadataIndex];
        } else {
            result->metadata = entity->metadata;
        }
        result->flags |= 6;
        /* This context also reloads both entity operands after publication. */
        if ((D_800DBEF4[candidate->padC].flags & 0x80) == 0x80) {
            result->flags |= 1;
        }
        result->state = 2;
        if (threshold <= result->height) {
            result->flags |= 2;
            return 1;
        }
        return 0;
    }
    result->flags &= ~2;
    return 0;
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_71820/func_15045D48.s")

s32 func_15045F8C(f32 *position, f32 threshold, s32 *input, HeightResult71820 *result) {
    s32 selected;
    s32 count;
    s32 i;
    f32 height;
    HeightCandidate71820 *candidate;
    QueryTriangle71820 *triangle;
    QueryVertex71820 *vertex;
    QueryVertex71820 **vertexPointers;
    s32 vertexOffset;
    HeightEntity71820 *entity;
    u32 *metadataTable;
    s32 metadataIndex;

    result->height = D_80098D5C;
    selected = -1;
    func_150A44F0(input[0], D_800D3830, 0);
    count = func_150A43E0((s32)position[0], (s32)position[2], input[0], D_800D3830);
    for (i = 0; i < count; i++) {
        height = D_800D3300[i].fixedHeight * (1.0f / 256.0f);
        if (height <= position[1] && result->height < height) {
            selected = i;
            result->height = height;
        }
    }
    if (selected != -1) {
        candidate = &D_800D3300[selected];
        triangle = candidate->triangle;
        vertexPointers = triangle->vertices;
        vertexOffset = candidate->vertexIndex;
        for (i = 0; i != 3; i++) {
            vertex = (QueryVertex71820 *)((u8 *)vertexPointers[i] + vertexOffset);
            result->vertices[i * 3] = vertex->x;
            result->vertices[i * 3 + 1] = vertex->y;
            result->vertices[i * 3 + 2] = vertex->z;
        }
        /* The fourth candidate word is an entity index in this collector. */
        entity = &D_800DBEF4[candidate->padC];
        result->value = (s32)entity;
        metadataTable = entity->metadataTable;
        if (metadataTable != NULL) {
            metadataIndex = (s32)((u32)(triangle - D_800DBE3C) - entity->firstTriangle);
            result->metadata = metadataTable[metadataIndex];
        } else {
            result->metadata = entity->metadata;
        }
        result->flags |= 6;
        if ((entity->flags & 0x80) == 0x80) {
            result->flags |= 1;
        }
        result->state = 3;
        if (threshold <= result->height) {
            result->flags |= 2;
            return 1;
        }
        return 0;
    }
    result->flags &= ~2;
    return 0;
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_71820/func_150461D0.s")

s32 func_15046460() {
    return 0;
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_71820/func_150466F8.s")

s32 func_1504697C(f32 *position, u16 selector, f32 threshold, HeightResult71820 *result) {
    return 0;
}

s32 func_15046C00(f32 *position, u16 selector, f32 threshold, HeightResult71820 *result) {
    switch (func_150470B0(position, threshold, result)) {
        case 0:
            return func_150466F8(position, selector, threshold, result);
        case 1:
            return 0;
        case 2:
            return 1;
    }
}

s32 func_15046C80(f32 *arg0, u16 arg1, f32 arg2, HeightResult71820 *arg3) {
    switch (func_15047004(arg0, arg2, arg3)) {
        case 0:
            return func_1504697C(arg0, arg1, arg2, arg3);
        case 1:
            return 0;
        case 2:
            return 1;
    }
}

s32 func_15046D00(f32 *position, u16 selector, f32 threshold, HeightResult71820 *result) {
    return 0;
}

s32 func_15046F84(f32 *arg0, u16 arg1, f32 arg2, HeightResult71820 *arg3) {
    switch (func_15047004(arg0, arg2, arg3)) {
        case 0:
            return func_15046D00(arg0, arg1, arg2, arg3);
        case 1:
            return 0;
        case 2:
            return 1;
    }
}

s32 func_15047004(f32 *position, f32 threshold, HeightResult71820 *result) {
    f32 height;

    if ((result->flags & 4) &&
        func_150A3FC4(position[0], position[2], NULL, result->vertices, &height)) {
        if (threshold <= height && height <= position[1]) {
            result->height = height;
            result->flags |= 2;
            return 2;
        }
        return 1;
    }
    return 0;
}

s32 func_150470B0(f32 *position, f32 threshold, HeightResult71820 *result) {
    f32 height;

    if ((result->flags & 4) &&
        func_150A3FC4(position[0], position[2], NULL, result->vertices, &height)) {
        if (height <= threshold && position[1] <= height) {
            result->height = height;
            result->flags |= 2;
            return 2;
        }
        return 1;
    }
    return 0;
}

s32 func_1504715C() {
    return 0;
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_71820/func_150472C0.s")

void func_15047390(f32 mf[4][4], f32 xEye, f32 yEye, f32 zEye, f32 xAt,
                   f32 yAt, f32 zAt, f32 xUp, f32 yUp, f32 zUp) {
}

void func_15047688(Mtx *m, f32 xEye, f32 yEye, f32 zEye, f32 xAt, f32 yAt,
                   f32 zAt, f32 xUp, f32 yUp, f32 zUp) {
    f32 mf[4][4];

    func_15047390(mf, xEye, yEye, zEye, xAt, yAt, zAt, xUp, yUp, zUp);
    guMtxF2L(mf, m);
}

void func_15047700(f32 mf[4][4], LookAt *l, f32 xEye, f32 yEye, f32 zEye,
                   f32 xAt, f32 yAt, f32 zAt, f32 xUp, f32 yUp, f32 zUp) {
}

void func_15047B80(Mtx *m, LookAt *l, f32 xEye, f32 yEye, f32 zEye,
                   f32 xAt, f32 yAt, f32 zAt, f32 xUp, f32 yUp, f32 zUp) {
    f32 mf[4][4];

    func_15047700(mf, l, xEye, yEye, zEye, xAt, yAt, zAt, xUp, yUp, zUp);
    guMtxF2L(mf, m);
}
