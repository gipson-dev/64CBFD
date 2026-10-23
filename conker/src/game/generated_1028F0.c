#include <ultra64.h>
#include "structs.h"

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

s32 func_150D596C() {
    return 0;
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

s32 func_150D64E8() {
    return 0;
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

s32 func_150D6F0C() {
    return 0;
}

s32 func_150D7068() {
    return 0;
}
