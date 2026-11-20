#include <ultra64.h>
#include "structs.h"

/* Non-matching placeholders for the text-only asm slice asm/133190.s. */

extern void (*D_80088C18[])(u8 *);
extern void (*D_80088C28[])(u8 *, s32, u8);
extern void (* volatile D_80088C38[])(u8 *, s32, u8);

#include "game/map_trail.h"
typedef MapTrailPoint MapTrailPoint133190;
typedef MapTrailPacket MapTrailPacket133190;
typedef struct {
    u32 flags00, zero04;
    s16 code08, lifetime;
    u32 zero0C, zero10;
    u8 rgba14[4], rgba18[4];
    u8 value1C, paletteIndex;
    s16 value1E, value20, value22;
    f32 scale, extentX, extentY;
    MapTrailPoint133190 position, velocity, acceleration;
    f32 zero54;
    u32 flags58, zero5C;
    u8 value60, value61;
    s8 value62, value63, value64, value65;
    u8 value66, pad67;
    s16 zero68;
    u8 pad6A[2];
    f32 coefficient;
} MapTrailEffect133190;
typedef struct {
    u8 header[0x10];
    MapTrailPacket133190 packet;
    void *extra;
    f32 reciprocal;
    s16 timer;
    u16 reserved6A;
    void *children[2];
    u8 scratch[0x10];
    s32 segmentBytes;
} MapTrailRecord133190;
extern MapTrailPoint133190 D_800A5480;
extern f32 D_800A2410, D_800A2414;
void *func_15167A68(s32, s32, s32, s32, u8, u8);
s32 func_150ADA20(void);
void func_15106214(MapTrailRecord133190 *);
void func_15106610(MapTrailRecord133190 *);
void *func_15130280(MapTrailEffect133190 *, u8, void *, s32, u8, s32);
void *memcpy(void *, const void *, u32);

/* Allocate a sampled map trail and attach an effect at each endpoint. */
void *func_15105CE0(MapTrailPacket133190 *packet, s32 extraBytes, u8 priority, s32 context) {
    s32 pieces;
    s32 pointBytes;
    MapTrailRecord133190 *record;
    u32 firstFlag;
    MapTrailEffect133190 effect;
    u8 i;

    pieces = packet->pieces;
    pointBytes = (pieces + 2) * sizeof(MapTrailPoint133190);
    record = func_15167A68(0x40, context,
                          pieces * 0x34 + pointBytes + extraBytes + 0x88,
                          1, priority, 1);
    if (record == 0) {
        return 0;
    }
    memcpy(&record->packet, packet, sizeof(*packet));
    /* Each sampled segment occupies thirteen 32-bit words. */
    record->extra = (u8 *)record + (((u32)pieces * 13U) << 2) + pointBytes + 0x88;
    record->reciprocal = 1.0f / (f32)(packet->pieces + 1);
    record->timer = (u32)func_150ADA20() % (packet->maximum + 1) + packet->minimum;
    func_15106214(record);
    func_15106610(record);
    record->children[0] = 0;
    record->children[1] = 0;
    bzero(record->scratch, sizeof(record->scratch));
    record->segmentBytes = record->packet.pieces * 0x30 + 0x60;

    effect.paletteIndex = 0x2B;
    effect.code08 = 0x4404;
    effect.flags00 = 0x200005;
    effect.zero04 = 0;
    effect.lifetime = 300;
    effect.zero0C = 0;
    effect.zero10 = 0;
    effect.rgba14[0] = 0xFF;
    effect.rgba14[1] = 0xFF;
    effect.rgba14[2] = 0xFF;
    effect.rgba14[3] = 0xFF;
    effect.rgba18[0] = packet->red;
    effect.rgba18[1] = packet->green;
    effect.rgba18[2] = packet->blue;
    effect.rgba18[3] = packet->alpha;
    effect.value1C = 0xFF;
    effect.velocity = D_800A5480;
    effect.acceleration = D_800A5480;
    effect.value1E = 1;
    effect.value20 = 0xFF;
    effect.value22 = 1;
    effect.flags58 = 0xC000;
    effect.value60 = 6;
    effect.value61 = 6;
    effect.value62 = -1;
    effect.value63 = -1;
    effect.value64 = -1;
    effect.value65 = 0;
    effect.zero5C = 0;
    effect.value66 = 0xFF;
    effect.zero68 = 0;
    effect.zero54 = 0.0f;
    effect.scale = 1.0f;
    effect.coefficient = D_800A2410;
    effect.extentY = (packet->spread * D_800A2414) * 200.0f;
    effect.extentX = effect.extentY;
    for (i = 0; i < 2; i++) {
        effect.position = packet->points[i == 0 ? 0 : 3];
        firstFlag = func_150ADA20() != 0 ? 0x40 : 0;
        effect.flags58 = (func_150ADA20() != 0 ? 0x80 : 0) | firstFlag;
        record->children[i] = func_15130280(&effect, 0, 0, 0, priority, context);
    }
    return record;
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_133190/func_1510608C.s")

s32 func_151061E0(s32 arg0) {
    return arg0 + 0x88;
}

// Matched with guarded commutative-add normalization.
u8 *func_151061EC(u8 *arg0) {
    s32 temp_v1 = *(s32 *) (arg0 + 0x48);

    return arg0 + temp_v1 * 0x34 + 0x88;
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_133190/func_15106214.s")

f32 func_151064B4(f32 arg0) {
    f32 temp = 1.0f - arg0;

    return temp * temp * temp;
}

f32 func_151064DC(f32 arg0) {
    f32 temp = 1.0f - arg0;

    return 3.0f * arg0 * temp * temp;
}

f32 func_15106510(f32 arg0) {
    return 3.0f * arg0 * arg0 * (1.0f - arg0);
}

f32 func_15106540(register f32 arg0) {
    return arg0 * arg0 * arg0;
}

f32 func_15106558(f32 arg0) {
    f32 temp = 1.0f - arg0;

    return -3.0f * temp * temp;
}

f32 func_15106584(f32 arg0) {
    return 9.0f * arg0 * arg0 - 12.0f * arg0 + 3.0f;
}

f32 func_151065BC(f32 arg0) {
    return -9.0f * arg0 * arg0 + 6.0f * arg0;
}

f32 func_151065EC(f32 arg0) {
    return 3.0f * arg0 * arg0;
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_133190/func_15106610.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_133190/func_151067B8.s")

void func_15106E78(u8 *arg0) {
    void (*callback)(u8 *) = D_80088C18[arg0[0x5C]];

    if (callback != NULL) {
        callback(arg0);
    }
    if (*(u8 **)(arg0 + 0x6C) != NULL) {
        func_1516972C(*(u8 **)(arg0 + 0x6C));
    }
    if (*(u8 **)(arg0 + 0x70) != NULL) {
        func_1516972C(*(u8 **)(arg0 + 0x70));
    }
    func_151D5E30(arg0 + 0x74);
}

void func_15106EF8(u8 *arg0) {
    func_15106E78(arg0);
    func_15169804(arg0);
}

void func_15106F24(u8 *arg0) {
    func_15106E78(arg0);
    func_15169824(arg0);
}

void func_15106F50(u8 *arg0, s32 arg1, u8 arg2) {
    void (*callback)(u8 *, s32, u8) = D_80088C28[arg0[0x5C]];

    if (callback != NULL) {
        callback(arg0, arg1, arg2);
    }
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_133190/func_15106F98.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_133190/func_151070F8.s")

s32 func_151072BC() {
    return 0;
}

void func_15107604(u8 *arg0) {
    u8 *temp_v0 = *(u8 **)(arg0 + 0x60);
    u8 *temp_v1 = *(u8 **)temp_v0 + 0x28;

    *(s32 *)(temp_v1 + 8) = 0;
}

s32 func_1510761C(u8 *arg0) {
    u8 *temp_a1 = arg0;

    if (*(s32 volatile *)(temp_a1 + 0x30) != 0) {
        func_1516972C(*(s32 volatile *)(temp_a1 + 0x30));
    }
}

s32 func_1510764C(s32 arg0) {
    func_1510761C(arg0);
    func_1514933C(arg0);
}

s32 func_15107678(s32 arg0) {
    func_1510761C(arg0);
    func_15149368(arg0);
}

void func_151076A4(u8 *arg0, s32 arg1, u8 arg2) {
    void (* volatile *callbacks)(u8 *, s32, u8) = D_80088C38;

    if (callbacks[*(volatile u8 *)(arg0 + 0x68)] != NULL) {
        callbacks[*(volatile u8 *)(arg0 + 0x68)](arg0, arg1, arg2);
    }
}

s32 func_15107700() {
    return 0;
}

void func_151078E4(u8 *arg0, s32 arg1, u8 arg2) {
    u8 *target = *(u8 **) (arg0 + 0x60);

    func_15169850(arg1, arg2, (s32) target, (s32) (target + 4), (s32) arg0);
}

void func_1515C244(struct127 *, struct17 *, f32 *, f32 *);
void func_15143794(s16, s16, f32, vertex *);
void func_15107A20(struct127 *, s16, s16, vertex *, struct17 *);
void func_15107AE0(const f32 *, const f32 *, f32 *, f32 *);

/* Update the linked actor point and rebuild its fractional points when changed. */
s32 func_15107924(u8 *owner, u8 *changed) {
    u8 *link = *(u8 **)(owner + 0x60);
    struct127 *actor = *(struct127 **)link;
    struct17 original;
    f32 *savedPoint;
    f32 *point;

    if (*(s32 *)actor == 0 ||
            (point = (f32 *)(owner + 0x14),
             link[4] != *((u8 *)actor + 0x3B))) {
        return 0;
    }
    *changed = 0;
    original = *(struct17 *)point;
    savedPoint = point;
    func_15107A20(actor, *(s16 *)(link + 6), *(s16 *)(link + 8),
                  (vertex *)point, NULL);
    if (original.unk0 != *(f32 *)(owner + 0x14) ||
            original.unk4 != *(f32 *)(owner + 0x18) ||
            original.unk8 != *(f32 *)(owner + 0x1C)) {
        *changed = 1;
        func_15107AE0(savedPoint, (f32 *)(owner + 0x38),
                      (f32 *)(owner + 0x20), (f32 *)(owner + 0x2C));
    }
    return 1;
}
/* Apply the actor-scaled direction to its queried origin and optionally return that origin. */
void func_15107A20(struct127 *actor, s16 yaw, s16 pitch, vertex *point, struct17 *originOut) {
    struct17 origin;
    f32 radius;
    f32 otherScale;

    func_1515C244(actor, &origin, &radius, &otherScale);
    func_15143794(yaw, pitch, radius, point);
    point->y *= actor->unkF0;
    point->x += origin.unk0;
    point->y += origin.unk4;
    point->z += origin.unk8;
    if (originOut != NULL) {
        *originOut = origin;
    }
}

/* Write two fractional points, retaining the original deltas across stores. */
void func_15107AE0(const f32 start[3], const f32 end[3], f32 first[3], f32 second[3]) {
    f32 firstFraction = 0.333f;
    f32 secondFraction = 0.6667f;
    f32 dx = end[0] - start[0];
    f32 dy = end[1] - start[1];
    f32 dz = end[2] - start[2];

    first[0] = start[0] + dx * firstFraction;
    first[1] = start[1] + dy * firstFraction;
    first[2] = start[2] + dz * firstFraction;
    second[0] = start[0] + dx * secondFraction;
    second[1] = start[1] + dy * secondFraction;
    second[2] = start[2] + dz * secondFraction;
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_133190/func_15107B78.s")

s32 func_15107C1C() {
    return 0;
}

void func_15107F54(u8 *, u8, u8 *, u8 *);

/* Transform a valid linked actor point and refresh its fractional points if moved. */
s32 func_15107E48(u8 *owner, u8 *changed) {
    u8 *link = *(u8 **)(owner + 0x60);
    u8 *actor = *(u8 **)link;
    struct17 original;
    f32 *savedPoint;
    f32 *point;

    if (*(s32 *)actor == 0 || link[4] != actor[0x3B]) {
        return 0;
    }
    if ((point = (f32 *)(owner + 0x14), *(s32 *)(actor + 0x1D4) == 0)) {
        return 0;
    }
    *changed = 0;
    original = *(struct17 *)point;
    savedPoint = point;
    func_15107F54(actor, link[0x14], link + 8, (u8 *)point);
    if (original.unk0 != *(f32 *)(owner + 0x14) ||
            original.unk4 != *(f32 *)(owner + 0x18) ||
            original.unk8 != *(f32 *)(owner + 0x1C)) {
        *changed = 1;
        func_15107AE0(savedPoint, (f32 *)(owner + 0x38),
                      (f32 *)(owner + 0x20), (f32 *)(owner + 0x2C));
    }
    return 1;
}

void func_15107F54(u8 *arg0, u8 arg1, u8 *arg2, u8 *arg3) {
    func_15143134(arg2, arg3, *(u32 *) (arg0 + 0x1D4) + (arg1 << 6));
}

void func_15107F98(u8 *arg0, s32 arg1, u8 arg2) {
    func_15169850(arg1, arg2, *(u8 **) (arg0 + 0x60), *(u8 **) (arg0 + 0x60) + 4, arg0);
}
