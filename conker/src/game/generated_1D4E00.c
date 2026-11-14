#include <ultra64.h>

u8 *func_15167A68(s32,s32,s32,s32,s32,s32);

#include "structs.h"
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
/* The unfinished allocator returns a pointer; this call supplies five arguments. */
u8 *func_151A8B20();
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

s32 func_151A7A90() {
    return 0;
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

s32 func_151A87F8() {
    return 0;
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

u8 *func_151A8B20() {
    return 0;
}

s32 func_151A8CEC() {
    return 0;
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

s32 func_151A9390() {
    return 0;
}

s32 func_151A9634() {
    return 0;
}

s32 func_151A9834() {
    return 0;
}
