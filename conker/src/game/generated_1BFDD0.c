#include <ultra64.h>
#include "structs.h"
void func_1516972C(struct102 *);

typedef struct { u8 *owner; u8 identity; u8 opaque5[3]; } EmbeddedOwnerLink;
typedef struct { u8 *before; u8 *after; u8 before_identity; u8 after_identity; u8 opaqueA[2]; } OwnerLinkEvent;

/* Partially recovered text-only slice asm/1BFDD0.s. */

void *func_151491F4(s16 arg0, s8 arg1, s8 arg2, u8 arg3, u8 arg4, s32 arg5, u8 arg6, s32 arg7);

typedef struct {
    void *owner;
    u8 selector;
    u8 pad5[3];
    f32 value;
} Generated1BFDD0Payload;

void func_15192920(u8 * volatile arg0) {
    u8 *record;
    Generated1BFDD0Payload payload;

    if (arg0 != NULL) {
        payload.owner = arg0;
        payload.selector = ((u8 *)payload.owner)[0x3B];
        payload.value = 0.0f;
        record = func_151491F4(0x23, -1, 0x14, 1, 0x10, 0xC, 0xFF, 1);
        if (record != NULL) {
            memcpy(record + 0x28, &payload, sizeof(payload));
        }
    }
}

s32 func_151929A4() {
    return 0;
}

/* Allocate an owner/selector payload record with the requested lifetime. */
void *func_15192D48(u8 * volatile owner, s16 volatile lifetime,
                   u8 volatile selector, s32 volatile parameter) {
    u8 *record;
    Generated1BFDD0Payload payload;

    if (owner == NULL) {
        return NULL;
    }
    payload.owner = owner;
    payload.selector = ((u8 *)payload.owner)[0x3B];
    payload.value = 0.0f;
    record = func_151491F4(lifetime, -1, 0x18, 1, 0x16, 0xC, selector, parameter);
    if (record != NULL) {
        memcpy(record + 0x28, &payload, sizeof(payload));
    }
    return record;
}

s32 func_15192DF0() {
    return 0;
}

/* Retarget the payload owner link or release its matching actor. */
void func_15193234(struct260 *owner, s32 eventAddress, u8 command) {
    EmbeddedOwnerLink *link = (EmbeddedOwnerLink *)((u8 *)owner + 0x28);
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

s32 func_151932E0() {
    return 0;
}
