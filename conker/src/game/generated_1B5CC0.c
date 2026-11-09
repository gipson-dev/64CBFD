#include <ultra64.h>
typedef struct {
    u8 retained0, stride, count, step;
    u32 retained4;
    Mtx *records;
    u32 retainedC;
    u8 *descriptor;
} DescriptorDraw151897A4;
extern u8 D_800BE9C0;
Gfx *func_151137D4(Gfx *, u8 *, Mtx *, s32, s32, s32);

typedef struct KeyedNode15188AD0 {
    u8 opaque[8];
    s32 *payload;
    struct KeyedNode15188AD0 *next;
    s32 key;
} KeyedNode15188AD0;
void func_100043B4(s32 *, u32);
void func_10004074(void *);

extern u8 *D_800DF7C8;

/* Non-matching placeholders for the text-only asm slice asm/1B5CC0.s. */

typedef struct ListNode15188A58 ListNode15188A58;

struct ListNode15188A58 {
    u8 active, kind, cleared, recordSize;
    u8 mode, retained05;
    s16 timer;
    u8 *buffer;
    ListNode15188A58 *next;
    s32 key;
};
extern ListNode15188A58 *D_800DF7CC;
s32 allocate_memory(s32, s32, s32, s32);
/* The matched helper receives its head through the existing node-pointer view. */
void func_15188A58(ListNode15188A58 *, ListNode15188A58 *);
typedef struct { ListNode15188A58 prefix; u32 cleared14; } OwnerBufferNode15188810;
s32 func_1502DB20(s32);

/* Extend an owner timer, or allocate and append its cleared record buffer. */
void func_15188810(u8 *owner, s32 timer, s32 mode) {
    ListNode15188A58 *node = (ListNode15188A58 *)D_800DF7C8;
    u32 count;
    s32 size;
    u8 *buffer;

    if (node != NULL) {
        do {
            if ((s32)owner == node->key) {
                if (node->timer < timer) {
                    node->timer = timer;
                }
                node->mode = mode;
                return;
            }
            node = node->next;
        } while (node != NULL);
    }
    node = (ListNode15188A58 *)allocate_memory(sizeof(OwnerBufferNode15188810), 1, 0, 0);
    if (node == NULL) {
        return;
    }
    count = func_1502DB20(owner[4]);
    if (count == 0) {
        func_10004074(node);
        return;
    }
    size = (count * 3) << 7;
    buffer = (u8 *)allocate_memory(size, 1, 1, 1);
    if (buffer == NULL) {
        func_10004074(node);
        return;
    }
    node->active = 0;
    node->kind = 3;
    node->cleared = 0;
    node->recordSize = 20;
    node->mode = mode;
    node->timer = timer;
    node->buffer = buffer;
    node->key = (s32)owner;
    ((OwnerBufferNode15188810 *)node)->cleared14 = 0;
    bzero(buffer, size);
    func_15188A58(node, (ListNode15188A58 *)&D_800DF7C8);
}

/* Extend the first matching timer, or allocate and append its cleared buffer. */
void func_1518894C(s32 key, s32 timer, s32 mode) {
    ListNode15188A58 *node = D_800DF7CC;
    u8 *buffer;

    if (node != NULL) {
        do {
            if (key == node->key) {
                if (node->timer < timer) {
                    node->timer = timer;
                }
                node->mode = mode;
                return;
            }
            node = node->next;
        } while (node != NULL);
    }
    node = (ListNode15188A58 *)allocate_memory(sizeof(*node), 1, 0, 0);
    if (node == NULL) {
        return;
    }
    buffer = (u8 *)allocate_memory(0x180, 1, 1, 0);
    if (buffer == NULL) {
        func_10004074(node);
        return;
    }
    node->active = 1;
    node->kind = 3;
    node->cleared = 0;
    node->recordSize = 20;
    node->mode = mode;
    node->timer = timer;
    node->buffer = buffer;
    node->key = key;
    bzero(buffer, 0x180);
    func_15188A58(node, (ListNode15188A58 *)&D_800DF7CC);
}

void func_15188A58(ListNode15188A58 *arg0, ListNode15188A58 *arg1) {
    ListNode15188A58 *temp_v0;
    ListNode15188A58 *temp_v1;

    arg0->next = 0;
    temp_v0 = *(ListNode15188A58 **)arg1;
    if (temp_v0 == 0) {
        *(ListNode15188A58 **)arg1 = arg0;
    } else {
        arg1 = temp_v0->next;
        temp_v1 = temp_v0;
        if (arg1 != 0) {
            do {
                temp_v1 = arg1;
                arg1 = arg1->next;
            } while (arg1 != 0);
        }
        temp_v1->next = arg0;
    }
}

void func_15188A9C(s32 arg0) {
    u8 *ptr = D_800DF7C8;

    if (ptr != 0) {
        do {
            if (arg0 == *(s32 *) (ptr + 0x10)) {
                *(u16 *) (ptr + 6) = 0;
            }
            ptr = *(u8 **) (ptr + 0xC);
        } while (ptr != 0);
    }
}

/* Unlink keyed nodes, mark their payload blocks, and free the removed nodes. */
void func_15188AD0(s32 key) {
    KeyedNode15188AD0 *next;
    KeyedNode15188AD0 *node = (KeyedNode15188AD0 *)D_800DF7C8;
    KeyedNode15188AD0 *previous = NULL;

    while (node != NULL) {
        next = node->next;
        if (key == node->key) {
            if (previous == NULL) {
                D_800DF7C8 = (u8 *)next;
            } else {
                previous->next = next;
            }
            func_100043B4(node->payload, 2);
            func_10004074(node);
        } else {
            previous = node;
        }
        node = next;
    }
}

s32 func_15188B74() {
    return 0;
}

s32 func_15188D00() {
    return 0;
}

/* Shift cached matrix history, then capture the owner's newest matrices. */
void func_15188E48(DescriptorDraw151897A4 *record) {
    s32 snapshots = record->stride;
    s32 matrices = func_1502DB20(record->descriptor[4]);
    u32 span = matrices * snapshots;
    u32 page = D_800BE9C0;
    u32 currentPage = page * span;
    u32 otherPage = (page ^ 1) * span;
    s32 previous = 0;
    s32 index = 1;
    Mtx *source;
    Mtx *destination;

    if (snapshots > 0) {
        do {
            if (snapshots == index) {
                source = *(Mtx **)(record->descriptor + 0x1D4);
                if (source == NULL) {
                    record->count = 0;
                    return;
                }
                destination = record->records + (previous * matrices + currentPage);
            } else {
                source = record->records + (index * matrices + otherPage);
                destination = record->records + (previous * matrices + currentPage);
            }
            bcopy(source, destination, (u32)matrices << 6);
            previous = index;
            index++;
        } while (previous != snapshots);
    }
    if (record->count != record->stride) {
        record->count++;
    }
}

s32 func_15188F84() {
    return 0;
}

s32 func_15189118() {
    return 0;
}

s32 func_151895A4(u8 *arg0) {
    u8 *temp_a2 = arg0;

    func_100043B4(*(s32 **)(temp_a2 + 8), 2);
}

s32 func_151895CC(u8 *arg0) {
    u8 *temp_a2 = arg0;

    func_100043B4(*(s32 **)(temp_a2 + 8), 2);
}

s32 func_151895F4() {
    return 0;
}

/* Draw matrix records with a temporary opacity ramp, then restore opacity. */
Gfx *func_151897A4(Gfx *cursor, DescriptorDraw151897A4 *draw, s16 viewIndex) {
    s32 index;
    s32 opacity;
    u32 current;
    u8 count;
    s32 increment;
    Gfx *next;
    u8 step;
    s32 start;
    s32 savedOpacity;
    s32 initialCount;

    initialCount = draw->count;
    if (initialCount == 0) {
        return cursor;
    }
    start = D_800BE9C0 * draw->stride;
    current = start;
    step = draw->step;
    opacity = step * 96;
    index = 0;
    savedOpacity = draw->descriptor[0x8A];
    increment = step << 5;
    count = initialCount;
    if (initialCount > 0) {
        do {
            draw->descriptor[0x8A] = opacity >> 8;
            next = func_151137D4(cursor, draw->descriptor,
                                (Mtx *)((u8 *)draw->records + (current << 6)), viewIndex, 0, 0);
            index++;
            opacity += increment;
            current++;
            cursor = next;
        } while (index != count);
    }
    draw->descriptor[0x8A] = savedOpacity;
    return cursor;
}

void func_151898C0(s32 arg0, s32 arg1) {
    u8 *ptr = D_800DF7C8;

    if (ptr != 0) {
        do {
            if (arg0 == *(s32 *) (ptr + 0x10)) {
                *(s32 *) (ptr + 0x14) = arg1;
                return;
            }
            ptr = *(u8 **) (ptr + 0xC);
        } while (ptr != 0);
    }
}
