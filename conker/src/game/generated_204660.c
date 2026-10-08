#include <ultra64.h>

typedef struct {
    f32 x, y, z;
} RingPosition151D792C;

extern f32 D_800BE9A4;
void func_151D8718(f32 *, f32 *, f32);

s32 func_151D792C(u8 *owner);

typedef struct {
    f32 x, y, z;
} SamplingPosition151D7A38;

typedef struct {
    u8 *actor;
    SamplingPosition151D7A38 position;
    f32 time;
    f32 progress;
} SamplingPayload151D7A38;


s32 func_151D7A38(u8 *owner);

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

extern f32 D_800AB2DC, D_800AB2E0, D_800AB2E4, D_800AB2E8;
f32 func_15143E64(f32 *vector);
f32 func_15144528(f32 value, f32 upper, f32 lower);

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

s32 func_151D792C(u8 *owner) {
    s32 state;
    u8 *records;
    s32 cursor;

    state = *(s8 *)(owner + 0x2C);
    records = *(u8 **)(owner + 0x94);
    if (state < 2 && (*(u16 *)(owner + 0x1E) & 8)) {
        return 0;
    }
    cursor = *(s8 *)(owner + 0x2E);
    while (cursor != *(s8 *)(owner + 0x2D)) {
        cursor--;
        if (cursor < 0) {
            cursor = owner[0x25] - 1;
        }
        func_151D8718((f32 *)(records + cursor * 0x1C),
                     (f32 *)(records + cursor * 0x1C + 0xC), D_800BE9A4);
    }
    if (*(s8 *)(owner + 0x2C) > 0) {
        RingPosition151D792C *position = (RingPosition151D792C *)(records + *(s8 *)(owner + 0x2D) * 0x1C);
        *(RingPosition151D792C *)(owner + 0x54) = *position;
    } else {
        *(f32 *)(owner + 0x54) = 0.0f;
        *(f32 *)(owner + 0x58) = 0.0f;
        *(f32 *)(owner + 0x5C) = 0.0f;
    }
    return 1;
}

s32 func_151D7A38(u8 *owner) {
    SamplingPayload151D7A38 *payload;
    u8 *records;
    SamplingPosition151D7A38 current;
    f32 xDelta;
    f32 yDelta;
    f32 zDelta;
    f32 fraction;
    f32 time;
    f32 timeStep;
    f32 xStep;
    f32 yStep;
    SamplingPosition151D7A38 point;
    f32 zStep;
    u8 *record;
    SamplingPosition151D7A38 *output;
    SamplingPosition151D7A38 *previous;

    payload = *(SamplingPayload151D7A38 **)(owner + 0x98);
    records = *(u8 **)(owner + 0x94);
    if ((payload->actor[0x2D] & 1) == 0) {
        return 0;
    }
    output = &point;
    current = *(SamplingPosition151D7A38 *)(payload->actor + 0x30);
    *(SamplingPosition151D7A38 *)(owner + 0x10) = current;
    payload->progress += 0.25f * D_800BE9A4;
    if (payload->progress > 1.0f) {
        fraction = 1.0f / payload->progress;
        previous = &payload->position;
        time = payload->time + D_800BE9A4;
        point = *previous;
        xDelta = current.x - previous->x;
        yDelta = current.y - previous->y;
        zDelta = current.z - previous->z;
        timeStep = time * fraction;
        xStep = xDelta * fraction;
        yStep = yDelta * fraction;
        zStep = zDelta * fraction;
        do {
            record = records + *(s8 *)(owner + 0x2E) * 0x1C;
            *(SamplingPosition151D7A38 *)record = *output;
            *(f32 *)(record + 0xC) = 0.0f;
            *(f32 *)(record + 0x10) = 0.0f;
            record[0x14] = 0;
            *(f32 *)(record + 0x18) = 0.0f;
            func_151D8718((f32 *)record, (f32 *)(record + 0xC), time);
            owner[0x2E] = *(s8 *)(owner + 0x2E) + 1;
            time -= timeStep;
            if (*(s8 *)(owner + 0x2E) == owner[0x25]) {
                owner[0x2E] = 0;
            }
            owner[0x2C] = *(s8 *)(owner + 0x2C) + 1;
            if (*(s8 *)(owner + 0x2D) == *(s8 *)(owner + 0x2E)) {
                owner[0x2D] = *(s8 *)(owner + 0x2D) + 1;
                if (*(s8 *)(owner + 0x2D) == owner[0x25]) {
                    owner[0x2D] = 0;
                }
                owner[0x2C] = *(s8 *)(owner + 0x2C) - 1;
            }
            point.x += xStep;
            point.y += yStep;
            point.z += zStep;
            payload->progress -= 1.0f;
        } while (payload->progress > 1.0f);
        *previous = point;
        payload->time = time;
    }
    return 1;
}

s32 func_151D7CD0(u8 *owner) {
    f32 *payload;
    u8 *records;
    f32 *previous;
    f32 total;
    f32 xTrim;
    f32 vector[3];
    f32 yTrim;
    f32 zTrim;
    f32 excess;
    f32 reciprocal;
    f32 length;
    f32 fraction;
    f32 start;
    f32 width;
    f32 inverse;

    payload = *(f32 **)(owner + 0x98);
    records = *(u8 **)(owner + 0x94);
    if (*(s8 *)(owner + 0x2C) >= 2) {
        s32 index;
        f32 *record;

        total = 0.0f;
        index = *(s8 *)(owner + 0x2E);
        if (*(u16 *)(owner + 0x1E) & 2) {
            previous = (f32 *)(owner + 0x10);
        } else {
            index--;
            if (index < 0) {
                index = owner[0x25] - 1;
            }
            previous = (f32 *)(records + index * 0x1C);
        }
        do {
            index--;
            if (index < 0) {
                index = owner[0x25] - 1;
            }
            record = (f32 *)(records + index * 0x1C);
            vector[0] = record[0] - previous[0];
            vector[1] = record[1] - previous[1];
            vector[2] = record[2] - previous[2];
            fraction = func_15143E64(vector);
            total += fraction;
            record[4] = fraction;
            if (total > 80.0f) {
                length = record[4];
                if (length) {
                    reciprocal = 1.0f / length;
                    excess = total - 80.0f;
                    fraction = excess * reciprocal;
                    xTrim = vector[0] * fraction;
                    record[0] -= xTrim;
                    yTrim = vector[1] * fraction;
                    record[1] -= yTrim;
                    zTrim = vector[2] * fraction;
                    record[2] -= zTrim;
                    record[4] = length * (1.0f - fraction);
                }
                total = 80.0f;
                while (index != *(s8 *)(owner + 0x2D)) {
                    owner[0x2D] = *(s8 *)(owner + 0x2D) + 1;
                    if (*(s8 *)(owner + 0x2D) == owner[0x25]) {
                        owner[0x2D] = 0;
                    }
                    owner[0x2C] = *(s8 *)(owner + 0x2C) - 1;
                }
            }
            previous = record;
        } while (index != *(s8 *)(owner + 0x2D));
    }
    if (*(s8 *)(owner + 0x2C) >= 2) {
        s32 index;
        f32 *record;
        f32 distance;

        payload[6] += -41.0f * D_800BE9A4;
        payload[6] = func_15144528(payload[6], D_800AB2DC, -16384.0f);
        distance = 0.0f;
        index = *(s8 *)(owner + 0x2E);
        do {
            index--;
            if (index < 0) {
                index = owner[0x25] - 1;
            }
            record = (f32 *)(records + index * 0x1C);
            distance += record[4];
            record[6] = func_15144528(payload[6] + distance * D_800AB2E0,
                D_800AB2E4, -16384.0f);
        } while (index != *(s8 *)(owner + 0x2D));
    }
    if (*(s8 *)(owner + 0x2C) >= 2) {
        s32 index;
        f32 *record;
        f32 distance;

        start = total * D_800AB2E8;
        width = total - start;
        inverse = 1.0f / width;
        distance = 0.0f;
        index = *(s8 *)(owner + 0x2E);
        do {
            index--;
            if (index < 0) {
                index = owner[0x25] - 1;
            }
            record = (f32 *)(records + index * 0x1C);
            if (start < distance) {
                fraction = distance - start;
                if (width < fraction) {
                    fraction = width;
                }
                ((u8 *)record)[0x14] = (u32)((width - fraction) * inverse * 60.0f);
                distance += record[4];
            } else {
                ((u8 *)record)[0x14] = 60;
                distance += record[4];
            }
        } while (index != *(s8 *)(owner + 0x2D));
    }
    return 1;
}

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
