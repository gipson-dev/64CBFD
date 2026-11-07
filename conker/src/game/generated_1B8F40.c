#include <ultra64.h>
#include "structs.h"
typedef struct {
    Vtx vertices[8];
    u32 value80;
    u32 retained84;
    s16 cleared88;
    u16 value8A;
    s16 x, y, z;
    s16 lifetime, remaining;
    s16 initialHeight;
    u16 flags;
    u16 retained9A;
    s16 cleared9C, cleared9E;
    u8 textureIndex, mode;
    s8 tag;
    u8 retainedA3;
    u32 retainedA4;
} SelectedVertexSprite;
void func_1516865C(void *, u8, u8, u8, u8);
void *func_15168800(void *, u8, s32);
u8 func_151D8E20(void);
f32 func_150ADA68(void);
void func_151DBCBC(u8, f32, s16, s32, void *, u8, s32);


/* Non-matching placeholders for the text-only asm slice asm/1B8F40.s. */

void *func_15167A68(s32, s32, s32, s32, u8, u8);
s32 func_150ADA20(void);

extern u8 D_800DCE50[0x340];
extern s8 D_800DD190;
extern u8 *D_800DD198[];
void func_1516972C(struct102 *);

/* The update routine samples base + random * range and indices 0..limit. */
typedef struct {
    f32 firstBase, firstRange, secondBase, secondRange;
    s16 firstChoiceLimit, secondChoiceLimit;
    u8 *owner;
    u8 tag, mode, subtype, retained;
} OwnerRecordRequest;
extern f32 D_800A7434, D_800A7438, D_800A743C;
void *func_1518BCD0(void *, u8, s32);

/* Reuse the first owner/tag record, or construct the owner's default effect. */
void *func_1518BA90(u8 *owner, u8 priority, s32 context) {
    void *result;
    OwnerRecordRequest request;
    u8 *row;
    u8 *end;
    u8 *record;
    if (owner == NULL) {
        return NULL;
    }
    row = D_800DCE50;
    end = (u8 *)&D_800DD190;
    do {
        record = *(u8 **)(row + 0x7C);
        while (record != NULL) {
            if (*(u8 **)(record + 0x24) == owner || owner[0x3B] == record[0x28]) {
                return record;
            }
            record = *(u8 **)(record + 8);
        }
        row += 0x1A0;
    } while (row != end);
    switch (owner[4]) {
        /* Unreachable for u8; preserves the original nine-entry table. */
        case -1:
            return NULL;
        case 7:
            request.firstBase = D_800A7434;
            request.firstRange = D_800A7438;
            request.secondBase = D_800A743C;
            request.secondRange = 5.0f;
            request.secondChoiceLimit = 55;
            request.firstChoiceLimit = 4;
            request.mode = 5;
            request.subtype = 19;
            break;
        case 0:
        case 1:
        case 2:
        case 3:
        case 4:
            request.secondChoiceLimit = 0;
            request.firstChoiceLimit = 5;
            request.mode = 5;
            request.subtype = 19;
            request.firstBase = 10.0f;
            request.firstRange = 10.0f;
            request.secondBase = 10.0f;
            request.secondRange = 10.0f;
            break;
        default:
            return NULL;
    }
    request.owner = owner;
    request.tag = owner[0x3B];
    result = func_1518BCD0(&request, priority, context);
    return result;
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

/* Emit the selected position as a white, randomized-lifetime sprite. */
s32 func_1518C57C(u8 *actor, f32 previousX, f32 previousY, f32 previousZ,
                  f32 height, void *context) {
    SelectedVertexSprite descriptor;
    u8 *owner = *(u8 **)(actor + 0x98);
    u8 *positions = *(u8 **)(actor + 0x94);
    s32 heightInt;
    descriptor.value80 = 0;
    descriptor.value8A = 0x100;
    descriptor.x = (s32)*(f32 *)(positions + *(s8 *)(actor + 0x2D) * 20);
    descriptor.y = heightInt = (s32)height;
    descriptor.z = (s32)*(f32 *)(positions + *(s8 *)(actor + 0x2D) * 20 + 8);
    descriptor.lifetime = (u32)func_150ADA20() % 21 + 35;
    descriptor.tag = -1;
    descriptor.textureIndex = 18;
    descriptor.flags = 12;
    descriptor.mode = 0;
    descriptor.remaining = descriptor.lifetime;
    descriptor.initialHeight = heightInt;
    func_1516865C(&descriptor, 255, 255, 255, 255);
    func_15168800(&descriptor, actor[0xC], actor[1]);
    owner[0x20] = 4;
    return 1;
}

/* Emit the impact sprite and submit a randomized effect at the updated position. */
s32 func_1518C69C(u8 *actor, f32 previousX, f32 previousY, f32 previousZ,
                  f32 height, void *context) {
    s32 heightInt;
    SelectedVertexSprite descriptor;
    u8 *owner = *(u8 **)(actor + 0x98);
    u8 *positions = *(u8 **)(actor + 0x94);
    u8 selector;
    f32 position[3];
    f32 magnitude;
    descriptor.value80 = 0;
    descriptor.value8A = 0x100;
    descriptor.x = (s32)*(f32 *)(positions + *(s8 *)(actor + 0x2D) * 20);
    descriptor.y = heightInt = (s32)height;
    descriptor.z = (s32)*(f32 *)(positions + *(s8 *)(actor + 0x2D) * 20 + 8);
    descriptor.lifetime = (u32)func_150ADA20() % 21 + 35;
    descriptor.tag = -1;
    descriptor.textureIndex = 18;
    descriptor.flags = 12;
    descriptor.mode = 0;
    descriptor.remaining = descriptor.lifetime;
    descriptor.initialHeight = heightInt;
    func_1516865C(&descriptor, 255, 255, 255, 255);
    func_15168800(&descriptor, actor[0xC], actor[1]);
    owner[0x20] = 4;
    position[0] = *(f32 *)(positions + *(s8 *)(actor + 0x2D) * 20);
    position[1] = height;
    position[2] = *(f32 *)(positions + *(s8 *)(actor + 0x2D) * 20 + 8);
    selector = func_151D8E20();
    magnitude = func_150ADA68() * 40.0f + 100.0f;
    func_151DBCBC(selector, magnitude, 255,
                  (s32)context, position, actor[0xC], actor[1]);
    return 1;
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
