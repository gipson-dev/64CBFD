#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/6CCB0.s. */

typedef struct {
    u8 pad0[0x14];
    f32 x;
    u8 pad18[0x4];
    f32 z;
    u8 pad20[0x300];
    u8 query_data;
} QueryActor;

s32 func_1503F800() {
    return 0;
}

s32 func_1503F904(QueryActor *actor, s32 arg1, s32 arg2) {
    return func_1503F800(&actor->query_data, (s16)actor->x, (s16)actor->z, arg1, 1);
}

s32 func_1503F964() {
    return 0;
}
