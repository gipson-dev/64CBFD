#include <ultra64.h>
#include "variables.h"
s32 func_1503EB78(s32, f32, f32, s32);
extern u8 D_800CC364[];
extern s32 *D_8008446C[];
void func_1503DF0C(s32, s32, s32, s32);
extern u8 D_800C6664[];
extern u8 D_800C6668[];
extern u8 D_80098914[];
extern s8 *D_80084454[];
extern void (*D_80084430[])(struct04 *, s32);
extern void (*D_8008443C[])(s32);
extern void (*D_80084448[])(s32);
s32 allocate_memory(s32, s32, s32, s32);
s32 func_1503E1F4(s32, s32);
s32 func_1503E3C4();
s32 func_1503EA54();
s32 func_1503E82C();

/* Non-matching placeholders for the text-only asm slice asm/6B320.s. */

void func_1503DE70(struct127 *actor, s32 group, s32 entry) {
    if (entry != -1) {
        func_1503DF0C(((s32)actor - (s32)D_800CC2D0) / (s32)sizeof(struct127),
            group, ((s32 (*)[2])D_8008446C[group])[entry][0], ((s32 (*)[2])D_8008446C[group])[entry][1]);
    } else {
        func_1503DF0C(((s32)actor - (s32)D_800CC2D0) / (s32)sizeof(struct127),
            group, -1, -1);
    }
}

void func_1503DF0C(s32 arg0, s32 arg1, s32 arg2, s32 arg3) {
    struct106 *ptr = &D_800C6660[arg0];

    ptr->unk4 |= arg2;
    ptr->unk8 |= arg3;
    ((u8 *) ptr)[0xE] = arg1;
    ptr->unkF = 2;
}

void func_1503DF48(s32 slot) {
    struct106 *record = &D_800C6660[slot];
    struct04 *element;
    struct04 *buffer;
    s8 *types;
    s32 state = record->unkF;
    s32 count;
    s32 index;

    if (state == 2) {
        D_800CC2D0[slot].unk74 |= 0x80;
        state = 3;
        if (D_800CC2D0[slot].unk1D4 == NULL) {
            return;
        }
    }
    if (state == 3) {
        count = D_80098914[((u8 *)record)[0xE]];
        if (record->unk0 == 0) {
            buffer = (struct04 *)allocate_memory(count * sizeof(struct04), 1, 0, 0);
            if (buffer == NULL) {
                return;
            }
            record->unk0 = (s32)buffer;
            for (index = 0; index < count; index++) {
                buffer[index].unk64 = 0;
            }
        }
        types = D_80084454[((u8 *)record)[0xE]];
        for (index = 0; index < count; index++) {
            switch (types[index]) {
            case -2:
                break;
            default:
                element = (struct04 *)record->unk0 + index;
                if (func_1503E1F4(index, slot) != 0 && element->unk64 == 0) {
                    func_1503E3C4(slot, index, 0, element, 0);
                    D_80084430[((u8 *)record)[0xE]](element, slot);
                    element->unk64 = 1;
                }
                break;
            }
        }
        D_8008443C[((u8 *)record)[0xE]](slot);
        state = 1;
        record->unkF = 1;
    }
    if (state == 1) {
        D_80084448[((u8 *)record)[0xE]](slot);
        if (record->unkF != 0) {
            func_1503EA54(slot);
            func_1503E82C(slot);
        }
    }
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
