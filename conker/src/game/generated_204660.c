#include <ultra64.h>

typedef struct {
    f32 x, y, z;
} AttachmentPosition151D7830;

typedef struct {
    AttachmentPosition151D7830 position;
    u16 duration;
    u16 flags;
    s32 kind;
    u8 mode;
    u8 count;
    s32 value;
} AttachmentRequest151D7830;

typedef struct {
    u8 *owner;
    AttachmentPosition151D7830 position;
    AttachmentPosition151D7830 velocity;
} AttachmentPayload151D7830;

u8 *func_15147A80(void *, s32, s32, s32, s32, s32, s32, s32, void *, u8, s32);

void func_151D7830(u8 *owner);

/* Non-matching placeholders for the text-only asm slice asm/204660.s. */

void func_151D77C8(u8 *owner);
void *memcpy(void *dst, const void *src, unsigned int len);

extern void (*D_8008FCA4[])(u8 *, s32, u8);
extern f32 D_800AB2EC;
extern f32 D_800AB2F0;

s32 func_151D71B0() {
    return 0;
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_204660/func_151D7264.s")

void func_151D73A8(u8 *arg0, s32 arg1, u8 arg2) {
    void (* volatile *table)(u8 *, s32, u8) = D_8008FCA4;

    if (table[*(volatile u8 *)(arg0 + 0x2C)] != 0) {
        table[*(volatile u8 *)(arg0 + 0x2C)](arg0, arg1, arg2);
    }
}

void func_151D7404(u8 *arg0) {
    func_151D77C8(arg0);
}

s32 func_151D7424(s32 arg0) {
    func_151D7404(arg0);
    func_1514933C(arg0);
}

s32 func_151D7450(s32 arg0) {
    func_151D7404(arg0);
    func_15149368(arg0);
}

s32 func_151D747C(u8 *arg0) {
    struct { u8 *ptr; u8 value; } temp;

    temp.ptr = arg0;
    temp.value = *(u8 *)(arg0 + 0x3B);
    func_151494E0(&temp, 0x3D);
}

void func_151D74B0(u8 *arg0, u8 arg1, s8 arg2, u8 arg3, s32 arg4) {
    struct { u8 *word0; u8 byte0; u8 byte1; s8 byte2; } rec;
    s32 temp_v0;

    rec.word0 = arg0;
    rec.byte0 = arg0[0x3B];
    rec.byte1 = arg1;
    rec.byte2 = arg2;
    temp_v0 = func_151D71B0(0x12C, 0, 0, 0x41400000, 8, arg3, arg4);
    if (temp_v0 != 0) {
        memcpy((u8 *)(temp_v0 + 0x40), &rec, 8);
    }
}

void func_151D7538(volatile s32 arg0, s32 * volatile arg1, volatile u8 arg2) {
    u8 selector = arg2;
    s32 object = arg0;
    u8 *record = (u8 *)(object + 0x40);

    if (selector == 0x3D) {
        s32 true_object = arg0;
        s32 *word_value = arg1;
        u8 *byte_value = (u8 *)arg1;
        u8 *true_record = (u8 *)true_object;
        s32 stored_value = *(s32 *)(true_record + 0x40);

        true_record += 0x40;

        if (stored_value == *word_value || true_record[4] == byte_value[4]) {
            func_1516972C(arg0);
        }
    } else {
        func_15149514(arg1, arg2, record, record + 4, object);
    }
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_204660/func_151D75C4.s")

s32 func_151D7724(u8 *arg0) {
    u8 *temp_v0 = *(u8 **)(arg0 + 0x40);
    u8 *temp_v1 = arg0 + 0x28;

    if ((*(s32 *)(temp_v0 + 0x94) & 2) != 0 || *(u16 *)(temp_v0 + 0x84) == 4 ||
        *(u16 *)(temp_v0 + 0x84) == 0xA || *(u16 *)(temp_v0 + 0x84) == 0xC) {
        temp_v1[5] &= 0xFFFE;
    }
    return 1;
}

s32 func_151D7770(u8 *arg0) {
    u8 *temp_v0 = *(u8 **) (arg0 + 0x40);
    u8 *temp_v1 = arg0 + 0x28;

    if (*(u16 *) (temp_v0 + 0x84) == 0) {
        temp_v1[5] &= 0xFFFE;
    }
    return 1;
}

s32 func_151D779C(u8 *arg0) {
    u8 *temp_v0 = *(u8 **) (arg0 + 0x40);
    u8 *temp_v1 = arg0 + 0x28;

    if (temp_v0[0xAD] != 0) {
        temp_v1[5] &= 0xFFFE;
    }
    return 1;
}

void func_151D77C8(u8 *owner) {
    u8 **slot = (u8 **)(owner + 0x28);
    s32 *nested;

    if (*slot != NULL) {
        nested = *(s32 **)(*slot + 0x98);
        (*slot)[0x30] = 0;
        *(u16 *)(*slot + 0x1E) &= 0xFFFD;
        *(u16 *)(*slot + 0x1E) |= 8;
        *(u16 *)(*slot + 0x1E) |= 1;
        *(u16 *)(*slot + 0x1C) = 20;
        *nested = 0;
        *slot = NULL;
    }
}

void func_151D7830(u8 *owner) {
    u8 *record;
    AttachmentPayload151D7830 payload;
    AttachmentRequest151D7830 request;
    AttachmentPosition151D7830 *position;

    position = (AttachmentPosition151D7830 *)(owner + 0x30);
    payload.owner = owner;
    payload.position = *position;
    payload.velocity.x = 0.0f;
    payload.velocity.y = 0.0f;
    payload.velocity.z = 0.0f;
    request.count = 25;
    request.position = *position;
    request.duration = 300;
    request.flags = 0x76;
    request.kind = 0x12;
    request.mode = 4;
    request.value = 0;
    record = func_15147A80(&request, 0x20, sizeof(payload), 0xD, 0x10, 0x10, 0, 0, NULL, owner[0xC], owner[1]);
    if (record != NULL) {
        memcpy(*(void **)(record + 0x98), &payload, sizeof(payload));
        *(u8 **)(owner + 0x28) = record;
    }
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_204660/func_151D792C.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_204660/func_151D7A38.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_204660/func_151D7CD0.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_204660/func_151D80C4.s")

void func_151D8718(f32 *position, f32 *velocity, f32 delta) {
    f32 oldVelocity = *velocity;

    *velocity = oldVelocity + D_800AB2EC * delta;
    position[1] += oldVelocity * delta + D_800AB2F0 * (delta * delta);
}

void func_151D8764(u8 *arg0) {
    u8 *temp_v0 = *(u8 **)(arg0 + 0x98);
    u8 *temp_v1 = *(u8 **)temp_v0;

    if (temp_v1 != NULL) {
        *(s32 *)(temp_v1 + 0x28) = 0;
    }
}

s32 func_151D8780(s32 arg0) {
    func_151D8764(arg0);
    func_151478F4(arg0);
}

s32 func_151D87AC(s32 arg0) {
    func_151D8764(arg0);
    func_15147928(arg0);
}
