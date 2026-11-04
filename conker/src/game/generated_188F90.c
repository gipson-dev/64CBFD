#include <ultra64.h>
#include "structs.h"

typedef struct {
    u8 retained00[0x14];
    f32 x;
    f32 y;
    f32 z;
} RequestedObject1515BE50;

typedef struct {
    RequestedObject1515BE50 *object;
    u8 uniqueId;
    u8 retained05;
    u16 size;
} ObjectRequest1515BE50;

typedef struct {
    u8 retained00[0x10];
    s32 active;
    s32 state;
    ObjectRequest1515BE50 request;
    f32 currentX;
    f32 currentY;
    f32 currentZ;
    f32 previousX;
    f32 previousY;
    f32 previousZ;
    f32 velocityX;
    f32 velocityY;
    f32 velocityZ;
    s32 listState;
    s32 listIndex;
} ObjectFollowRecord1515BE50;

void *func_15167A68(s32, s32, s32, s32, u8, u8);


typedef struct {
    u8 retained00[0x10];
    u8 mode;
    u8 flags;
    u8 command;
    u8 retained13;
    s16 timer;
    u8 retained16[2];
    s32 cursor;
    s32 packet;
    u8 retained20[0x18];
    s8 updateCallback;
    s8 removeCallback;
} TimedPacketRecord1515BAE0;
typedef s32 (*TimedPacketCallback1515BAE0)(void *);
extern TimedPacketCallback1515BAE0 D_8008B078[];
extern TimedPacketCallback1515BAE0 D_8008B07C[];
extern s32 D_800BE9E4;
s32 func_1514401C(u8, s32 *, s32 *, u8);
void func_1516972C(void *);

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

/* Advance a timed packet and remove it when its callbacks request completion. */
void func_1515BAE0(TimedPacketRecord1515BAE0 *record) {
    s32 remove = 0;
    s8 callbackIndex;

    if ((record->flags & 1) != 0) {
        record->timer -= D_800BE9E4;
        if (record->timer < 0) {
            remove = 1;
        }
    }
    if (remove == 0) {
        callbackIndex = record->updateCallback;
        if (callbackIndex != -1) {
            if (D_8008B078[callbackIndex](record) == 0) {
                remove = 1;
            }
        }
        if (record->packet != 0) {
            remove = func_1514401C(record->mode, &record->packet,
                                  &record->cursor, record->command) & 0xFF;
        }
    }
    if (remove != 0) {
        callbackIndex = record->removeCallback;
        if (callbackIndex != -1) {
            if (D_8008B07C[callbackIndex](record) != 0) {
                func_1516972C(record);
            }
        } else {
            func_1516972C(record);
        }
    }
}

s32 func_1515BBF0() {
    return 0;
}

/* Allocate a tracking record for an object request and seed both positions. */
ObjectFollowRecord1515BE50 *func_1515BE50(ObjectRequest1515BE50 *request,
                                          s32 extraBytes, u8 channel,
                                          s32 context) {
    ObjectFollowRecord1515BE50 *record;

    if (request->object == NULL) {
        return NULL;
    }
    record = func_15167A68(0x32, context, extraBytes + 0x50, 1, channel, 1);
    if (record == NULL) {
        return NULL;
    }
    memcpy(&record->request, request, sizeof(*request));
    record->currentX = request->object->x;
    record->currentY = request->object->y;
    record->currentZ = request->object->z;
    record->previousX = request->object->x;
    record->previousY = request->object->y;
    record->previousZ = request->object->z;
    record->listState = 0;
    record->listIndex = -1;
    record->active = 1;
    record->state = 0;
    record->velocityX = 0.0f;
    record->velocityY = 0.0f;
    record->velocityZ = 0.0f;
    return record;
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
