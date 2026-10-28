#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/C4DC0.s. */

typedef struct {
    u8 reserved0[2];
    u8 state;
    u8 reserved3[0x2D];
} SpawnLookupRecord;
extern SpawnLookupRecord *D_800D20FC;
s32 func_15083E0C(u8);
u8 *func_15083E90(u8);
s32 func_15082A44(SpawnLookupRecord *, s32, s32, s32, s32);

/* Ensure the selected object's record is active and return its tagged index. */
s32 func_15097910(s32 selector, u8 identity) {
    s32 index;
    u8 *actor;

    identity = selector;
    index = func_15083E0C(identity);
    if (index != -1) {
        actor = func_15083E90(identity);
        if (actor == NULL) {
            D_800D20FC[index].state = 0;
            if (func_15082A44(&D_800D20FC[index], index, 0, 0, 0) == 0) {
                return -1;
            }
            index = func_15083E0C(identity);
        } else {
            index = actor[0x13F];
        }
    }
    if (index != 0) {
        index |= 0x2000;
    }
    return index;
}

s32 func_150979CC() {
    return 0;
}

s32 func_15097A8C() {
    return 0;
}

s32 func_15099C14() {
    return 0;
}
