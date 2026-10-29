#include <ultra64.h>

extern f32 D_800A1B70;
void *func_15134DAC(s32, s32);
typedef struct {
    u8 owner_id;
    u8 pad1[3];
    u8 *owner;
    u8 attachmentIndex;
    u8 pad9[3];
    f32 zero0;
    f32 zero1;
    f32 zero2;
    f32 zero3;
    f32 value1C;
    f32 value20;
    u8 mode;
    u8 pad25;
    s16 activeFrames;
    s16 restartDelay;
    s16 lifetime;
    s16 value2C;
    s8 startCallback;
    s8 transformCallback;
    s8 updateCallback;
    u8 pad31[3];
    f32 rate;
    u8 flags;
    s8 finishCallback;
} OwnerLifetimeDescriptor1228D0;

#include "functions.h"

/* Non-matching placeholders for the text-only asm slice asm/1228D0.s. */

void func_150F55C8(u8 *record);

s32 func_15179008();

typedef struct {
    u8 *owner;
    u8 owner_id;
    u8 pad5[3];
    f32 value;
} Func150F5C08Payload;

s32 func_150F5420() {
    return 0;
}

void func_150F5590(u8 *arg0) {
    s32 val = 0x1000 - (*(s16 *) (arg0 + 0x24) << 2);

    *(s16 *) (arg0 + 0x38) = val;
    *(s16 *) (arg0 + 0x3A) = *(s16 *) (arg0 + 0x38);
    func_150F55C8(arg0);
}

/* Apply the record opacity envelope to its remaining lifetime. */
void func_150F55C8(u8 *record) {
    s32 duration = *(s32 *)(record + 0x1C) & 0xFFFF;
    s32 fadeIn = *(s32 *)(record + 0x18) >> 16;
    s32 hold = *(s32 *)(record + 0x18) & 0xFFFF;
    s32 fadeOut = *(s32 *)(record + 0x1C) >> 16;
    s32 boundary = duration - fadeIn;
    s32 remaining = *(s16 *)(record + 0x24);

    if (boundary < remaining) {
        record[0x45] = ((duration - remaining) * 255) / fadeIn;
    } else if (boundary - hold < remaining) {
        record[0x45] = 255;
    } else {
        record[0x45] = (remaining * 255) / fadeOut;
    }
}

void func_150F568C(s32 arg0) {
    func_15179008(0);
}

s32 func_150F56B0() {
    return 0;
}

s32 func_150F5A54() {
    return 0;
}

void func_150F5C08(u8 *arg0, s16 arg1, u8 arg2, s32 arg3) {
    Func150F5C08Payload payload;
    struct260 *object;

    payload.owner = arg0;
    payload.owner_id = arg0[0x3B];
    payload.value = 0.0f;

    object = func_15149130(arg1, -1, 0x51, -1, 1, 0x3E,
                           (struct37 *)sizeof(payload), arg2, arg3);
    if (object != NULL) {
        memcpy((u8 *)object + 0x28, &payload, sizeof(payload));
    }
}

s32 func_150F5C98() {
    return 0;
}

void func_150F6138(u8 *arg0, s32 arg1, u8 arg2) {
    func_15149514(arg1, arg2, (s32) (arg0 + 0x28), (s32) (arg0 + 0x2C), (s32) arg0);
}

s32 func_150F6178() {
    return 0;
}

void func_150F631C(u8 *arg0) {
    u8 *owner = arg0;

    if (*(struct102 * volatile *) (owner + 0x30) != NULL) {
        func_1516972C(*(struct102 * volatile *) (owner + 0x30));
    }
    if (*(struct102 **) (owner + 0x34) != NULL) {
        func_1516972C(*(struct102 **) (owner + 0x34));
    }
}

s32 func_150F6368(s32 arg0) {
    func_150F631C(arg0);
    func_1514933C(arg0);
}

s32 func_150F6394(s32 arg0) {
    func_150F631C(arg0);
    func_15149368(arg0);
}

void func_150F63C0(u8 *arg0, s32 arg1, u8 arg2) {
    func_15169850(arg1, arg2, (s32) (arg0 + 0x28), (s32) (arg0 + 0x2C), (s32) arg0);
}

void func_150F6400(u8 *arg0) {
    u8 *temp_v0;

    if (*(u8 * volatile *)(arg0 + 0x160) != NULL) {
        temp_v0 = *(u8 * volatile *)(arg0 + 0x160) + 0x28;
        *(s32 *)(temp_v0 + 8) = 0;
    }
}

s32 func_150F6420(s32 arg0) {
    func_150F6400(arg0);
    func_1513CA6C(arg0);
}

s32 func_150F644C(s32 arg0) {
    func_150F6400(arg0);
    func_1513CAA0(arg0);
}

void func_150F6478(s32 arg0) {
}

s32 func_150F6484(s32 arg0) {
    func_150F6478(arg0);
    func_151411A4(arg0);
}

s32 func_150F64B0(s32 arg0) {
    func_150F6478(arg0);
    func_151411C4(arg0);
}

s32 func_150F64DC() {
    return 0;
}

void func_150F6850(u8 *arg0, s32 arg1, u8 arg2) {
    func_15169850(arg1, arg2, (s32) (arg0 + 0x28), (s32) (arg0 + 0x2C), (s32) arg0);
}

/* Construct an owner-attached effect with a signed lifetime.
 * The two -1 callback indices disable those optional callbacks.
 * The original four-argument ABI retains the unused selector and context. */
void *func_150F6890(u8 *owner, s16 lifetime, s32 unusedSelector, s32 unusedContext) {
    OwnerLifetimeDescriptor1228D0 packet;
    packet.owner_id = owner[0x3B];
    packet.owner = owner;
    packet.attachmentIndex = 3;
    packet.zero0 = 0.0f;
    packet.zero1 = 0.0f;
    packet.zero2 = 0.0f;
    packet.zero3 = 0.0f;
    packet.value1C = D_800A1B70;
    packet.value20 = 8.5f;
    packet.mode = 2;
    packet.activeFrames = 40;
    packet.restartDelay = 16;
    packet.lifetime = lifetime;
    packet.startCallback = 5;
    packet.transformCallback = 8;
    packet.updateCallback = -1;
    packet.rate = 1.0f;
    packet.flags = 0;
    packet.finishCallback = -1;
    packet.value2C = 0;
    return func_15134DAC((s32)&packet, 0);
}

s32 func_150F695C() {
    return 0;
}
