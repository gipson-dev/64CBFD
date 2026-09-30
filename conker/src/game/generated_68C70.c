#include <ultra64.h>
#include "structs.h"

/* Non-matching placeholders for the text-only asm slice asm/68C70.s. */

extern u8 D_800CC5CB[];
extern void *allocate_memory(s32 size, s32 arg1, s32 arg2, s32 arg3);
extern s32 func_150ADA20(void);

typedef struct {
    u8 pad0[0x44];
    f32 unk44;
    u8 pad48[4];
    u16 unk4C;
    u8 pad4E[2];
} struct_1503B7C0;

void func_1503B7C0(struct127 *object) {
    object->unk31C->unk11C = allocate_memory(0x50, 1, 0, 0);
    bzero(object->unk31C->unk11C, 0x50);
    ((struct_1503B7C0 *)object->unk31C->unk11C)->unk44 = 30.0f;
    ((struct_1503B7C0 *)object->unk31C->unk11C)->unk4C =
        func_150ADA20() % 30U;
}

s32 func_1503B840() {
    return 0;
}

s32 func_1503B95C(s32 arg0, u8 *arg1) {
    s32 flags = D_800CC5CB[arg0 * 0x32C];

    if (flags & 2) {
        arg1[0x4E] = 0;
        return 0;
    }
    if (flags & 1) {
        return 0;
    }
    return 1;
}

s32 func_1503B9BC() {
    return 0;
}

s32 func_1503CB98() {
    return 0;
}
