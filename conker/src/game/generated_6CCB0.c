#include <ultra64.h>

#include "variables.h"

/* Recovered and remaining routines from the text-only asm slice asm/6CCB0.s. */

typedef struct {
    u8 pad0[0x14];
    f32 x;
    u8 pad18[0x4];
    f32 z;
    u8 pad20[0x300];
    u8 query_data;
} QueryActor;

extern u8 D_800C67F0;
extern u8 D_800C67F1;

s32 func_1503F800() {
    return 0;
}

s32 func_1503F904(QueryActor *actor, s32 arg1, s32 arg2) {
    return func_1503F800(&actor->query_data, (s16)actor->x, (s16)actor->z, arg1, 1);
}

void func_1503F964(void) {
    s32 start;
    s32 index;

    if (D_800C67F0 == 0) {
        return;
    }

    start = D_800C67F1;
    index = start + 1;
    if (index >= 25) {
        index = 0;
    }

    while (index != start) {
        if (D_800CC2D0[index].unkF8 & 0x00800000) {
            D_800C67F1 = index;
            return;
        }
        index++;
        if (index >= 25) {
            index = 0;
        }
    }
}
