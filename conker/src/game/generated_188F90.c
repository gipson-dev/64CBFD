#include <ultra64.h>
#include "structs.h"

typedef struct ResetNode {
    u8 pad0[8];
    struct ResetNode *next;
    u8 padC[0x38];
    s32 value44;
    s32 value48;
} ResetNode;

typedef struct {
    u8 pad0[0xC8];
    ResetNode *head;
    u8 padCC[0xD4];
} ResetRow;

extern ResetRow D_800DCE50[];
extern ResetRow D_800DD190[];

/* Non-matching placeholders for the text-only asm slice asm/188F90.s. */

s32 func_1515BAE0() {
    return 0;
}

s32 func_1515BBF0() {
    return 0;
}

s32 func_1515BE50() {
    return 0;
}

s32 func_1515BF50(u8 *arg0) {
    func_1514EDF0(arg0, *(s32 *)(arg0 + 0x18));
    func_15169804(arg0);
}

s32 func_1515BF7C(u8 *arg0) {
    func_1514EDF0(arg0, *(s32 *)(arg0 + 0x18));
    func_15169824(arg0);
}

s32 func_1515BFA8() {
    return 0;
}

void func_1515C0B8(u8 *arg0, s32 arg1, u8 arg2) {
    func_15169850(arg1, arg2, (s32) (arg0 + 0x18), (s32) (arg0 + 0x1C), (s32) arg0);
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_188F90/func_1515C0F8.s")

void func_1515C158(void) {
    ResetRow *row;
    ResetNode *node;

    row = D_800DCE50;
    do {
        node = row->head;
        row++;
        if (node != NULL) {
            do {
                node->value44 = 0;
                node->value48 = -1;
                node = node->next;
            } while (node != NULL);
        }
    } while (row != D_800DD190);
}

void func_1515C1A0(struct127 *arg0, struct17 *arg1, f32 *arg2, f32 *arg3) {
    if (arg0->id < 0xBB && arg0->id != 0xFF) {
        *arg2 = arg0->unkD2;
        *arg3 = arg0->unkD4;
        arg1->unk0 = arg0->x_position;
        arg1->unk4 = arg0->y_position + arg0->unkD6;
        arg1->unk8 = arg0->z_position;
    } else {
        *arg2 = 1.0f;
        *arg3 = 1.0f;
        arg1->unk0 = arg0->x_position;
        arg1->unk4 = arg0->y_position;
        arg1->unk8 = arg0->z_position;
    }
}

void func_1515C244(struct127 *arg0, struct17 *arg1, f32 *arg2, f32 *arg3) {
    if (arg0->id < 0xBB && arg0->id != 0xFF) {
        *arg2 = arg0->unkE4;
        *arg3 = arg0->unkE6;
        arg1->unk0 = arg0->x_position;
        arg1->unk4 = arg0->y_position + (s16)arg0->unkE8;
        arg1->unk8 = arg0->z_position;
    } else {
        *arg2 = 1.0f;
        *arg3 = 1.0f;
        arg1->unk0 = arg0->x_position;
        arg1->unk4 = arg0->y_position;
        arg1->unk8 = arg0->z_position;
    }
}
