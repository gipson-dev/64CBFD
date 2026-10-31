#include <ultra64.h>
#include "structs.h"
typedef struct { f32 x, y, z; } CommandVector;
typedef struct { CommandVector position; f32 value; } ActorCommandPayload;
typedef struct { u8 pad0[0x18]; CommandVector position; u8 pad24[0x18]; f32 value; void *owner; u8 flags; } ActorCommandState;
extern CommandVector D_800A5480;
void func_1516972C(struct102 *actor);


/* Non-matching placeholders for the text-only asm slice asm/FF0E0.s. */

s32 func_150D1C30() {
    return 0;
}

/* Apply a position payload, owner flag command, reset or actor release. */
void func_150D1F6C(struct260 *actor, s32 payloadAddress, u8 command) {
    void *payload = (void *)payloadAddress;
    ActorCommandState *state;
    state = (ActorCommandState *)((u8 *)actor + 0x28);
    if (command == 0x32) {
        state->position = ((ActorCommandPayload *)payload)->position;
        state->value = ((ActorCommandPayload *)payload)->value;
    } else if (command == 0x30 || command == 0x31) {
        if (payload == state->owner) {
            if (command == 0x30) {
                state->flags |= 1;
            } else {
                state->flags &= ~1;
            }
        }
    } else if (command == 0x4E) {
        *(CommandVector *)((u8 *)actor + 0x40) = D_800A5480;
    } else if (command == 0x4F) {
        func_1516972C((struct102 *)actor);
    }
}

void func_150D2054(void *arg0) {
    s32 base = (s32) arg0 + 0x28;
    s32 i = 0;

    do {
        void *entry = ((void **) base)[i + 9];

        if (entry != 0) {
            func_1516972C(entry);
        }
    } while ((i = (u8) (i + 1)) < 6);
}

s32 func_150D20B0(s32 arg0) {
    func_150D2054((void *) arg0);
    func_15149368(arg0);
}

s32 func_150D20DC(s32 arg0) {
    func_150D2054((void *) arg0);
    func_1514933C(arg0);
}
