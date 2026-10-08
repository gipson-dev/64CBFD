#include <ultra64.h>
extern u8 D_800E0A00;

/* Non-matching placeholders for the text-only asm slice asm/205C90.s. */

typedef struct {
    f32 x, y, z;
    f32 inner, width, inverseWidth;
    u8 player;
} RecordDistanceLevel;
f32 *func_15144B34(s32 player);
f32 func_15143E64(f32 *vector);

void func_151D8C00(u8 *owner, RecordDistanceLevel *parameters);
extern u8 D_80084060[];
extern u8 D_800BE944[];
#include <string.h>
extern u8 D_800E0B94;
extern u8 D_800BEAC0, D_800BEAC1, D_800BEAC2, D_800BEAC3;
extern s32 D_80082FA0;
s32 func_151D87E0(u8 mask);
s32 func_15181CC8(s32 player);
s32 func_1517EF00(s32 player);
void *func_15167A68(s32 kind, s32 context, s32 bytes, s32 flag, u8 slot, u8 pool);
void func_1501C010(u8 player, u8 level);
extern s32 D_800BE9E4;
extern void (*D_8008FCC0[])(u8 *);
void func_1516972C(u8 *);
void func_1501C17C(u8 player);
void func_15169260(s32, s32, s32, u8);
extern u8 D_800AB300[];

s32 func_151D87E0(u8 mask) {
    u8 player;
    u8 index;
    for (player = 0; player < 4; player++) {
        if (mask & (1 << player)) {
            index = D_80084060[player];
            if (index >= 4) {
                return 0;
            }
            if (D_800BE944[index] != 0) {
                return 1;
            }
        }
    }
    return 0;
}

u8 *func_151D8868(u8 *owner, s32 payloadBytes, u8 slot, s32 context) {
    u8 validationPlayer;
    u8 player;
    u8 *record;

    if (D_800E0B94 != 0) {
        return NULL;
    }
    if (func_151D87E0(owner[5]) == 0) {
        return NULL;
    }
    if (D_800BEAC0 || D_800BEAC1 || D_800BEAC2 || D_800BEAC3) {
        return NULL;
    }
    for (validationPlayer = 0; validationPlayer <= D_80082FA0; validationPlayer++) {
        if (owner[5] & (1U << validationPlayer)) {
            if (func_15181CC8(validationPlayer) == 0 || func_1517EF00(validationPlayer) != 0) {
                return NULL;
            }
        }
    }
    record = func_15167A68(0x3F, context, payloadBytes + 0x18, 1, slot, 1);
    if (record == NULL) {
        return NULL;
    }
    memcpy(record + 0xE, owner, 8);
    for (player = 0; player < 4; player++) {
        if (record[0x13] & (1U << player)) {
            func_1501C010(player, owner[4]);
        }
    }
    record[0x16] = owner[4];
    return record;
}

void func_151D8A24(u8 *record) {
    u8 player;
    u8 expired = 0;

    if (record[0xE] & 1) {
        *(s16 *)(record + 0x10) = (s16)((u32)(s32)*(s16 *)(record + 0x10) - (u32)D_800BE9E4);
        if (*(s16 *)(record + 0x10) < 0) {
            expired = 1;
        }
    }
    if (*(s8 *)(record + 0x14) != -1) {
        D_8008FCC0[*(s8 *)(record + 0x14)](record);
    }
    if (record[0x12] != record[0x16]) {
        for (player = 0; player < 4; player++) {
            if (record[0x13] & (1U << player)) {
                func_1501C17C(player);
                func_1501C010(player, record[0x12]);
            }
        }
        record[0x16] = record[0x12];
    }
    if (expired) {
        func_1516972C(record);
    }
}

void func_151D8B24(u8 *owner) {
    u8 player;
    for (player = 0; player < 4; player++) {
        if (owner[0x13] & (1 << player)) {
            func_1501C17C(player);
        }
    }
}

s32 func_151D8B88(s32 arg0) {
    func_151D8B24((u8 *)arg0);
    func_15169804(arg0);
}

s32 func_151D8BB4(s32 arg0) {
    func_151D8B24((u8 *)arg0);
    func_15169824(arg0);
}

void func_151D8BE0(u8 *record) {
    func_151D8C00(record, (RecordDistanceLevel *)(record + 0x18));
}

void func_151D8C00(u8 *owner, RecordDistanceLevel *parameters) {
    f32 *origin;
    f32 delta[3];
    f32 distance;
    f32 level;

    origin = func_15144B34(parameters->player);
    delta[0] = parameters->x - origin[0];
    delta[1] = parameters->y - origin[1];
    delta[2] = parameters->z - origin[2];
    distance = func_15143E64(delta);
    if (distance < parameters->inner) {
        level = 1.0f;
    } else if (parameters->inner + parameters->width < distance) {
        level = 0.0f;
    } else {
        level = 1.0f - (distance - parameters->inner) * parameters->inverseWidth;
    }
    owner[0x12] = (u32)(level * 8.0f);
}

void func_151D8D5C(u8 *arg0, f32 arg1, u8 arg2) {
    if (arg2 == 0x58) {
        func_1516972C(arg0);
    } else if (arg2 == 0x47) {
        func_1516972C(arg0);
    }
}

void func_151D8DB4(s32 arg0, u8 arg1) {
    func_15169260((s32) D_800AB300, 1, arg0, arg1);
}

void func_151D8DE8(void) {
    D_800E0A00 = 1;
    func_151D8DB4(0, 0x58);
}
