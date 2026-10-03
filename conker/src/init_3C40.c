#include <ultra64.h>

#include "functions.h"
#include "variables.h"

typedef struct {
    s16 values[5];
} MemoryAlignmentTable;

extern MemoryAlignmentTable D_8002AC34;
extern MemoryAlignmentTable D_8002AC40;

s32 allocate_memory(s32 arg0, s32 arg1, s32 arg2, s32 arg3) {
    return func_10003C6C(arg0, arg1, arg2, 0, arg3);
}

s32 func_10003C6C(s32 arg0, s32 arg1, s32 arg2, s32 arg3, s32 arg4) {
    MemoryAlignmentTable alignmentOffsets;
    MemoryAlignmentTable alignmentMasks;
    struct54 *savedResult;
    s32 savedAlignmentMask;
    s32 savedAlignmentOffset;
    OSIntMask savedMask;
    s16 alignmentMask;
    s16 alignmentOffset;
    s32 nextFreeValue;
    s32 previousFreeValue;
    s32 roundedSize;
    s32 alignedAddress;
    s32 blockEnd;
    s32 available;
    s32 splitEnd;
    struct54 *physicalPrevious;
    struct54 *physicalNext;
    struct54 *nextFree;
    struct54 *previousFree;
    struct54 *block;
    struct54 *allocated;
    struct54 *split;
    u32 blockSize;
    u32 remainderSize;

    roundedSize = arg0;
    alignmentOffsets = D_8002AC34;
    alignmentMasks = D_8002AC40;
    D_800380C0 = roundedSize;
    D_800380C4 = arg1;
    D_800380C8 = arg2;
    D_800380CC = arg3;
    D_800380D0 = arg4;
    if (arg2 == 2) {
        roundedSize = (roundedSize + 0xF) & ~0xF;
    }
    if (roundedSize < 8) {
        roundedSize = 8;
    }
    roundedSize = (roundedSize + 3) & ~3;
    alignmentOffset = alignmentOffsets.values[arg2];
    alignmentMask = alignmentMasks.values[arg2];
    if ((arg4 == 1) && (D_8002AC30 < 0x7800)) {
        return 0;
    }

    savedAlignmentMask = alignmentMask;
    savedAlignmentOffset = alignmentOffset;
    savedMask = osSetIntMask(1);
    if (arg3 == 0) {
        block = D_800380B8;
    } else {
        block = (struct54 *)D_800380BC;
    }

search:
    if (block == NULL) {
        osSetIntMask(savedMask);
        if (arg4 == 0) {
            D_8003C8E0 = 0x0C000042;
            func_150AD770();
        }
        return 0;
    }
    blockSize = block->unk8;
    alignedAddress = ((s32)block + alignmentOffset + 0xC) & alignmentMask;
    blockEnd = (s32)block + blockSize + 0xC;
    if ((u32)blockEnd < (u32)(alignedAddress + roundedSize)) {
        if (arg3 == 0) {
            block = (struct54 *)block->unkC;
        } else {
            block = (struct54 *)block->unk10;
        }
        goto search;
    }

    if (arg3 == 0) {
        allocated = (struct54 *)(alignedAddress - 0xC);
        splitEnd = (s32)allocated + roundedSize;
        split = (struct54 *)(splitEnd + 0xC);
        remainderSize = ((s32)block + blockSize) - splitEnd;
    } else {
        alignedAddress = ((blockEnd - roundedSize) & savedAlignmentMask);
        allocated = (struct54 *)(alignedAddress - 0xC);
        split = block->unk0;
        remainderSize = (s32)allocated - (s32)block;
    }
    physicalPrevious = block->unk4;
    nextFreeValue = block->unkC;
    previousFreeValue = block->unk10;
    nextFree = (struct54 *)nextFreeValue;
    previousFree = (struct54 *)previousFreeValue;
    if (arg3 == 0) {
        physicalNext = block->unk0;
        if (remainderSize >= 0x14) {
            split->unk0 = physicalNext;
            split->unk8 = remainderSize - 0xC;
            if (physicalNext != NULL) {
                physicalNext->unk4 = split;
            }
            remainderSize = 0;
            split->unkC = nextFreeValue;
            split->unk10 = previousFreeValue;
            if (nextFreeValue != 0) {
                nextFree->unk10 = (s32)split;
            } else {
                D_800380BC = (s32 *)split;
            }
            if (previousFreeValue != 0) {
                previousFree->unkC = (s32)split;
            } else {
                D_800380B8 = split;
            }
        } else {
            split = physicalNext;
            if (nextFreeValue != 0) {
                nextFree->unk10 = previousFreeValue;
            } else {
                D_800380BC = (s32 *)previousFreeValue;
            }
            if (previousFreeValue != 0) {
                previousFree->unkC = nextFreeValue;
            } else {
                D_800380B8 = (struct54 *)nextFreeValue;
            }
        }
        if (physicalPrevious == NULL) {
            D_800380B4 = allocated;
        } else {
            physicalPrevious->unk0 = allocated;
            physicalPrevious->unk8 = (physicalPrevious->unk8 & 0xFF000000) |
                                     ((s32)allocated - (s32)physicalPrevious - 0xC);
        }
        allocated->unk0 = split;
        allocated->unk4 = physicalPrevious;
        allocated->unk8 = (arg1 << 24) | (remainderSize + roundedSize);
        if (split != NULL) {
            split->unk4 = allocated;
        }
    } else if (remainderSize >= 0x14) {
        allocated->unk4 = block;
        allocated->unk0 = block->unk0;
        physicalNext = allocated->unk0;
        allocated->unk8 = (arg1 << 24) | (blockEnd - (s32)allocated - 0xC);
        if (physicalNext != NULL) {
            physicalNext->unk4 = allocated;
        }
        block->unk0 = allocated;
        block->unk8 = remainderSize - 0xC;
    } else {
        alignedAddress = ((s32)block + savedAlignmentOffset + 0xC) & savedAlignmentMask;
        allocated = (struct54 *)(alignedAddress - 0xC);
        allocated->unk0 = split;
        allocated->unk4 = physicalPrevious;
        allocated->unk8 = (arg1 << 24) | (blockEnd - (s32)allocated - 0xC);
        if (nextFreeValue != 0) {
            nextFree->unk10 = previousFreeValue;
        } else {
            D_800380BC = (s32 *)previousFreeValue;
        }
        if (previousFreeValue != 0) {
            previousFree->unkC = nextFreeValue;
        } else {
            D_800380B8 = (struct54 *)nextFreeValue;
        }
        if (physicalPrevious == NULL) {
            D_800380B4 = allocated;
        } else {
            physicalPrevious->unk0 = allocated;
            physicalPrevious->unk8 = (physicalPrevious->unk8 & 0xFF000000) |
                                     ((s32)allocated - (s32)physicalPrevious - 0xC);
        }
        physicalNext = allocated->unk0;
        if (physicalNext != NULL) {
            physicalNext->unk4 = allocated;
        }
        physicalPrevious = allocated->unk4;
        if (physicalPrevious != NULL) {
            physicalPrevious->unk0 = allocated;
        }
    }
    if (block == D_800380B0) {
        savedResult = allocated;
        func_1000440C();
        allocated = savedResult;
    }
    savedResult = allocated;
    osSetIntMask(savedMask);
    allocated = savedResult;
    return (s32)&allocated->unkC;
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
