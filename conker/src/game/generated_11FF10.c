#include <ultra64.h>
typedef struct {
    s32 active;
    u8 kind, reserved05[0x13];
    f32 positionY;
    u8 reserved1C[4];
    f32 verticalVelocity, acceleration, depth;
    u8 reserved2C[0x10];
    f32 speed, facingAngle, targetSpeed;
    u8 reserved48[0x2E];
    u16 heading, desiredHeading;
    s16 yaw;
    u8 reserved7C[2], turnStep, reserved7F, flag80, reserved81[2], flag83;
    u8 reserved84[2], flag86, reserved87[0x24], flagAB, reservedAC, flagAD;
    u8 reservedAE[0xA];
    f32 valueB8;
    u8 reservedBC[4];
    f32 valueC0, valueC4;
    u8 reservedC8[0x30];
    u32 flags;
    u8 reservedFC[6], mode, cooldown, disabled, reserved105[0x13];
    f32 thresholdY;
    u8 reserved11C[0x20], held, heldBy, reserved13E[0x8C], eligible, reserved1CB;
    f32 previousY;
    u8 reserved1D0[0x48];
    u32 state;
    u8 reserved21C[6], nearest, reserved223[0xF], animation, reserved233[0x29];
    u32 controlFlags;
    u8 reserved260[0xCC];
} MovementActor34F4;
typedef struct { u16 buttons; s8 x, y; } MovementInput34F4;
extern u16 D_800BE710;
extern MovementInput34F4 **D_800BE728, *D_800CC284;
extern s32 D_800CC288, D_80082FA0, D_800CC280, D_800BE9F0;
extern u8 D_800C3E78, D_800DDE3C[], D_800E0B94, D_800CC26D, D_800CBDD3;
extern u8 D_800CC2D0[];
extern u8 D_800CC5FC[], D_800D121C[];
extern f32 D_800DDDC8[], D_800D1550;
extern u32 D_800D1580;
extern MovementActor34F4 *D_800D154C;
extern f32 D_800A1988, D_800A198C, D_800A1990, D_800A1994, D_800A1998;
extern f32 D_800A199C, D_800A19A0, D_800A19A4, D_800A19A8, D_800A19AC;
extern f32 D_800A19B0, D_800A19B4, D_800A19B8, D_800A19BC, D_800A19C0;
extern f32 D_800A19C4, D_800A19C8, D_800A19CC, D_800A19D0, D_800A19D4;
void func_150585F0(MovementActor34F4 *, f32);
void func_15059140(MovementActor34F4 *);
u16 func_1505A630(f32, f32, s32);
f32 func_1505A5CC(MovementInput34F4 *);
void func_15052590(MovementActor34F4 *);
void func_1506E8D8(void);
void func_1506E5FC(void);
void func_1505959C(MovementActor34F4 *, s32);
f32 func_1505A6F8(MovementActor34F4 *, MovementActor34F4 *);
u8 func_150599C8(MovementActor34F4 *, u8, u16);
f32 func_1505A3A8(f32, MovementActor34F4 *, f32, f32, u8);
s32 func_15073FA0(void);
void func_1505E650(MovementActor34F4 *, u16, f32, f32, f32, f32, s32);
f32 func_150F34A0(u8 *, f32);
f32 fabsf(f32);
#pragma intrinsic (fabsf)

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

/* Update controller-driven movement, linked records, and animation state. */
void func_150F34F4(MovementActor34F4 *actor) {
    u16 angle;
    f32 amount;
    f32 rate;
    f32 magnitude;
    f32 input;
    f32 speed;
    f32 acceleration;
    f32 velocity;
    f32 value;
    f32 contactHeight;
    f32 initialMagnitude;
    s32 index;
    f32 nearestDistance;
    f32 distance;
    f32 previousInput;
    f32 pitchValue;
    s32 count;
    s32 animation;
    MovementActor34F4 *record;
    s32 heldIndex;
    u32 buttons;

    contactHeight = 0.0f;
    actor->flagAB = 1;
    actor->flag80 = 1;
    actor->nearest = 0;
    D_800CC288 = D_800BE710;
    D_800CC284 = *D_800BE728;
    if (D_80082FA0 >= D_800C3E78 && D_800DDE3C[D_800C3E78] != 0 &&
        D_800DDDC8[D_800C3E78] > 0.75f && D_800E0B94 != 2) {
        D_800CC284->x = 0;
        D_800CC284->y = 0;
        D_800CC284->buttons = 0;
        D_800CC288 = 0;
    }
    actor->flags |= 0x40;
    actor->previousY = actor->positionY;
    if (actor->cooldown != 0) {
        actor->cooldown--;
    }
    if (actor->disabled != 0) {
        func_150585F0(actor, 0.25f);
        func_15059140(actor);
        actor->facingAngle = (f32)(actor->yaw + 0x4000) * 0.005493164f;
        if (actor->held == 0) {
            goto disabled_done;
        }
        heldIndex = actor->held - 100;
        record = (MovementActor34F4 *)D_800CC2D0 + heldIndex;
        record->heldBy = 0;
        record->speed = actor->speed;
        record->animation = 0x21;
        record->state = 0;
        record->disabled = 0;
        record->flags &= ~0x400;
        actor->held = 0;
disabled_done:
        return;
    } else if (actor->mode == 0) {
        actor->flagAD = 0;
        angle = func_1505A630((f32)D_800CC284->x, (f32)D_800CC284->y, 0);
        initialMagnitude = func_1505A5CC(D_800CC284);
        if (D_800CC284->buttons & 0x10) {
            initialMagnitude = 0.0f;
        }
        angle = (u16)((u32)angle + (u32)D_800CC280);
        actor->desiredHeading = *(u16 *)&actor->yaw;
        if (initialMagnitude > 1.0f) {
            actor->desiredHeading = angle;
        }
        actor->targetSpeed = initialMagnitude * D_800A1988;
        actor->animation = 7;
        actor->state = 0;
        if ((D_800CC288 & 0xC000) || actor->depth > 100.0f) {
            actor->animation = 8;
            actor->mode = 1;
        }
        func_15052590(actor);
        if (D_800CC26D != 0) {
            if (actor->depth > 30.0f) {
                D_800D1580 = 0xFF010074;
                func_1506E8D8();
                func_1505959C((MovementActor34F4 *)(D_800CC2D0 +
                                  D_800CC26D * 0x32C - 100 * 0x32C),
                               D_800C3E78);
                actor->held = D_800CC26D;
                actor->mode = 1;
            }
            actor->verticalVelocity = 23.0f;
        }
        if (actor->positionY < actor->thresholdY) {
            actor->mode = 1;
            actor->flag86 = 1;
            actor->verticalVelocity = -6.0f;
        }
    } else {
        speed = actor->speed;
        if (speed > 60.0f) {
            speed = 60.0f;
        }
        input = (f32)D_800CC284->y * 1.25f;
        if (D_800CC284->buttons & 0x10) {
            input = 0.0f;
        }
        if (actor->held != 0) {
            if (!(D_800CC284->buttons & 0x10)) {
                actor->positionY -= 16.0f * D_800D1550;
            }
        } else {
            distance = 1000.0f;
            record = (MovementActor34F4 *)D_800CC2D0;
            index = 0;
            do {
                if (record->active != 0 && record->eligible != 0 &&
                    record->depth == 0.0f && record->animation != 0x21 &&
                    (record->kind == 0x9C || record->kind == 0x9D)) {
                    nearestDistance = func_1505A6F8(D_800D154C, record);
                    if (nearestDistance < distance) {
                        actor->nearest = index;
                        distance = nearestDistance;
                    }
                }
                index++;
                record++;
            } while (index != 25);
        }
        if (input < -90.0f) {
            input = -90.0f;
        }
        if (input > 90.0f) {
            input = 90.0f;
        }
        if (D_800A198C < actor->positionY) {
            if (-30.0f < (velocity = actor->verticalVelocity)) {
                actor->verticalVelocity = velocity - 1.5f;
            }
            input = 40.0f;
        }
        magnitude = (f32)D_800CC284->x;
        previousInput = actor->valueC4;
        actor->valueC4 += ((magnitude - previousInput) *
                                  (D_800A1990 * D_800D1550));
        actor->heading = (u32)actor->heading - (u32)(s32)(actor->valueC4 * D_800D1550 *
                  D_800A1994 * ((100.0f - speed) * D_800A1998) * 220.0f);
        actor->turnStep = 25;
        func_150599C8(actor, 8, actor->heading);
        actor->valueC0 = 0.0f;
        speed = 0.0f;
        rate = D_800A199C;
        if (actor->positionY < actor->thresholdY) {
            if (actor->flag86 == 0) {
                actor->flag86 = 1;
                actor->speed = 0.0f;
                actor->verticalVelocity = -6.0f;
            }
        } else if (actor->flag86 != 0) {
            actor->flag86 = 0;
            actor->verticalVelocity = 9.0f;
        }
        buttons = D_800CC284->buttons;
        if (!(buttons & 0x10)) {
            if (buttons & 0x8000) {
                actor->valueC0 = -22.0f;
                speed = 1.0f;
                rate = D_800A19A0;
                buttons = D_800CC284->buttons;
            }
            if (buttons & 0x4000) {
                velocity = actor->verticalVelocity;
                actor->valueC0 = 30.0f;
                if (velocity < 0.0f) {
                    actor->valueC0 -= velocity * D_800A19A4;
                }
                speed = 1.5f;
                rate = D_800A19A8;
            }
        }
        func_1505A3A8(actor->valueC0, actor, speed, rate, 1);
        actor->facingAngle = (f32)(actor->yaw + 0x4000) * 0.005493164f;
        actor->acceleration = input * D_800A19AC * (200.0f - actor->speed);
        if (actor->held == 0) {
            if ((velocity = actor->verticalVelocity) > 26.0f) {
                actor->verticalVelocity = 26.0f;
            }
            if ((velocity = actor->verticalVelocity) < -34.0f) {
                actor->verticalVelocity = -34.0f;
            }
        }
        magnitude = fabsf(input * 0.5f);
        if (actor->flag86 != 0) {
            magnitude *= D_800A19B0;
            actor->acceleration *= D_800A19B4;
        }
        acceleration = actor->acceleration;
        velocity = actor->verticalVelocity;
        if (contactHeight == acceleration) {
            if (fabsf(velocity) < 1.5f) {
                actor->verticalVelocity = 0.0f;
            } else if (velocity > 0.0f) {
                actor->acceleration = D_800A19B8;
            } else {
                actor->acceleration = D_800A19BC;
            }
        } else {
            if (magnitude * D_800A19C0 < velocity && acceleration < 0.0f) {
                actor->acceleration = 0.0f;
            } else if (velocity < -magnitude * 1.5f && acceleration > 0.0f) {
                actor->acceleration = 0.0f;
            }
        }
        actor->flagAD = 10;
        if (D_800CC284->buttons & 0x10) {
            index = D_800CC284->y;
            value = actor->valueB8;
            actor->valueB8 += (((f32)index - value) * D_800A19C4);
            actor->verticalVelocity = 0.0f;
            actor->acceleration = 0.0f;
        } else {
            pitchValue = (actor->verticalVelocity - contactHeight) * -2.0f;
            actor->valueB8 = pitchValue;
            if (pitchValue > 40.0f) {
                actor->valueB8 = 40.0f;
            } else if (actor->valueB8 < -55.0f) {
                actor->valueB8 = -55.0f;
            }
        }
        speed = actor->verticalVelocity;
        D_800CBDD3 = 1;
        func_15059140(actor);
        D_800CBDD3 = 0;
        if (actor->held != 0 && actor->depth < 50.0f) {
            contactHeight = 50.0f;
        }
        if (!(D_800CC284->buttons & 0x10)) {
            if (D_800CC26D != 0 && actor->held == 0) {
                if (((MovementActor34F4 *)D_800CC2D0)[D_800CC26D - 100].depth == 0.0f) {
                    actor->positionY = ((MovementActor34F4 *)D_800CC2D0)[D_800CC26D - 100].positionY + 70.0f;
                    actor->verticalVelocity = 20.0f;
                    func_1505959C((MovementActor34F4 *)(D_800CC2D0 +
                                      D_800CC26D * 0x32C - 100 * 0x32C),
                                   D_800C3E78);
                    actor->held = D_800CC26D;
                    D_800D1580 = 0xFF010074;
                    func_1506E8D8();
                }
            }
            if (actor->held != 0) {
                if (actor->controlFlags & 2) {
                    s32 releaseIndex = actor->held - 100;
                    actor->controlFlags &= ~2;
                    record = (MovementActor34F4 *)(D_800CC2D0 + releaseIndex * 0x32C);
                    record->heldBy = 0;
                    record->speed = actor->speed;
                    record->animation = 0x21;
                    record->state = 0;
                    record->disabled = 0;
                    record->flags &= ~0x400;
                    actor->held = 0;
                    actor->verticalVelocity = 0.0f;
                    D_800D1580 = 0x76;
                    func_1506E8D8();
                }
            } else if ((D_800CC288 & 0x2000) && actor->cooldown == 0) {
                MovementActor34F4 *countRecord;
                count = 0;
                if (D_800BE9F0 == 0x3C) {
                    countRecord = (MovementActor34F4 *)D_800CC5FC;
                    do {
                        if (countRecord->active != 0 && countRecord->kind == 0x25) {
                            count++;
                        }
                        countRecord++;
                    } while ((u8 *)countRecord != D_800D121C);
                    if (count < 5) {
                        D_800D1580 = 6;
                        actor->cooldown = 4;
                        func_15073FA0();
                    }
                }
            }
        }
        if (actor->depth <= contactHeight) {
            actor->speed *= D_800A19C8;
            if ((D_800CC284->buttons & 0x4000) || actor->flag86 != 0 ||
                actor->held != 0) {
                if (actor->held != 0) {
                    if (actor->verticalVelocity < -10.0f) {
                        D_800D1580 = 0xFF0100A7;
                        func_1506E5FC();
                        D_800D1580 = 0xFF060372;
                        func_1506E8D8();
                    }
                } else if (actor->positionY < 0.0f) {
                    D_800D1580 = 0xFF010072;
                    func_1506E8D8();
                }
                if (actor->held == 0) {
                    actor->verticalVelocity = 20.0f;
                } else if (actor->flag86 == 0) {
                    actor->verticalVelocity = 38.0f;
                }
                input = -80.0f;
            } else {
                actor->verticalVelocity = speed * -1.0f;
                actor->mode = 0;
                actor->depth = D_800A19CC;
                actor->valueB8 = 0.0f;
            }
        }
        if (!(D_800CC284->buttons & 0x10)) {
            actor->valueB8 += 20.0f;
        } else {
            actor->verticalVelocity = actor->valueB8 * D_800A19D0;
        }
        if (actor->flag86 != 0) {
            actor->flag83 = 0;
            if (fabsf(input) > 8.0f || actor->valueC0 > 7.0f) {
                amount = 1.0f;
            } else {
                amount = 0.5f;
            }
        } else {
            amount = func_150F34A0((u8 *)actor, input);
        }
        animation = 0xF;
        if (actor->valueB8 > 40.0f && input > 20.0f) {
            animation = 0x11;
        }
        if ((value = actor->speed) < 20.0f && actor->valueC0 <= 0.0f && input == 0.0f) {
            animation = 0x18;
        }
        if (value < 0) {
            animation = 0x1F;
        }
        if (actor->held != 0) {
            animation = 0x17;
            amount += D_800A19D4;
        }
        func_1505E650(actor, (u16)animation, amount, 9.0f, 0.0f, 0.0f, 0);
    }
}

s32 func_150F43F0() {
    return 0;
}
