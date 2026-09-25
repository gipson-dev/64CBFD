#include <ultra64.h>

#include "functions.h"
#include "variables.h"

/* Generated placeholder declarations. */
s32 func_150174C0(s32 arg0);
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

s32 func_150174C0(s32 arg0) {
    s32 descriptor_index;
    s32 entry_index;
    s32 descriptor;
    s32 entry;
    u16 value;

    for (descriptor_index = 0; descriptor_index < D_80087380; descriptor_index++) {
        descriptor = D_800D23C0 + descriptor_index * 24;
        for (entry_index = 0; entry_index < *(u16 *) (descriptor + 2); entry_index++) {
            entry = descriptor + 8 + entry_index * 2;
            value = *(u16 *) entry;
            if ((value >> 12) == 2) {
                *(u16 *) entry = value + arg0;
            }
        }
    }

    return descriptor_index;
}

void func_15017578(s32 arg0) {
    u32 tmp = 0;
    D_800D23C0 = func_1502B5C8(&tmp, 3, 12, arg0, 4);
    D_80087380 = tmp / 24;
    func_150174C0(D_800DBF00);
}
