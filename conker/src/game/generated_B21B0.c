#include <ultra64.h>
#include "structs.h"

extern struct127 D_800CC2D0[26];
extern u8 D_800D18A8;


/* Non-matching placeholders for the text-only asm slice asm/B21B0.s. */

typedef struct {
    u8 pad[0x11B];
    u8 value;
} GeneratedB21B0Target;

typedef struct {
    u8 pad[0x31C];
    GeneratedB21B0Target *target;
} GeneratedB21B0Owner;

extern u8 D_8009D954[];
extern u8 *D_80087240[];

s32 func_15084D00(u8 *arg0) {
    s32 value = arg0[4];
    s32 group;
    s32 i;

    for (group = 0; group < 7; group++) {
        for (i = 0; i < D_8009D954[group]; i++) {
            if (value == D_80087240[group][i]) {
                return D_80087240[group][0];
            }
        }
    }

    return value;
}

s32 func_15084D70() {
    return 0;
}

void func_15085410(GeneratedB21B0Owner *arg0, s32 arg1) {
    arg0->target->value = arg1;
}

u8 func_15085420(GeneratedB21B0Owner *arg0) {
    return arg0->target->value;
}

s32 func_15085430() {
    return 0;
}

s32 func_15085710() {
    return 0;
}

s32 func_150859AC() {
    return 0;
}

/* Publish each selected player's current health to its status record. */
void func_15085ABC(s16 mask) {
    s32 slot;

    if (!D_800D18A8) {
        for (slot = 0; slot < 4; slot++) {
            if ((1 << slot) & mask) {
                func_15085710((s16)slot, 5, D_800CC2D0[slot].health);
            }
        }
    }
}
