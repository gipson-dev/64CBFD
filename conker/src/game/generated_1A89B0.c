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

s32 func_1517B7F8() {
    return 0;
}

s32 func_1517B89C() {
    return 0;
}

s32 func_1517BBAC() {
    return 0;
}

s32 func_1517CFC4() {
    return 0;
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
