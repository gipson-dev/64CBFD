#include <ultra64.h>
#include <string.h>
#include "structs.h"
void func_15143134(f32 *, f32 *, u8 *);

extern void (*D_800887C0[])();
extern void (*D_800887B8[])();

/* Non-matching placeholders for the text-only asm slice asm/F2820.s. */

extern void (*D_800887C8[])(u8 *, s32, u8);

typedef struct {
    f32 first[3];
    f32 second[3];
    u8 attributes[12];
} Type46DistancePayload;

typedef struct {
    u8 header[0x10];
    s32 active;
    s32 state;
    Type46DistancePayload payload;
    u8 pad3C[0x84];
    f32 distance;
    u32 tail;
} Type46DistanceRecord;
void *func_15167A68(s32, s32, s32, s32, u8, u8);
f32 func_15143E64(f32 *);

/* Create a type-0x46 record and cache the distance between its first two points. */
Type46DistanceRecord *func_150C5370(const Type46DistancePayload *payload, u32 extraBytes) {
    Type46DistanceRecord *record;
    f32 delta[3];

    record = func_15167A68(0x46, 0, (s32)(extraBytes + 0xC8u), 1, 0xFF, 1);
    if (record == NULL) {
        return NULL;
    }
    memcpy(&record->payload, payload, 0x24);
    delta[0] = record->payload.first[0] - record->payload.second[0];
    delta[1] = record->payload.first[1] - record->payload.second[1];
    delta[2] = record->payload.first[2] - record->payload.second[2];
    record->distance = func_15143E64(delta);
    record->active = 1;
    record->state = 0;
    return record;
}

void func_150C5430() {
    func_15169804();
}

void func_150C5450(u8 *arg0) {
    func_15169824(arg0);
}

void func_150C5470(u8 *arg0) {
    s32 idx = *(arg0 + 0x38);

    if (idx < 0) {
        idx = 0;
    } else if (idx >= 2) {
        idx = 0;
    }
    D_800887B8[idx]();
}

void func_150C54C0(u8 *arg0) {
    s32 idx = *(arg0 + 0x38);

    if (idx < 0) {
        idx = 0;
    } else if (idx >= 2) {
        idx = 0;
    }
    D_800887C0[idx]();
}

s32 func_150C5510(u8 *arg0) {
    func_1514EDF0(arg0, *(s32 *)(arg0 + 0xC8));
    func_150C5430(arg0);
}

s32 func_150C553C(u8 *arg0) {
    func_1514EDF0(arg0, *(s32 *)(arg0 + 0xC8));
    func_150C5450(arg0);
}

s32 func_150C5568() {
    return 0;
}

s32 func_150C56A4() {
    return 0;
}

s32 func_150C5B88(u8 *arg0) {
    u8 *temp_v1 = arg0 + 0xC8;

    if (**(u32 **) (arg0 + 0xC8) == 0) {
        return 0;
    }
    *(f32 *) (arg0 + 0x24) = *(f32 *) (*(u32 *) temp_v1 + 0x14);
    *(f32 *) (arg0 + 0x28) = *(f32 *) (*(u32 *) temp_v1 + 0x18);
    *(f32 *) (arg0 + 0x2C) = *(f32 *) (*(u32 *) temp_v1 + 0x1C);
    return 1;
}

/* Refresh a live attachment's position only while its saved identity matches. */
s32 func_150C5BD4(u8 *effect) {
    u8 *attachment = effect + 0xC8;
    struct255 *matrices;

    if ((*(struct127 **)attachment)->interaction_state == 0) {
        return 0;
    }
    if (attachment[4] != (*(struct127 **)attachment)->unique_id) {
        return 0;
    }
    matrices = (*(struct127 **)attachment)->unk1D4;
    if (matrices == NULL) {
        *(f32 *)(effect + 0x24) = (*(struct127 **)attachment)->x_position;
        *(f32 *)(effect + 0x28) = (*(struct127 **)attachment)->y_position;
        *(f32 *)(effect + 0x2C) = (*(struct127 **)attachment)->z_position;
    } else {
        func_15143134((f32 *)(attachment + 8), (f32 *)(effect + 0x24),
            (u8 *)matrices + (attachment[5] << 6));
    }
    return 1;
}

s32 func_150C5C74(s32 arg0) {
    func_1514D3B0(arg0, 0x15, 1, 0);
}

s32 func_150C5C9C(s32 arg0) {
    func_1514D3B0(arg0, 0x15, 2, 0);
}

void func_150C5CC4(u8 *arg0, s32 arg1, u8 arg2) {
    void (*callback)(u8 *, s32, u8) = D_800887C8[arg0[0x38]];

    if (callback != NULL) {
        callback(arg0, arg1, arg2);
    }
}

void func_1516972C(struct102 *);

/* Only the attachment's identity word and saved key are exposed here. */
typedef struct {
    s32 value;
    u8 key;
} AttachmentIdentityF2820;

/* Release a matching attachment or retarget its saved identity and key. */
void func_150C5D0C(u8 *owner, s32 eventAddress, u8 command) {
    AttachmentIdentityF2820 *state = (AttachmentIdentityF2820 *)(owner + 0xC8);
    u8 *event = (u8 *)eventAddress;
    s32 code = command;

    if (command == 0) {
        if (state->value == *(s32 *)event || state->key == event[4]) {
            func_1516972C((struct102 *)owner);
        }
    } else if (code == 0x2D) {
        s32 current = state->value;
        s32 first = *(s32 *)event;
        if (first == current) {
            state->value = *(s32 *)(event + 4);
            state->key = event[9];
        } else if (*(s32 *)(event + 4) == current) {
            state->value = first;
            state->key = event[8];
        }
    }
}
