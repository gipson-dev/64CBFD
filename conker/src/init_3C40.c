#include <ultra64.h>

#include "functions.h"
#include "variables.h"

s32 allocate_memory(s32 arg0, s32 arg1, s32 arg2, s32 arg3) {
    return func_10003C6C(arg0, arg1, arg2, 0, arg3);
}

/* Non-matching C placeholders for asm/nonmatchings/init_3C40/func_10003C6C.s. */
s32 func_10003C6C(s32 arg0, s32 arg1, s32 arg2, s32 arg3, s32 arg4) {
    return 0;
}
void func_10004074(void *arg0) {
    struct54 *block;
    struct54 *freeBlock;
    struct54 *next;
    struct54 *nextFree;
    struct54 *previous;
    OSIntMask mask;
    s32 merged;

    if (arg0 == NULL) {
        return;
    }

    block = (struct54 *)((u8 *)arg0 - 0xC);
    freeBlock = block;
    merged = 0;
    mask = osSetIntMask(1);
    *((u8 *)block + 8) = 0;

    previous = block->unk4;
    if ((previous != NULL) && ((previous->unk8 >> 24) == 0)) {
        next = block->unk0;
        previous->unk0 = next;
        previous->unk8 += block->unk8 + 0xC;
        if (next != NULL) {
            next->unk4 = previous;
        }
        freeBlock = previous;
        merged = 1;
    }

    next = freeBlock->unk0;
    if ((next != NULL) && ((next->unk8 >> 24) == 0)) {
        previous = next->unk0;
        freeBlock->unk0 = previous;
        freeBlock->unk8 += next->unk8 + 0xC;
        if (previous != NULL) {
            previous->unk4 = freeBlock;
        }

        nextFree = (struct54 *)next->unkC;
        freeBlock->unkC = (s32)nextFree;
        if (nextFree != NULL) {
            nextFree->unk10 = (s32)freeBlock;
        }

        previous = (struct54 *)next->unk10;
        if (previous == NULL) {
            D_800380B8 = freeBlock;
            freeBlock->unk10 = 0;
        } else if (previous != freeBlock) {
            freeBlock->unk10 = (s32)previous;
            previous->unkC = (s32)freeBlock;
        }
        merged = 1;
    }

    if (!merged) {
        next = D_800380B8;
        if (next == NULL) {
            freeBlock->unkC = 0;
            freeBlock->unk10 = 0;
            D_800380B8 = freeBlock;
        } else if (freeBlock < next) {
            freeBlock->unkC = (s32)next;
            freeBlock->unk10 = 0;
            next->unk10 = (s32)freeBlock;
            D_800380B8 = freeBlock;
        } else {
            previous = next;
            next = (struct54 *)previous->unkC;
            while ((next != NULL) && (next <= freeBlock)) {
                previous = next;
                next = (struct54 *)next->unkC;
            }
            freeBlock->unkC = (s32)next;
            freeBlock->unk10 = (s32)previous;
            if (next != NULL) {
                next->unk10 = (s32)freeBlock;
            }
            previous->unkC = (s32)freeBlock;
        }
    }

    if (freeBlock->unkC == 0) {
        D_800380BC = (s32 *)freeBlock;
    }
    if ((u32)D_8002AC30 < freeBlock->unk8) {
        D_8002AC30 = freeBlock->unk8;
        D_800380B0 = freeBlock;
    }

    osSetIntMask(mask);
}

void func_10004250(void) {
    s32 temp_v0;
    u32 temp_v1;
    OSIntMask mask;
    struct54 *phi_s0;

    mask = osSetIntMask(1);

    if (phi_s0 = D_800380B4) {
        do {
            temp_v1 = phi_s0->unk8;
            temp_v0 = temp_v1 >> 0x18;
            if (2 == temp_v0) {
                func_10004074(&phi_s0->unkC);
            } else if ((temp_v0 == 3) || (temp_v0 == 4)) {
                phi_s0->unk8 = ((temp_v0 - 1) << 0x18) | (temp_v1 & 0xFFFFFF);
            }
        } while(phi_s0 = phi_s0->unk0);
    }
    osSetIntMask(mask);
}

void func_10004308(void) {
    u32 temp_t6;
    struct54 *phi_s0;
    OSIntMask mask;

    mask = osSetIntMask(1);
    phi_s0 = D_800380B4;
    func_15042D50();

    if (phi_s0) {
        do {
            temp_t6 = phi_s0->unk8 >> 24;
            if (temp_t6 == 1 || temp_t6 == 2 || temp_t6 == 3 || temp_t6 == 4) {
                func_10004074(&phi_s0->unkC);
            }
        }
        while (phi_s0 = phi_s0->unk0);
    }
    osSetIntMask(mask);
}

void func_100043B4(s32 *arg0, u32 arg1) {
    OSIntMask mask = osSetIntMask(1);

    arg0[-1] = (arg0[-1] & 0xFFFFFF) | (arg1 << 24);
    osSetIntMask(mask);
}

void func_1000440C(void) {
    struct54 *foo;
    struct54 *last_good_foo;
    s32 tmp0;

    for (foo = D_800380B8, tmp0 = NULL; foo != NULL; foo = (struct54 *)foo->unkC) {
        if (tmp0 < (s32) foo->unk8) {
            tmp0 = foo->unk8;
            last_good_foo = foo;
        }
    }

    D_800380B0 = last_good_foo;
    D_8002AC30 = tmp0;
}
