#include <ultra64.h>

u8 *func_15167A68(s32,s32,s32,s32,s32,s32);

#include "structs.h"
void *memcpy(void *, const void *, u32);
typedef struct {
    u8 kind;
    u8 reserved01[3];
    u8 *owner;
    f32 primary;
    f32 secondary;
    f32 zero[5];
    u8 enabled;
    s8 mode;
    u8 flags;
} ParitySpawnRequest;
extern f32 D_800A8F58, D_800A8F5C, D_800A8F60, D_800A8F64;
/* Shared allocator: descriptor, lifetime, extra payload bytes, channel and context. */
u8 *func_151A8B20(void *, s16, s32, u8, s32);
void func_1516972C(struct102 *);

/* Non-matching placeholders for the text-only asm slice asm/1D4E00.s. */

void func_151A931C(u8 *, s32, u8);
void func_15169804(u8 *);
void func_15169824(u8 *);

s32 func_151D5E30();
void func_151432BC(void *, f32 *, f32 *, f32 *, f32 *);

extern s32 (*D_8008F94C[])();
extern s32 (*D_8008F958[])();
extern void (*D_8008F964[])(u8 *, s32, u8);
extern void (*D_8008F984[])(u8 *, s32);

/* Allocate a record, copy its descriptor, and initialize endpoint vectors. */
s32 func_151A7950(u8 *source, s32 bytes, u8 mode, s32 parameter) {
    u8 *record;
    record = func_15167A68(0x2D, parameter, (s32)((u32)bytes + (u32)*(s16 *)(source + 2) * 24u + 0x80u), 1, mode, 1);
    if (record == NULL) return 0;
    memcpy(record + 0x10, source, 0x50);
    *(u8 **)(record + 0x64) = record + 0x80;
    *(u8 **)(record + 0x60) = *(u8 **)(record + 0x64) + (s32)*(s16 *)(source + 2) * 24;
    *(f32 *)(record + 0x68) = 0.0f;
    *(f32 *)(*(u8 **)(record + 0x64) + 0) = 0.0f;
    *(f32 *)(*(u8 **)(record + 0x64) + 4) = 0.0f;
    *(f32 *)(*(u8 **)(record + 0x64) + 8) = 0.0f;
    *(f32 *)(*(u8 **)(record + 0x64) + (s32)*(s16 *)(source + 2) * 24 - 24) = 0.0f;
    *(f32 *)(*(u8 **)(record + 0x64) + (s32)*(s16 *)(source + 2) * 24 - 20) = 0.0f;
    *(f32 *)(*(u8 **)(record + 0x64) + (s32)*(s16 *)(source + 2) * 24 - 16) = 1.0f;
    bzero(record + 0x6C, 0x10);
    *(s32 *)(record + 0x7C) = (s32)(((u32)*(s16 *)(record + 0x12) << 6) + 0x140u);
    return (s32)record;
}

typedef struct {f32 x,y,z,outX,outY,outZ;} DirectionVertex151A7A90;
typedef struct {
    u8 pad00[16];
    s16 lifetime, count;
    f32 minimum, range;
    u8 flags, pad1D[3];
    s32 context;
    u8 pad24[8];
    s8 firstCallback, secondCallback;
    u8 pad2E[2];
    struct17 start, end, direction;
    f32 length, reciprocal;
    u8 kind, pad5D[3];
    void *cache;
    DirectionVertex151A7A90 *vertices;
    f32 timer;
} DirectionState151A7A90;
extern s32 (*D_8008F940[])(u8 *);
extern s32 (*D_8008F948[])(u8 *);
extern s32 D_800BE9E4;
extern f32 D_800BE9A4;
s32 func_151A8340();
f32 func_150ADA68(void);
void func_151450B4(struct17 *,struct17 *,struct17 *);
/* Run lifecycle checks, refresh expired geometry and transform the vertex outputs. */
void func_151A7A90(struct102 *record) {
    DirectionState151A7A90 *state;
    u8 *loopOwner;
    u8 dead;
    struct17 cross, side, delta;
    state = (DirectionState151A7A90 *)record;
    /* Keep the original count owner live across the callbacks and vertex writes. */
    loopOwner = (u8 *)record;
    dead = 0;
    if (state->flags & 1) {
        state->lifetime = (s16)((u32)(s32)state->lifetime - (u32)D_800BE9E4);
        if (state->lifetime < 0) dead = 1;
    }
    if (state->firstCallback != -1 && !dead) dead = !D_8008F940[state->firstCallback]((u8 *)record);
    if (state->secondCallback != -1 && !dead) dead = !D_8008F948[state->secondCallback]((u8 *)record);
    if (!dead) {
        state->timer -= D_800BE9A4;
        if (state->timer < 0.0f) {
            func_151A8340((u8 *)record, 0, (s16)(state->count - 1), state->context, 100);
            /* Sequence the sample before re-reading helper-mutable interval fields. */
            state->timer = func_150ADA68();
            state->timer = state->timer * state->range + state->minimum;
        }
        if (state->flags & 2) {
            DirectionVertex151A7A90 *vertex;
            s32 index;
            delta.unk0 = state->end.unk0 - state->start.unk0;
            delta.unk4 = state->end.unk4 - state->start.unk4;
            delta.unk8 = state->end.unk8 - state->start.unk8;
            side = state->direction;
            func_151450B4(&delta, &side, &cross);
            cross.unk0 *= state->reciprocal;
            cross.unk4 *= state->reciprocal;
            cross.unk8 *= state->reciprocal;
            index = 0;
            vertex = state->vertices;
            if (state->count > 0) {
                do {
                    vertex->outX = state->start.unk0 + vertex->x * cross.unk0 + vertex->y * side.unk0 + vertex->z * delta.unk0;
                    vertex->outY = state->start.unk4 + vertex->x * cross.unk4 + vertex->y * side.unk4 + vertex->z * delta.unk4;
                    vertex->outZ = state->start.unk8 + vertex->x * cross.unk8 + vertex->y * side.unk8 + vertex->z * delta.unk8;
                    index++;
                    vertex++;
                } while (index < *(s16 *)(loopOwner + 0x12));
            }
        }
    }
    if (dead) func_1516972C((struct102 *)record);
}


s32 func_151A7D6C() {
    return 0;
}

s32 func_151A8340() {
    return 0;
}

void func_151A8560(u8 *arg0) {
    func_151D5E30(arg0 + 0x6C, arg0);
}

s32 func_151A8584(u8 *arg0) {
    if (D_8008F94C[arg0[0x5C]] != NULL) {
        D_8008F94C[arg0[0x5C]]();
    }
    func_151A8560(arg0);
    func_15169804(arg0);
}

s32 func_151A85D4(u8 *arg0) {
    if (D_8008F958[arg0[0x5C]] != NULL) {
        D_8008F958[arg0[0x5C]]();
    }
    func_151A8560(arg0);
    func_15169824(arg0);
}

s32 func_151A8624() {
    return 0;
}

typedef struct {
    u8 *target;
    u8 identity, pad05[3];
    f32 local[3];
    u8 matrixIndex, pad15[3];
    f32 offset[3];
    u8 pad24, flags;
} AttachedDirection151A87F8;
void func_15143134(f32 *, f32 *, u8 *);
s32 func_150AC9C0(f32, f32, f32, f32, f32, f32, s32, s32,
    f32 *, f32 *, f32 *, f32 *, s32 *, s32, f32);
u8 func_15145C90(s32);
f32 func_15143E64(f32 *);
s32 func_15146078(struct17 *, struct17 *, struct17 *);
/* Refresh an attached point and cache its collision-limited direction. */
s32 func_151A87F8(u8 *record) {
    AttachedDirection151A87F8 *cache;
    u8 *target, *matrices;
    struct17 delta, temporary;
    f32 dx, dy, dz;
    /* Keep both pointers across helper-visible changes to the owner and cache. */
    cache = *(AttachedDirection151A87F8 **)(record + 0x60);
    target = cache->target;
    if (*(s32 *)target == 0 || cache->identity != target[0x3B] || target[4] == 0xFF) return 0;
    matrices = *(u8 **)(target + 0x1D4);
    if (matrices != NULL) {
        func_15143134(cache->local, (f32 *)(record + 0x30), matrices + ((u32)cache->matrixIndex << 6));
        if (!(cache->flags & 1)) {
            s32 hit;
            dx = *(f32 *)(record + 0x30) - (cache->offset[0] + *(f32 *)(target + 0x14));
            dy = *(f32 *)(record + 0x34) - (cache->offset[1] + *(f32 *)(target + 0x18));
            dz = *(f32 *)(record + 0x38) - (cache->offset[2] + *(f32 *)(target + 0x1c));
            if (func_150AC9C0(*(f32 *)(record + 0x30), *(f32 *)(record + 0x34), *(f32 *)(record + 0x38),
                    dx,
                    dy,
                    dz,
                    0, 0, (f32 *)(record + 0x3C), (f32 *)(record + 0x40), (f32 *)(record + 0x44),
                    NULL, &hit, 0, 0.0f)) {
                if (func_15145C90(hit)) cache->flags |= 1;
                else {record[0x1C] &= ~2;return 1;}
            } else {record[0x1C] &= ~2;return 1;}
        }
        delta.unk0 = *(f32 *)(record + 0x3C) - *(f32 *)(record + 0x30);
        delta.unk4 = *(f32 *)(record + 0x40) - *(f32 *)(record + 0x34);
        delta.unk8 = *(f32 *)(record + 0x44) - *(f32 *)(record + 0x38);
        *(f32 *)(record + 0x54) = func_15143E64(&delta.unk0);
        if (*(f32 *)(record + 0x54) != 0.0f) {
            *(f32 *)(record + 0x58) = 1.0f / *(f32 *)(record + 0x54);
            func_15146078(&delta, &temporary, (struct17 *)(record + 0x48));
            record[0x1C] |= 2;
            return 1;
        }
        record[0x1C] &= ~2;
        return 1;
    } else record[0x1C] &= ~2;
    return 1;
}


void func_151A8A20(u8 *arg0, s32 arg1, u8 arg2) {
    s32 index = arg0[0x5C];
    void (*callback)(u8 *, s32, u8);

    if (index >= 3) {
        index = 0;
    }
    callback = D_8008F964[index];
    if (callback != NULL) {
        callback(arg0, arg1, arg2);
    }
}

/* Handle release notifications and switch the selected descriptor pair. */
void func_151A8A78(u8 *owner, s32 eventAddress, u8 command) {
    u8 *state = *(u8 **)(owner + 0x60);
    u8 *event = (u8 *)eventAddress;
    s32 value = command;

    if (command == 0) {
        value = *(s32 *)event;
        if (value == *(s32 *)state || event[4] == state[4]) {
            func_1516972C((struct102 *)owner);
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

typedef struct {
    ParitySpawnRequest request;
    f32 zero28, initial2C;
    u8 retained30[20];
    s32 zero44;
    u8 zero48, zero49, retained4A[2];
    s32 zero4C;
    s32 spatial;
    f32 scale;
} SpawnPayload151A8B20;
extern f32 D_800A8F50, D_800A8F54;
struct260 *func_15149130(s16,s8,s8,s8,u8,u8,struct37 *,u8,s32);
void func_1510F800(s32);
u8 *func_1510FD20(s32,s32);
f32 func_15144598(struct134 *);
/* Allocate an actor from a snapshotted request and initialize its spatial data. */
u8 *func_151A8B20(void *request, s16 lifetime, s32 extraBytes, u8 channel, s32 context) {
    u8 *created;
    SpawnPayload151A8B20 payload;
    f32 x, z;
    SpawnPayload151A8B20 *state;

    memcpy(&payload, request, 0x28);
    payload.zero44 = 0;
    payload.zero48 = 0;
    payload.zero49 = 0;
    payload.zero4C = 0;
    payload.zero28 = 0.0f;
    payload.initial2C = D_800A8F50;
    created = (u8 *)func_15149130(lifetime == -1 ? 300 : lifetime, -1, 0x25, -1,
        lifetime == -1 ? 0 : 1, 0x22, (struct37 *)(extraBytes + 0x58), channel, context);
    if (created != 0) {
        state = (SpawnPayload151A8B20 *)(created + 0x28);
        memcpy(state, &payload, 0x58);
        if (state->request.kind & 4) {
            if ((state->request.kind & 2) && state->request.owner != 0) {
                x = ((s16 *)state->request.owner)[0];
                z = ((s16 *)state->request.owner)[2];
            } else {
                x = state->request.zero[0];
                z = state->request.zero[2];
            }
            func_1510F800(0);
            state->spatial = (s32)func_1510FD20((s32)x, (s32)z);
        } else state->spatial = 0;
        if ((state->request.kind & 2) && state->request.owner != 0) {
            state->scale = func_15144598((struct134 *)state->request.owner);
        } else {
            state->scale = state->request.zero[4] * state->request.zero[4] * D_800A8F54;
        }
    }
    return created;
}


typedef struct HeightResult71820 { f32 height; s16 vertices[9]; s16 pad16; u32 metadata; u8 flags; u8 state; u16 pad1E; s32 value; } HeightResult71820;
typedef struct {
    ParitySpawnRequest request;
    f32 accumulator;
    HeightResult71820 ground;
    s16 *spatial;
    f32 scale;
} UpdatePayload151A8CEC;
extern s32 (*D_8008F980[])(u8 *);
extern void (*D_8008F970[])(u8 *, f32 *, f32, u8);
extern f32 D_800BE9A4;
u8 func_151464B8(s16 *);
s32 func_15046C80(f32 *, u16, f32, HeightResult71820 *);
f32 func_150ADA68(void);
void func_151A8F1C(u8 *, f32 *, f32 *, f32 *);
void func_151A8F6C(u8 *, f32 *, f32 *, f32 *);
/* Advance the effect accumulator, resolve emission positions and dispatch each tick. */
void func_151A8CEC(struct260 *owner) {
    UpdatePayload151A8CEC *state;
    /* Snapshot the helper result before reading mutable effect parameters. */
    f32 draw;
    f32 vector[3], out1, out0;
    /* Retail retains this byte until a forced-height or fallback path sets it. */
    u8 accepted;
    void (*position)(u8 *, f32 *, f32 *, f32 *);
    state = (UpdatePayload151A8CEC *)((u8 *)owner + 0x28);
    /* Keep the original separate signed selector reads. */
    if (*(volatile s8 *)((u8 *)owner + 0x4D) != -1 && !D_8008F980[*(volatile s8 *)((u8 *)owner + 0x4D)]((u8 *)owner)) {
        *(s16 *)((u8 *)owner + 0xE) = -1;
        return;
    }
    if ((state->request.kind & 4) && state->spatial != 0 && func_151464B8(state->spatial)) return;
    if (!(state->request.kind & 1)) return;
    draw = func_150ADA68();
    state->accumulator += (state->request.primary + draw * state->request.secondary) * D_800BE9A4 * state->scale;
    if (state->accumulator > 1.0f) {
        if ((state->request.kind & 2) && state->request.owner != 0) position = func_151A8F1C;
        else position = func_151A8F6C;
        do {
            position((u8 *)owner, vector, &out0, &out1);
            if (state->request.kind & 8) {
                vector[1] = out1;
                accepted = 1;
            } else if (func_15046C80(vector, 0, out1, &state->ground)) {
                vector[1] = state->ground.height;
            } else {
                vector[1] = out1;
                accepted = 1;
            }
            if ((s8)state->request.flags != -1) D_8008F970[(s8)state->request.flags]((u8 *)owner, vector, out0, accepted);
            state->accumulator -= 1.0f;
        } while (state->accumulator > 1.0f);
    }
}


void func_151A8F1C(u8 *arg0, f32 *arg1, f32 *arg2, f32 *arg3) {
    func_151432BC(*(void **) (arg0 + 0x2C), arg1, arg1 + 2, arg2, arg3);
    arg1[1] = arg2[0];
}

s32 func_150ADA20(void);
f32 func_150ADA68(void);
void func_15143874(s16, f32, f32 *, f32 *);

/* Build a random horizontal offset and return the owner height values. */
void func_151A8F6C(u8 *owner, f32 *vector, f32 *out0, f32 *out1) {
    f32 *state = (f32 *)(owner + 0x28);
    s32 code = func_150ADA20();
    func_15143874((s16)(code & 0xFF), state[8] * func_150ADA68(), vector, vector + 2);
    vector[0] += state[4];
    vector[2] += state[6];
    vector[1] = state[5];
    *out0 = state[5];
    *out1 = state[7];
}

void func_151A9024(u8 *arg0, s32 arg1, u8 arg2) {
    if (*(arg0 + 0x4C) == 1) {
        func_151A931C(arg0, arg1, arg2);
    }
}

s32 func_151A9060(u8 *arg0) {
    s32 index;
    void (*callback)(u8 *, s32);

    arg0[0x16] |= 4;
    index = *(s32 *)(arg0 + 0x18);
    if (index < 0 || index >= 8) {
        return 1;
    }
    callback = D_8008F984[index];
    if (callback != NULL) {
        callback(arg0, index);
    }
    return 1;
}

/* Create a parity-selected descriptor and attach the selector's low byte. */
void func_151A90C0(u8 *owner, s32 selector) {
    ParitySpawnRequest request;
    f32 parity = selector & 1;
    u8 tag[1];
    u8 *created;
    request.kind = 2;
    request.owner = owner;
    request.primary = parity ? D_800A8F58 : D_800A8F5C;
    request.secondary = parity ? D_800A8F60 : D_800A8F64;
    request.zero[0] = 0.0f;
    request.zero[1] = 0.0f;
    request.zero[2] = 0.0f;
    request.zero[3] = 0.0f;
    request.zero[4] = 0.0f;
    request.enabled = 1;
    request.mode = -1;
    request.flags = 0;
    tag[0] = selector;
    created = func_151A8B20(&request, -1, 1, 0xFF, 0);
    if (created != NULL) {
        memcpy(created + 0x80, tag, 1);
    }
}

typedef struct { s16 value[3]; } RandomChoice151A91AC;
typedef struct {
    u32 flags;
    s16 lifetime;
    u8 slot, kind;
    s32 zero8, zeroC;
    u8 random, value11, value12, value13, value14, value15, zero16, seven;
    s32 effect, sourceWord;
    u8 value20, pad21;
    s16 size, count;
} RandomEmitter151A91AC;
extern RandomChoice151A91AC D_8008F9A4;
f32 func_150ADA68(void);

struct210 *func_1513C650(s32, u8, u8, s32, f32, f32, f32, f32, f32, u8, u8, s32, s32, s32, u8, s32);
/* Submit a randomized emitter using the owner's position and attachment. */
void func_151A91AC(u8 *owner, f32 *position, s32 unused2, s32 unused3) {
    u32 third;
    RandomEmitter151A91AC descriptor;
    f32 range;
    RandomChoice151A91AC choices;
    u32 second, first;
    /* Preserve the unused retail stack slot after the local choice table. */
    u32 retained;
    choices = D_8008F9A4;
    range = func_150ADA68() * 50.0f + 50.0f;
    descriptor.slot = choices.value[(u32)func_150ADA20() % 3U];
    descriptor.kind = 0;
    descriptor.zero16 = 0;
    descriptor.seven = 7;
    descriptor.zero8 = 0;
    descriptor.zeroC = 0;
    descriptor.flags = 0x1701;
    descriptor.lifetime = 60;
    descriptor.random = 160;
    descriptor.value11 = 255;
    descriptor.value12 = 0;
    descriptor.value13 = 0;
    descriptor.value14 = 0;
    descriptor.value15 = 255;
    descriptor.effect = 0x3B0002;
    first = func_150ADA20();
    second = func_150ADA20();
    /* Finish the random calls before reading the position and owner bytes. */
    third = func_150ADA20();
    func_1513C650((s32)&descriptor, 1, 0, (s32)(owner + 0x58),
        position[0], position[1], position[2], range, range, first & 255,
        (third & 1) + (second & 1), 3, 255, 0, owner[0xC], owner[1]);
}

void func_151A931C(u8 *arg0, s32 arg1, u8 arg2) {
    u8 *flags;

    if (arg2 == 0x17) {
        flags = arg0 + 0x28;
        if (*(u8 *)arg1 == arg0[0x80]) {
            *flags |= 1;
        }
    } else if (arg2 == 0x18) {
        flags = arg0 + 0x28;
        if (*(u8 *)arg1 == arg0[0x80]) {
            *flags &= ~1;
        }
    }
}

typedef struct { f32 x, y, z; } TemplatePosition151A9390;
typedef struct {
    f32 primary, secondary;
    u8 arg2, arg3, arg4, headerKind, effectKind;
    u8 pad0D[3];
    void *payload;
} EffectTemplate151A9390;
typedef struct {
    u8 flags, pad01[3];
    s16 *owner;
    f32 primary, secondary;
    TemplatePosition151A9390 position;
    f32 parameter0, parameter1;
    u8 type;
    s8 mode;
    u8 enabled;
} TemplateRequest151A9390;
extern EffectTemplate151A9390 D_8008F9AC[];
struct225 *func_1516284C(Header *, s32, s32, s32, s32, u8, u8, s32, u8, u8, s32);
/* Select a template, create its actor payload, and optionally submit an effect. */
void func_151A9390(u8 flags, u8 selector, s16 *owner,
                  TemplatePosition151A9390 *position, f32 parameter0,
                  f32 parameter1, s16 lifetime, u8 channel, s32 context) {
    TemplateRequest151A9390 request;
    EffectTemplate151A9390 *table;
    s32 low;
    Header header;
    s32 coordinates[3];
    s32 ownerBits;
    s32 high;
    u8 *record;
    u8 *created;
    low = flags & 1;
    if (selector < 9) {
        low = low ? 4 : 0;
        ownerBits = owner ? 2 : 0;
        high = (flags & 2) ? 8 : 0;
        table = &D_8008F9AC[selector];
        request.flags = high | 1 | ownerBits | low;
        request.owner = owner;
        request.primary = table->primary;
        request.secondary = table->secondary;
        if (position != 0) request.position = *position;
        else { request.position.x = 0.0f; request.position.y = 0.0f; request.position.z = 0.0f; }
        request.parameter0 = parameter0;
        request.parameter1 = parameter1;
        request.type = 2;
        request.mode = -1;
        request.enabled = 1;
        created = func_151A8B20(&request, lifetime, 0x2C, channel, context);
        if (created != 0) {
            record = created + 0x80;
            memcpy(record, table->payload, 0x2C);
            if (flags & 8) record[0x28] |= 1;
            if (flags & 16) record[0x28] |= 2;
        }
        if (flags & 4) {
            high = lifetime == -1 ? 0 : 1;
            header.unk0 = high | 2;
            header.unk1 = 2;
            header.unk2 = lifetime == -1 ? 300 : lifetime;
            header.unk4 = table->headerKind;
            if (position != 0) {
                coordinates[0] = (s32)position->x;
                coordinates[1] = (s32)position->y;
                coordinates[2] = (s32)position->z;
            } else {
                coordinates[0] = owner[0];
                coordinates[1] = owner[1];
                coordinates[2] = owner[2];
            }
            func_1516284C(&header, (s32)coordinates, table->arg2, table->arg3,
                table->arg4, 255, 0, 0, table->effectKind, 255, 1);
        }
    }
}


typedef struct {
    f32 base0, base1, range0, range1;
    s16 countBase, countRange, lifetimeBase, lifetimeRange;
    s16 variantBase, variantRange, parameter0, parameter1;
    f32 extraBase, extraRange;
    u8 flags;
} RangedEffect151A9634;
typedef struct { f32 scale; s16 lifetime; u16 retained; } EffectExtra151A9634;
u8 *func_1514B8E4(f32 *, f32 *, s16, u8, void *, f32, f32, f32, u8, u8, u8, u8, u8, s16, s16, s32, u8, s32);
/* Create an effect from the owner's randomized ranges and copy its extra values. */
void func_151A9634(u8 *owner, f32 *position, s32 unused2, s32 unused3) {
    f32 ranges[2];
    s32 mode;
    EffectExtra151A9634 extra;
    RangedEffect151A9634 *parameters;
    s32 tag;
    s32 choice;
    s32 flags;
    u32 second, first;
    u8 *result;
    parameters = (RangedEffect151A9634 *)(owner + 0x80);
    ranges[0] = func_150ADA68() * parameters->range0 + parameters->base0;
    ranges[1] = func_150ADA68() * parameters->range1 + parameters->base1;
    extra.scale = func_150ADA68() * parameters->extraRange + parameters->extraBase;
    extra.lifetime = (u32)func_150ADA20() % (parameters->lifetimeRange + 1) + parameters->lifetimeBase;
    first = func_150ADA20();
    second = func_150ADA20();
    flags = parameters->flags;
    if (flags & 1) {
        tag = 0x71;
    } else {
        choice = (func_150ADA20() & 1) ? 0x13 : 0x14;
        tag = choice;
        flags = parameters->flags;
    }
    mode = (flags & 2) ? 0 : 2;
    result = func_1514B8E4(position, ranges,
        (s16)(first % (parameters->countRange + 1) + parameters->countBase),
        (u8)(second % (parameters->variantRange + 1) + parameters->variantBase),
        0, 0.0f, 1.0f, 1.0f, 0x21, 0x23, 2, tag, mode,
        parameters->parameter0, parameters->parameter1, 8, owner[0xC], owner[1]);
    if (result != 0) memcpy(result + 0x160, &extra, 8);
}


s32 func_151A9834() {
    return 0;
}
