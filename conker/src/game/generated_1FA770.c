#include <ultra64.h>
#include "structs.h"
void func_1516972C(struct102 *);
typedef struct { s32 a, b, c; } ThreeWord1FA770;

extern ThreeWord1FA770 D_800AAF9C[];
extern f32 D_800BE9A4;

/* Non-matching placeholders for the text-only asm slice asm/1FA770.s. */

s32 func_151D10E4(u8 *, void *, u8);
void func_151D13E0(u8 *);

typedef struct {
    void *source;
    s32 value;
    s32 zero;
    u8 selector;
    u8 reserved[3];
} EffectRecordPayload;
void *func_15149130(s16, s8, s8, s8, u8, u8, s32, u8, s32);
void *memcpy(void *, const void *, u32);

typedef struct {
    u8 *source;
    s32 identity;
    u8 *effect;
    u8 variant;
    u8 reservedD[3];
} EffectLinkRecord151CD3CC;
typedef struct {
    u8 reserved0;
    u8 sourceKind;
    u8 reserved2[10];
    u8 ownerMode;
    u8 reservedD[27];
    EffectLinkRecord151CD3CC link;
} EffectLinkOwner151CD3CC;
void *func_151CD4C0();
void func_151CE47C(u8 *);

/* Capture record state, attach the payload and return the allocated effect. */
void *func_151CD2C0(void *source, u8 variant, s32 parameter) {
    u8 *effect;
    EffectRecordPayload payload;
    payload.source = source;
    payload.value = *(s32 *)((u8 *)source + 0x18);
    payload.zero = 0;
    payload.selector = *(s32 *)((u8 *)source + 0x1C);
    effect = func_15149130(300, -1, -1, -1, 0, 30, 16, variant, parameter);
    if (effect != 0) {
        memcpy(effect + 0x28, &payload, 16);
    }
    return effect;
}

void func_151CD35C(s32 arg0) {
    s32 value;

    if ((arg0 >= 0) && (arg0 < 4)) {
        value = arg0;
        func_151494E0(&value, 0x17);
    }
}

void func_151CD394(s32 arg0) {
    s32 value;

    if ((arg0 >= 0) && (arg0 < 4)) {
        value = arg0;
        func_151494E0(&value, 0x18);
    }
}

/* Create, retire or detach the linked effect selected by an event command. */
void func_151CD3CC(EffectLinkOwner151CD3CC *owner, s32 *identity, u8 command) {
    EffectLinkRecord151CD3CC *link = &owner->link;

    if (command == 0x17) {
        if (link->identity == *identity && link->effect == 0) {
            link->effect = func_151CD4C0(
                link->source, link->variant, link->identity,
                owner->ownerMode, owner->sourceKind);
            link->source[0x14] = 0;
        }
    } else if (command == 0x18) {
        if (link->identity == *identity && link->effect != 0) {
            func_151CE47C(link->effect);
        }
    } else if (command == 0x23 && link->identity == *identity) {
        link->effect = 0;
        link->source[0x14] = 1;
    }
}

void *func_151CD4C0() {
    return 0;
}

extern f32 D_800AAFC0, D_800AAFC4;
typedef struct { f32 retained00, position, retained08, velocity; u8 retained10[12]; } MotionRingEntry151CD674;
typedef struct { u8 retained00[0x44]; f32 threshold; } MotionRingLimit151CD674;
typedef struct {
    u8 retained00[0x10]; ThreeWord1FA770 source; u8 retained1C[2]; u16 flags;
    u8 retained20[5]; u8 capacity; u8 retained26[6]; s8 count, current, end;
    u8 retained2F[0x25]; ThreeWord1FA770 output; u8 retained60[0x34];
    MotionRingEntry151CD674 *entries; MotionRingLimit151CD674 *limit;
} MotionRingOwner151CD674;

/* Integrate ring entries, retire those below the limit, and publish position. */
s32 func_151CD674(MotionRingOwner151CD674 *owner) {
    MotionRingEntry151CD674 *entries = owner->entries, *entry;
    MotionRingLimit151CD674 *limit = owner->limit;
    s32 index, current;
    f32 step, velocity, threshold;
    if (owner->count < 2 && (owner->flags & 8)) return 0;
    index = owner->end;
    current = owner->current;
    while (index != current) {
        index--;
        if (index < 0) index = owner->capacity - 1;
        entry = &entries[index];
        step = D_800BE9A4;
        velocity = entry->velocity;
        entry->position += velocity * step + D_800AAFC4 * (step * step);
        entry->velocity = velocity + D_800AAFC0 * D_800BE9A4;
        threshold = limit->threshold;
        if (entry->position < threshold) {
            while (index != current) {
                owner->current = current + 1;
                current = owner->current;
                if (current == owner->capacity) {
                    owner->current = 0;
                    current = owner->current;
                }
                owner->count = owner->count - 1;
            }
            entries[current].position = limit->threshold;
        }
        current = owner->current;
    }
    owner->output = owner->source;
    return 1;
}

s32 func_151CD7BC() {
    return 0;
}

s32 func_151CDB94() {
    return 0;
}

s32 func_151CDE20() {
    return 0;
}

void func_151CE47C(u8 *arg0) {
    *(u8 *)(arg0 + 0x30) = 0;
    *(u16 *)(arg0 + 0x1E) &= ~2;
    *(u16 *)(arg0 + 0x1E) |= 8;
}

void func_151CE49C(u8 *arg0) {
    s32 value;
    u8 *temp_v0 = *(u8 **) (arg0 + 0x98);

    value = *(s32 *) (temp_v0 + 0x48);
    func_151494E0(&value, 0x23);
    func_151478F4(arg0);
}

void func_151CE4DC(u8 *arg0) {
    s32 value;
    u8 *temp_v0 = *(u8 **) (arg0 + 0x98);

    value = *(s32 *) (temp_v0 + 0x48);
    func_151494E0(&value, 0x23);
    func_15147928(arg0);
}

typedef struct HeightEntry151CE51C { u8 prefix[4]; f32 height; u8 rest[20]; } HeightEntry151CE51C;
typedef struct HeightOwner151CE51C {
    u8 prefix[0x1E]; u16 flags; u8 pad20[5]; u8 count25; u8 pad26[6];
    s8 count, current, previous; u8 pad2F[0x65]; HeightEntry151CE51C *entries;
} HeightOwner151CE51C;
void *func_151CE634(void *);
void func_1515C1A0(struct127 *, struct17 *, f32 *, f32 *);
s32 func_1505D024(struct127 *, s32, u16, s32);
/* Dispatch the event when the actor reaches the selected height boundary. */
void func_151CE51C(struct127 *actor, u8 *event) {
    struct17 position;
    f32 radius;
    f32 height;
    HeightOwner151CE51C *owner;
    s32 index;
    HeightEntry151CE51C *entries;
    f32 boundary;
    f32 limit;
    f32 centerY;
    f32 extent;
    s32 command;
    owner = func_151CE634(*(void **)(event + 0x18));
    if (owner != NULL) {
        func_1515C1A0(actor, &position, &radius, &height);
        if (owner->flags & 8) {
            if (owner->count > 0) {
                index = owner->previous - 1;
                if (index < 0) index = owner->count25 - 1;
                centerY = position.unk4;
                extent = height;
                boundary = centerY - extent;
                entries = owner->entries;
                limit = entries[index].height;
                command = 0x60019;
                if (boundary <= limit) {
                    func_1505D024(actor, command, 0, -1);
                }
            }
        } else {
            if (owner->count > 0) {
                centerY = position.unk4;
                extent = height;
                boundary = centerY + extent;
                entries = owner->entries;
                limit = entries[owner->current].height;
                command = 0x60019;
                if (limit <= boundary) {
                    func_1505D024(actor, command, 0, -1);
                }
            }
        }
    }
}


extern u8 D_800DCE50[0x340];
extern s8 D_800DD190;
extern s32 D_800A5760[2];

/* Find the first type-11 node whose associated payload names this context. */
void *func_151CE634(void *context) {
    u8 phase;
    u8 *row;
    void **column;
    void *node;

    for (phase = 0; phase < 2; phase++) {
        row = D_800DCE50;
        column = (void **)(row + D_800A5760[phase] * 4);
        do {
            node = *column;
            while (node != 0) {
                if (*(s32 *)((u8 *)node + 0x20) == 11 &&
                    *(void **)((u8 *)*(void **)((u8 *)node + 0x98) + 0x48) == context) {
                    return node;
                }
                node = *(void **)((u8 *)node + 8);
            }
            row += 0x1A0;
            column = (void **)((u32)column + 0x1A0);
        } while (row != (u8 *)&D_800DD190);
    }
    return 0;
}

s32 func_151CE6D0() {
    return 0;
}

s32 func_151CEA20(f32 *arg0) {
    f32 acceleration = arg0[0x40 / 4];
    f32 velocity = arg0[0x44 / 4];

    arg0[0x44 / 4] = velocity + acceleration * D_800BE9A4;
    arg0[0x38 / 4] += (velocity + acceleration * 0.5f * D_800BE9A4) * D_800BE9A4;
    arg0[0x50 / 4] += arg0[0x4C / 4] * D_800BE9A4;
    if (arg0[0x50 / 4] > 1.0f) {
        arg0[0x50 / 4] = 1.0f;
    }
    return 1;
}

typedef struct {
    u8 *owner; u8 identity; u8 pad05[3]; u8 *attachment;
    f32 first, second, third, fourth; u8 flags; u8 pad1D[3]; f32 extent, velocity;
} LinkedEffectPayload151CEAAC;
/* The helper copies 28 bytes, including the untouched request tail. */
typedef struct {
    f32 position[3]; s16 lifetime, mode; s32 active; u8 kind, count; u8 untouched16[2]; u8 untouched18[4];
} LinkedEffectRequest151CEAAC;
extern f32 D_800AB008;
f32 func_150ADA68(void);
s32 func_151CEC10(f32 *, u8 *, u8 *);
u8 *func_15147A80(void *, s32, s32, s32, s32, s32, s32, s32, void *, u8, s32);
/* Construct a linked effect and copy its captured payload on success. */
u8 *func_151CEAAC(u8 *owner, u8 *attachment, u8 mode, u8 channel, s32 context) {
    LinkedEffectRequest151CEAAC request;
    LinkedEffectPayload151CEAAC payload;
    u8 *effect;
    s32 effectFlags;
    request.count = 25;
    request.lifetime = 300;
    request.mode = 16;
    request.active = 17;
    request.kind = 3;
    payload.owner = owner;
    if (owner != NULL) payload.identity = owner[0x3b];
    else payload.identity = 0;
    payload.second = 1.0f;
    payload.fourth = 1.0f;
    payload.attachment = attachment;
    payload.first = 0.0f;
    payload.third = 0.0f;
    if (mode) effectFlags = 2; else effectFlags = 0;
    payload.flags = effectFlags;
    payload.extent = func_150ADA68() * 400.0f + 400.0f;
    payload.velocity = (func_150ADA68() * 2.0f) * D_800AB008;
    if (func_151CEC10(request.position, owner, attachment) == 0) {
        request.position[0] = 0.0f;
        request.position[1] = 0.0f;
        request.position[2] = 0.0f;
    }
    effect = func_15147A80(&request, 0x28, 0x28, 0, 15, 15, 0, 0, NULL, channel, context);
    if (effect != NULL) memcpy(*(void **)(effect + 0x98), &payload, 0x28);
    return effect;
}



s32 func_151CEC10(f32 *arg0, u8 *arg1, u8 *arg2) {
    if (arg2 != 0) {
        *(ThreeWord1FA770 *) arg0 = *(ThreeWord1FA770 *) (arg2 + 0x40);
    } else {
        arg0[0] = *(f32 *) (arg1 + 0x14);
        arg0[1] = *(f32 *) (arg1 + 0x18);
        arg0[2] = *(f32 *) (arg1 + 0x1C);
    }
    return 1;
}

s32 func_151CEC54() {
    return 0;
}

s32 func_151CF120() {
    return 0;
}

s32 func_151CF380() {
    return 0;
}

void func_151CF844(u8 *arg0, s32 arg1, u8 arg2) {
    u8 *target = *(u8 **) (arg0 + 0x98);

    if (*(s32 *) target != 0) {
        func_15169850(arg1, arg2, (s32) target, (s32) (target + 4), (s32) arg0);
    }
}

s32 func_151CF898() {
    return 0;
}

s32 func_151CFA4C() {
    return 0;
}

s32 func_151D0024(u8 *arg0) {
    struct { u8 *ptr; u8 value; } temp;

    temp.ptr = arg0;
    temp.value = *(u8 *)(arg0 + 0x3B);
    func_151494E0(&temp, 0x18);
}

typedef struct {
    u8 *owner;
    u8 ownerId;
    u8 reserved0;
    u16 flags;
    f32 midpoint;
    u8 randomByte;
    u8 variant;
    u8 reserved1[2];
} OwnerRandomPacket;
s32 func_150ADA20(void);
void *func_15149130(s16, s8, s8, s8, u8, u8, s32, u8, s32);
void *memcpy(void *, const void *, u32);
/* Capture owner state and submit a randomized sixteen-byte effect packet. */
void func_151D0058(void *owner, u8 variant, u8 priority, s32 context) {
    u8 *effect;
    OwnerRandomPacket packet;

    packet.owner = owner;
    packet.ownerId = ((u8 *)owner)[0x3B];
    packet.midpoint = (*(f32 *)((u8 *)owner + 0x150) + *(f32 *)((u8 *)owner + 0x14C)) * 0.5f;
    packet.variant = variant;
    packet.randomByte = (u32)func_150ADA20() % 56U + 200;
    packet.flags = *(u16 *)((u8 *)owner + 0x84);
    effect = func_15149130(300, -1, 0x61, 4, 0, 0x31, sizeof(packet), priority, context);
    if (effect != NULL) {
        memcpy(effect + 0x28, &packet, sizeof(packet));
    }
}

void func_151D0128(u8 *arg0) {
    u8 *temp_v0 = *(u8 **)(arg0 + 0x28);

    if (*(u16 *)(temp_v0 + 0x84) != *(u16 *)(arg0 + 0x2E)) {
        *(s16 *)(arg0 + 0xE) = -1;
    }
}

s32 func_151D014C() {
    return 0;
}

/* Release the owner or retarget its embedded source/identity pair. */
void func_151D08F0(struct260 *record, s32 eventAddress, u8 command) {
    u8 *owner = (u8 *)record;
    u8 *event = (u8 *)eventAddress;
    u8 *state = owner + 0x28;
    s32 value = command;
    if (command == 0 || value == 0x18) {
        value = *(s32 *)event;
        if (value == *(s32 *)state || state[4] == event[4]) {
            func_1516972C((struct102 *)owner);
        }
    } else if (value == 0x2D) {
        s32 current = *(s32 *)state;
        value = *(s32 *)event;
        if (value == current) {
            *(s32 *)state = *(s32 *)(event + 4);
            state[4] = event[9];
        } else if (*(s32 *)(event + 4) == current) {
            *(s32 *)state = value;
            state[4] = event[8];
        }
    }
}

s32 func_151D09A8() {
    return 0;
}

s32 func_151D0ED8(u8 *arg0) {
    u8 *temp_a1 = arg0;

    if (*(s32 volatile *)(temp_a1 + 0xA8) != 0) {
        func_1516972C((struct102 *)*(s32 volatile *)(temp_a1 + 0xA8));
    }
}

s32 func_151D0F08(s32 arg0) {
    func_151D0ED8(arg0);
    func_1513173C(arg0);
}

s32 func_151D0F34(s32 arg0) {
    func_151D0ED8(arg0);
    func_1513175C(arg0);
}

typedef struct { f32 x, y, z; } PositionVector151D0F60;
typedef struct {
    u8 *owner;
    u8 ownerId;
    s32 zero08;
    PositionVector151D0F60 first, second, third;
    f32 zero30;
    u8 selector;
} PositionPayload151D0F60;
extern s32 (*D_8008FC30[])(u8 *, PositionVector151D0F60 *);
extern PositionVector151D0F60 D_800A5480;

/* Capture the position callback result and attach its duplicated payload. */
void func_151D0F60(u8 *owner, u8 selector, u8 priority, s32 context) {
    u8 *created;
    PositionPayload151D0F60 payload;
    payload.owner = owner;
    payload.ownerId = owner[0x3B];
    payload.zero08 = 0;
    if (!D_8008FC30[selector](owner, &payload.second)) {
        payload.second = D_800A5480;
    }
    payload.first = payload.second;
    payload.third = D_800A5480;
    payload.zero30 = 0.0f;
    payload.selector = selector;
    created = func_15149130(300, -1, 95, -1, 0, 72, 56, priority, context);
    if (created != NULL) {
        memcpy(created + 0x28, &payload, 56);
    }
}

s32 func_151D1074(u8 *owner, PositionVector151D0F60 *output) {
    output->x = *(f32 *)(owner + 0x14);
    output->y = *(f32 *)(owner + 0x180) + 8.0f;
    output->z = *(f32 *)(owner + 0x1C);
    return 1;
}

/* Preserve the transform status returned through the position callback. */
s32 func_151D10A4(u8 *owner, PositionVector151D0F60 *output) {
    return func_151D10E4(owner, output, 0);
}

/* Query the second transform row through the same callback ABI. */
s32 func_151D10C4(u8 *owner, PositionVector151D0F60 *output) {
    return func_151D10E4(owner, output, 1);
}

s32 func_151D10E4(u8 *owner, void *output, u8 mode) {
    void *target;

    target = *(void **)(owner + 0x1D4);
    if (target == NULL) {
        return 0;
    }
    func_15143134(&D_800AAF9C[mode], output, target);
    return 1;
}

s32 func_151D1138() {
    return 0;
}

void func_151D1328(u8 *arg0, s32 arg1, u8 arg2) {
    func_15169850(arg1, arg2, (s32) (arg0 + 0x28), (s32) (arg0 + 0x2C), (s32) arg0);
}

void func_151D1368(u8 *arg0) {
    func_151D13E0(arg0);
}

s32 func_151D1388(s32 arg0) {
    func_151D1368(arg0);
    func_1514933C(arg0);
}

s32 func_151D13B4(s32 arg0) {
    func_151D1368(arg0);
    func_15149368(arg0);
}

void func_151D13E0(u8 *arg0) {
    u8 *owner = arg0 + 0x28;
    u8 *linked;

    if (*(u8 **)(owner + 8) != NULL) {
        linked = *(u8 **)(*(u8 **)(owner + 8) + 0x98);
        *(u8 *)(*(u8 **)(owner + 8) + 0x30) = 0;
        *(u16 *)(*(u8 **)(owner + 8) + 0x1E) &= ~2;
        *(u16 *)(*(u8 **)(owner + 8) + 0x1E) |= 8;
        *(u16 *)(*(u8 **)(owner + 8) + 0x1E) |= 1;
        *(u16 *)(*(u8 **)(owner + 8) + 0x1C) = 0x28;
        *(s32 *)linked = 0;
        *(u8 **)(owner + 8) = NULL;
    }
}

s32 func_151D1448() {
    return 0;
}

s32 func_151D15D0() {
    return 0;
}

s32 func_151D197C() {
    return 0;
}

s32 func_151D1C98() {
    return 0;
}

void func_151D223C(u8 *arg0) {
    u8 *temp_v0 = *(u8 **)(arg0 + 0x98);
    u8 *temp_v1 = *(u8 **)temp_v0;

    if (temp_v1 != NULL) {
        *(s32 *)(temp_v1 + 0x30) = 0;
    }
}

s32 func_151D2258(s32 arg0) {
    func_151D223C(arg0);
    func_151478F4(arg0);
}

s32 func_151D2284(s32 arg0) {
    func_151D223C(arg0);
    func_15147928(arg0);
}

s32 func_151D22B0() {
    return 0;
}
