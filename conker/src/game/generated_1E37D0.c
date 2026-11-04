#include <ultra64.h>
typedef struct {
    f32 x;
    f32 y;
    f32 z;
} ActorPosition151B6320;

typedef struct {
    ActorPosition151B6320 position;
    s16 duration;
    u16 flags;
    s32 kind;
    u8 reserved14; /* Preserved stack byte copied by the retail helper. */
    u8 count;
    u8 reserved16[2]; /* Preserved stack bytes copied by the retail helper. */
} ActorEffectRequest151B6320;

typedef struct {
    u8 *owner;
    u8 identity;
    u8 reserved05[3];
    ActorPosition151B6320 position;
    f32 velocityX;
    f32 velocityY;
    f32 lowerBound;
    f32 upperBound;
    f32 velocityZ;
    u32 reserved28; /* Retail copies this untouched stack word. */
} ActorEffectPayload151B6320;

typedef struct {
    ActorEffectPayload151B6320 payload;
    u32 layoutGap; /* Original local spacing; not part of either packet. */
    ActorEffectRequest151B6320 request;
    u32 layoutTail; /* Preserves the original 0x90-byte frame. */
} ActorEffectLocals151B6320;

u8 *func_15147A80(void *, s32, s32, s32, s32, s32, s32, s32,
    void *, u8, s32);
void *memcpy(void *, const void *, unsigned int);

extern void (*D_8008FB98[])(u8 *, s32, u8);

/* Non-matching placeholders for the text-only asm slice asm/1E37D0.s. */

/* Snapshot one actor position and submit its retail effect packet. */
void func_151B6320(u8 *actor, u8 channel, s32 context) {
    ActorEffectLocals151B6320 locals;
    u8 *record;

    locals.request.count = 10;
    locals.request.position.x = *(f32 *)(actor + 0x14);
    locals.request.position.y = *(f32 *)(actor + 0x18);
    locals.request.position.z = *(f32 *)(actor + 0x1C);
    locals.request.duration = 300;
    locals.request.flags = 6;
    locals.payload.owner = actor;
    locals.payload.identity = actor[0x3B];
    locals.payload.position = locals.request.position;
    locals.payload.velocityX = 0.0f;
    locals.payload.velocityY = 0.0f;
    locals.payload.upperBound = -16384.0f;
    locals.payload.lowerBound = -16384.0f;
    locals.payload.velocityZ = 0.0f;
    locals.request.kind = 13;
    record = func_15147A80(&locals.request, 0x30, 0x1C, 0xB, 0xB, 0xB,
        0, 0, NULL, channel, context);
    if (record != NULL) {
        memcpy(*(void **)(record + 0x98), &locals.payload, 0x2C);
    }
}

s32 func_151B6420() {
    return 0;
}

s32 func_151B65D4() {
    return 0;
}

s32 func_151B6928() {
    return 0;
}

// Matched with guarded event/current register and return scheduling.
void func_151B70B4(u8 *arg0, u8 *arg1, u8 arg2) {
    u8 *link;
    u8 *current;
    u8 *first;
    u8 event;

    link = *(u8 **)(arg0 + 0x98);
    event = arg2;
    current = *(u8 **)link;

    if (arg2 == 0) {
        if (*(u8 **)arg1 != current) {
            return;
        }
        arg0[0x30] = 0;
        *(u16 *)(arg0 + 0x1E) |= 8;
        return;
    }

    if (event == 0x2D) {
        first = *(u8 **)arg1;
        if (first == current) {
            *(u8 **)link = *(u8 **)(arg1 + 4);
            link[4] = arg1[9];
            return;
        }
        if (*(u8 **)(arg1 + 4) == current) {
            *(u8 **)link = first;
            link[4] = arg1[8];
        }
    }
}

s32 func_151B7144() {
    return 0;
}

s32 func_151B7328() {
    return 0;
}

s32 func_151B7678(u8 *arg0, f32 *arg1) {
    u8 *container = *(u8 **)(arg0 + 0x98);
    u8 *entry = *(u8 **)(container + 4);
    u8 *record = *(u8 **)entry;

    if (*(s32 *)record == 0 || entry[4] != record[0x3B]) {
        return 0;
    }
    arg1[0] = *(f32 *)(record + 0x14);
    arg1[1] = *(f32 *)(record + 0x18);
    arg1[2] = *(f32 *)(record + 0x1C);
    return 1;
}

s32 func_151B76CC() {
    return 0;
}

s32 func_151B77F4() {
    return 0;
}

s32 func_151B7998() {
    return 0;
}

s32 func_151B7C38() {
    return 0;
}

void func_151B82CC(u8 *arg0, s32 arg1, u8 arg2) {
    u8 *temp_v0 = *(u8 **) (arg0 + 0x98);
    void (*temp_v1)(u8 *, s32, u8) =
        D_8008FB98[*(temp_v0 + 8)];

    if (temp_v1 != 0) {
        temp_v1(arg0, arg1, arg2);
    }
}

void func_151B8318(u8 *arg0, u8 *arg1, u8 arg2) {
    u8 *container = *(u8 **)(arg0 + 0x98);
    u8 *entry = *(u8 **)(container + 4);

    if (arg2 == 0) {
        s32 value = *(s32 *)arg1;

        if (value == *(s32 *)entry || entry[4] == arg1[4]) {
            func_1516972C(arg0);
        }
    }
}

void func_151B8370(arg0, arg1)
u8 *arg0;
s32 arg1;
{
    u8 *temp_v0 = *(u8 **) (arg0 + 0x98);

    arg1 = *(s32 *) temp_v0;
    if (arg1 != 0) {
        func_1516972C(arg1);
    }
}

s32 func_151B83A0(s32 arg0) {
    func_151B8370(arg0);
    func_151478F4(arg0);
}

s32 func_151B83CC(s32 arg0) {
    func_151B8370(arg0);
    func_15147928(arg0);
}
