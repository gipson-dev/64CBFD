#include <ultra64.h>

#include "functions.h"
#include "variables.h"

typedef struct {
    u16 unused;
    u16 count;
    u32 reserved;
    u16 entries[8];
} DescriptorTagRow;

void *func_1502B5C8(s32 *size, u32 depth, ...);

/* Generated placeholder declarations. */
void func_150174C0(s32 adjustment);
/* End generated placeholder declarations. */

void func_15017300(s16 arg0, s16 arg1) {
    s32 i;
    s16 tmp;

    tmp = arg0;
    bzero(&D_800D2138, 524);
    D_800D2138 = tmp;

    for (i = 0; i < 16; i++) {
        if ((1 << i) & arg1) {
            func_15085710(i, 0, D_80087270[i]);
            D_800D2457 = D_800D2456 = 6;
            func_15085710(i, 5, D_8008726C);
            func_15085710(i, 2, D_80087260);
            if (D_800BE616 != 0) {
                func_15085710(i, 9, D_80087264);
            }
        }
        func_1501748C(arg1);
    }
    D_800D2340 = arg1;
    D_800D2132 = 0;
}

void func_1501748C(s16 arg0) {
}

void func_15017498(void) {
    bzero(&D_800D2138, 524);
}

/* Adjust tag-2 entries while retaining live descriptor table/count reloads. */
void func_150174C0(s32 adjustment) {
    s32 descriptorIndex;
    s32 entryIndex;

    for (descriptorIndex = 0; descriptorIndex < (s32)D_80087380; descriptorIndex++) {
        for (entryIndex = 0; entryIndex < ((DescriptorTagRow *)D_800D23C0)[descriptorIndex].count; entryIndex++) {
            u16 *entry = &((DescriptorTagRow *)D_800D23C0)[descriptorIndex].entries[entryIndex];
            u16 value = *entry;
            if ((value >> 12) == 2) {
                *entry = (u32)value + (u32)adjustment;
            }
        }
    }
}

void func_15017578(s32 arg0) {
    u32 tmp = 0;
    D_800D23C0 = func_1502B5C8((s32 *)&tmp, 3, 12, arg0, 4);
    D_80087380 = tmp / 24;
    func_150174C0(D_800DBF00);
}
