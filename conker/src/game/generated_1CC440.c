#include <ultra64.h>
#include "structs.h"
#include <math.h>
f32 fabsf(f32);
#pragma intrinsic (fabsf)
typedef struct { u8 retained00[0x10]; f32 offset; } SideParameters1519EF90;
typedef struct {
    u8 retained00[0x18];
    struct127 *actor;
    u8 retained1C[0x3C];
    SideParameters1519EF90 parameters;
} SideState1519EF90;
extern f32 D_800A8CE0, D_800A8CE4;
s32 func_15143E08(struct127 *);
f32 func_151423D8(u8);

typedef struct { f32 x, y, z; } SidePosition1519F1C8;
typedef struct {
    SidePosition1519F1C8 position;
    s16 lifetime;
    u16 flags;
    s32 mode;
    u8 reserved14, count, reserved16[6];
} SideRequest1519F1C8;
typedef struct {
    u8 *state;
    u8 kind, reserved05[3];
    f32 scale, phase;
    SidePosition1519F1C8 position;
    f32 elapsed, referenceX, referenceZ;
    s16 zero28;
    u8 red, green, blue, reserved2D;
    s16 duration, alpha, width, height;
    u8 reserved36[2];
    f32 speed, limit;
    u8 style, first, second, third, fourth, fifth;
    s16 zero46, count, command;
    f32 rate;
} SidePayload1519F1C8;
extern f32 D_800A8CE8, D_800A8CEC;
extern u8 D_800AB414[];
u8 func_151D8E20(void);
u8 *func_15147A80(void *, s32, s32, s32, s32, s32, s32, s32, void *, u8, s32);
void *memcpy(void *, const void *, u32);

typedef struct {
    f32 x, z, height, phase;
    s16 alpha, delay, light, reserved16, lifetime, reserved1A;
    f32 velocityX, velocityZ;
} SideEntry1519F4F0;
typedef struct {
    f32 height;
    s16 vertices[9], reserved16;
    u32 metadata;
    u8 flags, state;
    u16 reserved1E;
    s32 value;
} SideFloor1519F4F0;
typedef struct {
    u8 reserved00[0x25], capacity, reserved26[6];
    s8 count, head, tail;
    u8 reserved2F[0x25];
    f32 position[3];
    SideFloor1519F4F0 floor;
    u8 reserved84[0x10];
    SideEntry1519F4F0 *entries;
    SidePayload1519F1C8 *payload;
    s32 reserved9C;
} SideEffect1519F4F0;
extern f32 D_800A8CF0, D_800BE9A4;
s32 func_15045800(f32 *, u16, f32, void *);

typedef struct { f32 x, z; } SideVelocity1519F7F0;
typedef struct {
    f32 x, z, height, phase;
    s16 alpha, delay, light, tag, lifetime, reserved1A;
    SideVelocity1519F7F0 velocity;
} SideEmitEntry1519F7F0;
typedef struct {
    u8 reserved00[0x10];
    SidePosition1519F1C8 point;
    s16 lifetime;
    u16 flags;
    s32 mode;
    u8 reserved24, capacity, reserved26[6];
    s8 count, head, tail;
    u8 reserved2F[0x25];
    SidePosition1519F1C8 published;
    SideFloor1519F4F0 floor;
    u8 reserved84[0x10];
    SideEmitEntry1519F7F0 *entries;
    SidePayload1519F1C8 *payload;
    s32 reserved9C;
} SideEmitter1519F7F0;
typedef struct {
    u8 *state;
    u8 mode, reserved05[3];
} SideTransition1519F7F0;
struct260 *func_151491F4(s16, s8, s8, u8, u8, s32, u8, s32);
s32 func_150ADA20(void);

extern u8 D_80090E0C[];
extern u32 D_800D2C9C;
void func_151D5D60(void *, s16, s32, Vtx **, u8 *);
Gfx *func_15142E24(Gfx *, void *, s32, s32, s32, s32, s32, u8, u8 *, u8 *, s32);
Gfx *func_15142B7C(Gfx *, u32, u32);
Gfx *func_15142C10(Gfx *, s32, s32, s32, s32, u8 *);
Gfx *func_15142CF0(Gfx *, s32, s32, s32, s32, s32, s32, u8 *);
Gfx *func_1513F4E4(Gfx *, u8, u8 *);
Gfx *func_15142FBC(Gfx *, u32, u32, u8 *);

extern s32 D_800BE9E4;


typedef struct {
    u8 *first;
    u8 *second;
    u8 *third;
    u8 *fourth;
} FourWord1CC440;

typedef struct {
    f32 x, y, z;
    u8 tag;
    u8 retained0D[3];
    f32 phase;
} FractionalBurstPayload151A0AF8;
typedef struct {
    u8 retained00[0x0C];
    u8 context;
    u8 retained0D[0x1B];
    FractionalBurstPayload151A0AF8 payload;
} FractionalBurstEmitter151A0AF8;
extern f32 D_800A8D10, D_800BE9A4;
f32 func_150ADA68(void);
void func_1514C678(f32, f32, f32, f32, s16, s16, s16, u8, s32, f32, void *, u8);

/* Non-matching placeholders for the text-only asm slice asm/1CC440.s. */

void func_1519F48C(u8 *arg0);
void func_151A0928(u8 *arg0);
void func_1516972C(u8 *arg0);

/* Query a side-offset point with a sampled-heading fallback. */
s32 func_1519EF90(u8 *record, u8 mode, f32 *output) {
    SideState1519EF90 *state = *(SideState1519EF90 **)record;
    SideParameters1519EF90 *parameters = &state->parameters;
    u8 *actor = (u8 *)state->actor;
    f32 deltaX, deltaZ;
    f32 tangentX, tangentZ;
    f32 reciprocalLength;
    f32 offset;
    u8 heading;

    if (*(void **)(actor + 0x1D4) == 0) return 0;
    deltaX = *(f32 *)(actor + 0x14) - *(f32 *)(record + 0x20);
    deltaZ = *(f32 *)(actor + 0x1C) - *(f32 *)(record + 0x24);
    if (D_800A8CE0 < fabsf(deltaX) || D_800A8CE0 < fabsf(deltaZ)) {
        reciprocalLength = 1.0f / sqrtf(deltaX * deltaX + deltaZ * deltaZ);
        tangentX = deltaZ * reciprocalLength;
        tangentZ = deltaX * reciprocalLength;
    } else {
        heading = func_15143E08((struct127 *)actor);
        tangentX = func_151423D8(heading);
        tangentZ = func_151423D8((u8)(heading - 0x40));
    }
    if (mode == 6) offset = parameters->offset;
    else offset = -parameters->offset;
    output[0] = *(f32 *)(actor + 0x14) + offset * tangentX;
    output[2] = *(f32 *)(actor + 0x1C) - offset * tangentZ;
    if (*(f32 *)(actor + 0x118) < D_800A8CE4) output[1] = *(f32 *)(actor + 0x18);
    else output[1] = *(f32 *)(actor + 0x118);
    return 1;
}

void func_1519F108(u8 *arg0) {
    register u8 **link = *(u8 ***)(arg0 + 0x98);
    register u8 *record = *link;

    if (record != NULL) {
        register s32 state = *(s32 *)(arg0 + 0x20);
        register FourWord1CC440 *fields = (FourWord1CC440 *)(record + 0x58);

        if (state == 6) {
            fields->first = 0;
        }
        if (*(s32 *)(arg0 + 0x20) == 7) {
            fields->third = 0;
        }
    }
    func_151478F4(arg0);
}

void func_1519F168(u8 *arg0) {
    register u8 **link = *(u8 ***)(arg0 + 0x98);
    register u8 *record = *link;

    if (record != NULL) {
        register s32 state = *(s32 *)(arg0 + 0x20);
        register FourWord1CC440 *fields = (FourWord1CC440 *)(record + 0x58);

        if (state == 6) {
            fields->first = 0;
        }
        if (*(s32 *)(arg0 + 0x20) == 7) {
            fields->third = 0;
        }
    }
    func_15147928(arg0);
}

/* Create a side-offset effect and attach its owner-linked payload. */
u8 *func_1519F1C8(u8 *state, u8 mode) {
    u8 *actor = *(u8 **)(state + 0x18);
    SideRequest1519F1C8 request;
    SidePayload1519F1C8 packet;
    u8 *created;
    u8 color;

    color = func_151D8E20();
    /* Reserved fields and a failed position query retain their stack bytes. */
    request.flags = 0x42;
    request.lifetime = 300;
    request.count = 10;
    packet.duration = 200;
    packet.style = 3;
    packet.state = state;
    packet.kind = 6;
    packet.first = 0x55;
    packet.second = 3;
    packet.third = 0x55;
    packet.fourth = 0x88;
    packet.fifth = 0xC4;
    packet.zero28 = 0;
    packet.zero46 = 0;
    packet.alpha = 255;
    packet.width = 40;
    packet.height = 25;
    packet.count = 6;
    packet.command = 0x325;
    packet.scale = D_800A8CE8;
    packet.speed = D_800A8CEC;
    packet.limit = 1.0f;
    packet.phase = 0.0f;
    packet.elapsed = 0.0f;
    request.mode = mode;
    packet.rate = 1.5f;
    packet.referenceX = *(f32 *)(actor + 0x14);
    packet.referenceZ = *(f32 *)(actor + 0x1C);
    if (func_1519EF90((u8 *)&packet, mode, (f32 *)&request.position)) {
        packet.position = request.position;
        request.flags |= 4;
    }
    packet.red = D_800AB414[color * 3];
    packet.green = D_800AB414[color * 3 + 1];
    packet.blue = D_800AB414[color * 3 + 2];
    created = func_15147A80(&request, 0x50, 0x24, 5, 5, 5, 0, 0, state + 0x34, 255, 1);
    if (created != NULL) {
        memcpy(*(void **)(created + 0x98), &packet, 0x50);
    }
    return created;
}

void func_1519F3B8(u8 *arg0) {
    FourWord1CC440 *temp_v1;
    u8 *r = func_1519F1C8(arg0, 6);

    temp_v1 = (FourWord1CC440 *) (arg0 + 0x58);
    temp_v1->first = r;
    temp_v1->second = 0;
    r = func_1519F1C8(arg0, 7);
    temp_v1->third = r;
    temp_v1->fourth = 0;
}

/* Note 535: four-resource ownership-specific teardown. */
void func_1519F400(u8 *arg0) {
    u8 **resources = (u8 **) (arg0 + 0x58);

    if (resources[0] != NULL) {
        func_1519F48C(resources[0]);
    }
    if (resources[2] != NULL) {
        func_1519F48C(resources[2]);
    }
    if (resources[1] != NULL) {
        func_151A0928(resources[1]);
        func_1516972C(resources[1]);
    }
    if (resources[3] != NULL) {
        func_151A0928(resources[3]);
        func_1516972C(resources[3]);
    }
}

void func_1519F48C(u8 *arg0) {
    register u8 **link = *(u8 ***)(arg0 + 0x98);
    register u8 *record = *link;

    if (record != NULL) {
        register s32 state = *(s32 *)(arg0 + 0x20);
        register FourWord1CC440 *fields = (FourWord1CC440 *)(record + 0x58);

        if (state == 6) {
            fields->first = 0;
        }
        if (*(s32 *)(arg0 + 0x20) == 7) {
            fields->third = 0;
        }
        *link = NULL;
    }

    arg0[0x30] = 0;
    *(u16 *)(arg0 + 0x1E) &= ~2;
    ((u8 *)link)[4] |= 1;
}

/* Advance side-effect ring entries, retire expired spans and publish the head position. */
s32 func_1519F4F0(SideEffect1519F4F0 *effect) {
    SidePayload1519F1C8 *packet = effect->payload;
    SideEntry1519F4F0 *entries = effect->entries;
    SideEntry1519F4F0 *entry;
    s32 cursor;
    s32 expired;
    f32 position[3];
    f32 limit;

    if (effect->count < 2 && (packet->kind & 1)) return 0;
    cursor = effect->tail;
    if (cursor != effect->head) {
        limit = D_800A8CF0;
        do {
            cursor--;
            if (cursor < 0) cursor = effect->capacity - 1;
            expired = 0;
            entry = &entries[cursor];
            entry->lifetime = (u32)entry->lifetime - (u32)D_800BE9E4;
            if (entry->lifetime < 0) expired = 1;
            entry->light = 255;
            if (entry->delay > 0) entry->delay = (u32)entry->delay - (u32)D_800BE9E4;
            else entry->alpha = (u32)entry->alpha - (u32)packet->height * (u32)D_800BE9E4;
            entry->phase += packet->limit * D_800BE9A4;
            entry->x += entry->velocityX * D_800BE9A4;
            entry->z += entry->velocityZ * D_800BE9A4;
            position[0] = entry->x;
            position[1] = entry->height + 30.0f;
            position[2] = entry->z;
            if (limit < fabsf(position[0]) || limit < fabsf(position[2])) expired = 1;
            else if (func_15045800(position, 0, entry->height - 30.0f, &effect->floor)) entry->height = effect->floor.height;
            else expired = 1;
            if (entry->alpha < 0) expired = 1;
            if (expired) {
                while (cursor != effect->head) {
                    effect->head++;
                    if (effect->head == effect->capacity) effect->head = 0;
                    effect->count--;
                }
                entries[effect->head].alpha = 0;
            }
        } while (cursor != effect->head);
    }
    packet->zero46 = (u32)packet->zero46 + (u32)packet->count * (u32)D_800BE9E4;
    if (effect->count > 0) {
        effect->position[0] = entries[effect->head].x;
        effect->position[1] = entries[effect->head].height;
        effect->position[2] = entries[effect->head].z;
    } else {
        effect->position[0] = 0.0f;
        effect->position[1] = 0.0f;
        effect->position[2] = 0.0f;
    }
    return 1;
}

/* Sample movement into the side-effect ring and smooth its transverse velocity. */
s32 func_1519F7F0(SideEmitter1519F7F0 *effect) {
    SidePayload1519F1C8 *packet = effect->payload;
    SideEmitEntry1519F7F0 *entries = effect->entries;
    u8 *state = packet->state;
    struct127 *actor = *(struct127 **)(state + 0x18);
    s32 initialized;
    f32 dx, dy, dz, inverseLength;
    SideTransition1519F7F0 transition;
    f32 length, fraction, remaining, weight, timeStep, weightStep;
    SidePosition1519F1C8 position;
    FourWord1CC440 *outputs;
    SideEmitEntry1519F7F0 *entry;
    u8 *created;
    s32 previous, earlier, accepted;
    SideVelocity1519F7F0 velocity;
    f32 stepX, stepY, stepZ, bound;
    f32 point[3];
    u32 random;
    f32 weightDifference;

    if (actor->interaction_state == 0) return 0;
    if (actor->unk1D4 == NULL) return 0;
    if (state[0x1C] != actor->unique_id) return 0;
    initialized = 0;
    if (!(effect->flags & 4)) {
        if (func_1519EF90((u8 *)packet, (u8)effect->mode, (f32 *)&effect->point)) {
            packet->position = effect->point;
            effect->flags |= 4;
            initialized = 1;
        } else return 1;
    }
    if (!initialized && !func_1519EF90((u8 *)packet, (u8)effect->mode, (f32 *)&effect->point)) {
        func_1519F48C((u8 *)effect);
        transition.state = packet->state;
        transition.mode = effect->mode;
        outputs = (FourWord1CC440 *)(transition.state + 0x58);
        /* Preserve the three untouched bytes copied with this transition. */
        created = (u8 *)func_151491F4(300, -1, 11, 0, 6, 8, 255, 0);
        if (created != NULL) memcpy(created + 0x28, &transition, 8);
        if (effect->mode == 6) outputs->second = created;
        else outputs->fourth = created;
        return 1;
    }
    packet->referenceX = actor->x_position;
    packet->referenceZ = actor->z_position;
    dx = effect->point.x - packet->position.x;
    dy = effect->point.y - packet->position.y;
    dz = effect->point.z - packet->position.z;
    /* Retail leaves inverseLength untouched when motion is below the bound.
     * Normal retained progress is <= 1 on that path, so no sample uses it. */
    if (0.0001f < fabsf(dx) || 0.0001f < fabsf(dy) || 0.0001f < fabsf(dz)) {
        length = sqrtf(dx * dx + dy * dy + dz * dz);
        inverseLength = 1.0f / length;
        packet->phase += length * packet->scale;
    }
    if (1.0f < packet->phase) {
        fraction = 1.0f / packet->phase;
        remaining = packet->elapsed + D_800BE9A4;
        timeStep = remaining * fraction;
        position = packet->position;
        weight = packet->speed + packet->limit * remaining;
        weightDifference = packet->speed - weight;
        if (effect->mode == 7) {
            velocity.x = (-dz * inverseLength) * packet->rate;
            velocity.z = (dx * inverseLength) * packet->rate;
        } else {
            velocity.x = (dz * inverseLength) * packet->rate;
            velocity.z = (-dx * inverseLength) * packet->rate;
        }
        previous = effect->tail - 1;
        if (previous < 0) previous = effect->capacity - 1;
        if (previous != effect->head && effect->count != 0) {
            earlier = previous - 1;
            if (earlier < 0) earlier = effect->capacity - 1;
            entries[earlier].velocity.x = (entries[earlier].velocity.x + velocity.x) * 0.5f;
            entries[earlier].velocity.z = (entries[earlier].velocity.z + velocity.z) * 0.5f;
        }
        stepX = dx * fraction;
        stepY = dy * fraction;
        stepZ = dz * fraction;
        weightStep = weightDifference * fraction;
        bound = 20000.0f;
        do {
            entry = &entries[effect->tail];
            entry->velocity = velocity;
            entry->x = position.x;
            entry->z = position.z;
            entry->lifetime = packet->duration;
            entry->phase = weight;
            entry->alpha = packet->alpha;
            entry->delay = packet->width;
            entry->light = 255;
            entry->tag = packet->zero28;
            random = (u32)func_150ADA20();
            packet->zero28 = (u32)packet->zero28 + packet->fourth + random % ((u32)packet->fifth + 1);
            entry->x += entry->velocity.x * remaining;
            entry->z += entry->velocity.z * remaining;
            point[0] = entry->x;
            if (actor->unk118 < -9500.0f) point[1] = actor->y_position + 100.0f;
            else point[1] = actor->unk118 + 100.0f;
            point[2] = entry->z;
            accepted = 1;
            if (bound < fabsf(point[0]) || bound < fabsf(point[2])) accepted = 0;
            else if (func_15045800(point, 0, point[1] - 200.0f, &effect->floor)) entry->height = effect->floor.height;
            else accepted = 0;
            if (accepted) {
                effect->tail++;
                if (effect->tail == effect->capacity) effect->tail = 0;
                effect->count++;
                if (effect->head == effect->tail) {
                    effect->head++;
                    if (effect->head == effect->capacity) effect->head = 0;
                    effect->count--;
                }
            }
            position.x += stepX;
            position.y += stepY;
            position.z += stepZ;
            weight += weightStep;
            remaining -= timeStep;
            packet->phase -= 1.0f;
        } while (1.0f < packet->phase);
        packet->position = position;
        packet->elapsed = remaining;
    }
    return 1;
}

/* Render the backward side-effect ring as a three-vertex ribbon strip. */
Gfx *func_1519FE6C(SideEmitter1519F7F0 *effect, Gfx *output, s16 view) {
    Vtx *cursor;
    SidePayload1519F1C8 *packet;
    SideEmitEntry1519F7F0 *entries;
    SidePosition1519F1C8 position, previousPosition;
    f32 previousWidth, currentWidth, dx, dz, inverseLength, offsetX, offsetZ;
    s32 index, previous, high, low;
    u8 previousAlpha, alpha;
    s16 previousTag, tag;
    s16 texture[3];
    s16 remaining;
    u8 sync;
    u8 factor;
    SideEmitEntry1519F7F0 *entry;

    if (effect->count >= 2) {
    func_151D5D60(effect->reserved84, view,
        effect->capacity * 48 + 0x120, &cursor, NULL);
    if (cursor != NULL) {
    packet = effect->payload;
    entries = effect->entries;
    sync = 1;
    factor = 0;
    if (packet->kind & 2) {
        s32 forwardIndex;
        remaining = packet->style;
        forwardIndex = effect->head;
        /* Retail enters even when the initial fade count is zero. */
        do {
            entries[forwardIndex].light = factor;
            factor += packet->first;
            forwardIndex++;
            if (forwardIndex == effect->capacity) forwardIndex = 0;
            remaining = (s16)(remaining - 1);
        } while (remaining != 0 && forwardIndex != effect->tail);
    }
    if (packet->kind & 4) {
        s16 backwardRemaining;
        u8 backwardFactor;
        s32 backwardIndex;
        backwardIndex = effect->tail - 1;
        backwardFactor = 0;
        backwardRemaining = packet->second;
        if (backwardIndex < 0) backwardIndex = effect->capacity - 1;
        do {
            entries[backwardIndex].light = (entries[backwardIndex].light * backwardFactor) >> 8;
            backwardFactor += packet->third;
            backwardIndex--;
            if (backwardIndex < 0) backwardIndex = effect->capacity - 1;
            backwardRemaining = (s16)(backwardRemaining - 1);
        } while (backwardRemaining != 0 && backwardIndex != effect->tail);
    }
    output = func_15142E24(output, D_80090E0C, 0, 0, 0, 0, 57, 0, NULL, &sync, 62);
    output = func_15142B7C(output, 1, 0x160600);
    output = func_15142C10(output, packet->red, packet->green, packet->blue, 255, &sync);
    output = func_15142CF0(output, 0, 0, 255, 255, 255, 0, &sync);
    output = func_1513F4E4(output, 7, &sync);
    output = func_15142FBC(output, D_800D2C9C | 0x80000 | 0x2CA0, 0x5049D8, &sync);
    if (effect->flags & 2) {
        index = effect->tail - 1;
        if (index < 0) index = effect->capacity - 1;
        previousPosition = effect->point;
        previousWidth = packet->speed;
        entry = &entries[index];
        previousAlpha = (entry->light * entry->alpha) >> 8;
        previousTag = entry->tag;
    } else {
        previous = effect->tail - 1;
        if (previous < 0) previous = effect->capacity - 1;
        index = previous - 1;
        if (index < 0) index = effect->capacity - 1;
        entry = &entries[previous];
        previousPosition.x = entry->x;
        previousPosition.y = entry->height;
        previousPosition.z = entry->z;
        previousWidth = entry->phase;
        previousAlpha = (entry->light * entry->alpha) >> 8;
        previousTag = entry->tag;
    }
    entry = &entries[index];
    position.x = entry->x;
    position.y = entry->height;
    position.z = entry->z;
    dx = position.x - previousPosition.x;
    dz = position.z - previousPosition.z;
    alpha = (entry->light * entry->alpha) >> 8;
    tag = entry->tag;
    currentWidth = entry->phase;
    if (0.0001f < fabsf(dx) || 0.0001f < fabsf(dz))
        inverseLength = 1.0f / sqrtf(dx * dx + dz * dz);
    else inverseLength = 1.0f;
    /* zero46 and command hold the signed texture interval for this strip. */
    texture[0] = packet->zero46;
    texture[2] = packet->zero46 + packet->command;
    if (texture[2] < texture[0]) {
        texture[0] = packet->zero46 % 1024;
        packet->zero46 = texture[0];
        texture[2] = packet->zero46 + packet->command;
    }
    texture[1] = (texture[2] + texture[0]) >> 1;
    if (effect->mode == 6) { high = 0; low = 2; }
    else if (effect->mode == 7) { high = 2; low = 0; }
    else { high = 2; low = 0; }
    offsetX = (-dz * inverseLength) * previousWidth;
    offsetZ = (dx * inverseLength) * previousWidth;
    cursor->v.ob[0] = (s32)(previousPosition.x + offsetX);
    cursor->v.ob[1] = (s32)previousPosition.y;
    cursor->v.ob[2] = (s32)(previousPosition.z + offsetZ);
    cursor->v.tc[0] = previousTag;
    cursor->v.tc[1] = texture[high];
    cursor->v.cn[0] = 255;
    cursor->v.cn[1] = 255;
    cursor->v.cn[2] = 255;
    cursor->v.cn[3] = 0;
    cursor->v.flag = 0;
    cursor++;
    cursor->v.ob[0] = (s32)(previousPosition.x);
    cursor->v.ob[1] = (s32)previousPosition.y;
    cursor->v.ob[2] = (s32)(previousPosition.z);
    cursor->v.tc[0] = previousTag;
    cursor->v.tc[1] = texture[1];
    cursor->v.cn[0] = 255;
    cursor->v.cn[1] = 255;
    cursor->v.cn[2] = 255;
    cursor->v.cn[3] = previousAlpha;
    cursor->v.flag = 0;
    cursor++;
    cursor->v.ob[0] = (s32)(previousPosition.x - offsetX);
    cursor->v.ob[1] = (s32)previousPosition.y;
    cursor->v.ob[2] = (s32)(previousPosition.z - offsetZ);
    cursor->v.tc[0] = previousTag;
    cursor->v.tc[1] = texture[low];
    cursor->v.cn[0] = 255;
    cursor->v.cn[1] = 255;
    cursor->v.cn[2] = 255;
    cursor->v.cn[3] = 0;
    cursor->v.flag = 0;
    cursor++;
    do {
        offsetX = (-dz * inverseLength) * currentWidth;
        offsetZ = (dx * inverseLength) * currentWidth;
        cursor->v.ob[0] = (s32)(position.x + offsetX);
        cursor->v.ob[1] = (s32)position.y;
        cursor->v.ob[2] = (s32)(position.z + offsetZ);
        cursor->v.tc[0] = tag;
        cursor->v.tc[1] = texture[high];
        cursor->v.cn[0] = 255;
        cursor->v.cn[1] = 255;
        cursor->v.cn[2] = 255;
        cursor->v.cn[3] = 0;
        cursor->v.flag = 0;
        cursor++;
        cursor->v.ob[0] = (s32)(position.x);
        cursor->v.ob[1] = (s32)position.y;
        cursor->v.ob[2] = (s32)(position.z);
        cursor->v.tc[0] = tag;
        cursor->v.tc[1] = texture[1];
        cursor->v.cn[0] = 255;
        cursor->v.cn[1] = 255;
        cursor->v.cn[2] = 255;
        cursor->v.cn[3] = alpha;
        cursor->v.flag = 0;
        cursor++;
        cursor->v.ob[0] = (s32)(position.x - offsetX);
        cursor->v.ob[1] = (s32)position.y;
        cursor->v.ob[2] = (s32)(position.z - offsetZ);
        cursor->v.tc[0] = tag;
        cursor->v.tc[1] = texture[low];
        cursor->v.cn[0] = 255;
        cursor->v.cn[1] = 255;
        cursor->v.cn[2] = 255;
        cursor->v.cn[3] = 0;
        cursor->v.flag = 0;
        cursor++;
        gSPVertex(output++, cursor - 6, 6, 0);
        gSP1Triangle(output++, 0, 3, 4, 0);
        gSP1Triangle(output++, 0, 4, 1, 0);
        gSP1Triangle(output++, 1, 4, 5, 0);
        gSP1Triangle(output++, 1, 5, 2, 0);
        previous = index;
        index--;
        if (index < 0) index = effect->capacity - 1;
        if (previous != effect->head) {
            previousPosition = position;
            entry = &entries[index];
            position.x = entry->x;
            position.y = entry->height;
            position.z = entry->z;
            alpha = (entry->light * entry->alpha) >> 8;
            tag = entry->tag;
            dx = position.x - previousPosition.x;
            dz = position.z - previousPosition.z;
            /* Later joins use exact zero, unlike the initial epsilon gate. */
            if (position.x == previousPosition.x && dz == 0.0f) inverseLength = 1.0f;
            else inverseLength = 1.0f / sqrtf(dx * dx + dz * dz);
            currentWidth = entry->phase;
        }
    } while (previous != effect->head);
    }
    }
    return output;
}


/* Refresh the selected linked-state value and invalidate a completed entry. */
void func_151A084C(struct260 *entry) {
    u8 **link;
    u8 *actor;
    FourWord1CC440 *outputs;
    u8 invalid;
    link = (u8 **)((u8 *)entry + 0x28);
    actor = *(u8 **)(*link + 0x18);
    outputs = (FourWord1CC440 *)(*link + 0x58);
    invalid = 0;
    if (*(s32 *)actor == 0) invalid = 1;
    if ((*link)[0x1C] != actor[0x3B]) invalid = 1;
    if (invalid == 0 && *(s32 *)(actor + 0x1D4) != 0) {
        u8 *result;
        invalid = 1;
        result = func_1519F1C8(*link, ((u8 *)link)[4]);
        if (((u8 *)link)[4] == 6) outputs->first = result;
        else outputs->third = result;
    }
    if (invalid) {
        func_151A0928((u8 *)entry);
        entry->unkE = -1;
        entry->unkD |= 1;
    }
}

void func_151A0928(u8 *arg0) {
    u8 *temp_v0 = *(u8 **) (arg0 + 0x28) + 0x58;

    if (arg0[0x2C] == 6) {
        *(s32 *) (temp_v0 + 4) = 0;
    } else {
        *(s32 *) (temp_v0 + 0xC) = 0;
    }
}

void func_151A0950(u8 *arg0, u8 *arg1, u8 arg2) {
    u8 **link = *(u8 ***)(arg0 + 0x98);
    u8 *record;
    s32 owner;

    if (arg2 == 0xA) {
        record = *link;
        if (record != NULL) {
            owner = *(s32 *)(record + 0x18);
            if (owner == *(s32 *)arg1 || record[0x1C] == arg1[4]) {
                func_1519F48C(arg0);
            }
        }
    }
}

void func_151A09B4(u8 *arg0, u8 *arg1, u8 arg2) {
    u8 *child = *(u8 **)(*(u8 **)(arg0 + 0x28) + 0x18);

    if (arg2 == 0 &&
            (child == *(u8 **)arg1 || child[0x3B] == arg1[4])) {
        func_151A0928(arg0);
        func_1516972C(arg0);
    }
}

typedef struct {
    f32 x;
    f32 y;
    f32 z;
    u8 selected;
    u8 padD[3];
    f32 zero;
} ActorHeightEffectPayload;
extern u8 D_800C35EA;
u32 func_1510F8CC(u32);
struct260 *func_151491F4(s16, s8, s8, u8, u8, s32, u8, s32);
void *memcpy(void *, const void *, u32);
/* Capture the actor position and cached height, then submit the selected effect. */
void func_151A0A10(u8 *actor, s16 effect, u8 variant, s32 flags) {
    struct260 *record;
    ActorHeightEffectPayload payload;

    if (actor != NULL) {
        payload.x = *(f32 *)(actor + 0x14);
        payload.z = *(f32 *)(actor + 0x1C);
        if (D_800C35EA != 1) {
            payload.y = *(f32 *)(actor + 0x180);
            payload.zero = 0.0f;
            switch (func_1510F8CC(*(u32 *)(actor + 0x184))) {
                case 10:
                    payload.selected = 0;
                    break;
                case 15:
                case 17:
                    payload.selected = 1;
                    break;
                default:
                    payload.selected = 0;
                    break;
            }
            record = func_151491F4(effect, -1, 1, 1, 0, 0x14, variant, flags);
            if (record != NULL) {
                memcpy((u8 *)record + 0x28, &payload, 0x14);
            }
        }
    }
}

/* Accumulate fractional emissions and submit each burst using live payload fields. */
void func_151A0AF8(FractionalBurstEmitter151A0AF8 *record) {
    record->payload.phase += D_800A8D10 * D_800BE9A4;
    if (record->payload.phase > 1.0f) {
        FractionalBurstPayload151A0AF8 *payload = &record->payload;

        do {
            f32 magnitude = func_150ADA68() * 25.0f + 15.0f;

            func_1514C678(payload->x, payload->y, payload->z,
                magnitude,
                0, 255, 5, 4, payload->tag, 0.0f, NULL, record->context);
            payload->phase -= 1.0f;
        } while (payload->phase > 1.0f);
    }
}

typedef struct {
    const void *template;
    u8 private04[8];
    s16 zero0C;
    s16 fixed0E;
    s16 positionX;
    s16 positionY;
    s16 positionZ;
    s16 directionX;
    s16 directionZ;
    u8 private1A[2];
    s8 scaledX;
    s8 scaledY;
    s8 scaledZ;
    s8 fixed1F;
    s16 directionY;
    s16 field22;
    s16 field24;
    s16 field26;
    s16 magnitude;
    s8 field2A;
    u8 private2B;
    u8 color0;
    u8 color1;
    u8 color2;
    u8 alpha;
    s8 zero30;
    s8 zero31;
    s8 zero32;
    u8 private33;
    u16 fixed34;
    u8 privateTail36[2];
} RandomShortPacket151A0C0C;
extern u8 D_800918A0[], D_8009187C[], D_8008F8D0[];
u8 *func_15167D84(void *, s32, s32, s8, u8, s32);
extern const f32 D_800A8D14, D_800A8D18;

/* Submit one randomized short-form particle through the shared callback ABI. */
s32 func_151A0C0C(s32 first, s32 ordinal, f32 x, f32 y, f32 z,
    f32 originX, f32 originY, f32 originZ, s32 heading, u8 startAngle,
    f32 radius, s32 style, f32 intensity, void *user, u8 mode) {
    RandomShortPacket151A0C0C packet;
    s16 angle;
    f32 firstPrimary, firstQuarter, headingPrimary, headingQuarter;
    f32 speed;
    s32 size;
    angle = (u32)func_150ADA20() % 15U - 63;
    firstPrimary = func_151423D8((u8)angle);
    firstQuarter = func_151423D8((u8)(angle - 64));
    headingPrimary = func_151423D8((u8)heading);
    headingQuarter = func_151423D8((u8)(heading - 64));
    speed = func_150ADA68() * D_800A8D14 + D_800A8D18;
    packet.directionX = (s16)((speed * firstPrimary) * headingQuarter);
    packet.directionY = (s16)((-speed) * firstQuarter);
    packet.directionZ = (s16)((speed * firstPrimary) * headingPrimary);
    packet.field22 = (u32)func_150ADA20() % 41U - 130;
    packet.field2A = (u32)func_150ADA20() % 3U + 6;
    size = (u32)func_150ADA20() % 451U + 250;
    packet.field24 = size;
    packet.zero30 = 0;
    packet.zero31 = 0;
    packet.zero32 = 0;
    packet.alpha = 255;
    packet.fixed1F = -1;
    packet.fixed34 = 0;
    packet.zero0C = 0;
    packet.fixed0E = 0;
    packet.field26 = size;
    packet.positionX = (s16)x;
    packet.positionY = (s16)y;
    packet.positionZ = (s16)z;
    packet.color0 = D_8008F8D0[style];
    packet.color1 = packet.color0;
    packet.color2 = packet.color0;
    /* All three fractional bytes intentionally come from x in retail. */
    packet.scaledX = (s8)(s32)(x * 256.0f);
    packet.scaledY = packet.scaledX;
    packet.scaledZ = packet.scaledX;
    switch (style) {
    case 0: packet.template = D_800918A0; break;
    case 1: packet.template = D_8009187C; break;
    }
    packet.magnitude = 200;
    func_15167D84(&packet, 0, 0, -1, mode, 1);
    return 1;
}


extern f32 D_800A8D20;
void func_151A11CC(f32, f32, f32, f32, f32, s32, s32, s32, s32, s32, f32, s32, s32, s32, s32, s32, s32, f32, s32, s32, s32, s32, s32, s32, s32, s32, u32, s32);
/* Submit the original fixed debug-display argument packet to its retail stub. */
void func_151A0E40(f32 x, f32 y, f32 value, u8 variant, s32 flags) {
    func_151A11CC(
        x, y, value, 163.0f, D_800A8D20,
        160, 75, 1055, 1270, 1, D_800A8D20,
        135, 68, 1055, 1270, 2, 1, D_800A8D20,
        70, 66, 1055, 1270, 7, 65, 4, 1, variant, flags);
}

extern f32 D_800A8D24;
/* Submit the original fixed debug-display argument packet to its retail stub. */
void func_151A0F28(f32 x, f32 y, f32 value, u8 variant, s32 flags) {
    func_151A11CC(
        x, y, value, 163.0f, D_800A8D24,
        160, 75, 1055, 1270, 1, D_800A8D24,
        135, 68, 1055, 1270, 2, 1, D_800A8D24,
        70, 66, 1055, 1270, 7, 65, 4, 1, variant, flags);
}

extern const f32 D_800A8D28;
/* Submit the scaled 28-argument packet to its original retail stub. */
void func_151A1010(f32 x, f32 y, f32 value, s16 span, f32 scale, f32 rate,
    u8 variant, s32 flags) {
    s16 clampedSpan;
    s32 finalSpan;
    span -= 32;
    clampedSpan = span;
    /* Keep the original span offset separate from the clamped width. */
    finalSpan = (s32)span + 16;
    if (clampedSpan <= 0) clampedSpan = 1;
    func_151A11CC(x, y, value, (250.0f * scale), 1.0f,
        ((s16)(s32)(70.0f * rate)), ((s16)(s32)(30.0f * rate)), ((s16)(s32)(D_800A8D28 * scale)), ((s16)(s32)(100.0f * scale)), 18, 1.0f,
        ((s32)(90.0f * rate)), ((s32)(20.0f * rate)), ((s16)(s32)(D_800A8D28 * scale)), ((s16)(s32)(100.0f * scale)), clampedSpan, 16, 1.0f,
        ((s16)(s32)(70.0f * rate)), ((s16)(s32)(30.0f * rate)), ((s16)(s32)(D_800A8D28 * scale)), ((s16)(s32)(100.0f * scale)), ((s32)(15.0f * scale)), ((s32)(10.0f * scale)),
        18, finalSpan, variant, flags);
}


void func_151A11CC(f32 arg0, f32 arg1, f32 arg2, f32 arg3, f32 arg4, s32 arg5, s32 arg6, s32 arg7, s32 arg8, s32 arg9, f32 arg10, s32 arg11, s32 arg12, s32 arg13, s32 arg14, s32 arg15, s32 arg16, f32 arg17, s32 arg18, s32 arg19, s32 arg20, s32 arg21, s32 arg22, s32 arg23, s32 arg24, s32 arg25, u32 arg26, s32 arg27) {
}

typedef struct {
    f32 x, y, z;
} EffectPacketPosition1CC440;

typedef struct {
    EffectPacketPosition1CC440 position;
    f32 sourceValueA;
    f32 phase;
    f32 sourceValueB;
    s16 parameters[4];
} RecordEffectPacket1CC440;

typedef struct {
    u8 *descriptor;
    u32 flags;
    u8 private08[4];
    s16 zero0C, lifetime;
    s16 x, y, z, zero16, zero18;
    u8 private1A[2];
    u8 fractionX, fractionZ, fractionY, fractionScale;
    s16 zero20, zero22, sizeY, sizeX, age;
    u8 zero2A, private2B;
    u8 red, green, blue, alpha;
    u8 zero30, zero31, zero32, private33;
    u16 curveFlags;
    u8 private36[2];
} EmissionPacket151A11E4;

extern u8 D_80090D34[];
extern u8 D_80090B60[];

/* Emit randomized particles with a 17-short motion and intensity curve. */
void func_151A11E4(struct260 *record) {
    RecordEffectPacket1CC440 *state = (RecordEffectPacket1CC440 *)((u8 *)record + 0x28);
    EmissionPacket151A11E4 packet;
    s16 curve[17];
    s32 firstAngle, secondAngle;
    f32 componentX, componentY, componentZ, polarSine;
    f32 targetX, targetZ, targetY;
    f32 radius, planar;
    f32 inverseHalf;
    u32 random;
    s16 size, peak;

    u8 *created;

    state->phase = state->phase + state->sourceValueB * D_800BE9A4;
    if (state->phase > 1.0f) {
        packet.red = 255;
        packet.green = 255;
        packet.blue = 255;
        packet.zero30 = 0;
        packet.zero31 = 0;
        packet.zero32 = 0;
        packet.fractionScale = 16;
        packet.curveFlags = 0x120;
        packet.flags = 0xC0001;
        packet.zero0C = 0;
        packet.descriptor = D_80090D34;
        packet.zero16 = 0;
        packet.zero20 = 0;
        packet.zero18 = 0;
        packet.zero22 = 0;
        packet.zero2A = 0;
        packet.alpha = 0;
        packet.sizeX = 2000;
        packet.sizeY = 2000;
        do {
            firstAngle = func_150ADA20() & 255;
            secondAngle = func_150ADA20() & 255;
            /* Capture the target before later providers can change the record. */
            componentX = func_151423D8((u8)(firstAngle - 64));
            componentY = func_151423D8((u8)firstAngle);
            componentZ = func_151423D8((u8)(secondAngle - 64));
            polarSine = func_151423D8((u8)secondAngle);
            radius = func_150ADA68() * state->sourceValueA;
            planar = radius * polarSine;
            targetX = state->position.x + planar * componentX;
            targetY = state->position.y - radius * componentZ;
            targetZ = state->position.z + planar * componentY;

            if (func_150ADA20() & 1) packet.curveFlags |= 4;
            if (func_150ADA20() & 1) packet.curveFlags |= 8;
            random = (u32)func_150ADA20();
            packet.lifetime = random % (u32)(state->parameters[1] + 1) + state->parameters[0];
            random = (u32)func_150ADA20();
            size = random % (u32)(state->parameters[3] + 1) + state->parameters[2];
            packet.age = D_80090B60[0x1D8] * (256 / packet.lifetime);
            peak = packet.age;
            curve[5] = peak >> 1;
            curve[0] = 255 / (peak - (s16)(peak - (peak >> 2)));
            curve[1] = peak;
            curve[2] = peak - (peak >> 2);
            curve[3] = size / (peak - curve[5]);
            curve[4] = peak;
            curve[6] = (peak >> 1);
            curve[13] = (peak >> 2);
            curve[14] = 255 / (s16)(peak >> 2);
            curve[15] = (peak >> 1);
            curve[16] = size / (s16)(peak >> 1);

            packet.x = (s32)state->position.x;
            packet.y = (s32)state->position.y;
            packet.z = (s32)state->position.z;
            packet.fractionX = (s32)(state->position.x * 256.0f);
            packet.fractionY = (s32)(state->position.y * 256.0f);
            packet.fractionZ = (s32)(state->position.z * 256.0f);
            inverseHalf = 1.0f / (f32)(s16)(peak >> 1);
            /* The basis components are dead; reuse them for velocity. */
            componentX = (targetX - state->position.x) * inverseHalf;
            componentY = (targetY - state->position.y) * inverseHalf;
            componentZ = (targetZ - state->position.z) * inverseHalf;
            curve[7] = (s32)componentX;
            curve[8] = (s32)componentY;
            curve[9] = (s32)componentZ;
            curve[10] = (u8)(s32)(componentX * 256.0f);
            curve[11] = (u8)(s32)(componentY * 256.0f);
            curve[12] = (u8)(s32)(componentZ * 256.0f);
            created = func_15167D84(&packet, 0, 34, -1,
                                  *((u8 *)record + 12), *((u8 *)record + 1));
            if (created != NULL) memcpy(created + 0x50, curve, 34);
            state->phase = state->phase - 1.0f;
        } while (state->phase > 1.0f);
    }
}



typedef struct {
    u8 pad00[0x20];
    s16 x, y, z;
    u8 pad26[6];
    u8 fractionX, fractionZ, fractionY;
    u8 pad2F[5];
    s16 sizeX, sizeY, age;
    u8 pad3A[5];
    u8 intensity;
    u8 pad40[0x10];
    s16 curve[17];
} EffectCurve1CC440;

/* Apply the age-dependent intensity, size, and fixed-point motion curves. */
void func_151A175C(EffectCurve1CC440 *effect) {
    s16 *curve = effect->curve;
    s32 age = effect->age;
    s32 value, velocity;
    if (curve[2] < age) {
        effect->intensity = curve[0] * (curve[1] - age);
    }
    if (curve[5] < age) {
        value = curve[3] * (curve[4] - age);
        effect->sizeY = value;
        effect->sizeX = value;
    }
    if (curve[6] < age) {
        velocity = (s32)(((u32)(s32)curve[7] << 8) | (u32)(s32)curve[10]);
        value = (s32)(((u32)(s32)effect->x << 8) | effect->fractionX);
        value = (s32)((u32)value + (u32)velocity * (u32)D_800BE9E4);
        effect->x = value >> 8;
        effect->fractionX = value;
        velocity = (s32)(((u32)(s32)curve[8] << 8) | (u32)(s32)curve[11]);
        value = (s32)(((u32)(s32)effect->y << 8) | effect->fractionY);
        value = (s32)((u32)value + (u32)velocity * (u32)D_800BE9E4);
        effect->y = value >> 8;
        effect->fractionY = value;
        velocity = (s32)(((u32)(s32)curve[9] << 8) | (u32)(s32)curve[12]);
        value = (s32)(((u32)(s32)effect->z << 8) | effect->fractionZ);
        value = (s32)((u32)value + (u32)velocity * (u32)D_800BE9E4);
        effect->z = value >> 8;
        effect->fractionZ = value;
        age = effect->age;
    }
    if (age < curve[13]) effect->intensity = curve[14] * age;
    if (age < curve[15]) {
        value = curve[16] * age;
        effect->sizeY = value;
        effect->sizeX = value;
    }
}



struct260 *func_151491F4(s16, s8, s8, u8, u8, s32, u8, s32);
void *memcpy(void *, const void *, u32);

/* Spawn an effect from the record's captured 32-byte parameter packet. */
void func_151A18DC(struct260 *record) {
    struct260 *effect;
    RecordEffectPacket1CC440 packet;

    packet.position = *(EffectPacketPosition1CC440 *)((u8 *)record + 0x28);
    packet.sourceValueA = *(f32 *)((u8 *)record + 0x34);
    packet.phase = 0.0f;
    packet.sourceValueB = *(f32 *)((u8 *)record + 0x38);
    packet.parameters[0] = *(s16 *)((u8 *)record + 0x3E);
    packet.parameters[1] = *(s16 *)((u8 *)record + 0x40);
    packet.parameters[2] = *(s16 *)((u8 *)record + 0x42);
    packet.parameters[3] = *(s16 *)((u8 *)record + 0x44);
    effect = func_151491F4(*(s16 *)((u8 *)record + 0x3C), -1, 3, 1, 0,
                          sizeof(packet), ((u8 *)record)[0xC], ((u8 *)record)[1]);
    if (effect != NULL) {
        memcpy((u8 *)effect + 0x28, &packet, sizeof(packet));
    }
}

/* Emit randomized particles with a ten-short intensity and size curve. */
void func_151A1998(struct260 *record) {
    RecordEffectPacket1CC440 *state = (RecordEffectPacket1CC440 *)((u8 *)record + 0x28);
    EmissionPacket151A11E4 packet;
    s16 curve[10];
    union { s32 integer; u8 *pointer; } scratch;
    s32 secondAngle;
    f32 componentX, componentY, componentZ, polarSine;
    f32 targetX, targetZ, targetY;
    s16 peak, half, quarter;

    state->phase = state->phase + state->sourceValueB * D_800BE9A4;
    if (state->phase > 1.0f) {
        packet.red = 255;
        packet.green = 255;
        packet.blue = 255;
        packet.zero30 = 0;
        packet.zero31 = 0;
        packet.zero32 = 0;
        packet.fractionScale = 17;
        packet.curveFlags = 0x120;
        packet.flags = 0xC0001;
        packet.zero0C = 0;
        packet.descriptor = D_80090D34;
        packet.zero16 = 0;
        packet.zero20 = 0;
        packet.zero18 = 0;
        packet.zero22 = 0;
        packet.zero2A = 0;
        packet.alpha = 0;
        packet.sizeX = 2000;
        packet.sizeY = 2000;
        do {
            scratch.integer = func_150ADA20() & 255;
            secondAngle = func_150ADA20() & 255;
            componentX = func_151423D8((u8)(scratch.integer - 64));
            componentY = func_151423D8((u8)scratch.integer);
            componentZ = func_151423D8((u8)(secondAngle - 64));
            polarSine = func_151423D8((u8)secondAngle);
            targetY = func_150ADA68() * state->sourceValueA;
            polarSine = targetY * polarSine;
            targetX = state->position.x + polarSine * componentX;
            targetY = state->position.y - targetY * componentZ;
            targetZ = state->position.z + polarSine * componentY;

            if (func_150ADA20() & 1) packet.curveFlags |= 4;
            if (func_150ADA20() & 1) packet.curveFlags |= 8;
            scratch.integer = func_150ADA20();
            packet.lifetime = (u32)scratch.integer % (u32)(state->parameters[1] + 1) + state->parameters[0];
            scratch.integer = func_150ADA20();
            secondAngle = (s16)((u32)scratch.integer % (u32)(state->parameters[3] + 1) + state->parameters[2]);
            packet.age = D_80090B60[0x1D8] * (256 / packet.lifetime);
            peak = packet.age;
            half = peak >> 1;
            quarter = (s16)(peak >> 2);
            curve[5] = half;
            curve[0] = 255 / (peak - (s16)(peak - quarter));
            curve[1] = peak;
            curve[2] = peak - quarter;
            curve[3] = secondAngle / (peak - half);
            curve[4] = peak;
            curve[6] = quarter;
            curve[7] = 255 / (s16)quarter;
            curve[8] = half;
            curve[9] = secondAngle / (s16)half;

            packet.x = (s32)targetX;
            packet.y = (s32)targetY;
            packet.z = (s32)targetZ;
            packet.fractionX = (s32)(targetX * 256.0f);
            packet.fractionY = (s32)(targetY * 256.0f);
            packet.fractionZ = (s32)(targetZ * 256.0f);
            scratch.pointer = func_15167D84(&packet, 0, 20, -1,
                                  *((u8 *)record + 12), *((u8 *)record + 1));
            if (scratch.pointer != NULL) memcpy(scratch.pointer + 0x50, curve, 20);
            state->phase = state->phase - 1.0f;
        } while (state->phase > 1.0f);
    }
}

/* Later matching lifetime ramps intentionally override earlier ramps. */
void func_151A1E34(u8 *effect) {
    s16 *parameters = (s16 *)(effect + 0x50);
    s32 time = *(s16 *)(effect + 0x38);

    if (parameters[2] < time) {
        effect[0x3F] = parameters[0] * (parameters[1] - time);
    }
    if (parameters[5] < time) {
        *(s16 *)(effect + 0x34) = *(s16 *)(effect + 0x36) = parameters[3] * (parameters[4] - time);
    }
    if (time < parameters[6]) {
        effect[0x3F] = parameters[7] * time;
    }
    if (time < parameters[8]) {
        *(s16 *)(effect + 0x34) = *(s16 *)(effect + 0x36) = parameters[9] * time;
    }
}

typedef struct {
    EffectPacketPosition1CC440 position;
    f32 sourceValueA;
    f32 phase;
    f32 sourceValueB;
    s16 parameters[6];
} RecordEffectPacketSix1CC440;

/* Spawn an effect from the record's captured 36-byte parameter packet. */
void func_151A1EE8(struct260 *record) {
    struct260 *effect;
    RecordEffectPacketSix1CC440 packet;
    u8 *bytes = (u8 *)record;

    packet.position = *(EffectPacketPosition1CC440 *)(bytes + 0x28);
    packet.sourceValueA = *(f32 *)(bytes + 0x34);
    packet.phase = 0.0f;
    packet.sourceValueB = *(f32 *)(bytes + 0x38);
    packet.parameters[0] = *(s16 *)(bytes + 0x3E);
    packet.parameters[1] = *(s16 *)(bytes + 0x40);
    packet.parameters[2] = *(s16 *)(bytes + 0x42);
    packet.parameters[3] = *(s16 *)(bytes + 0x44);
    packet.parameters[4] = *(s16 *)(bytes + 0x46);
    packet.parameters[5] = *(s16 *)(bytes + 0x48);
    effect = func_151491F4(*(s16 *)(bytes + 0x3C), -1, 4, 1, 0,
                          sizeof(packet), bytes[0xC], bytes[1]);
    if (effect != NULL) {
        memcpy((u8 *)effect + 0x28, &packet, sizeof(packet));
    }
}

s32 func_151A1FB4() {
    return 0;
}

/* Apply ordered lifetime ramps, a colour-mode transition and a one-shot switch. */
void func_151A24A8(u8 *effect) {
    s16 *parameters = (s16 *)(effect + 0x50);
    s32 time = *(s16 *)(effect + 0x38);

    if (parameters[2] < time) {
        effect[0x3F] = parameters[0] * (parameters[1] - time);
    }
    if (parameters[5] < time) {
        *(s16 *)(effect + 0x34) = *(s16 *)(effect + 0x36) = parameters[3] * (parameters[4] - time);
    }
    if (time < parameters[8]) {
        effect[0x3F] = parameters[9] * time;
    }
    if (time < parameters[10]) {
        u32 increment = parameters[11] * (u32)D_800BE9E4;

        *(s16 *)(effect + 0x34) += increment;
        *(s16 *)(effect + 0x36) += increment;
        time = *(s16 *)(effect + 0x38);
    }
    if (time < parameters[6]) {
        s32 colour;

        effect[0x2F] = 0x13;
        *(u16 *)(effect + 0x44) |= 0x101;
        colour = parameters[7] * time;
        *(u32 *)(effect + 0x14) = 0x00520003;
        effect[0x40] = effect[0x41] = effect[0x42] = colour;
    }
    if (time < parameters[12]) {
        *(s16 *)(effect + 0x32) = parameters[13];
        parameters[12] = -9999;
    }
}

/* Apply lifetime ramps in order, with live size growth and a one-shot switch. */
void func_151A25E0(u8 *effect) {
    s16 *parameters = (s16 *)(effect + 0x50);
    s32 time = *(s16 *)(effect + 0x38);

    if (parameters[2] < time) {
        effect[0x3F] = parameters[0] * (parameters[1] - time);
    }
    if (parameters[5] < time) {
        *(s16 *)(effect + 0x34) = *(s16 *)(effect + 0x36) = parameters[3] * (parameters[4] - time);
    }
    if (time < parameters[8]) {
        effect[0x3F] = parameters[9] * time;
    }
    if (time < parameters[10]) {
        u32 increment = parameters[11] * (u32)D_800BE9E4;

        *(s16 *)(effect + 0x34) += increment;
        *(s16 *)(effect + 0x36) += increment;
        time = *(s16 *)(effect + 0x38);
    }
    if (time < parameters[12]) {
        *(s16 *)(effect + 0x32) = parameters[13];
        parameters[12] = -9999;
        time = *(s16 *)(effect + 0x38);
    }
    effect[0x40] = effect[0x41] = effect[0x42] = parameters[7] * time;
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1CC440/func_151A26EC.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1CC440/func_151A2960.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1CC440/func_151A2A14.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1CC440/func_151A2AD4.s")

void func_151A2B84(f32 *arg0, s32 arg1, s32 arg2, s32 arg3, f32 arg4, f32 *arg5) {
    f32 t = 1.0f - arg4;

    arg5[0] = arg0[0] * t;
    arg5[1] = arg0[1] * t;
    arg5[2] = arg0[2] * t;
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1CC440/func_151A2BD0.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1CC440/func_151A2C24.s")

s32 func_151A2F0C() {
    return 0;
}

s32 func_151A3150() {
    return 0;
}
