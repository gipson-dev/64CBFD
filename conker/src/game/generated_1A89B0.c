#include <ultra64.h>
#include "structs.h"

/* Non-matching placeholders for the text-only asm slice asm/1A89B0.s. */

extern s16 D_800DD470[];
extern u8 D_8008CEB0[];

typedef struct {
    s16 unk0;
    s16 unk2;
    s16 unk4;
    u8 unk6;
    u8 pad7;
    s16 unk8;
    s16 unkA;
    f32 unkC;
} PositionQueueEntry;

extern PositionQueueEntry D_800DDD28[];
extern struct108 *D_800DBFF0;
extern u8 D_800DDD1C;

s32 func_1517B500() {
    return 0;
}

s32 func_1517B6E8() {
    return 0;
}

s32 func_1517B7A8(s16 *arg0, s16 *arg1, s32 *arg2, s32 arg3) {
    s32 temp_v0 = *arg2;

    if (temp_v0 >= 0x300) {
        if (temp_v0 >= 0x501) {
            *arg2 = temp_v0 - 0x200;
        } else {
            *arg2 = 0x300;
        }
    }
    arg1[0] = arg0[0];
    arg1[1] = arg0[1];
    arg1[2] = arg0[2];
    return 0;
}

/* Apply the quadratic Y offset and advance the position callback counter. */
s32 func_1517B7F8(s16 *input, s16 *output, s32 *counter, s32 unused) {
    s32 offset;

    if (*counter >= 0xD00) {
        return 1;
    }
    if (*counter >= 0x100) {
        offset = *counter - 0x600;
        offset = 0x190000 - offset * offset;
        output[1] = input[1] + offset / 0x1E00;
        if (*counter >= 0x200) {
            if (*counter >= 0xA01) {
                *counter -= 0x800;
            } else {
                *counter = 0x200;
            }
        }
    } else {
        output[1] = input[1];
    }
    output[0] = input[0];
    output[2] = input[2];
    return 0;
}

s32 func_1517B89C() {
    return 0;
}

s32 func_1517BBAC() {
    return 0;
}

/* Private view of the pending pointer in each 16-byte record. */
typedef struct {
    u8 reserved00[8];
    void *pending;
    u8 reserved0C[4];
} PendingRecord1A89B0;

extern s32 D_800DDA90;
extern s32 D_800DD478;
extern u32 D_8003809C;
s32 func_10006240(void *, void *, u32);
void func_10004074(void *);

/* Process present destinations, then consume each nonempty pending slot. */
void func_1517CFC4(void) {
    PendingRecord1A89B0 *record;
    s32 index;
    void *destination;

    record = (PendingRecord1A89B0 *)&D_800DDA90;
    for (index = 0; index != 15; index++) {
        if (record->pending != NULL) {
            destination = ((void **)&D_800DD478)[index * 26];
            if (destination != NULL) {
                func_10006240(record->pending, destination, D_8003809C);
                func_10004074(record->pending);
            }
            record->pending = NULL;
        }
        record++;
    }
}

s32 func_1517D074() {
    return 0;
}

void func_1517D578(s16 arg0, s16 arg1, s16 arg2, f32 arg3, s32 arg4, s32 arg5, u8 arg6) {
    register s16 x;
    register s16 y;
    register s16 z;
    PositionQueueEntry *entry;
    u8 index;

    x = arg0;
    y = arg1;
    z = arg2;
    index = D_8008CEB0[0];
    if (index < 3) {
        entry = &D_800DDD28[index];
        entry->unk0 = x;
        entry->unk2 = y;
        entry->unk4 = z;
        entry->unkC = arg3;
        D_8008CEB0[0] = index + 1;
        entry->unk8 = arg4;
        entry->unkA = arg5;
        entry->unk6 = arg6;
    }
}

void func_1517D5FC(s16 arg0, s16 arg1, s16 arg2, s32 arg3, s32 arg4, s32 arg5) {
    func_1517D578(arg0, arg1, arg2, D_800DBFF0[arg3].unk380,
                 arg4, arg5, D_800DDD1C >> 3);
}

s32 func_1517D690() {
    return 0;
}

s32 func_1517D7B0() {
    return 0;
}

s32 func_1517DE5C() {
    return 0;
}

void func_1517E05C(s32 arg0, s32 arg1, s32 arg2) {
    D_800DD470[0] = arg0;
    D_800DD470[1] = arg1;
    D_800DD470[2] = arg2;
}
