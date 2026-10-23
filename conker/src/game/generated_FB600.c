#include <ultra64.h>
#include "structs.h"

typedef struct { u8 *owner; u8 identity; u8 opaque5[3]; } EmbeddedOwnerLink;
typedef struct { u8 *before; u8 *after; u8 before_identity; u8 after_identity; u8 opaqueA[2]; } OwnerLinkEvent;

void func_1516972C(struct102 *);

/* Non-matching placeholders for the text-only asm slice asm/FB600.s. */

s32 func_150CE150() {
    return 0;
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
