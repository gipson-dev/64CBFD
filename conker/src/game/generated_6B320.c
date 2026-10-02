#include <ultra64.h>
#include "variables.h"
s32 func_1503EB78(s32, f32, f32, s32);
extern u8 D_800CC364[];
extern s32 *D_8008446C[];
extern u8 D_800C6664[];
extern u8 D_800C6668[];

/* Non-matching placeholders for the text-only asm slice asm/6B320.s. */

s32 func_1503DE70() {
    return 0;
}

void func_1503DF0C(s32 arg0, s32 arg1, s32 arg2, s32 arg3) {
    struct106 *ptr = &D_800C6660[arg0];

    ptr->unk4 |= arg2;
    ptr->unk8 |= arg3;
    ((u8 *) ptr)[0xE] = arg1;
    ptr->unkF = 2;
}

s32 func_1503DF48() {
    return 0;
}

s32 func_1503E1F4(s32 bit, s32 index) {
    if (bit < 0x20) {
        if ((D_800C6660[index].unk4 & (1 << bit)) != 0) {
            return 1;
        }
    } else if ((D_800C6660[index].unk8 & (1 << bit)) != 0) {
        return 1;
    }

    return 0;
}

s32 func_1503E260() {
    return 0;
}

s32 func_1503E3C4() {
    return 0;
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_6B320/func_1503E5F8.s")

s32 func_1503E82C() {
    return 0;
}

s32 func_1503EA54() {
    return 0;
}

s32 func_1503EB78(s32 arg0, f32 arg1, f32 arg2, s32 arg3) {
    return 0;
}

s32 func_1503ECA0() {
    return 0;
}

void func_1503EEB8() {
}

s32 func_1503EEC0(s32 index) {
    struct106 *entry;
    s32 value;

    func_1503ECA0(index);
    entry = &D_800C6660[index];
    value = *(s16 *)((u8 *)entry + 0xC) - D_800BE9E4;
    *(s16 *)((u8 *)entry + 0xC) = value;

    if (value <= 0) {
        func_15060F28(&D_800CC2D0[index], 1);
    }
}

s32 func_1503EF4C(s32 arg0, s32 arg1, s32 arg2) {
    s32 *base;
    s32 *entry;
    s32 first;
    s32 entry_offset;
    s32 mask_offset;

    base = D_8008446C[arg0];
    entry_offset = arg1 * 8;
    mask_offset = arg2 * 0x10;
    entry = (s32 *) ((u8 *) base + entry_offset);
    first = entry[0];

    if (first == 0 ||
            (*(s32 *) (D_800C6664 + mask_offset) & first) != 0) {
        s32 second = entry[1];

        if (second == 0 ||
                (*(s32 *) (D_800C6668 + mask_offset) & second) != 0) {
            return 1;
        }
    }
    return 0;
}

s32 func_1503EFC4() {
    return 0;
}

void func_1503F078(s32 arg0, u8 arg1) {
    func_1503EB78(arg0, 2.0f, 2.0f, 0);
}

void func_1503F0AC(s32 arg0, u8 arg1) {
    func_1503EB78(arg0, 1.0f, 2.0f, 1);
}

void func_1503F0D8(s32 arg0, u8 arg1) {
    func_1503EB78(arg0, 2.06f, 3.0f, 1);
}

void func_1503F108(s32 arg0) {
    struct106 *entry = &D_800C6660[arg0];

    *(s16 *) ((u8 *) entry + 0xC) = 0x8C;
    *(s32 *) (D_800CC364 + arg0 * sizeof(struct127)) = 6;
    *(f32 *) (entry->unk0 + 0x1EC) = 10.0f;
}

s32 func_1503F16C() {
    return 0;
}

s32 func_1503F2B0() {
    return 0;
}

s32 func_1503F404() {
    return 0;
}
