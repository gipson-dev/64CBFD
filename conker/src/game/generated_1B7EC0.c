#include <ultra64.h>

#include "structs.h"
extern s32 D_800BE9E4;
extern void (*D_8008D5C0[])(u8 *);
void func_1516972C(struct102 *);


/* Non-matching placeholders for the text-only asm slice asm/1B7EC0.s. */

typedef struct {
    u8 pad0[0x10];
    s32 owner;
    s32 unk14;
    s32 unk18;
    u8 selector;
    u8 pad1D[3];
} Generated1B7EC0Command1E;

typedef struct {
    u8 pad0[0x10];
    s32 unk10;
    s32 unk14;
    s32 owner;
    s32 unk1C;
    s16 unk20;
    s16 unk22;
    u8 selector;
    u8 pad25[3];
} Generated1B7EC0Command1D;

void *func_15167A68(s32 arg0, s32 arg1, s32 arg2, s32 arg3, u8 arg4, u8 arg5);

/* Retire the queued entry after expiry, or advance the enabled timer. */
void func_1518AA10(u8 *queue) {
    u8 *next;
    u8 *entry;

    if (*(u32 *)(queue + 0x1C) != 0) {
        if (*(s16 *)(queue + 0x22) < 0) {
            entry = *(u8 **)(queue + 0x14);
            next = *(u8 **)(entry + 0x18);
            if (next == NULL) {
                *(s32 *)(queue + 0x10) = 0;
                *(s32 *)(queue + 0x14) = 0;
            } else {
                /* Reload the link after clearing next: the fields may alias. */
                *(s32 *)(next + 0x14) = 0;
                *(u8 **)(queue + 0x14) = *(u8 **)(entry + 0x18);
            }
            if (entry[0x1C] != 0) {
                D_8008D5C0[entry[0x1C]](*(u8 **)(entry + 0x10));
            }
            func_1516972C((struct102 *)entry);
            /* Release callbacks can change the count before this decrement. */
            *(u32 *)(queue + 0x1C) -= 1;
        } else if (queue[0x24] & 1) {
            *(s16 *)(queue + 0x22) = (u32)*(s16 *)(queue + 0x22) - (u32)D_800BE9E4;
        }
    }
}

Generated1B7EC0Command1D *func_1518AADC(s32 arg0, volatile s16 arg1, volatile u8 arg2) {
    volatile Generated1B7EC0Command1D *record;
    s16 value;

    record = func_15167A68(0x1D, 0, 0x28, 1, 0xFF, 1);
    value = arg1;
    if (record == NULL) {
        return NULL;
    }

    record->unk1C = 0;
    record->unk22 = value;
    record->unk20 = value;
    record->unk10 = 0;
    record->unk14 = 0;
    record->owner = arg0;
    record->selector = arg2;
    return (Generated1B7EC0Command1D *)record;
}

Generated1B7EC0Command1E *func_1518AB60(s32 arg0, volatile u8 arg1) {
    volatile Generated1B7EC0Command1E *record;
    u8 selector;

    record = func_15167A68(0x1E, 0, 0x20, 1, 0xFF, 1);
    if (record == NULL) {
        return NULL;
    }

    record->owner = arg0;
    selector = arg1;
    record->unk14 = 0;
    record->unk18 = 0;
    record->selector = selector;
    return (Generated1B7EC0Command1E *)record;
}

/* Append one command record and retire the oldest if the queue exceeds its limit. */
s32 func_1518ABD0(u8 *queue, s32 owner, u8 selector) {
    u8 *entry, *tail, *next;
    Generated1B7EC0Command1E *record;
    u32 count;
    s32 limit;
    s16 duration;

    if (queue == NULL) {
        if (selector != 0) D_8008D5C0[selector]((u8 *)owner);
        return 0;
    }
    record = func_1518AB60(owner, selector);
    if (record == NULL) {
        if (selector != 0) D_8008D5C0[selector]((u8 *)owner);
        return 0;
    }
    tail = *(u8 **)(queue + 0x10);
    record->unk14 = (s32)tail;
    if (tail != NULL) {
        *(u8 **)(tail + 0x18) = (u8 *)record;
    } else {
        *(u8 **)(queue + 0x14) = (u8 *)record;
    }
    *(u8 **)(queue + 0x10) = (u8 *)record;
    record->unk18 = 0;
    count = *(u32 *)(queue + 0x1C) + 1;
    limit = *(s32 *)(queue + 0x18);
    duration = *(s16 *)(queue + 0x20);
    *(u32 *)(queue + 0x1C) = count;
    *(s16 *)(queue + 0x22) = duration;
    if (limit < (s32)count) {
        entry = *(u8 **)(queue + 0x14);
        *(u32 *)(queue + 0x1C) = count - 1;
        next = *(u8 **)(entry + 0x18);
        if (next == NULL) {
            *(u8 **)(queue + 0x10) = NULL;
            *(u8 **)(queue + 0x14) = NULL;
        } else {
            *(u8 **)(next + 0x14) = NULL;
            *(u8 **)(queue + 0x14) = *(u8 **)(entry + 0x18);
        }
        if (entry[0x1C] != 0) D_8008D5C0[entry[0x1C]](*(u8 **)(entry + 0x10));
        func_1516972C((struct102 *)entry);
    }
    return 1;
}
