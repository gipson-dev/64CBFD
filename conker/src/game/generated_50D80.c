#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/50D80.s. */

typedef struct {
    s32 unk0;
    s32 unk4;
    u8 unk8;
    u8 pad9;
    u16 unkA;
} Struct15024130;

extern Struct15024130 *D_800C3D50;
s32 func_1502A8A0();

void func_150238D0() {
}

s32 func_150238D8() {
    return 0;
}

s32 func_15023BB0() {
    return 0;
}

s32 func_15023DE0() {
    return 0;
}

void func_15024130(s32 count, s32 arg1) {
    s32 i;

    for (i = 0; i < count; i++) {
        Struct15024130 *entry = &D_800C3D50[i];

        func_1502A8A0(entry->unk0, entry->unk8, entry->unkA, entry->unk4, arg1);
    }
}

extern u16 D_800C3C9A;

/* Insert a record before the first equal or greater sort key. */
void func_150241B4(Struct15024130 *entries, s32 *count, s32 value,
                   s32 tag, s32 parameter, s32 priority, s32 context) {
    s32 size = *count;
    s32 index = size;
    s32 i;
    if (size >= D_800C3C9A) {
        func_15024130(size, context);
        *count = 0;
        return;
    }
    for (i = 0; i < size; i++) {
        if (entries[i].unk4 >= priority) {
            index = i;
            break;
        }
    }
    for (i = size - 1; i >= index; i--) entries[i + 1] = entries[i];
    entries[index].unk0 = value;
    entries[index].unk8 = tag;
    entries[index].unk4 = priority;
    entries[index].unkA = parameter;
    *count = *count + 1;
}

s32 func_150242F8() {
    return 0;
}

s32 func_1502460C() {
    return 0;
}

s32 func_150265CC() {
    return 0;
}

s32 func_15029BB8() {
    return 0;
}

s32 func_1502A8A0() {
    return 0;
}
