#include <ultra64.h>
#include "structs.h"
void func_1516972C(struct102 *);

typedef struct { u8 *owner; u8 identity; u8 opaque5[3]; } PayloadOwnerLink;
typedef struct { u8 *before; u8 *after; u8 before_identity; u8 after_identity; u8 opaqueA[2]; } PayloadOwnerLinkEvent;
typedef struct {
    u32 zero0, zero4;
    u8 ownerSelector, reserved09[3];
    u8 *owner;
    u8 attachment, reserved11[3];
    f32 vector[3];
    f32 value20, value24;
    s16 value28;
    u8 flags, value2B;
    s8 value2C;
    u8 value2D;
} OwnerPresetDescriptor1D0840;
extern f32 D_800A8D5C;
void *func_1513418C(OwnerPresetDescriptor1D0840 *, s32, u8, s32);

void func_151A4E9C(u8 *);
void *func_15167A68(s32, s32, s32, s32, u8, u8);

typedef struct {
    u8 header[0x10];
    u32 value;
    u8 selector;
    u8 red;
    u8 green;
    u8 blue;
    u8 state;
    u8 callback;
    u8 view;
    u8 reserved[5];
} Type5AColorRecord;

void func_15169260(void *, s32, s32, u8);
void func_15143134(void *, void *, s32);
extern u8 D_800A8D70[];
extern s32 D_800BE9E4;
typedef struct { s32 val; } OneWord1D0840;
extern void (*D_8008F900[])();

/* Partially recovered text-only slice asm/1D0840.s. */

extern void (*D_8008F904[])(u8 *, s32, u8);

typedef struct {
    u8 *owner;
    u8 identity, attachment, reserved06[2];
    f32 vector[3];
    f32 value14;
    s16 value18, value1A, value1C;
    u8 reserved1E[2];
    f32 value20, value24;
    u8 value28, value29, value2A, value2B, value2C, value2D, value2E;
    u8 reserved2F;
} OwnerSetupDescriptor151A3390;
extern f32 D_800A8D50, D_800A8D54;
u8 *func_151A3504(void *, u8);
void func_151A4590(u8 * volatile, u8);
void func_151A499C(void *, u8);
s32 func_10010154(u16, void *, u16, s16, u16);
struct225 *func_15160A58(u8 *, u8, void *, u8, s16, s32, s32, s32, s32, s32, s32, s8, s32, u8, u8, s32);

/* Submit the owner descriptor, companion presets, sound and vector effect. */
void func_151A3390(u8 *owner, u8 channel) {
    OwnerSetupDescriptor151A3390 descriptor;
    f32 position[3];

    descriptor.owner = owner;
    descriptor.identity = owner[0x3B];
    descriptor.attachment = 1;
    descriptor.vector[0] = 0.0f;
    descriptor.vector[1] = 0.0f;
    descriptor.vector[2] = 0.0f;
    descriptor.value2B = 1;
    descriptor.value2C = 255;
    descriptor.value2D = 8;
    descriptor.value2E = 31;
    descriptor.value18 = 170;
    descriptor.value1A = 40;
    descriptor.value1C = 7;
    descriptor.value28 = 2;
    descriptor.value29 = 4;
    descriptor.value2A = 1;
    descriptor.value14 = D_800A8D50;
    descriptor.value20 = 30.0f;
    descriptor.value24 = D_800A8D54;
    func_151A3504(&descriptor, channel);
    func_151A4590(owner, channel);
    func_151A499C(owner, channel);
    func_10010154(0x1AA, owner, 0x55F0, 1000, 4000);
    position[0] = 0.0f;
    position[1] = 0.0f;
    position[2] = 0.0f;
    func_15160A58(owner, 1, position, 2, 300, 80, 255, 255, 117, 255, 0, -1, 0, 0, channel, 1);
}

typedef struct OwnerPosition151A3504 { f32 x, y, z; } OwnerPosition151A3504;
typedef struct OwnerSnapshot151A3504 {
    u8 *owner;
    u8 identity, slot, reserved06[2], remainder08[0x28];
} OwnerSnapshot151A3504;
typedef struct OwnerPayload151A3504 {
    OwnerSnapshot151A3504 snapshot;
    u8 kind, reserved31[3];
    OwnerPosition151A3504 position;
    f32 value40;
    u8 flag44, reserved45[3];
    f32 value48;
    u8 flag4C, reserved4D[3];
} OwnerPayload151A3504;
typedef struct OwnerRequest151A3504 {
    OwnerPosition151A3504 position;
    s16 lifetime;
    u16 flags;
    s32 step;
    u8 reserved14, count, reserved16[6];
} OwnerRequest151A3504;
void *memcpy(void *, const void *, u32);
s32 func_151A4E34(u8 *, void *);
u8 *func_15147A80(void *, s32, s32, s32, s32, s32, s32, s32, void *, u8, s32);
/* Snapshot an owner link, query its position, and attach the payload to a new record. */
u8 *func_151A3504(void *input, u8 channel) {
    OwnerRequest151A3504 request;
    OwnerPayload151A3504 payload;
    u8 *created;

    if (*(u8 **)input == NULL) {
        return NULL;
    }
    /* The query and factory consume partial records; leave reserved bytes alone. */
    memcpy(&payload, input, 0x30);
    payload.flag44 = 0;
    request.count = 50;
    request.flags = 2;
    request.lifetime = 1000;
    payload.kind = 6;
    payload.flag4C = 0;
    payload.value40 = 0.0f;
    payload.value48 = 0.0f;
    if (func_151A4E34((u8 *)&payload, &request.position)) {
        payload.position = request.position;
        request.flags |= 4;
    }
    request.step = 8;
    created = func_15147A80(&request, 0x50, 0x18, 6, 6, 6, 0, 0, NULL, channel, 0);
    if (created != NULL) {
        memcpy(*(void **)(created + 0x98), &payload, 0x50);
    }
    return created;
}

typedef struct { f32 x, y, z; } RingPosition151A361C;
typedef struct {
    RingPosition151A361C position;
    f32 value;
    s16 lifetime, delay;
    u8 mark, reserved15[3];
} RingEntry151A361C;
extern f32 D_800BE9A4;

/* Age the live ring records and select the oldest remaining output position. */
s32 func_151A361C(u8 *owner) {
    u8 *state;
    RingEntry151A361C *entries;
    s32 cursor;
    RingEntry151A361C *entry;

    state = *(u8 **)(owner + 0x98);
    entries = *(RingEntry151A361C **)(owner + 0x94);
    if (*(s8 *)(owner + 0x2C) < 2 && (state[0x30] & 1)) {
        return 0;
    }
    state[0x4C] += (u32)*(s8 *)(state + 0x2A) * (u32)D_800BE9E4;
    cursor = *(s8 *)(owner + 0x2E);
    while (cursor != *(s8 *)(owner + 0x2D)) {
        cursor--;
        if (cursor < 0) {
            cursor = owner[0x25] - 1;
        }
        entry = &entries[cursor];
        if (entry->delay > 0) {
            entry->delay = (s16)((u32)(s32)entry->delay - (u32)D_800BE9E4);
        } else {
            entry->lifetime -= (u32)D_800BE9E4 * (u32)(s32)*(s16 *)(state + 0x1C);
        }
        entry->mark = 255;
        entry->value += D_800BE9A4 * *(f32 *)(state + 0x24);
        if (entry->lifetime < 0) {
            state[0x30] &= ~2;
            while (cursor != *(s8 *)(owner + 0x2D)) {
                owner[0x2D] = *(s8 *)(owner + 0x2D) + 1;
                if (owner[0x25] == *(s8 *)(owner + 0x2D)) {
                    owner[0x2D] = 0;
                }
                owner[0x2C] = *(s8 *)(owner + 0x2C) - 1;
            }
            entries[*(s8 *)(owner + 0x2D)].lifetime = 0;
        }
    }
    if (*(s8 *)(owner + 0x2C) > 0) {
        *(RingPosition151A361C *)(owner + 0x54) = entries[*(s8 *)(owner + 0x2D)].position;
    } else {
        *(f32 *)(owner + 0x54) = 0.0f;
        *(f32 *)(owner + 0x58) = 0.0f;
        *(f32 *)(owner + 0x5C) = 0.0f;
    }
    return 1;
}

#include <math.h>
f32 fabsf(f32);
#pragma intrinsic (fabsf)
extern f32 D_800A8D58;
s32 func_150ADA20(void);
void *func_151491F4(s16, s8, s8, u8, u8, s32, u8, s32);
typedef struct {
    u8 *owner;
    u8 identity, attachment, reserved06[2];
    f32 vector08[3], scale;
    s16 lifetime, delay, lifetimeScale;
    u8 reserved1E[2];
    f32 value, rate;
    u8 phaseBase, phaseRange, phaseStep, reserved2B[5];
    u8 kind, reserved31[3];
    RingPosition151A361C position;
    f32 pending;
    u8 phase, reserved45[3];
    f32 elapsed;
    u8 flags, reserved4D[3];
} RingPayload151A37C0;
typedef struct {
    RingPosition151A361C position;
    f32 value;
    s16 lifetime, delay;
    u8 mark, phase, reserved16[2];
} RingSample151A37C0;

/* Sample linked-owner movement into the ring, retaining fractional progress. */
s32 func_151A37C0(u8 *owner) {
    RingPayload151A37C0 *state = *(RingPayload151A37C0 **)(owner + 0x98);
    RingSample151A37C0 *entries = *(RingSample151A37C0 **)(owner + 0x94);
    s32 initialized;
    f32 dx, dy, dz;
    OwnerSetupDescriptor151A3390 snapshot;
    f32 points, fraction, remaining, value, timeStep, valueStep;
    RingPosition151A361C position;
    RingSample151A37C0 *entry;
    u8 *created;
    f32 stepX, stepY, stepZ;
    f32 valueDifference;
    u32 random;

    if (*(s32 *)state->owner == 0) return 0;
    if (state->identity != state->owner[0x3B]) return 0;
    initialized = 0;
    if (!(*(u16 *)(owner + 0x1E) & 4)) {
        if (func_151A4E34((u8 *)state, owner + 0x10)) {
            state->position = *(RingPosition151A361C *)(owner + 0x10);
            *(u16 *)(owner + 0x1E) |= 4;
            initialized = 1;
        } else return 1;
    }
    if (!initialized && !func_151A4E34((u8 *)state, owner + 0x10)) {
        func_151A4E9C(owner);
        memcpy(&snapshot, state, 0x30);
        created = func_151491F4(300, -1, 10, 0, 5, 48, owner[0xC], 0);
        if (created != NULL) memcpy(created + 0x28, &snapshot, 0x30);
        return 1;
    }
    dx = *(f32 *)(owner + 0x10) - state->position.x;
    dy = *(f32 *)(owner + 0x14) - state->position.y;
    dz = *(f32 *)(owner + 0x18) - state->position.z;
    if (D_800A8D58 < fabsf(dx) || D_800A8D58 < fabsf(dy) || D_800A8D58 < fabsf(dz)) {
        state->pending += sqrtf(dx * dx + dy * dy + dz * dz) * state->scale;
    }
    points = state->pending;
    if (1.0f < points) {
        fraction = 1.0f / points;
        position = state->position;
        remaining = state->elapsed + D_800BE9A4;
        timeStep = remaining * fraction;
        value = state->value + state->rate * remaining;
        valueDifference = state->value - value;
        stepX = dx * fraction;
        stepY = dy * fraction;
        stepZ = dz * fraction;
        valueStep = valueDifference * fraction;
        do {
            entry = &entries[*(s8 *)(owner + 0x2E)];
            entry->position = position;
            entry->value = value;
            entry->lifetime = state->lifetime;
            entry->delay = state->delay;
            entry->phase = state->phase;
            /* The RNG may change the phase fields; read them after it returns. */
            random = (u32)func_150ADA20();
            state->phase = (u32)state->phase + state->phaseBase +
                random % ((u32)state->phaseRange + 1);
            entry->mark = 255;
            owner[0x2E] = *(s8 *)(owner + 0x2E) + 1;
            if (owner[0x25] == *(s8 *)(owner + 0x2E)) owner[0x2E] = 0;
            owner[0x2C] = *(s8 *)(owner + 0x2C) + 1;
            if (*(s8 *)(owner + 0x2D) == *(s8 *)(owner + 0x2E)) {
                owner[0x2D] = *(s8 *)(owner + 0x2D) + 1;
                if (owner[0x25] == *(s8 *)(owner + 0x2D)) owner[0x2D] = 0;
                owner[0x2C] = *(s8 *)(owner + 0x2C) - 1;
            }
            position.x += stepX;
            position.y += stepY;
            position.z += stepZ;
            value += valueStep;
            remaining -= timeStep;
            state->pending -= 1.0f;
        } while (1.0f < state->pending);
        state->position = position;
        state->elapsed = remaining;
    }
    return 1;
}


typedef struct {
    u8 reserved00[0x2B];
    u8 fadeInCount, fadeInStep, fadeOutCount, fadeOutStep, reserved2F;
    u8 flags, reserved31[0x1B];
    u8 phaseOffset, reserved4D[3];
} RibbonProfile151A3BE4;

extern u8 *D_800DBFF0;
extern u8 D_80090CD4[];
extern u32 D_800D2C9C;
void func_151D5D60(void *, s16, s32, Vtx **, u8 *);
Gfx *func_15142E24(Gfx *, void *, s32, s32, s32, s32, s32, u8, u8 *, u8 *, s32);
Gfx *func_15142B7C(Gfx *, u32, u32);
Gfx *func_15142C10(Gfx *, s32, s32, s32, s32, u8 *);
Gfx *func_15142CF0(Gfx *, s32, s32, s32, s32, s32, s32, u8 *);
Gfx *func_1513F4E4(Gfx *, u8, u8 *);
Gfx *func_15142FBC(Gfx *, u32, u32, u8 *);

/* Build a camera-facing ribbon from the live ring, preserving texture seams. */
Gfx *func_151A3BE4(u8 *owner, Gfx *output, s16 view) {
    Vtx *cursor;
    RibbonProfile151A3BE4 *profile;
    RingSample151A37C0 *entries;
    RingSample151A37C0 *entry;
    RingPosition151A361C *eye;
    f32 eyeX, eyeY, eyeZ, dx, dy, dz;
    f32 normalX, normalY, normalZ;
    RingPosition151A361C position, previousPosition;
    s32 index, previous;
    u8 phase, previousPhase, alpha, previousAlpha;
    u8 sync, factor;
    s16 remaining;
    f32 lengthSquared, scale;

    if (*(s8 *)(owner + 0x2C) >= 2) {
        func_151D5D60(owner + 0x84, view, owner[0x25] * 32 + 0xA0, &cursor, NULL);
        if (cursor != NULL) {
            profile = *(RibbonProfile151A3BE4 **)(owner + 0x98);
            entries = *(RingSample151A37C0 **)(owner + 0x94);
            eye = (RingPosition151A361C *)(D_800DBFF0 + view * 0x9A0 + 0x2F8);
            sync = 1;
            factor = 0;
            if (profile->flags & 2) {
                s32 forwardIndex;
                remaining = profile->fadeInCount;
                forwardIndex = *(s8 *)(owner + 0x2D);
                /* Retail enters once even when the fade count initially equals zero. */
                do {
                    entries[forwardIndex].mark = factor;
                    factor += profile->fadeInStep;
                    forwardIndex++;
                    if (forwardIndex == owner[0x25]) forwardIndex = 0;
                    remaining = (s16)(remaining - 1);
                } while (remaining != 0 && forwardIndex != *(s8 *)(owner + 0x2E));
            }
            if (profile->flags & 4) {
                s32 backwardIndex;
                s16 backwardRemaining;
                u8 backwardFactor;
                backwardIndex = *(s8 *)(owner + 0x2E) - 1;
                backwardFactor = 0;
                backwardRemaining = profile->fadeOutCount;
                if (backwardIndex < 0) backwardIndex = owner[0x25] - 1;
                do {
                    entries[backwardIndex].mark = (entries[backwardIndex].mark * backwardFactor) >> 8;
                    backwardFactor += profile->fadeOutStep;
                    backwardIndex--;
                    if (backwardIndex < 0) backwardIndex = owner[0x25] - 1;
                    backwardRemaining = (s16)(backwardRemaining - 1);
                } while (backwardRemaining != 0 && backwardIndex != *(s8 *)(owner + 0x2E));
            }
            output = func_15142E24(output, D_80090CD4, 0, 0, 0, 0, 31, 0, NULL, &sync, 3);
            output = func_15142B7C(output, 1, 0x160600);
            output = func_15142C10(output, 255, 255, 255, 255, &sync);
            output = func_15142CF0(output, 0, 0, 0, 0, 0, 0, &sync);
            output = func_1513F4E4(output, 6, &sync);
            output = func_15142FBC(output, D_800D2C9C | 0x80000 | 0x2CA0, 0x5049D8, &sync);
            if (*(u16 *)(owner + 0x1E) & 2) {
                index = *(s8 *)(owner + 0x2E) - 1;
                if (index < 0) index = owner[0x25] - 1;
                previousPosition = *(RingPosition151A361C *)(owner + 0x10);
                entry = &entries[index];
                previousAlpha = (entry->mark * entry->lifetime) >> 8;
                previousPhase = entry->phase + profile->phaseOffset;
            } else {
                previous = *(s8 *)(owner + 0x2E) - 1;
                if (previous < 0) previous = owner[0x25] - 1;
                index = previous - 1;
                if (index < 0) index = owner[0x25] - 1;
                entry = &entries[previous];
                previousPosition = entry->position;
                previousAlpha = (entry->mark * entry->lifetime) >> 8;
                previousPhase = entry->phase + profile->phaseOffset;
            }
            entry = &entries[index];
            position = entry->position;
            alpha = (entry->mark * entry->lifetime) >> 8;
            phase = entry->phase + profile->phaseOffset;
            eyeX = previousPosition.x - eye->x;
            eyeY = previousPosition.y - eye->y;
            eyeZ = previousPosition.z - eye->z;
            dy = previousPosition.y - position.y;
            dz = previousPosition.z - position.z;
            dx = previousPosition.x - position.x;
            normalX = dy * eyeZ - eyeY * dz;
            normalY = dz * eyeX - eyeZ * dx;
            normalZ = dx * eyeY - eyeX * dy;
            lengthSquared = normalX * normalX + normalY * normalY + normalZ * normalZ;
            if (lengthSquared == 0.0f) normalX = normalY = normalZ = 0.0f;
            else {
                scale = entry->value / sqrtf(lengthSquared);
                normalX = normalX * scale;
                normalY = normalY * scale;
                normalZ = normalZ * scale;
            }
            cursor->v.ob[0] = (s32)(previousPosition.x + normalX);
            cursor->v.ob[1] = (s32)(previousPosition.y + normalY);
            cursor->v.ob[2] = (s32)(previousPosition.z + normalZ);
            cursor->v.tc[0] = previousPhase << 6;
            cursor->v.tc[1] = 0x7C0;
            cursor->v.cn[0] = 255;
            cursor->v.cn[1] = 255;
            cursor->v.cn[2] = 255;
            cursor->v.cn[3] = previousAlpha;
            cursor->v.flag = 0;
            cursor++;
            cursor->v.ob[0] = (s32)(previousPosition.x - normalX);
            cursor->v.ob[1] = (s32)(previousPosition.y - normalY);
            cursor->v.ob[2] = (s32)(previousPosition.z - normalZ);
            cursor->v.tc[0] = previousPhase << 6;
            cursor->v.tc[1] = 0;
            cursor->v.cn[0] = 255;
            cursor->v.cn[1] = 255;
            cursor->v.cn[2] = 255;
            cursor->v.cn[3] = previousAlpha;
            cursor->v.flag = 0;
            cursor++;
            do {
                eyeX = position.x - eye->x;
                eyeY = position.y - eye->y;
                eyeZ = position.z - eye->z;
                dy = previousPosition.y - position.y;
                dz = previousPosition.z - position.z;
                dx = previousPosition.x - position.x;
                normalX = dy * eyeZ - eyeY * dz;
                normalY = dz * eyeX - eyeZ * dx;
                normalZ = dx * eyeY - eyeX * dy;
                lengthSquared = normalX * normalX + normalY * normalY + normalZ * normalZ;
                if (lengthSquared == 0.0f) normalX = normalY = normalZ = 0.0f;
                else {
                    scale = entries[index].value / sqrtf(lengthSquared);
                    normalX = normalX * scale;
                    normalY = normalY * scale;
                    normalZ = normalZ * scale;
                }
                cursor->v.ob[0] = (s32)(position.x + normalX);
                cursor->v.ob[1] = (s32)(position.y + normalY);
                cursor->v.ob[2] = (s32)(position.z + normalZ);
                cursor->v.tc[0] = phase << 6;
                cursor->v.tc[1] = 0x7C0;
                cursor->v.cn[0] = 255;
                cursor->v.cn[1] = 255;
                cursor->v.cn[2] = 255;
                cursor->v.cn[3] = alpha;
                cursor->v.flag = 0;
                cursor++;
                cursor->v.ob[0] = (s32)(position.x - normalX);
                cursor->v.ob[1] = (s32)(position.y - normalY);
                cursor->v.ob[2] = (s32)(position.z - normalZ);
                cursor->v.tc[0] = phase << 6;
                cursor->v.tc[1] = 0;
                cursor->v.cn[0] = 255;
                cursor->v.cn[1] = 255;
                cursor->v.cn[2] = 255;
                cursor->v.cn[3] = alpha;
                cursor->v.flag = 0;
                cursor++;
                gSPVertex(output++, cursor - 4, 4, 0);
                gSP1Triangle(output++, 0, 1, 2, 0);
                gSP1Triangle(output++, 1, 3, 2, 0);
                if (previousPhase < phase) {
                    /* Preserve the next segment before shifting both emitted seam vertices. */
                    memcpy(cursor, cursor - 2, sizeof(Vtx) * 2);
                    cursor[-2].v.tc[0] -= 0x4000;
                    cursor++;
                    cursor[-2].v.tc[0] -= 0x4000;
                    cursor++;
                }
                previous = index;
                index--;
                if (index < 0) index = owner[0x25] - 1;
                if (previous != *(s8 *)(owner + 0x2D)) {
                    previousPosition = position;
                    entry = &entries[index];
                    position = entry->position;
                    alpha = (entry->mark * entry->lifetime) >> 8;
                    previousPhase = phase;
                    phase = entry->phase + profile->phaseOffset;
                }
            } while (previous != *(s8 *)(owner + 0x2D));
        }
    }
    return output;
}


/* Submit the source-backed descriptor preset for the selected variant. */
void func_151A4590(u8 * volatile owner, u8 variant) {
    OwnerPresetDescriptor1D0840 descriptor;

    if (owner != NULL) {
        descriptor.zero0 = 0;
        descriptor.zero4 = 0;
        descriptor.owner = owner;
        descriptor.ownerSelector = descriptor.owner[0x3B];
        descriptor.attachment = 1;
        descriptor.vector[0] = 0.0f;
        descriptor.vector[1] = 0.0f;
        descriptor.vector[2] = 0.0f;
        descriptor.value20 = D_800A8D5C;
        descriptor.value24 = 3.0f;
        descriptor.value28 = 100;
        descriptor.flags = 10;
        descriptor.value2B = 1;
        descriptor.value2C = -1;
        descriptor.value2D = 0;
        func_1513418C(&descriptor, 0, variant, 0);
    }
}

typedef struct {
    u32 field00, field04;
    s16 field08, counter;
    u32 field0C, field10;
    u8 field14, field15, field16, field17;
    u8 field18, field19, field1A, field1B, field1C, field1D;
    s16 field1E, field20, field22;
    f32 field24, firstValue, secondValue;
    RingPosition151A361C position;
    u8 reserved3C[12];
    RingPosition151A361C velocity;
    f32 field54;
    u32 flags;
    u8 reserved5C[4];
    u8 field60, field61, field62;
    s8 field63;
    /* The factory copies all 0x70 descriptor bytes, including this tail. */
    u8 reserved64[12];
} InverseMotionEffect151A4638;
extern f32 D_800A8D60, D_800BE9A8;
f32 func_150ADA68(void);
void *func_15130374(void *, u8, s32, u8, s32);

/* Submit an inverse-motion effect with a random initial counter and flag bits. */
void func_151A4638(f32 x, f32 y, f32 z, f32 vx, f32 vy, f32 vz, u8 *owner) {
    InverseMotionEffect151A4638 packet;
    f32 scale;
    s16 parameters[6];
    u8 *created;

    packet.field1D = 0x27;
    packet.field08 = 0x1401;
    packet.field00 = 0x200005;
    packet.field04 = 0;
    packet.counter = (u32)func_150ADA20() % 5U + 15;
    packet.field0C = 0;
    packet.field10 = 0;
    packet.field14 = 0x8A;
    packet.field15 = 0;
    packet.field16 = 0;
    packet.field17 = 255;
    packet.field18 = 0;
    packet.field19 = 0;
    packet.field1A = 0;
    packet.field1E = 1;
    packet.field20 = 255;
    packet.field22 = 1;
    packet.field24 = 1.0f;
    scale = func_150ADA68();
    packet.position.x = x;
    packet.position.y = y;
    packet.position.z = z;
    /* The two volatile accesses preserve the retail floating-point order. */
    scale = scale * 50.0f + 500.0f;
    ((volatile InverseMotionEffect151A4638 *)&packet)->firstValue = scale;
    packet.secondValue = scale;
    scale = D_800A8D60 * D_800BE9A8;
    ((volatile InverseMotionEffect151A4638 *)&packet)->velocity.x = -vx * scale;
    packet.velocity.y = -vy * scale;
    packet.velocity.z = -vz * scale;
    packet.field54 = 0.0f;
    packet.flags = 13;
    packet.field60 = 1;
    packet.field61 = 1;
    if (func_150ADA20() & 1) packet.flags |= 0x40;
    if (func_150ADA20() & 1) packet.flags |= 0x80;
    packet.field1B = 255;
    packet.field1C = 255;
    packet.field62 = 0;
    packet.field63 = -1;
    parameters[0] = 16;
    parameters[1] = 15;
    parameters[2] = 13;
    parameters[3] = 19;
    parameters[4] = 17;
    parameters[5] = -24;
    created = func_15130374(&packet, 0, sizeof(parameters), owner[0xC], 1);
    if (created != NULL) memcpy(created + 0xA8, parameters, sizeof(parameters));
}


/* Update lifetime-scaled outputs and switch to the next update callback. */
typedef struct {
    u8 reserved00[0x18];
    s16 state;
    s16 counter;
    u8 reserved1C[0xF];
    u8 firstOutput;
    u8 secondOutput;
    u8 reserved2D[0xB];
    f32 firstValue;
    f32 secondValue;
    u8 reserved40[0x30];
    u8 firstMode;
    u8 secondMode;
    u8 updateSelector;
    u8 reserved73[0x35];
    s16 parameters[6];
} ThresholdEffectRecord1D0840;

s32 func_151A483C(ThresholdEffectRecord1D0840 *record, void *unusedContext) {
    s16 *parameters = record->parameters;
    s32 counter = record->counter;
    f32 increment;

    if (counter < parameters[2]) {
        record->firstOutput = counter * parameters[3];
    }
    if (counter < parameters[4]) {
        increment = (s32)((u32)parameters[5] * (u32)D_800BE9E4);
        record->firstValue += increment;
        record->secondValue += increment;
        counter = record->counter;
    }
    if (counter < parameters[0]) {
        record->updateSelector = 1;
        record->firstMode = 2;
        record->secondMode = 2;
        record->secondOutput = counter * parameters[1];
        record->state = 0x5203;
    }
    return 1;
}

typedef struct {
    u8 pad0[0x1A];
    s16 counter;
    u8 pad1[0xF];
    u8 firstOutput;
    u8 secondOutput;
    u8 pad2[0xB];
    f32 firstValue;
    f32 secondValue;
    u8 pad3[0x68];
    s16 parameters[6];
} UpdateRecord1D0840;

s32 func_151A4900(UpdateRecord1D0840 *arg0, s32 arg1) {
    s16 *parameters = arg0->parameters;
    s32 counter = arg0->counter;
    f32 increment;

    if (counter < parameters[2]) {
        arg0->firstOutput = counter * parameters[3];
    }
    if (counter < parameters[4]) {
        increment = (s32)((u32)parameters[5] * (u32)D_800BE9E4);
        arg0->firstValue += increment;
        arg0->secondValue += increment;
        counter = arg0->counter;
    }
    arg0->secondOutput = counter * parameters[1];
    return 1;
}

extern f32 D_800A8D64;
typedef struct {
    void *source;
    u8 sourceByte;
    u8 reserved0[3];
    f32 value;
    f32 zero;
    u8 active;
    u8 reserved1[3];
    f32 vector[3];
} ExtendedEffectPayload;
void *func_151491F4(s16, s8, s8, u8, u8, s32, u8, s32);
void *memcpy(void *, const void *, u32);

/* Initialize the extended source-backed effect payload. */
void func_151A499C(void *source, u8 variant) {
    u8 *effect;
    ExtendedEffectPayload payload;
    u8 *actor = source;
    payload.source = actor;
    payload.sourceByte = actor[0x3B];
    payload.value = D_800A8D64;
    payload.zero = 0.0f;
    payload.active = 1;
    payload.vector[0] = 0.0f;
    payload.vector[1] = 0.0f;
    payload.vector[2] = 0.0f;
    effect = func_151491F4(300, -1, 5, 0, 1, 32, variant, 0);
    if (effect != 0) {
        memcpy(effect + 0x28, &payload, 32);
    }
}

typedef struct {
    u8 *source;
    u8 identity, reserved05[3];
    f32 rate, accumulator;
    u8 matrixIndex, reserved11[3];
    f32 point[3];
} AttachedEmissionPayload151A4A38;
typedef struct {
    s16 count, countRange;
    u8 kind, reserved05;
    u16 field06;
    u32 header, field0C;
    s16 field10, field12;
    u32 field14, field18;
    u8 field1C, field1D, field1E, field1F;
    u8 field20, field21, field22, field23, field24, field25;
    s16 field26, field28, field2A;
    f32 field2C, field30, field34;
    RingPosition151A361C position;
    s16 field44, field46, field48, field4A;
    f32 field4C, field50, field54, field58;
    u32 flags;
    s8 field60, field61;
    u8 field62, field63, field64;
    u8 reserved65[7];
} AttachedEmissionDescriptor151A4A38;
extern f32 D_800BE9A4;
void func_15153634(void *, u8, u8, u8);

/* Emit at the attached actor's transformed point when its accumulator exceeds one. */
void func_151A4A38(u8 *owner) {
    AttachedEmissionPayload151A4A38 *state = (AttachedEmissionPayload151A4A38 *)(owner + 0x28);
    RingPosition151A361C position;
    AttachedEmissionDescriptor151A4A38 packet;
    s16 angle;

    if (*(s32 *)state->source == 0 || *(s32 *)state->source == 8 ||
        state->identity != ((u8 *)state->source)[0x3B]) {
        *(s16 *)(owner + 0xE) = -1;
        owner[0xD] |= 1;
        return;
    }
    if (*(s32 *)((u8 *)state->source + 0x1D4) == 0 || (((u8 *)state->source)[0x74] & 15) == 15) return;
    state->accumulator += state->rate * D_800BE9A4;
    if (1.0f < state->accumulator) {
        angle = (*(u16 *)((u8 *)state->source + 0x76) >> 8) - 64;
        func_15143134(state->point, &position,
            *(s32 *)((u8 *)state->source + 0x1D4) + (state->matrixIndex << 6));
        packet.count = state->accumulator;
        packet.countRange = 0;
        state->accumulator -= packet.count;
        packet.kind = 40;
        packet.field06 = 0xC01;
        packet.header = 0x200005;
        packet.field0C = 0;
        packet.field10 = 23;
        packet.field12 = 13;
        packet.field14 = 0;
        packet.field18 = 0;
        packet.field1C = 0;
        packet.field1D = 0;
        packet.field1E = 0;
        packet.field1F = 255;
        packet.field20 = 0;
        packet.field21 = 0;
        packet.field22 = 0;
        packet.field30 = 300.0f;
        packet.field34 = 400.0f;
        packet.position = position;
        packet.field26 = 1;
        packet.field28 = 0;
        packet.field2A = 1;
        packet.field64 = 0;
        packet.field44 = angle - 25;
        packet.field46 = -44;
        packet.field48 = 50;
        packet.field4A = 50;
        packet.flags = 7;
        packet.field62 = 1;
        packet.field63 = 0;
        packet.field54 = -0.5f;
        packet.field58 = -0.5f;
        packet.field2C = 1.0f;
        packet.field4C = 0.0f;
        packet.field50 = 15.0f;
        if (func_150ADA20() & 1) packet.flags |= 0x40;
        if (func_150ADA20() & 1) packet.flags |= 0x80;
        packet.field23 = 255;
        packet.field24 = 0;
        packet.field25 = 255;
        packet.field60 = -1;
        packet.field61 = -1;
        func_15153634(&packet, 255, owner[0xC], owner[1]);
    }
}


/* Handle linked-record notifications and swap its selected descriptor pair. */
void func_151A4CE0(u8 *owner, s32 eventAddress, u8 command) {
    u8 *state = *(u8 **)(owner + 0x98);
    u8 *event = (u8 *)eventAddress;
    s32 value = command;

    if (command == 0) {
        if (*(s32 *)state == *(s32 *)event || state[4] == event[4]) {
            func_151A4E9C(owner);
        }
    } else if (value == 0x2D) {
        s32 first = *(s32 *)event;
        value = *(s32 *)state;
        if (first == value) {
            *(s32 *)state = *(s32 *)(event + 4);
            state[4] = event[9];
        } else if (*(s32 *)(event + 4) == value) {
            *(s32 *)state = first;
            state[4] = event[8];
        }
    }
}

/* Retarget the payload owner link or release its matching actor. */
void func_151A4D88(struct260 *owner, s32 eventAddress, u8 command) {
    PayloadOwnerLink *link = (PayloadOwnerLink *)((u8 *)owner + 0x28);
    PayloadOwnerLinkEvent *event = (PayloadOwnerLinkEvent *)eventAddress;

    if (command == 0) {
        if (link->owner == event->before || link->identity == ((u8 *)event)[4]) {
            func_1516972C((struct102 *)owner);
        }
    } else if (command == 0x2D) {
        u8 *current = link->owner;
        if (current == event->before) {
            link->owner = event->after;
            link->identity = event->after_identity;
        } else if (current == event->after) {
            link->owner = event->before;
            link->identity = event->before_identity;
        }
    }
}

s32 func_151A4E34(u8 *arg0, void *arg1) {
    u8 *actor = *(u8 **)arg0;
    s32 target = *(s32 *)(actor + 0x1D4);

    if (target == 0) {
        return 0;
    }
    if ((actor[0x74] & 0xF) == 0xF) {
        return 0;
    }
    func_15143134(arg0 + 8, arg1, target + (arg0[5] << 6));
    return 1;
}

void func_151A4E9C(u8 *arg0) {
    u8 *temp_v0 = *(u8 **) (arg0 + 0x98);

    *(u16 *) (arg0 + 0x1E) &= 0xFFFD;
    *(arg0 + 0x30) = 0;
    *(temp_v0 + 0x30) |= 1;
    *(temp_v0 + 0x30) |= 4;
}

/* Retire an invalid owner link, submitting the final effect when needed. */
void func_151A4ECC(struct260 *owner) {
    PayloadOwnerLink *link = (PayloadOwnerLink *)((u8 *)owner + 0x28);
    s32 failed = 0;

    if (*(s32 *)link->owner == 0) {
        failed = 1;
    }
    if (link->identity != link->owner[0x3B]) {
        failed = 1;
    }
    if (failed == 0 && *(s32 *)(link->owner + 0x1D4) != 0
        && (link->owner[0x74] & 0xF) != 0xF) {
        func_151A3504(link, ((u8 *)owner)[0xC]);
        failed = 1;
    }
    if (failed != 0) {
        *(s16 *)((u8 *)owner + 0xE) = -1;
        ((u8 *)owner)[0xD] |= 1;
    }
}

void func_151A4F7C(u8 *arg0, u8 *arg1, u8 arg2) {
    u8 *temp_v0 = arg0 + 0x28;

    if (arg2 == 0) {
        if ((*(s32 *)temp_v0 == *(s32 *)arg1) || (temp_v0[4] == arg1[4])) {
            func_1516972C((struct102 *)arg0);
        }
    }
}

/* Create a type-0x5A color record with optional trailing payload. */
Type5AColorRecord *func_151A4FD0(s32 selector, u32 value, s32 red, s32 green,
    s32 blue, s32 view, u8 callback, u32 extraBytes) {
    Type5AColorRecord *record = func_15167A68(0x5A, 0,
        (s32)(extraBytes + 0x20U), 0, 0xFF, 1);

    if (record == NULL) {
        return NULL;
    }
    record->selector = selector;
    record->value = value;
    record->red = red;
    record->green = green;
    record->blue = blue;
    record->callback = callback;
    record->state = 0;
    record->view = view;
    return record;
}

void func_10011FA0(s32 *);
/* Update a finite lifetime and pulse the record color between 0x90 and 0xFF. */
void func_151A5070(struct102 *object) {
    Type5AColorRecord *record = (Type5AColorRecord *)object;
    s32 remaining = (s32)record->value;
    s32 step;
    s32 shade;

    if (remaining != 0) {
        remaining = (s32)((u32)remaining - (u32)D_800BE9E4);
        if (remaining <= 0) {
            func_1516972C((struct102 *)record);
            return;
        }
        record->value = remaining;
    }
    if (record->callback == 0) {
        func_10011FA0((s32 *)2);
    }
    step = (s32)((u32)D_800BE9E4 * 2U);
    shade = record->red;
    if (record->state == 0) {
        shade = (s32)((u32)shade - (u32)step);
        if (shade < 0x90) {
            shade = 0x90;
            record->state = 1;
        }
    } else {
        shade = (s32)((u32)shade + (u32)step);
        if (shade >= 0x100) {
            shade = 0xFF;
            record->state = 0;
        }
    }
    record->red = shade;
}

void func_151A5130(arg0, arg1, arg2)
s32 arg0;
u8 *arg1;
s16 arg2;
{
    D_8008F900[*(arg1 + 0x14)](arg0, arg1, arg2);
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1D0840/func_151A5170.s")

void func_151A55D4(u8 *arg0, s32 arg1, u8 arg2) {
    void (*callback)(u8 *, s32, u8) = D_8008F904[arg0[0x19]];

    if (callback != NULL) {
        callback(arg0, arg1, arg2);
    }
}

void func_151A561C(s32 arg0, u8 arg1) {
    OneWord1D0840 tmp;

    tmp = *(OneWord1D0840 *) D_800A8D70;
    func_15169260(&tmp, 1, arg0, arg1);
}
