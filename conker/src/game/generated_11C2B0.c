#include <ultra64.h>
#include "structs.h"

typedef struct {
    f32 x, y, z;
} EffectRayVector;

typedef struct {
    u8 opaque0[0x18];
    u8 active;
    u8 opaque19[0x17];
    EffectRayVector direction;
} EffectRayMotion;

typedef struct {
    u8 opaque0[0x34];
    EffectRayVector position;
    u8 opaque40[0xD0];
    EffectRayMotion motion;
} EffectRayOwner;

typedef struct {
    u8 opaque0[0x34];
    EffectRayVector position;
    EffectRayVector endPoint;
    u8 opaque4C[0xC];
    u32 flags;
    u8 opaque5C[0x11C];
    EffectRayOwner *owner;
} OwnerRayEffect;

void func_1516972C(struct102 *);

typedef struct { u8 *owner; u8 identity; u8 opaque5[3]; } EmbeddedOwnerLink;
typedef struct { u8 *before; u8 *after; u8 before_identity; u8 after_identity; u8 opaqueA[2]; } OwnerLinkEvent;
s32 func_150ADA20(void);
void func_15143874(s16, f32, f32 *, f32 *);
void func_15143134(f32 *, f32 *, u8 *);
void func_151C329C(struct17 *, s32, s32);

extern s32 D_800A1674;
extern s32 D_800A1680;
s32 func_15160A58(s32, s32, s32, s32, s32, s32, s32, s32, s32, s32, s32, s32, s32, s32, s32, s32);

/* Non-matching placeholders for the text-only asm slice asm/11C2B0.s. */

void func_150F0318();
void func_150F0380();
void func_150F03E8();

void func_150F02A0(u8 *arg0);

s32 func_150EEE00() {
    return 0;
}

void func_150EEF40(u8 *arg0, u8 arg1) {
    struct {
        u8 *target;
        u8 code;
        u8 value;
    } rec;

    rec.target = arg0;
    rec.code = *(arg0 + 0x3B);
    rec.value = arg1;
    func_151403A8(&rec, 0x43);
}

s32 func_150EEF80() {
    return 0;
}

s32 func_150EF38C() {
    return 0;
}

s32 func_150EF784(u8 *arg0, u8 arg1, u8 arg2) {
    if (*(arg0 + 4) == 0x28) {
        return 1;
    }
    return 0;
}

typedef struct {
    u8 opaque0[0x1C];
    struct102 *children[5];
} ChildReleaseState11C2B0;

void func_1516972C(struct102 *);
void func_1516979C(struct102 *);
void func_1513CA6C(struct210 *);
void func_1513CAA0(struct210 *);

/* Release the five attached children, then run the actor's base teardown. */
void func_150EF7B0(struct210 *owner) {
    ChildReleaseState11C2B0 *state = (ChildReleaseState11C2B0 *)((u8 *)owner + 0x110);
    s32 index;

    for (index = 0; index < 2; index++) {
        if (state->children[index] != NULL) {
            func_1516972C(state->children[index]);
        }
    }
    if (state->children[2] != NULL) {
        func_1516972C(state->children[2]);
    }
    if (state->children[3] != NULL) {
        func_1516972C(state->children[3]);
    }
    if (state->children[4] != NULL) {
        func_1516972C(state->children[4]);
    }
    func_1513CA6C(owner);
}

/* Release the five attached children, then run the actor's base teardown. */
void func_150EF860(struct210 *owner) {
    ChildReleaseState11C2B0 *state = (ChildReleaseState11C2B0 *)((u8 *)owner + 0x110);
    s32 index;

    for (index = 0; index < 2; index++) {
        if (state->children[index] != NULL) {
            func_1516979C(state->children[index]);
        }
    }
    if (state->children[2] != NULL) {
        func_1516979C(state->children[2]);
    }
    if (state->children[3] != NULL) {
        func_1516979C(state->children[3]);
    }
    if (state->children[4] != NULL) {
        func_1516979C(state->children[4]);
    }
    func_1513CAA0(owner);
}

s32 func_150EF910() {
    return 0;
}

s32 func_150EFA4C() {
    return 0;
}

s32 func_150EFB80() {
    return 0;
}

s32 func_150EFEC8() {
    return 0;
}

/* Follow the active owner's position and project its direction by 500 units. */
s32 func_150F00EC(OwnerRayEffect *effect) {
    EffectRayOwner *owner = effect->owner;
    EffectRayMotion *motion = &owner->motion;

    if (owner->motion.active & 1) {
        effect->position = owner->position;
        effect->endPoint.x = owner->position.x + motion->direction.x * 500.0f;
        effect->endPoint.y = owner->position.y + motion->direction.y * 500.0f;
        effect->endPoint.z = owner->position.z + motion->direction.z * 500.0f;
        effect->flags |= 6;
    } else {
        effect->flags &= ~4;
        effect->flags &= ~2;
    }
    return 1;
}

s32 func_150F0198() {
    return 0;
}

void func_150F0260(register u8 *arg0) {
    func_150F02A0(arg0);
}

void func_150F0280(register u8 *arg0) {
    func_150F02A0(arg0);
}

// Matched with a base-pointer lifetime and guarded index-register normalization.
void func_150F02A0(u8 *arg0) {
    u8 *temp_v0 = *(u8 **)(arg0 + 0x60);
    u8 *base = *(u8 **)(temp_v0 + 8);
    u8 index = *(u8 *)(temp_v0 + 0xC);

    *(s32 *)(base + (index * 4) + 0x12C) = 0;
}

s32 func_150F02C0(s32 arg0) {
    func_150F0318(arg0);
    func_1514933C(arg0);
}

s32 func_150F02EC(s32 arg0) {
    func_150F0318(arg0);
    func_15149368(arg0);
}

void func_150F0318(u8 *arg0) {
    u8 *temp_v0;

    temp_v0 = *(u8 **)(arg0 + 0x28);
    *(s32 *)(temp_v0 + 0x134) = 0;
}

s32 func_150F0328(s32 arg0) {
    func_150F0380(arg0);
    func_151411A4(arg0);
}

s32 func_150F0354(s32 arg0) {
    func_150F0380(arg0);
    func_151411C4(arg0);
}

void func_150F0380(u8 *arg0) {
    u8 *temp_v0;

    temp_v0 = *(u8 **)(arg0 + 0x178);
    *(s32 *)(temp_v0 + 0x138) = 0;
}

s32 func_150F0390(s32 arg0) {
    func_150F03E8(arg0);
    func_151617C4(arg0);
}

s32 func_150F03BC(s32 arg0) {
    func_150F03E8(arg0);
    func_151617E4(arg0);
}

void func_150F03E8(u8 *arg0) {
    u8 *temp_v0;

    temp_v0 = *(u8 **)(arg0 + 0x18);
    *(s32 *)(temp_v0 + 0x13C) = 0;
}

s32 func_150F03F8() {
    return 0;
}

/* Handle release notifications and swap the selected descriptor pair. */
void func_150F07E4(u8 *owner, s32 eventAddress, u8 command) {
    u8 *state = *(u8 **)(owner + 0x60);
    u8 *event = (u8 *)eventAddress;
    s32 value = command;

    if (command == 0) {
        value = *(s32 *)event;
        if (value == *(s32 *)state || state[4] == event[4]) {
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

/* Retarget the embedded owner link or release its matching actor. */
void func_150F088C(u8 *owner, u8 *eventBytes, u8 command) {
    EmbeddedOwnerLink *link = (EmbeddedOwnerLink *)(owner + 0x170);
    OwnerLinkEvent *event = (OwnerLinkEvent *)eventBytes;

    if (command == 0) {
        u8 *first = event->before;
        if (first == link->owner || link->identity == ((u8 *)event)[4]) {
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

/* Submit the two preset descriptors through the common 16-argument helper. */
void func_150F0938(s32 context) {
    func_15160A58(context, 0x25, (s32)&D_800A1674, 2, 0x12C, 4, 0, 0xFF, 0, 0xFF, 0, -1, 0, 0, 0xFF, 1);
    func_15160A58(context, 2, (s32)&D_800A1680, 2, 0x12C, 0xD, 0xFF, 0xFF, 0xFF, 0xFF, 0, -1, 0, 0, 0xFF, 1);
}

s32 func_150F0A24() {
    return 0;
}

s32 func_150F0BEC() {
    return 0;
}

s32 func_150F0E48() {
    return 0;
}

/* Only the payload's identity word and saved key are exposed. */
typedef struct {
    s32 value;
    u8 key;
} IdentityEvent11C2B0;

/* Retarget an embedded identity, or release its owner for a matching event. */
void func_150F1020(u8 *owner, s32 eventAddress, u8 command) {
    IdentityEvent11C2B0 *state = (IdentityEvent11C2B0 *)(owner + 0xA8);
    u8 *event = (u8 *)eventAddress;
    s32 code = command;

    if (command == 0x2D) {
        s32 current = state->value;
        s32 first = *(s32 *)event;
        if (first == current) {
            state->value = *(s32 *)(event + 4);
            state->key = event[9];
        } else if (*(s32 *)(event + 4) == current) {
            state->value = first;
            state->key = event[8];
        }
    } else if (code == 0 || code == 0x43) {
        if (*(s32 *)event == state->value || state->key == event[4]) {
            func_1516972C((struct102 *)owner);
        }
    }
}

typedef struct {
    void *source;
    u8 sourceByte;
    u8 reserved[3];
    f32 value;
    f32 position[3];
} EffectPositionPayload;
void *func_15149130(s16, s8, s8, s8, u8, u8, s32, u8, s32);
void *memcpy(void *, const void *, u32);

/* Capture the source position and attach the complete payload to an effect. */
void func_150F10D4(void *source) {
    EffectPositionPayload payload;
    u8 *effect;
    payload.source = source;
    payload.sourceByte = ((u8 *)source)[0x3B];
    payload.value = 0.0f;
    payload.position[0] = *(f32 *)((u8 *)source + 0x14);
    payload.position[1] = *(f32 *)((u8 *)source + 0x18);
    payload.position[2] = *(f32 *)((u8 *)source + 0x1C);
    effect = func_15149130(0x12C, -1, 0x4C, -1, 0, 0x3A, 24, 0xFF, 1);
    if (effect != 0) {
        memcpy(effect + 0x28, &payload, 24);
    }
}

s32 func_150F1170() {
    return 0;
}

void func_150F15F8(u8 *arg0, u8 *volatile arg1, volatile u8 arg2) {
    u8 *target = arg0 + 0x28;

    if (arg2 == 0x43) {
        u8 *word_owner = arg1;
        u8 *byte_owner = arg1;

        if ((*(s32 *)word_owner == *(s32 *)target) ||
            (target[4] == byte_owner[4])) {
            func_1516972C((struct102 *)arg0);
        }
    } else {
        func_15149514((s32)arg1, arg2, (s32)target,
                      (s32)(target + 4), (s32)arg0);
    }
}

// Matched with guarded identity-comparison register normalization.
void func_150F1684(u8 *arg0, u8 *arg1, u8 arg2) {
    u8 *target = arg0 + 0x18;

    if (arg2 == 0x43) {
        if ((*(s32 *)arg1 == *(s32 *)target) || (target[4] == arg1[4])) {
            func_1516972C((struct102 *)arg0);
        }
    }
}

s32 func_150F16DC() {
    return 0;
}

s32 func_150F1A00() {
    return 0;
}

s32 func_150F1B48() {
    return 0;
}

void func_150F1CB0(u8 *arg0) {
    if (*(u16 *) (arg0 + 0x84) == 0x14) {
        arg0[0x68] = 0x1B;
    } else {
        arg0[0x68] = 0xC;
    }

    arg0[0x69] = 0x13;
    if ((*(u32 *) (arg0 + 0x2E4) & 3) == 3) {
        arg0[0x69] = 0x14;
    }
    if ((*(u32 *) (arg0 + 0x2E4) & 0xC) == 0xC) {
        arg0[0x69] = 0x17;
    }
}

s32 func_150F1D10() {
    return 0;
}

s32 func_150F20F0() {
    return 0;
}

/* Transform a random horizontal offset through the actor's matrix and submit it. */
void func_150F2230(struct127 *actor, u8 kind, s32 flags) {
    struct17 offset;
    struct17 point;

    if (actor->unk1D4 != 0 && (actor->unk74 & 0xF) != 0xF) {
        offset.unk0 = 0.0f;
        offset.unk4 = 0.0f;
        offset.unk8 = 0.0f;
        func_15143874((u8)func_150ADA20(), 100.0f, &offset.unk0, &offset.unk8);
        func_15143134((f32 *)&offset, (f32 *)&point, (u8 *)((u32)actor->unk1D4 + 0x4C0));
        func_151C329C(&point, kind, flags);
    }
}
