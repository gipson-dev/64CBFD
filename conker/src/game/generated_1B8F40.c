#include <ultra64.h>
#include "structs.h"

/* Non-matching placeholders for the text-only asm slice asm/1B8F40.s. */

void *func_15167A68(s32, s32, s32, s32, u8, u8);
s32 func_150ADA20(void);

extern u8 D_800DCE50[0x340];
extern s8 D_800DD190;
extern u8 *D_800DD198[];
void func_1516972C(struct102 *);

s32 func_1518BA90() {
    return 0;
}

/* Walk both rows, retaining each next link across record cleanup. */
void func_1518BBF4(u8 *owner) {
    u8 *row;
    u8 *record;
    u8 *rowEnd;
    if (owner != NULL) {
        row = D_800DCE50;
        rowEnd = D_800DCE50 + 0x340;
        do {
            record = *(u8 **)(row + 0x7C);
            D_800DD190++;
            while (record != NULL) {
                D_800DD198[D_800DD190] = *(u8 **)(record + 8);
                *(u8 **)(record + 0x24) = owner;
                if (owner != NULL || owner[0x3B] == record[0x28]) {
                    func_1516972C((struct102 *)record);
                }
                record = D_800DD198[D_800DD190];
            }
            D_800DD190--;
            row += 0x1A0;
        } while (row != rowEnd);
    }
}

void *func_1518BCD0(void *arg0, u8 arg1, s32 arg2) {
    u8 *record;

    record = func_15167A68(0x1F, arg2, 0x44, 1, arg1, 1);
    if (record == NULL) {
        return NULL;
    }
    memcpy(record + 0x10, arg0, 0x1C);
    *(u32 *)(record + 0x2C) = func_150ADA20() & 0x1F;
    *(u32 *)(record + 0x30) = func_150ADA20() & 0x1F;
    return record;
}

s32 func_1518BD60() {
    return 0;
}

s32 func_1518C0B8() {
    return 0;
}

s32 func_1518C540(u8 *arg0) {
    u8 *temp_v0 = *(u8 **) (arg0 + 0x98);
    s32 temp_v1 = *(s16 *) (arg0 + 0x1C) << 3;

    if (temp_v1 >= 0x100) {
        temp_v1 = 0xFF;
    }
    *(temp_v0 + 0x1B) = temp_v1;
    if ((temp_v1 & 0xFF) < 0) {
        return 0;
    }
    return 1;
}

s32 func_1518C57C() {
    return 0;
}

s32 func_1518C69C() {
    return 0;
}

void func_1516972C(struct102 *owner);

/* Exchange a paired reference/tag, or release an owner matching the event. */
void func_1518C850(void *owner, s32 pairAddress, u8 command) {
    s32 *pair = (s32 *)pairAddress;
    if (command == 0x2D) {
        s32 first = pair[0];
        if (first == *(s32 *)((u8 *)owner + 0x24)) {
            *(s32 *)((u8 *)owner + 0x24) = pair[1];
            *((u8 *)owner + 0x28) = ((u8 *)pair)[9];
        } else if (pair[1] == *(s32 *)((u8 *)owner + 0x24)) {
            *(s32 *)((u8 *)owner + 0x24) = first;
            *((u8 *)owner + 0x28) = ((u8 *)pair)[8];
        }
    } else if (command == 0) {
        s32 first = pair[0];
        if (first == *(s32 *)((u8 *)owner + 0x24) || *((u8 *)owner + 0x28) == ((u8 *)pair)[4]) {
            func_1516972C(owner);
        }
    }
}
