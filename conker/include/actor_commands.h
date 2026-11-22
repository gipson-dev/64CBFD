#ifndef ACTOR_COMMANDS_H
#define ACTOR_COMMANDS_H

#include <ultra64.h>

/* Four view-slot gates also share the retail aggregate zero/nonzero word. */
typedef union {
    u32 word;
    u8 bytes[4];
} ActorCommandGates;

extern ActorCommandGates D_800DBFF4;

#endif
