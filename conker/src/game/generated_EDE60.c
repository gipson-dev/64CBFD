#include <ultra64.h>

extern void func_1516972C(void *arg0);

/* Non-matching placeholders for the text-only asm slice asm/EDE60.s. */

void func_150C0A48(u8 *arg0);

void func_150C09B0(u8 *arg0, s32 arg1, u8 arg2) {
    func_15169850(arg1, arg2, (s32) (arg0 + 0x20), (s32) (arg0 + 0x24), (s32) arg0);
}

s32 func_150C09F0(s32 arg0) {
    func_150C0A48(arg0);
    func_15169804(arg0);
}

s32 func_150C0A1C(s32 arg0) {
    func_150C0A48(arg0);
    func_15169824(arg0);
}

void func_150C0A48(u8 *arg0) {
    s16 index = *(s16 *)(arg0 + 0x44);

    while (index != -1) {
        u8 *entries = *(u8 **)(arg0 + 0x40);

        func_1516972C(*(void **)((s32)entries + index * 8));
        entries = *(u8 **)(arg0 + 0x40);
        index = *(s16 *)((s32)entries + index * 8 + 4);
    }
}

void *func_15167A68(s32, s32, s32, s32, u8, u8);
void *memcpy(void *, const void *, u32);
/* Allocate an owner record and initialize its free-entry chain. */
u8 *func_150C0AC0(u8 *descriptor, u8 slot, s32 context) {
    /* Retain the allocation size and result in the retail stack order. */
    struct { s32 size; u8 *result; } allocation;
    u8 *position;
    s16 index;
    allocation.size = *(s16 *)(descriptor + 0x14) * 8 + 0x48;
    if (!(descriptor[0x18] & 2)) {
        if (!*(u32 **)(descriptor + 8)) return 0;
        if (!**(u32 **)(descriptor + 8)) return 0;
    }
    allocation.result = func_15167A68(0x25, context, allocation.size, 1, slot, 1);
    if (!allocation.result) return 0;
    memcpy(allocation.result + 0x18, descriptor, 0x1c);
    *(u8 **)(allocation.result + 0x40) = allocation.result + 0x48;
    if (descriptor[0x18] & 2) {
        position = *(u8 **)(allocation.result + 0x18);
        *(f32 *)(allocation.result + 0x34) = *(f32 *)position;
        *(f32 *)(allocation.result + 0x38) = *(f32 *)(position + 8);
    } else {
        position = *(u8 **)(allocation.result + 0x20);
        *(f32 *)(allocation.result + 0x34) = *(f32 *)(position + 0x14);
        *(f32 *)(allocation.result + 0x38) = *(f32 *)(position + 0x1c);
    }
    *(f32 *)(allocation.result + 0x3c) = 0.0f;
    *(s16 *)(allocation.result + 0x44) = -1;
    *(s16 *)(allocation.result + 0x46) = 0;
    for (index = 0; index < *(s16 *)(descriptor + 0x14) - 1; index++) {
        *(s16 *)(*(u8 **)(allocation.result + 0x40) + index * 8 + 4) = index + 1;
    }
    *(s16 *)(*(u8 **)(allocation.result + 0x40) + *(s16 *)(descriptor + 0x14) * 8 - 4) = -1;
    *(s32 *)(allocation.result + 0x10) = 1;
    *(s32 *)(allocation.result + 0x14) = 0;
    return allocation.result;
}

s32 func_150C0C38() {
    return 0;
}

typedef struct { void *actor; s16 next; s16 unused; } OwnerChainEntry150C1198;
/* Unlink the actor from its owner's active chain, then prepend its slot to the free chain. */
void func_150C1198(u8 *actor) {
    u8 *owner;
    s32 found;
    s16 previous;
    s16 index;
    s16 head;
    OwnerChainEntry150C1198 *entries;
    OwnerChainEntry150C1198 *entry;

    owner = *(u8 **)(actor + 0xA8);
    found = 0;
    previous = -1;
    index = *(s16 *)(owner + 0x44);
    head = index;
    while (index != -1 && !found) {
        entries = *(OwnerChainEntry150C1198 **)(owner + 0x40);
        if (entries[index].actor == actor) {
            found = 1;
        } else {
            previous = index;
            index = entries[index].next;
        }
    }
    if (found) {
        entries = *(OwnerChainEntry150C1198 **)(owner + 0x40);
        entry = (OwnerChainEntry150C1198 *)((s32)entries + index * 8);
        if (index == head) {
            *(s16 *)(owner + 0x44) = entry->next;
        } else {
            entries[previous].next = entry->next;
            /* The link store may change the shared entry-table pointer. */
            entry = (OwnerChainEntry150C1198 *)((s32)*(OwnerChainEntry150C1198 **)(owner + 0x40) + index * 8);
        }
        entry->next = *(s16 *)(owner + 0x46);
        *(s16 *)(owner + 0x46) = index;
    }
}
