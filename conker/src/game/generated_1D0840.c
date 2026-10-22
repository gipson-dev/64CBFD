#include <ultra64.h>
void func_151A4E9C(u8 *);
void *func_15167A68(s32, s32, s32, s32, u8, u8);

typedef struct {
    u8 header[0x10];
    u32 value;
    u8 selector;
    u8 red;
    u8 green;
    u8 blue;
    u8 state;
    u8 callback;
    u8 view;
    u8 reserved[5];
} Type5AColorRecord;

void func_15169260(void *, s32, s32, u8);
void func_15143134(void *, void *, s32);
extern u8 D_800A8D70[];
extern s32 D_800BE9E4;
typedef struct { s32 val; } OneWord1D0840;
extern void (*D_8008F900[])();

/* Non-matching placeholders for the text-only asm slice asm/1D0840.s. */

extern void (*D_8008F904[])(u8 *, s32, u8);

s32 func_151A3390() {
    return 0;
}

s32 func_151A3504() {
    return 0;
}

s32 func_151A361C() {
    return 0;
}

s32 func_151A37C0() {
    return 0;
}

s32 func_151A3BE4() {
    return 0;
}

s32 func_151A4590() {
    return 0;
}

s32 func_151A4638() {
    return 0;
}

s32 func_151A483C() {
    return 0;
}

typedef struct {
    u8 pad0[0x1A];
    s16 counter;
    u8 pad1[0xF];
    u8 firstOutput;
    u8 secondOutput;
    u8 pad2[0xB];
    f32 firstValue;
    f32 secondValue;
    u8 pad3[0x68];
    s16 parameters[6];
} UpdateRecord1D0840;

s32 func_151A4900(UpdateRecord1D0840 *arg0, s32 arg1) {
    s16 *parameters = arg0->parameters;
    s32 counter = arg0->counter;
    f32 increment;

    if (counter < parameters[2]) {
        arg0->firstOutput = counter * parameters[3];
    }
    if (counter < parameters[4]) {
        increment = (s32)((u32)parameters[5] * (u32)D_800BE9E4);
        arg0->firstValue += increment;
        arg0->secondValue += increment;
        counter = arg0->counter;
    }
    arg0->secondOutput = counter * parameters[1];
    return 1;
}

extern f32 D_800A8D64;
typedef struct {
    void *source;
    u8 sourceByte;
    u8 reserved0[3];
    f32 value;
    f32 zero;
    u8 active;
    u8 reserved1[3];
    f32 vector[3];
} ExtendedEffectPayload;
void *func_151491F4(s16, s8, s8, u8, u8, s32, u8, s32);
void *memcpy(void *, const void *, u32);

/* Initialize the extended source-backed effect payload. */
void func_151A499C(void *source, u8 variant) {
    u8 *effect;
    ExtendedEffectPayload payload;
    u8 *actor = source;
    payload.source = actor;
    payload.sourceByte = actor[0x3B];
    payload.value = D_800A8D64;
    payload.zero = 0.0f;
    payload.active = 1;
    payload.vector[0] = 0.0f;
    payload.vector[1] = 0.0f;
    payload.vector[2] = 0.0f;
    effect = func_151491F4(300, -1, 5, 0, 1, 32, variant, 0);
    if (effect != 0) {
        memcpy(effect + 0x28, &payload, 32);
    }
}

s32 func_151A4A38() {
    return 0;
}

/* Handle linked-record notifications and swap its selected descriptor pair. */
void func_151A4CE0(u8 *owner, s32 eventAddress, u8 command) {
    u8 *state = *(u8 **)(owner + 0x98);
    u8 *event = (u8 *)eventAddress;
    s32 value = command;

    if (command == 0) {
        if (*(s32 *)state == *(s32 *)event || state[4] == event[4]) {
            func_151A4E9C(owner);
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

s32 func_151A4D88() {
    return 0;
}

s32 func_151A4E34(u8 *arg0, void *arg1) {
    u8 *actor = *(u8 **)arg0;
    s32 target = *(s32 *)(actor + 0x1D4);

    if (target == 0) {
        return 0;
    }
    if ((actor[0x74] & 0xF) == 0xF) {
        return 0;
    }
    func_15143134(arg0 + 8, arg1, target + (arg0[5] << 6));
    return 1;
}

void func_151A4E9C(u8 *arg0) {
    u8 *temp_v0 = *(u8 **) (arg0 + 0x98);

    *(u16 *) (arg0 + 0x1E) &= 0xFFFD;
    *(arg0 + 0x30) = 0;
    *(temp_v0 + 0x30) |= 1;
    *(temp_v0 + 0x30) |= 4;
}

s32 func_151A4ECC() {
    return 0;
}

void func_151A4F7C(u8 *arg0, u8 *arg1, u8 arg2) {
    u8 *temp_v0 = arg0 + 0x28;

    if (arg2 == 0) {
        if ((*(s32 *)temp_v0 == *(s32 *)arg1) || (temp_v0[4] == arg1[4])) {
            func_1516972C(arg0);
        }
    }
}

/* Create a type-0x5A color record with optional trailing payload. */
Type5AColorRecord *func_151A4FD0(s32 selector, u32 value, s32 red, s32 green,
    s32 blue, s32 view, u8 callback, u32 extraBytes) {
    Type5AColorRecord *record = func_15167A68(0x5A, 0,
        (s32)(extraBytes + 0x20U), 0, 0xFF, 1);

    if (record == NULL) {
        return NULL;
    }
    record->selector = selector;
    record->value = value;
    record->red = red;
    record->green = green;
    record->blue = blue;
    record->callback = callback;
    record->state = 0;
    record->view = view;
    return record;
}

s32 func_151A5070() {
    return 0;
}

void func_151A5130(arg0, arg1, arg2)
s32 arg0;
u8 *arg1;
s16 arg2;
{
    D_8008F900[*(arg1 + 0x14)](arg0, arg1, arg2);
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1D0840/func_151A5170.s")

void func_151A55D4(u8 *arg0, s32 arg1, u8 arg2) {
    void (*callback)(u8 *, s32, u8) = D_8008F904[arg0[0x19]];

    if (callback != NULL) {
        callback(arg0, arg1, arg2);
    }
}

void func_151A561C(s32 arg0, u8 arg1) {
    OneWord1D0840 tmp;

    tmp = *(OneWord1D0840 *) D_800A8D70;
    func_15169260(&tmp, 1, arg0, arg1);
}
