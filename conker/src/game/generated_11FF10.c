#include <ultra64.h>
typedef struct { f32 x, y, z; } BurstVector2D14;
typedef struct {
    u8 *owner;
    u8 ownerId, reserved05[3];
    f32 time, limit, multiplier, byteBase, decay;
    BurstVector2D14 vector1C, vector28;
} BurstPayload2D14;
typedef struct {
    u8 byte00, byte01;
    s16 half02, half04;
    u8 reserved06[2];
    u32 word08, word0C;
    u8 bytes10[4];
    f32 float14, float18;
    BurstVector2D14 position, vector28, scale;
    u32 word40;
    u8 byte44, byte45, byte46, byte47;
    u32 word48;
    u8 byte4C, reserved4D[3];
    u32 word50;
    s16 half54, half56;
} BurstDescriptorFields2D14;
typedef union { BurstDescriptorFields2D14 fields; u64 alignment; } BurstDescriptor2D14;
extern u8 D_800C35EA, D_800CC2D0[], D_800A4AA0[];
extern f32 D_800A195C[], D_800A1968, D_800A196C;
extern BurstVector2D14 D_800A5480;
void func_1502EA98(u8 *, u8, u8, u8, u8, s32, u8);
f32 func_150ADA68(void);
void func_15145EA4(BurstVector2D14 **, BurstVector2D14 **, u8 *, s32);
s32 func_15146078(BurstVector2D14 *, BurstVector2D14 *, BurstVector2D14 *);
u8 *func_1513D2F0(BurstDescriptor2D14 *, void *, u8, u8, u8, u8, u8,
                   s32, s32, s32, u8, s32);
typedef union {
    BurstVector2D14 *points[2];
    u8 *created;
    u64 alignment;
} BurstInputPair2D14;

extern f32 D_800A1950[];
extern f32 D_800BE9A4;
f32 sqrtf(f32);
void func_15143134(f32 *, f32 *, u8 *);

extern f32 D_800A1970;
extern s16 *D_800D9A40;

extern u8 *D_800DBFF0;
extern f32 D_800A1980;
extern f32 D_800A1984;

void *func_15149130(s16 arg0, s8 arg1, s8 arg2, s8 arg3, u8 arg4,
                    u8 arg5, s32 arg6, u8 arg7, s32 arg8);

typedef struct {
    u8 *owner;
    u8 owner_id;
    u8 state;
    u8 pad6[2];
    f32 value;
    u8 mode;
    u8 padD[3];
} Generated11FF10Payload;

/* Non-matching placeholders for the text-only asm slice asm/11FF10.s. */

s32 func_150F2A60() {
    return 0;
}

void func_150F2C8C(u8 *arg0) {
    Generated11FF10Payload payload;
    u8 *object;

    payload.owner = arg0;
    payload.owner_id = arg0[0x3B];
    payload.state = 0;
    payload.value = 0.0f;
    payload.mode = 0;

    object = func_15149130(0x12C, -1, 0x5C, -1, 0, 0x44,
                           sizeof(payload), 0xFF, 1);
    if (object != NULL) {
        memcpy(object + 0x28, &payload, sizeof(payload));
    }
}

/* Emit timed records while the linked owner and byte epoch remain valid. */
void func_150F2D14(u8 *actor) {
    Generated11FF10Payload *savedData;
    u8 *created;
    BurstDescriptor2D14 request;
    BurstPayload2D14 payload;
    u8 *owner;
    BurstInputPair2D14 inputs;
    BurstVector2D14 *outputs[2];
    BurstVector2D14 delta;

    savedData = (Generated11FF10Payload *)(actor + 0x28);
    if (D_800C35EA != 1) {
        owner = savedData->owner;
        if (*(s32 *)owner == 0 || savedData->owner_id != owner[0x3B]) {
            *(s16 *)(actor + 0xE) = -1;
            return;
        }
        if (savedData->state != owner[0x222] && owner[0x222] != 0) {
            savedData->mode = 3;
            savedData->value = 0.0f;
        }
        savedData->state = owner[0x222];
        if (owner[0x222] != 0) {
            func_1502EA98(D_800CC2D0 + owner[0x222] * 0x32C,
                           255, 0, 0, 0x50, 0, 15);
        }
        if (*(u8 **)(owner + 0x1D4) != NULL && (s8)savedData->mode > 0) {
            savedData->value += D_800A1968 * D_800BE9A4;
            if (savedData->value > 1.0f) {
                do {
                    payload.owner = owner;
                    payload.ownerId = owner[0x3B];
                    payload.time = 0.0f;
                    payload.limit = func_150ADA68() * 6.0f + 13.0f;
                    payload.multiplier = 58.14f;
                    payload.byteBase = func_150ADA68() * 40.0f + 60.0f;
                    payload.decay = payload.byteBase / (payload.limit * payload.limit);
                    inputs.points[0] = (BurstVector2D14 *)D_800A1950;
                    inputs.points[1] = (BurstVector2D14 *)D_800A195C;
                    outputs[0] = &request.fields.position;
                    outputs[1] = &delta;
                    func_15145EA4(inputs.points, outputs, *(u8 **)(owner + 0x1D4) + 0x3C0, 2);
                    delta.x -= request.fields.position.x;
                    delta.y -= request.fields.position.y;
                    delta.z -= request.fields.position.z;
                    if (func_15146078(&delta, &payload.vector1C, &payload.vector28) == 0) {
                        return;
                    }
                    request.fields.byte44 = (u32)payload.byteBase;
                    request.fields.byte00 = 0x79;
                    request.fields.byte01 = 0xC;
                    request.fields.half02 = 0x4405;
                    request.fields.half04 = 0x12C;
                    request.fields.word08 = 0;
                    request.fields.word0C = 0;
                    request.fields.bytes10[0] = 0xD5;
                    request.fields.bytes10[1] = 0xDB;
                    request.fields.bytes10[2] = 0xFF;
                    request.fields.bytes10[3] = 0xFF;
                    request.fields.float18 = 0.0f;
                    request.fields.float14 = 0.0f;
                    request.fields.vector28 = D_800A5480;
                    request.fields.scale.x = 1.0f;
                    request.fields.scale.y = 1.0f;
                    request.fields.scale.z = 1.0f;
                    request.fields.word40 = 0x04EC0000;
                    request.fields.byte45 = 0xFF;
                    request.fields.byte46 = 0;
                    request.fields.byte47 = 6;
                    request.fields.word48 = 0;
                    request.fields.byte4C = 0xFF;
                    request.fields.word50 = 0;
                    request.fields.half54 = 1;
                    request.fields.half56 = 0xFF;
                    created = func_1513D2F0(&request, D_800A4AA0, 0x26, 0, 0, 0x25,
                                            0, 0, 0, sizeof(payload), actor[0xC], actor[1]);
                    if (created != NULL) {
                        memcpy(created + 0x110, &payload, sizeof(payload));
                    }
                    savedData->mode = (s8)savedData->mode - 1;
                    savedData->value -= 1.0f;
                } while (savedData->value > 1.0f && (s8)savedData->mode > 0);
            }
        }
    }
}

void func_150F3194(u8 *arg0, s32 arg1, u8 arg2) {
    func_15169850(arg1, arg2, (s32) (arg0 + 0x28), (s32) (arg0 + 0x2C), (s32) arg0);
}

void func_150F31D4(u8 *arg0, s32 arg1, u8 arg2) {
    func_15169850(arg1, arg2, (s32) (arg0 + 0x110), (s32) (arg0 + 0x114), (s32) arg0);
}

/* Refresh a linked actor's position, scale, byte value, and timer. */
s32 func_150F3214(u8 *actor) {
    u8 *data;
    f32 scale;

    data = actor + 0x110;
    if (*(s32 *)(*(u8 **)(actor + 0x110)) == 0 ||
        data[4] != (*(u8 **)(actor + 0x110))[0x3B] ||
        *(u8 **)(*(u8 **)(actor + 0x110) + 0x1D4) == NULL) {
        return 0;
    }
    func_15143134(D_800A1950, (f32 *)(actor + 0x34),
                 *(u8 **)(*(u8 **)(actor + 0x110) + 0x1D4) + 0x3C0);
    scale = sqrtf(*(f32 *)(data + 8)) * *(f32 *)(data + 0x10);
    *(f32 *)(actor + 0x30) = scale;
    *(f32 *)(actor + 0x2C) = scale;
    actor[0x5C] = (u32)(*(f32 *)(data + 0x14) -
                        *(f32 *)(data + 0x18) * *(f32 *)(data + 8) * *(f32 *)(data + 8));
    *(f32 *)(data + 8) += D_800BE9A4;
    if (*(f32 *)(data + 0xC) < *(f32 *)(data + 8)) {
        return 0;
    }
    return 1;
}

void func_150F337C(u8 *arg0, s16 arg1) {
    func_15140410(arg0, arg0 + 0x12C, arg0 + 0x138, arg1);
}

// Matched with guarded set-bit temporary register normalization.
void func_150F33B0(u8 *arg0) {
    if (*(f32 *) (D_800DBFF0 + 0x300) < -2000.0f) {
        *(arg0 + 0x4F) &= 0xFFFE;
    } else {
        *(arg0 + 0x4F) |= 1;
    }
}

/* Update an indexed state-mask bit from two floating-point thresholds. */
void func_150F33F8(s32 index) {
    u8 *record = (u8 *)((s32)D_800DBFF0 + index * 0x9A0);

    if (*(f32 *)(record + 0x300) < D_800A1970) {
        if (*(f32 *)(record + 0x2FC) > 840.0f) {
            *D_800D9A40 |= 1 << index;
        } else {
            *D_800D9A40 &= ~(1 << index);
        }
    }
}

f32 func_150F34A0(u8 *arg0, f32 arg1) {
    f32 result;

    if (arg1 < -5.0f) {
        result = arg1 * D_800A1980 + D_800A1984;
    } else {
        result = 0.75f;
    }
    return result;
}

s32 func_150F34F4() {
    return 0;
}

s32 func_150F43F0() {
    return 0;
}
