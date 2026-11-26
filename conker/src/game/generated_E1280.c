#include <ultra64.h>
void func_15147D64(void *, u8);
void func_151494E0(void *, u8);


/* Recovered particle routines and remaining placeholders from asm/E1280.s. */

void func_1000FC18(u16, s16, s16, s16, u16);
s32 func_151478F4(s32);
s32 func_15147928(s32);

/* Submit the six ordered byte selections after initializing the first group. */
void func_150B3DD0(void) {
    u8 selection[4];

    func_15147D64(0, 5);
    selection[0] = 0;
    func_151494E0(selection, 0x18);
    selection[0] = 2;
    func_151494E0(selection, 0x18);
    selection[0] = 4;
    func_151494E0(selection, 0x18);
    selection[0] = 1;
    func_151494E0(selection, 0x18);
    selection[0] = 3;
    func_151494E0(selection, 0x18);
    selection[0] = 5;
    func_151494E0(selection, 0x18);
}

void func_150B3E74(s32 arg0) {
    func_1000FC18(0x221, (s16) *(f32 *) (arg0 + 0x10), (s16) *(f32 *) (arg0 + 0x14),
                  (s16) *(f32 *) (arg0 + 0x18), 0xFA0);
    func_151478F4(arg0);
}

void func_150B3EE8(s32 arg0) {
    func_1000FC18(0x221, (s16) *(f32 *) (arg0 + 0x10), (s16) *(f32 *) (arg0 + 0x14),
                  (s16) *(f32 *) (arg0 + 0x18), 0xFA0);
    func_15147928(arg0);
}

#include <string.h>
#include "structs.h"

typedef struct { f32 x, y, z; } ParticlePosition150B3F5C;
typedef struct {
    u8 source[0x40];
    f32 first;
    f32 zero0;
    u8 flag0;
    u8 reserved49[3];
    f32 second;
    u8 flag1;
    u8 reserved51[3];
    f32 zero1;
} ParticlePayload150B3F5C;
typedef struct {
    ParticlePosition150B3F5C position;
    s16 lifetime;
    s16 flags;
    s32 kind;
    u8 reserved14;
    u8 count;
    u8 reserved16[6];
} ParticleRequest150B3F5C;
typedef struct {
    ParticlePayload150B3F5C payload;
    ParticleRequest150B3F5C request;
} ParticleLocals150B3F5C;
u8 *func_15147A80(void *, s32, s32, s32, s32, s32, s32, s32, void *, u8, s32);
u32 func_150ADA20(void);
s32 func_1000EF40(struct57 *, struct57 *, s32 *, s32, s32, s32, u16 *);
u16 func_1000FA64(u16, s16, s16, s16, s32, u16, s16, s32, void *, s32, s32, s32);

/* Create the particle payload, preserving the request's unwritten bytes. */
u8 *func_150B3F5C(f32 *source, ParticlePosition150B3F5C *position, s16 count) {
    ParticleLocals150B3F5C local;
    u8 *created;

    memcpy(local.payload.source, source, 0x40);
    local.request.count = count;
    local.payload.flag0 = 0;
    local.request.flags = 2;
    local.request.lifetime = 500;
    local.payload.zero0 = 0.0f;
    local.payload.second = source[6] + source[5];
    local.payload.flag1 = 0;
    local.payload.zero1 = 0.0f;
    local.payload.first = local.payload.second;
    local.request.position = *position;
    local.request.kind = 9;
    created = func_15147A80(&local.request, 0x58, 0x24, 7, 7, 7, 0, 0, NULL, 255, 1);
    if (created != NULL) {
        u32 random;

        random = func_150ADA20();
        func_1000FA64(0x221, (s16)(s32)position->x, (s16)(s32)position->y,
                     (s16)(s32)position->z, 25000, 4000, 600, (s32)func_1000EF40,
                     NULL, 0, 8, random & 0x40);
        memcpy(*(u8 **)(created + 0x98), &local.payload, 0x58);
    }
    return created;
}


typedef struct {
    ParticlePosition150B3F5C position;
    ParticlePosition150B3F5C velocity;
    f32 extent;
    u16 opacity;
    s16 lifetime;
    u8 retained20[4];
} ParticleRingRecord150B40E8;

typedef struct {
    u8 retained00[0xC];
    f32 verticalAcceleration;
    u8 retained10[0xC];
    u8 flags;
    u8 retained1D[0xB];
    f32 extentRate;
} ParticleRingAux150B40E8;

typedef struct {
    u8 retained00[0x25];
    u8 capacity;
    u8 retained26[6];
    s8 count, tail, head;
    u8 retained2F[0x25];
    ParticlePosition150B3F5C referencePosition;
    u8 retained60[0x34];
    ParticleRingRecord150B40E8 *records;
    ParticleRingAux150B40E8 *aux;
} ParticleRingOwner150B40E8;
extern s32 D_800BE9E4;
extern f32 D_800BE9A4;

/* Advance the particle ring, expire old entries, and update its reference point. */
s32 func_150B40E8(ParticleRingOwner150B40E8 *owner) {
    ParticleRingAux150B40E8 *aux = owner->aux;
    ParticleRingRecord150B40E8 *records = owner->records;
    ParticleRingRecord150B40E8 *record;
    s32 index;
    s32 expired;

    if (owner->count < 2 && (aux->flags & 1)) {
        return 0;
    }
    index = owner->head;
    while (index != owner->tail) {
        index--;
        if (index < 0) index = owner->capacity - 1;
        expired = 0;
        record = &records[index];
        record->opacity = 255;
        record->lifetime -= D_800BE9E4;
        if (record->lifetime < 0) expired = 1;
        record->velocity.y += aux->verticalAcceleration * D_800BE9A4;
        record->position.x += record->velocity.x * D_800BE9A4;
        record->position.y += record->velocity.y * D_800BE9A4;
        record->position.z += record->velocity.z * D_800BE9A4;
        record->extent += aux->extentRate * D_800BE9A4;
        if (expired && index != owner->tail) {
            do {
                owner->tail++;
                if (owner->tail == owner->capacity) owner->tail = 0;
                owner->count--;
            } while (index != owner->tail);
        }
    }
    if (owner->count > 0) {
        owner->referencePosition = records[owner->tail].position;
    } else {
        owner->referencePosition.x = 0.0f;
        owner->referencePosition.y = 0.0f;
        owner->referencePosition.z = 0.0f;
    }
    return 1;
}


s32 func_150B4294() {
    return 0;
}

s32 func_150B4710() {
    return 0;
}

void func_150B5060(u8 *arg0) {
    u8 *temp_v0 = *(u8 **) (arg0 + 0x98);

    arg0[0x30] = 0;
    *(u16 *) (arg0 + 0x1E) &= ~2;
    temp_v0[0x1C] |= 1;
}

s32 func_150B5088() {
    return 0;
}

void func_150B538C(u8 *arg0, u8 arg1, u8 arg2) {
    if (arg2 == 5) {
        func_150B5060(arg0);
    }
}
