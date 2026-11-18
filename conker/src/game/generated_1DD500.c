#include <ultra64.h>
#include "structs.h"
extern s32 D_800BE9E4;
f32 func_151423D8(u8);

/* Non-matching placeholders for the text-only asm slice asm/1DD500.s. */

typedef struct { f32 x, y, z; } TrailPoint151B0050;
extern f32 D_800AA28C, D_800AA290, D_800AA294, D_800AA298, D_800AA29C;
s32 func_150ADA20(void);
f32 func_150ADA68(void);
void func_15143794(s16, s16, f32, TrailPoint151B0050 *);
u8 *func_151DA6F8(void *, void *, f32, s16, u8, f32, s32, u8,
    f32, f32, u8, u8, s32, s16, s16, s32, u8, s32);

/* Snapshot position before the providers and submit all captured trail fields. */
s32 func_151B0050(s32 kind, s16 index, f32 x, f32 y, f32 z,
    f32 unused5, f32 unused6, f32 unused7, s16 pitch, s16 heading,
    f32 unused10, s32 unused11, f32 unused12, s32 unused13, u8 slot) {
    TrailPoint151B0050 position;
    TrailPoint151B0050 direction;
    struct { f32 extentSample; u32 durationSample, colorSample; f32 timeSample; } captures;

    position.x = x;
    position.y = y;
    position.z = z;
    func_15143794(heading, pitch,
        func_150ADA68() * D_800AA28C + D_800AA290, &direction);
    captures.extentSample = func_150ADA68();
    captures.durationSample = (u32)func_150ADA20();
    captures.colorSample = (u32)func_150ADA20();
    captures.timeSample = func_150ADA68();
    func_151DA6F8(&position, &direction,
        captures.extentSample * (f32)(s32)0 + D_800AA294, /* Retain the explicit zero multiply. */
        (s16)(captures.durationSample % 20U + 31), (u8)(captures.colorSample % 101U + 155),
        captures.timeSample * D_800AA298 + D_800AA29C,
        ((u32)func_150ADA20() & 1) + 3, 1, 1.0f, 1.0f,
        0, 0, 0, 16, 15, 0, slot, 1);
    return 1;
}

typedef struct HeightResult71820 {
    f32 height; s16 vertices[9]; s16 pad16; u32 metadata;
    u8 flags, state; u16 pad1E; s32 value;
} HeightResult71820;
typedef struct HeightActor71820 HeightActor71820;
typedef struct { s16 firstAngleBase, firstAngleRange, secondAngleBase, secondAngleRange; } ActorTrailAngles151B01B8;
typedef struct {
    f32 position[3], timeBase, timeRange, scaleBase, scaleRange, radiusBase, radiusRange;
    s16 countBase, countRange, requestSelectorBase, requestSelectorRange;
    s16 durationBase, durationRange, modeBase, modeRange;
    u8 selector, private35[3]; f32 opaqueChance; s16 firstValue, secondValue; s32 requestValue;
} ActorTrail151B01B8;
extern u8 D_800A3FD8[];
extern f32 D_800AA120[], D_800AA2A0, D_800AA2A4, D_800AA2A8, D_800AA2AC, D_800AA2B0;
void func_1504715C(HeightResult71820 *, HeightActor71820 *);
s32 func_15134070(u8 *);
void func_15143134(f32 *, f32 *, u8 *);
void func_15153F18(void *, void *, s32, s32, s32);

/* Build an angular trail for the actor unless its selected type is disabled. */
void func_151B01B8(u8 *actor, u8 *source) {
    ActorTrail151B01B8 trail;
    ActorTrailAngles151B01B8 angles;
    u8 heading;
    HeightResult71820 surface;
    union { s32 type; u8 *record; } selected;

    if (actor != NULL && *(u8 **)(actor + 0x1D4) != NULL && (actor[0x74] & 15) != 15) {
        func_1504715C(&surface, (HeightActor71820 *)actor);
        selected.type = source != NULL ?
            ((source[4] == 0x53 || source[4] == 0xA5) ? 4 : func_15134070(source)) : 4;
        if (selected.type != 99) {
            selected.record = &D_800A3FD8[selected.type * 16];
            if (selected.record[14] != 2) {
                heading = (*(u16 *)(actor + 0x7A) >> 8) + 64;
                func_15143134(D_800AA120, trail.position, *(u8 **)(actor + 0x1D4) + 0x180);
                angles.firstAngleBase = heading - 104;
                trail.timeBase = D_800AA2A0;
                trail.countBase = 10;
                trail.countRange = 20;
                angles.firstAngleRange = 208;
                angles.secondAngleBase = -27;
                angles.secondAngleRange = 54;
                trail.requestSelectorBase = 3;
                trail.requestSelectorRange = 2;
                trail.durationBase = 30;
                trail.durationRange = 40;
                trail.modeBase = 155;
                trail.modeRange = 100;
                trail.timeRange = D_800AA2A4;
                trail.scaleBase = D_800AA2A8;
                trail.scaleRange = D_800AA2AC;
                trail.radiusBase = 6.0f;
                trail.radiusRange = D_800AA2B0;
                trail.opaqueChance = 0.5f;
                if (selected.record[14] == 1) trail.selector = 1;
                else trail.selector = 0;
                trail.firstValue = 16;
                trail.secondValue = 15;
                trail.requestValue = 0;
                func_15153F18(&angles, &trail, (s32)&surface, 255, 1);
            }
        }
    }
}

/* Note 362: original ROM blood effect and dependencies. */
#pragma GLOBAL_ASM("asm/nonmatchings/generated_1DD500/func_151B03B8.s")

s32 func_151B09BC() {
    return 0;
}

s32 func_151B0B88() {
    return 0;
}

s32 func_151B118C() {
    return 0;
}

s32 func_151B1478(u8 *arg0) {
    s32 temp_v0 = *(s16 *)(arg0 + 0x1C);

    if (temp_v0 < 0x20) {
        s32 temp_v1 = temp_v0 << 3;
        if (temp_v1 < *(u8 *)(arg0 + 0x5C)) {
            *(u8 *)(arg0 + 0x5C) = temp_v1;
        }
    }
    return 1;
}

s32 func_151B14AC() {
    return 0;
}

/* Advance two phase bytes and ease the planar position toward their sampled offsets. */
s32 func_151B1828(u8 *state) {
    u8 *parameters = state;
    f32 firstSample;
    f32 secondSample;
    f32 firstCurrent;
    f32 secondCurrent;

    state[0x120] += (s32)*(s8 *)(state + 0x122) * (u32)D_800BE9E4;
    state[0x121] += (s32)*(s8 *)(state + 0x123) * (u32)D_800BE9E4;
    firstSample = func_151423D8((u8)(state[0x120] - 0x40));
    parameters += 0x110;
    secondSample = func_151423D8((u8)(parameters[0x11] - 0x40));

    firstCurrent = *(f32 *)(state + 0x2C);
    secondCurrent = *(f32 *)(state + 0x30);
    *(f32 *)(state + 0x2C) =
        ((*(f32 *)(parameters + 0x1C) * firstSample +
          *(f32 *)(parameters + 0x14)) - firstCurrent) * 0.5f + firstCurrent;
    *(f32 *)(state + 0x30) =
        ((*(f32 *)(parameters + 0x20) * secondSample +
          *(f32 *)(parameters + 0x18)) - secondCurrent) * 0.5f + secondCurrent;
    return 1;
}

void func_1516972C(void *arg0);

typedef struct {
    void *child;
    s32 first;
    s32 second;
} CleanupSlot1DD500;

void func_151B1918(u8 *arg0) {
    u8 *cursor = arg0 + 0x28;
    CleanupSlot1DD500 *slot;
    CleanupSlot1DD500 *current;
    s32 offset;

    *(s32 *)(arg0 + 0x30) = 0;
    slot = (CleanupSlot1DD500 *)(cursor + 0xC);
    *(f32 *)(arg0 + 0xB8) = 0.0f;
    offset = 0;
    do {
        current = slot;
        if (*(void **)(cursor + 0xC) != NULL) {
            func_1516972C(slot->child);
        }
        current->child = NULL;
        current->first = 0;
        current->second = 0;
        offset += 0xC;
        cursor += 0xC;
        slot++;
    } while (offset != 0x84);
}

/* Only the owner identity word, saved key and event pair are exposed. */
typedef struct {
    void *owner;
    u8 key;
} OwnerIdentity1DD500;
typedef struct {
    void *before;
    void *after;
    u8 before_key;
    u8 after_key;
} OwnerIdentityEvent1DD500;

/* Capture the owner before dispatch, then release or retarget this record. */
void func_151B19A4(struct260 *record, s32 eventAddress, u8 command) {
    u8 *owner = (u8 *)record;
    OwnerIdentity1DD500 *state = (OwnerIdentity1DD500 *)(owner + 0x28);
    OwnerIdentityEvent1DD500 *event = (OwnerIdentityEvent1DD500 *)eventAddress;
    void *saved = state->owner;
    s32 code = command;

    if (command == 0 || command == 0x13) {
        if (saved == event->before || state->key == ((u8 *)event)[4]) {
            func_1516972C(owner);
        }
    } else if (code == 0x2D) {
        void *current = state->owner;
        void *first = event->before;
        if (current == first) {
            state->owner = event->after;
            state->key = event->after_key;
        } else if (event->after == current) {
            state->owner = first;
            state->key = event->before_key;
        }
    }
}

s32 func_151B1A58(s32 arg0) {
    func_151B1918((u8 *)arg0);
    func_1514933C(arg0);
}

s32 func_151B1A84(s32 arg0) {
    func_151B1918((u8 *)arg0);
    func_15149368(arg0);
}

void *func_151491F4(s16 arg0, s8 arg1, s8 arg2, u8 arg3, u8 arg4, s32 arg5, u8 arg6, s32 arg7);

typedef struct {
    void *owner;
    u8 selector;
    u8 pad5[3];
    f32 value;
} Generated1DD500Payload;

void func_151B1AB0(u8 * volatile arg0) {
    u8 *record;
    Generated1DD500Payload payload;

    if (arg0 != NULL) {
        payload.owner = arg0;
        payload.selector = ((u8 *)payload.owner)[0x3B];
        payload.value = 0.0f;
        record = func_151491F4(0x3C, -1, 0x15, 1, 0x11, 0xC, 0xFF, 1);
        if (record != NULL) {
            memcpy(record + 0x28, &payload, sizeof(payload));
        }
    }
}

s32 func_151B1B34() {
    return 0;
}

/* Only the record payload's identity word and saved key are exposed. */
typedef struct {
    s32 value;
    u8 key;
} RecordIdentity1DD500;

/* Retarget a saved record identity, or release it for a matching event. */
void func_151B1FAC(struct260 *record, s32 eventAddress, u8 command) {
    u8 *owner = (u8 *)record;
    RecordIdentity1DD500 *state = (RecordIdentity1DD500 *)(owner + 0x28);
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
    } else if (code == 0) {
        if (*(s32 *)event == state->value || state->key == event[4]) {
            func_1516972C(owner);
        }
    }
}
