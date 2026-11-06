#include <ultra64.h>
#include "structs.h"

/* Recovered routines and remaining placeholders for asm/68C70.s. */

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

extern u16 D_8009877C, D_8009877E;
extern u16 D_80098780[88], D_80098830[3], D_80098836[];
/* Set the ID-classification flag for objects in interaction state one. */
void func_1503B840(struct127 *object) {
    u16 *cursor;
    u16 *end;
    u32 identity;
    s32 index;

    if (object->interaction_state != 1) {
        return;
    }
    end = D_80098836;
    identity = object->unk84.uh;
    cursor = D_80098830;
    do {
        if (identity == *cursor++) {
            object->unk2FB |= 2;
            return;
        }
    } while ((u32)cursor < (u32)end);
    if (identity == D_8009877C) {
        object->unk2FB |= 1;
        return;
    }
    if (identity == D_8009877E) {
        object->unk2FB |= 1;
        return;
    }
    for (index = 0; index < 88; index++) {
        if (identity == D_80098780[index]) {
            object->unk2FB |= 1;
            return;
        }
    }
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
