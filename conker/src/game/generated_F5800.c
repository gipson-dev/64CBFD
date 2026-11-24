#include <ultra64.h>
extern f32 D_800BE9A4;
extern s32 D_800BE4E0;
s32 func_150ADA20(void);
void func_150CDB6C(s32 value);


/* Restored functions and remaining placeholders for asm/F5800.s. */

typedef struct { u8 group, pad1; s8 direction; u8 pad3; s16 position, current, target; } MotionEntry150C8350;
extern u8 D_800BE9A0;
extern s32 D_800BE9E4;
/* Advance ten motion records and reflect positions at both limits. */
void func_150C8350(void) {
    s32 offset, current, target, desired, difference, magnitude, step;
    MotionEntry150C8350 *entry;
    for (offset = 0; offset < 10; offset++) {
        entry = ((MotionEntry150C8350 *)D_800BE4E0 + offset);
        current = entry->current;
        target = entry->target;
        if (current != target) {
            desired = target;
            if (current < 0) desired = -target;
            difference = desired - current;
            step = (s32)((u32)D_800BE9E4 << 4);
            magnitude = difference < 0 ? -difference : difference;
            if (magnitude < step) {
                entry->current = desired;
                entry = ((MotionEntry150C8350 *)D_800BE4E0 + offset);
                current = entry->current;
            } else {
                entry->current = (s32)((u32)current + (u32)step * (u32)(difference < 0 ? -1 : 1));
                entry = ((MotionEntry150C8350 *)D_800BE4E0 + offset);
                current = entry->current;
            }
        }
        entry->position += current * entry->direction * D_800BE9A0;
        entry = ((MotionEntry150C8350 *)D_800BE4E0 + offset);
        if (entry->position >= 0x500) {
            entry->position -= 0x500;
            entry = ((MotionEntry150C8350 *)D_800BE4E0 + offset);
            entry->position = 0x500 - entry->position;
            entry = ((MotionEntry150C8350 *)D_800BE4E0 + offset);
            entry->direction = -entry->direction;
            entry = ((MotionEntry150C8350 *)D_800BE4E0 + offset);
            if (entry->position >= 0x500) entry->position = 0x4FF;
        } else if (entry->position < 0) {
            entry->position = -entry->position;
            entry = ((MotionEntry150C8350 *)D_800BE4E0 + offset);
            entry->direction = -entry->direction;
            entry = ((MotionEntry150C8350 *)D_800BE4E0 + offset);
            if (entry->position < 0) entry->position = 0;
        }
    }
}

/* Advance the motion table once for the primary frame layer. */
void func_150C84F4(s32 view) {
    if (view == 0) {
        func_150C8350();
    }
}

/* Randomize ten motion targets from the selected intensity. */
void func_150C851C(s32 intensity) {
    s32 offset;
    s32 base;
    u32 span;
    s32 target;

    if (D_800BE4E0 != 0) {
        func_150CDB6C(intensity);
        base = (intensity * 300) >> 8;
        span = ((intensity * 50) >> 8) + 50;
        for (offset = 0; offset != 100; offset += 10) {
            target = base;
            target += (u32)func_150ADA20() % span;
            *(s16 *)(D_800BE4E0 + offset + 8) = target;
        }
    }
}

typedef struct { u8 group, reserved01; s8 marker; u8 reserved03; s16 choice, previous, next; } SegmentEntry150C8600;
extern s32 *D_80088810[2];
u32 func_1510D0EC(s32 resource, s32 *extent, s32 mode, s32 flags);

/* Emit ten segment bindings for the current group and clamped resource choice. */
Gfx *func_150C8600(Gfx *cursor) {
    s32 *groups[2];
    s32 index, choice, extent;
    u32 address;
    SegmentEntry150C8600 *entry;
    groups[0] = D_80088810[0];
    groups[1] = D_80088810[1];
    for (index = 0; index < 10; index++) {
        entry = (SegmentEntry150C8600 *)D_800BE4E0 + index;
        choice = entry->choice >> 8;
        if (choice < 0) choice = 0;
        if (choice >= 5) choice = 4;
        if (entry->group >= 2) {
            entry->group = 0;
            entry = (SegmentEntry150C8600 *)D_800BE4E0 + index;
        }
        address = func_1510D0EC(groups[entry->group][choice], &extent, 3, 0);
        gSPSegment(cursor++, index + 1, address);
    }
    return cursor;
}

s32 func_150C8730() {
    return 0;
}

typedef struct {
    u8 reserved0[0x14]; s32 count; s16 lifetime; u8 reserved1A[0x16];
} RingDescriptor150C88D0;
typedef struct {
    u8 reserved0[0x10]; RingDescriptor150C88D0 descriptor;
    f32 field40,field44,angleStep; s16 lifetime; u8 reserved4E[2]; f32 field50;
    u8 *field54,*field58; u8 reserved5C[0x304]; f32 (*lookup)[2]; u8 *field364;
    u8 storage[1];
} RingEffect150C88D0;
extern f32 D_800A0528;
void *func_15167A68(s32,s32,s32,s32,u8,u8);
void *memcpy(void *,const void *,unsigned int);
f32 sinf(f32); f32 cosf(f32);

/* Allocate the ring record and initialize its sine/cosine lookup table. */
void *func_150C88D0(RingDescriptor150C88D0 *descriptor,s32 extraBytes,u8 priority,s32 group) {
    RingEffect150C88D0 *effect;
    s32 index;
    s32 bands;
    s32 offset;
    f32 angle;
    f32 value;
    effect = func_15167A68(0x31,group,extraBytes + (descriptor->count << 3) + (descriptor->count * 5 << 5) + 0x408,1,priority,1);
    bands = 5;
    if (effect == 0) return 0;
    memcpy(&effect->descriptor,descriptor,0x30);
    effect->lookup = (f32 (*)[2])((u8 *)effect + 0x368);
    effect->field54 = (u8 *)effect + (descriptor->count << 3) + 0x368;
    effect->field58 = (u8 *)effect + (descriptor->count << 3) + (descriptor->count * bands << 4) + 0x3B8;
    effect->field40 = 0.0f;
    effect->field44 = 0.0f;
    effect->field364 = (u8 *)effect + (descriptor->count << 3) + (descriptor->count * bands << 5) + 0x408;
    effect->angleStep = D_800A0528 / effect->descriptor.count;
    effect->field50 = 0.0f;
    effect->lifetime = effect->descriptor.lifetime;
    index = 0;
    offset = 0;
    if (effect->descriptor.count > 0) {
        angle = 0.0f;
        do {
            value = sinf(angle);
            ((f32 *)((u8 *)effect->lookup + offset))[0] = value;
            value = cosf(angle);
            ((f32 *)((u8 *)effect->lookup + offset))[1] = value;
            ++index;
            offset += 8;
            angle += effect->angleStep;
        } while (index < effect->descriptor.count);
    }
    return effect;
}

#include "structs.h"
typedef struct {
    u8 reserved00[0x10]; f32 x,y,z;
    u8 flags; s8 finish; u8 reserved1E[2];
    f32 growthRate; s32 count;
    s16 lifetime,fadeStart; f32 fadeInScale;
    s16 fadeEnd; u8 reserved32[2]; f32 fadeOutScale,emissionRate;
    s8 emission,update; u8 reserved3E[2];
    f32 amplitude,radius,angleStep; s16 initialLifetime; u8 reserved4E[2]; f32 remainder;
} RingUpdate150C8A68;
typedef struct { u8 reserved00[0x380]; f32 heading; u8 reserved384[0x61C]; } RingPlayer150C8A68;

extern s32 D_80082FA4;
extern RingPlayer150C8A68 *D_800DBFF0;
extern void (*D_80088858[])(RingUpdate150C8A68 *,f32 *,u8,f32,f32);
extern void (*D_80088864[])(RingUpdate150C8A68 *,f32);
extern s32 (*D_80088860[])(RingUpdate150C8A68 *);
f32 func_151423D8(u8);
void func_1516972C(struct102 *);

/* Age and grow a ring, emit perimeter callbacks, then update or retire it.
 * Float literals retain retail bits 40C90FDB, 4B263BD7 and 3F360B61. */
void func_150C8A68(RingUpdate150C8A68 *effect) {
    s32 heading;
    u8 expired = 0;
    f32 previousRadius;
    f32 sine,cosine;
    s16 elapsed;
    u8 angle;
    f32 point[3];
    f32 *step = &D_800BE9A4;
    if (effect->flags & 1) {
        effect->lifetime -= D_800BE9E4;
        if (effect->lifetime < 0) expired = 1;
    }
    if (!expired) {
        previousRadius = effect->radius;
        effect->radius += effect->growthRate * *step;
        if (effect->fadeStart < effect->lifetime) {
            elapsed = effect->initialLifetime - effect->lifetime;
            effect->amplitude = elapsed * effect->fadeInScale;
        }
        if (effect->lifetime < effect->fadeEnd) effect->amplitude = effect->lifetime * effect->fadeOutScale;
        if (effect->emission != -1) {
            effect->remainder += (effect->emissionRate * *step) * (6.2831854820251465f * effect->radius);
            while (effect->remainder > 1.0f) {
                heading = (s32)(D_800DBFF0[D_80082FA4].heading * 0.7111111283302307f);
                angle = (u32)func_150ADA20() % 81U + heading - 40;
                sine = func_151423D8((u8)(angle - 64));
                cosine = func_151423D8(angle);
                point[0] = effect->x + sine * effect->radius;
                point[1] = effect->y;
                point[2] = effect->z + cosine * effect->radius;
                if (point[2] * point[2] + point[0] * point[0] < 10894295.0f) D_80088858[effect->emission](effect,point,angle,sine,cosine);
                effect->remainder -= 1.0f;
            }
        }
        if (effect->update != -1) D_80088864[effect->update](effect,previousRadius);
        if (effect->finish != -1 && D_80088860[effect->finish](effect) == 0) expired = 1;
    }
    if (expired) func_1516972C((struct102 *)effect);
}


s32 func_150C8DB8() {
    return 0;
}

s32 func_150C99B4() {
    return 0;
}

s32 func_150C9BDC() {
    return 0;
}

s32 func_150C9DC4() {
    return 0;
}

/* Integrate position and angles, retaining the original single-precision grouping. */
s32 func_150CA07C(u8 *record) {
    f32 acceleration = *(f32 *)(record + 0x5C);
    f32 verticalVelocity = *(f32 *)(record + 0x48);
    *(f32 *)(record + 0x38) += *(f32 *)(record + 0x44) * D_800BE9A4;
    *(f32 *)(record + 0x3C) += verticalVelocity * D_800BE9A4
        + acceleration * D_800BE9A4 * D_800BE9A4 * 0.5f;
    *(f32 *)(record + 0x40) += *(f32 *)(record + 0x4C) * D_800BE9A4;
    { f32 delta = acceleration * D_800BE9A4;
    *(f32 *)(record + 0x48) = verticalVelocity + delta; }
    *(f32 *)(record + 0x20) += *(f32 *)(record + 0x50) * D_800BE9A4;
    *(f32 *)(record + 0x24) += *(f32 *)(record + 0x54) * D_800BE9A4;
    *(f32 *)(record + 0x28) += *(f32 *)(record + 0x58) * D_800BE9A4;
    return 1;
}

s32 func_150CA150() {
    return 0;
}

#include "structs.h"
s32 func_150ADA20(void);
f32 func_150ADA68(void);
void func_1514C678(f32, f32, f32, f32, s16, s16, s16, u8, s32, f32, void *, u8);

/* Submit a randomized type-19 burst at the point after both RNG calls. */
void func_150CA930(struct17 *point) {
    s16 count = (u32)func_150ADA20() % 21U + 10;
    f32 scale = func_150ADA68() * 59.0f + 170.0f;

    func_1514C678(point->unk0, point->unk4, point->unk8, scale,
        0, 255, count, 0x13, 0, 0.0f, 0, 255);
}

s32 func_150CA9D0(u8 *arg0) {
    s32 temp_v0 = *(s16 *)(arg0 + 0x1C);

    if (temp_v0 < 0x20) {
        s32 temp_v1 = temp_v0 << 3;
        if (temp_v1 < *(u8 *)(arg0 + 0x28)) {
            *(u8 *)(arg0 + 0x28) = temp_v1;
        }
    }
    return 1;
}

s32 func_150CAA04() {
    return 0;
}

extern s32 D_800BE9E4;
typedef struct { u8 pad00[0x58]; f32 x, pad5C, z; u8 pad64[0x44]; f32 damping; } DampingState150CAC28;
/* Apply one damping step for each elapsed tick. */
s32 func_150CAC28(DampingState150CAC28 *state, s32 unused) {
    u32 ticks;
    f32 *factor = &state->damping;
    for (ticks = (u32)D_800BE9E4; ticks != 0; ticks--) {
        state->x *= *factor;
        state->z *= *factor;
    }
    return 1;
}

s32 func_150CADD0() {
    return 0;
}

/* Integrate position and angles, retaining the original single-precision grouping. */
s32 func_150CB008(u8 *record) {
    f32 acceleration = *(f32 *)(record + 0x5C);
    f32 verticalVelocity = *(f32 *)(record + 0x48);
    *(f32 *)(record + 0x38) += *(f32 *)(record + 0x44) * D_800BE9A4;
    *(f32 *)(record + 0x3C) += verticalVelocity * D_800BE9A4
        + acceleration * D_800BE9A4 * D_800BE9A4 * 0.5f;
    *(f32 *)(record + 0x40) += *(f32 *)(record + 0x4C) * D_800BE9A4;
    { f32 delta = acceleration * D_800BE9A4;
    *(f32 *)(record + 0x48) = verticalVelocity + delta; }
    *(f32 *)(record + 0x20) += *(f32 *)(record + 0x50) * D_800BE9A4;
    *(f32 *)(record + 0x24) += *(f32 *)(record + 0x54) * D_800BE9A4;
    *(f32 *)(record + 0x28) += *(f32 *)(record + 0x58) * D_800BE9A4;
    return 1;
}
