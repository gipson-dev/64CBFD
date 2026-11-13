#include <ultra64.h>
#include <stdarg.h>
#include "functions.h"
#include "variables.h"

void *func_1502B5C8(s32 *size, u32 depth, ...);

typedef struct ScriptNodeC8950 {
    u16 kind;
    u8 padding[0x16];
    struct ScriptNodeC8950 *next;
    struct ScriptNodeC8950 *prev;
} ScriptNodeC8950;
typedef struct {
    u16 length;
    u16 padding;
    ScriptNodeC8950 *unk4;
    ScriptNodeC8950 *unk8;
} ScriptListC8950;
#define SCRIPT_LIST_C8950 (*(ScriptListC8950 *)&D_800D2F48)

s32 allocate_memory(s32 size, s32 color, s32 side, s32 flags);

/* Generated placeholder declarations. */
s32 func_1509B5AC(s32 arg0, s32 arg1);
void func_1509B810(ScriptNodeC8950 *node);
struct248 *func_1509B950(struct248 *block);
s32 func_1509BA04();
s32 func_1509BBA0();
s32 func_1509BE40(s32, ...);
/* End generated placeholder declarations. */

struct249 *func_1509B704(s16 arg0);
void func_1509C120(void);
void func_1509C3A0(void);


void func_1509B4A0(s32 arg0, s32 arg1) {
    s32 i;

    if(0) {};

    D_8003C8E0 = 0x5000000;
    func_1509C120();
    func_15096970();

    for (i = 0; i < D_800D2F3C; i++) {
        if (func_1509CBD4(D_800D2F40[i])) {
            func_1509B5AC(D_800D2F40[i], arg1);
        }
    }

    func_1509C3A0();
    D_8003C8E0 = 0;
}

u16 *func_1509B570(s32 arg0) {
    struct248 *temp_v0;
    u16 res;

    temp_v0 = func_1509B704(arg0);
    if (temp_v0 != 0) {
        res = temp_v0->unkA;
        return (s32)temp_v0 + (res & 0xFFFF);
    }
    return NULL;
}

/* Non-matching C placeholders for asm/nonmatchings/game_C8950/func_1509B5AC.s. */
s32 func_1509B5AC(s32 arg0, s32 arg1) {
    return 0;
}

struct249 *func_1509B704(s16 arg0) {
    struct249 *tmp;
    s32 mask = 0xFFFF03FF;
    s32 i;

    tmp = D_800D2F48.unk4;
    for (i = 0; i < D_800D2F48.length; i++) {
        if (arg0 == (tmp->unk0 & mask)) {
            return tmp;
        }
        tmp = tmp->next;
    }
    return NULL;
}


/* Unlink and free a script node, maintaining both ends of the list. */
void func_1509B764(ScriptNodeC8950 *node) {
    if (SCRIPT_LIST_C8950.length == 1) {
        SCRIPT_LIST_C8950.unk4 = NULL;
        SCRIPT_LIST_C8950.unk8 = NULL;
    } else {
        if (node == SCRIPT_LIST_C8950.unk4) {
            SCRIPT_LIST_C8950.unk4 = node->next;
            node->next->prev = NULL;
        } else {
            node->prev->next = node->next;
        }
        if (node == SCRIPT_LIST_C8950.unk8) {
            SCRIPT_LIST_C8950.unk8 = node->prev;
            node->prev->next = NULL;
        } else {
            node->next->prev = node->prev;
        }
    }
    func_10004074(node);
    SCRIPT_LIST_C8950.length--;
}

/* Insert by the low ten kind bits, scanning backward from the script-list tail. */
void func_1509B810(ScriptNodeC8950 *node) {
    s32 length;
    ScriptNodeC8950 *cursor;
    ScriptNodeC8950 *tail;
    s32 key;
    s32 count;
    s32 mask = 0xFFFF03FF;

    cursor = SCRIPT_LIST_C8950.unk8;
    tail = cursor;
    key = node->kind & mask;
    length = SCRIPT_LIST_C8950.length;
    if (length == 0) {
        SCRIPT_LIST_C8950.unk4 = node;
        SCRIPT_LIST_C8950.unk8 = node;
        node->next = NULL;
        node->prev = NULL;
        SCRIPT_LIST_C8950.length++;
        return;
    }
    if (length > 0) {
        count = 0;
        do {
            count++;
            if ((cursor->kind & mask) >= key) {
                goto next_node;
            }
            {
                if (cursor == tail) {
                    node->prev = cursor;
                    node->next = NULL;
                    cursor->next = node;
                    SCRIPT_LIST_C8950.unk8 = node;
                    SCRIPT_LIST_C8950.length++;
                    return;
                }
                node->prev = cursor;
                node->next = cursor->next;
                cursor->next->prev = node;
                cursor->next = node;
                SCRIPT_LIST_C8950.length++;
                return;
            }
next_node:
            cursor = cursor->prev;
        } while ((count < length) != 0);
    }
    cursor = SCRIPT_LIST_C8950.unk4;
    SCRIPT_LIST_C8950.unk4 = node;
    node->prev = NULL;
    node->next = cursor;
    cursor->prev = node;
    SCRIPT_LIST_C8950.length++;
}

void func_1509B8FC(s16 arg0) {
    struct248 *temp_v0;
    s16 sp18[2];

    temp_v0 = func_1502B5C8((s32 *)&sp18, 2, 20, arg0);
    temp_v0->unk0 |= arg0;
    temp_v0->unk2 = D_800BE9F0;
    func_1509B950(temp_v0);
}

/* Append a zeroed tail at the next eight-byte boundary and release the source.
 * Both alignments advance a full eight bytes when already aligned.
 * Keep header updates before allocation and reload fields after helper calls. */
struct248 *func_1509B950(struct248 *block) {
    s32 alignmentPadding;
    u32 tailOffset;
    u32 newSize;
    u32 tailSize;
    struct248 *copy;

    tailSize = block->unk6;
    alignmentPadding = 8 - (((u32)block + block->unk4) & 7);
    tailOffset = block->unk4 + alignmentPadding;
    newSize = tailOffset + tailSize;
    block->unk4 = newSize;
    block->unkA = tailOffset;
    block->unk4 = block->unk4 - (((u32)block + block->unk4) & 7) + 8;
    copy = (struct248 *)allocate_memory(block->unk4, 255, 2, 0);
    if (copy == NULL) {
        for (;;) {}
    }
    bcopy(block, copy, block->unk4);
    bzero((u8 *)copy + copy->unkA, copy->unk6);
    func_10004074(block);
    return copy;
}

/* Non-matching C placeholders for asm/nonmatchings/game_C8950/func_1509BA04.s. */
s32 func_1509BA04() {
    return 0;
}

/* Non-matching C placeholders for asm/nonmatchings/game_C8950/func_1509BBA0.s. */
s32 func_1509BBA0() {
    return 0;
}

//
/* Build the variable-argument script query and dispatch its selected provider. */
extern s32 D_800D3840;
extern s32 D_800D2F60[];
extern s32 (*D_80088498[])(s32, s32, s32 *);
s32 func_1509BE40(s32 count, ...) {
    va_list args;
    s32 key, selector, type, previous, result, i;
    register s32 flags;
    va_start(args, count);
    flags = va_arg(args, s32);
    key = va_arg(args, s32);
    previous = D_800D3840;
    type = ((flags & 0xf000) >> 12) - 1;
    flags &= 0xfff;
    selector = flags;
    D_800D2F60[0] = selector;
    D_800D2F60[1] = key;
    for (i = 0; i < count; i++) D_800D2F60[i + 2] = va_arg(args, s32);
    D_800D3840 = count + 2;
    result = D_80088498[type](selector, key, D_800D2F60);
    D_800D3840 = previous;
    va_end(args);
    return result;
}

/* Retail variable-argument script dispatcher, also used by Race respawn. */
#pragma GLOBAL_ASM("asm/nonmatchings/game_C8950/func_1509BFB0.s")

/* Replace the active state block through a randomized allocation slot. */
void func_1509C120(void) {
    s32 index;
    struct102 *old;
    s32 blocks[4];
    s32 i;
    s32 kept;

    index = func_150ADA20() & 3;
    old = D_800D2E4C;
    if ((old == NULL) || ((func_150ADA20() & 4) != 0)) {
        for (i = 0; i <= index; i++) {
            blocks[i] = allocate_memory(0x1B, 0xFF, 2, 0);
        }

        for (i = 0; i <= index; i++) {
            if (i != index) {
                func_10004074((void *)blocks[i]);
            }
        }

        kept = blocks[index];
        D_800D2E4C = (struct102 *)kept;
        if (old != NULL) {
            bcopy(old, D_800D2E4C, 0x1B);
            func_10004074(old);
        }
    }
}

void func_1509C228(void) {
    if ((D_800D2E68 & 8) || (D_800D2E4C->unkF & 1)) {
        func_1509BFB0(2, 0x2000, 0x36, 0, 1);
        return;
    }
    func_1509BFB0(2, 0x2000, 0x36, 1, 1);
}

s32 func_1509C2A4(void) {
    s32 temp_v0 = D_800BE9F0;
    if ((temp_v0 == 3) ||
        (temp_v0 == 5) ||
        (temp_v0 == 9) ||
        (temp_v0 == 13) ||
        (temp_v0 == 15) ||
        (temp_v0 == 17) ||
        (temp_v0 == 21) ||
        (temp_v0 == 22) ||
        (temp_v0 == 24) ||
        (temp_v0 == 26) ||
        (temp_v0 == 29) ||
        (temp_v0 == 31) ||
        (temp_v0 == 32) ||
        (temp_v0 == 33) ||
        (temp_v0 == 34) ||
        (temp_v0 == 36) ||
        (temp_v0 == 37) ||
        (temp_v0 == 42) ||
        (temp_v0 == 43) ||
        (temp_v0 == 45) ||
        (temp_v0 == 48) ||
        (temp_v0 == 51) ||
        (temp_v0 == 52) ||
        (temp_v0 == 56) ||
        (temp_v0 == 62) ||
        (temp_v0 == 63) ||
        (D_800D2E44 != 0)
      ) {
        return 0;
    }
    return 1;
}

void func_1509C3A0(void) {
    if ((D_800D2E43 != 0) && (D_800D2E44 == 0) && (func_1509C2A4() != 0)) {
        D_800BE3DF = (s8) D_800BE9F4;
        if (D_800C35C4 == 0) {
            func_15007718(D_8008FDA8);
        }
        D_800D2E43 = 0;
    }
}


s32 func_1509C414(s32 arg0) {
    return ((D_800D2E4C->unk3 & 1) << 0xA) + arg0 + 0x1400;
}
