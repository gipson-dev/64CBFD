#include <ultra64.h>
#include <string.h>
#include "structs.h"

typedef struct { u8 *owner; u8 identity; u8 opaque5[3]; } EmbeddedOwnerLink;
typedef struct { u8 *before; u8 *after; u8 before_identity; u8 after_identity; u8 opaqueA[2]; } OwnerLinkEvent;

void func_1516972C(struct102 *);

/* Non-matching placeholders for the text-only asm slice asm/FB600.s. */

typedef struct {
    u8 active, callback, flags, reserved3;
    s16 duration;
    u8 category, reserved7;
} OwnerPayloadHeaderFB600;

typedef struct {
    u8 *owner;
    u8 identity, reserved5[3];
    f32 first, second;
    s32 limit;
    u8 enabled, reserved15[0x8DB];
} LargeOwnerPayloadFB600;

extern f32 D_800A07FC;
void *func_1515FF74(void *, s32, u8, s32);

/* Allocate an owner-linked record and copy its partially initialized payload. */
void *func_150CE150(u8 *owner, s16 duration, u8 selector, s32 category) {
    OwnerPayloadHeaderFB600 header;
    LargeOwnerPayloadFB600 payload;
    void *record;

    if (owner == NULL) {
        return NULL;
    }
    header.active = 1;
    header.callback = 1;
    header.flags = 0;
    header.duration = duration;
    header.category = 2;
    payload.first = D_800A07FC;
    payload.second = D_800A07FC;
    payload.limit = 10000;
    payload.enabled = 0;
    payload.owner = owner;
    payload.identity = owner[0x3B];
    record = func_1515FF74(&header, sizeof(payload), selector, category);
    if (record != NULL) {
        record = memcpy((u8 *)record + 0x18, &payload, sizeof(payload));
    }
    return record;
}

s32 func_150CE200() {
    return 0;
}

s32 func_150CE450() {
    return 0;
}

/* Retarget an embedded owner reference or release a matching reference. */
void func_150CE694(u8 *owner, s32 eventAddress, u8 command) {
    EmbeddedOwnerLink *link = (EmbeddedOwnerLink *)(owner + 0x18);
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

#pragma GLOBAL_ASM("asm/nonmatchings/game_FB600/func_150CE740.s")
