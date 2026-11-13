#include <ultra64.h>
#include "structs.h"

typedef struct {
    s32 kind;
    s32 variant;
    u8 reserved08[0xC];
    f32 value14;
    f32 value18;
    f32 value1C;
    f32 value20;
    f32 value24;
    f32 value28;
    s32 selector2C;
    s32 selector30;
    f32 value34;
    f32 value38;
    f32 value3C;
    f32 value40;
    s16 value44;
    s16 value46;
    s16 value48;
    s16 value4A;
    s16 value4C;
    s16 value4E;
    s8 mode;
} EffectPreset150D64E8;

extern f32 D_800A0AB8;
extern f32 D_800A0ABC;
extern f32 D_800A0AC0;
extern f32 D_800A0AC4;
extern f32 D_800A0AC8;
extern s32 D_80082FA0;
extern s8 D_8008FD8C;

typedef struct { u8 *owner; u8 identity; u8 opaque5[3]; } EmbeddedOwnerLink;
typedef struct { u8 *before; u8 *after; u8 before_identity; u8 after_identity; u8 opaqueA[2]; } OwnerLinkEvent;

void func_1516972C(struct102 *);

/* Non-matching placeholders for the text-only asm slice asm/1028F0.s. */

void *func_15149130(s16 arg0, s8 arg1, s8 arg2, s8 arg3, u8 arg4,
                    u8 arg5, s32 arg6, u8 arg7, s32 arg8);

typedef struct {
    u8 *owner;
    u8 owner_id;
    u8 pad5[3];
    f32 value;
} OwnerPayload;

void func_150D5440(u8 *arg0, u8 arg1, s32 arg2) {
    OwnerPayload payload;
    u8 *object;

    payload.owner = arg0;
    payload.owner_id = arg0[0x3B];
    payload.value = 0.0f;

    object = func_15149130(0x12C, -1, 0x38, -1, 0, 0x28,
                           sizeof(payload), arg1, arg2);
    if (object != NULL) {
        memcpy(object + 0x28, &payload, sizeof(payload));
    }
}

s32 func_150D54C8() {
    return 0;
}

/* Release matching owner links for 0/3/0x2F, or retarget them for 0x2D. */
void func_150D596C(struct260 *owner, s32 eventAddress, u8 command) {
    EmbeddedOwnerLink *link = (EmbeddedOwnerLink *)((u8 *)owner + 0x28);
    OwnerLinkEvent *event = (OwnerLinkEvent *)eventAddress;

    if (command == 0 || command == 0x2F || command == 3) {
        u8 *first = event->before;
        /* Retail compares byte +4: the second pointer overlaps this identity. */
        if (first == link->owner || link->identity == ((u8 *)event)[4]) {
            func_1516972C((struct102 *)owner);
        }
    } else if (command == 0x2D) {
        u8 *current = link->owner;
        if (current == event->before) {
            link->owner = event->after;
            /* Read the identity after the pointer store; packet/link may overlap. */
            link->identity = event->after_identity;
        } else if (current == event->after) {
            link->owner = event->before;
            link->identity = event->before_identity;
        }
    }
}

void func_150D5A2C(u8 *arg0) {
    func_1514933C(arg0);
}

void func_150D5A4C(u8 *arg0) {
    func_15149368(arg0);
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1028F0/func_150D5A6C.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1028F0/func_150D6388.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1028F0/func_150D6434.s")

/* Initialize the fixed effect descriptor and its auxiliary scalar. */
void func_150D64E8(EffectPreset150D64E8 *preset, f32 *auxiliary) {
    preset->kind = 6;
    preset->variant = 3;
    *auxiliary = D_800A0AB8;
    preset->value14 = D_800A0ABC;
    preset->value18 = D_800A0AC0;
    preset->value1C = 150.0f;
    preset->value20 = 105.0f;
    preset->value24 = 396.0f;
    preset->value28 = 612.0f;
    preset->selector2C = 4;
    preset->selector30 = 3;
    preset->value34 = 25.0f;
    preset->value38 = D_800A0AC4;
    preset->value3C = -2.0f;
    preset->value40 = D_800A0AC8;
    preset->value44 = 20;
    preset->value46 = 30;
    preset->value48 = 100;
    preset->value4A = 100;
    preset->value4C = 12;
    preset->value4E = 20;
    if ((D_80082FA0 >= 2) || (D_8008FD8C >= 8)) {
        preset->mode = -1;
    } else {
        preset->mode = 0;
    }
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1028F0/func_150D65F0.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1028F0/func_150D66A4.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1028F0/func_150D6730.s")

void func_150D6C98(f32 *arg0, f32 *arg1) {
    arg1[0] = arg0[5];
    arg1[1] = arg0[6] + 60.0f;
    arg1[2] = arg0[7];
}

s32 func_150D6CC4() {
    return 0;
}

/* Retarget an embedded owner reference or release a matching reference. */
void func_150D6E60(u8 *owner, s32 eventAddress, u8 command) {
    EmbeddedOwnerLink *link = (EmbeddedOwnerLink *)(owner + 0xA8);
    OwnerLinkEvent *event = (OwnerLinkEvent *)eventAddress;

    if (command == 0x2D) {
        u8 *current = link->owner;
        if (current == event->before) {
            link->owner = event->after;
            link->identity = event->after_identity;
        } else if (current == event->after) {
            link->owner = event->before;
            link->identity = event->before_identity;
        }
    } else if (command == 0) {
        u8 *first = event->before;
        if (first == link->owner || link->identity == ((u8 *)event)[4]) {
            func_1516972C((struct102 *)owner);
        }
    }
}

extern f32 D_800BE9A4;
f32 sqrtf(f32);
typedef struct {
    u8 *target;
    u8 identity;
    u8 pad05[3];
    f32 elapsed;
    f32 limit;
    f32 scale;
    f32 alpha;
    f32 decay;
} Motion150D6F0C;

/* Update the linked owner's position, scale, alpha and elapsed time. */
s32 func_150D6F0C(u8 *owner, void *context) {
    Motion150D6F0C *link = (Motion150D6F0C *)(owner + 0xA8);
    u8 *target = link->target;
    f32 size;
    f32 time;

    if (*(s32 *)target == 0 || link->identity != target[0x3B]) {
        return 0;
    }
    func_150D6C98((f32 *)target, (f32 *)(owner + 0x40));
    size = sqrtf(link->elapsed) * link->scale;
    *(f32 *)(owner + 0x3C) = size;
    *(f32 *)(owner + 0x38) = size;
    time = link->elapsed;
    owner[0x2B] = (u32)(link->alpha - (link->decay * time * time));
    link->elapsed += D_800BE9A4;
    if (link->limit < link->elapsed) {
        return 0;
    }
    return 1;
}

/* Retarget the embedded owner reference, or release the owner for a matching event. */
void func_150D7068(u8 *owner, s32 eventAddress, u8 command) {
    EmbeddedOwnerLink *link = (EmbeddedOwnerLink *)(owner + 0xA8);
    u8 *event = (u8 *)eventAddress;
    s32 code = command;

    if (command == 0x2D) {
        u8 *current = link->owner;
        u8 *first = *(u8 **)event;
        if (first == current) {
            link->owner = *(u8 **)(event + 4);
            link->identity = event[9];
        } else if (*(u8 **)(event + 4) == current) {
            link->owner = first;
            link->identity = event[8];
        }
    } else if (code == 0) {
        if (*(u8 **)event == link->owner || link->identity == event[4]) {
            func_1516972C((struct102 *)owner);
        }
    }
}
