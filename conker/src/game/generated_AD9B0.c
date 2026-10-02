#include <ultra64.h>
#include "variables.h"

extern u8 D_800BE580[];
extern u8 D_800D1941;
extern u8 *D_800D199C;

/* Non-matching placeholders for the text-only asm slice asm/AD9B0.s. */

s32 func_15080500() {
    return 0;
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_AD9B0/func_15080620.s")

void func_150806A8(s32 index) {
    struct127 *object = &D_800CC2D0[index];
    u8 *state = (u8 *) object->unk31C;
    u8 first_value = state[0x74];
    u8 second_value;

    if ((first_value != 0) && !(first_value & 0x80)) {
        state[0x74] = 0;
        state = (u8 *) object->unk31C;
    }

    second_value = state[0x75];
    if ((second_value != 0) && !(second_value & 0x80)) {
        state[0x75] = 0;
    }
}

void func_15080718(register s32 arg0, s32 *arg1, s32 *arg2) {
    *arg2 = 1 << (arg0 & 7);
    *arg1 = arg0 >> 3;
}

s32 func_15080738(arg0)
s32 arg0;
{
    s32 spA;
    s32 spB;

    func_15080718(arg0, &spA, &spB);
    if (D_800BE580[spA] & spB) {
        return 1;
    }
    return 0;
}

void func_15080784(void) {
    u16 *sequence = (u16 *)D_800D1998;

    if ((sequence != NULL) && (D_800D1994 != D_800D1995)) {
        s32 value = sequence[D_800D1994];

        if (value != 0) {
            func_1001263C(value, 0x7FFF, 0x40);
        }
        D_800D1994++;
    }
}

void func_150807F4(u8 arg0, u8 arg1, s32 arg2) {
    if (arg2 == 0x20) {
        func_15080784();
    }
}

s32 func_15080828() {
    return 0;
}

void func_15080BE8(void) {
    D_800D1941 = 0;
    func_1516D2E0(D_800D1950);
    func_10004074(D_800D1944);

    if (D_800D1948 != 0) {
        func_10004074(D_800D1948);
        func_10004074(D_800D194C);
        func_10004074(D_800D1998);
        D_800D1948 = 0;
    }

    func_151F2D6C(0, 0x5622);
}

void func_15080C64(void) {
    if (D_800D1941 == 0) {
        return;
    }

    if (((u8 *)D_800D1950)[0x15] != 0) {
        return;
    }

    func_15080BE8();
    if ((D_800BE9F0 != 0x29) && (D_800BE9F0 != 0x2E)) {
        D_800D2E60[8] |= 0x10;
    }

    if (D_800D199C != NULL) {
        D_800D199C[0x14] = 1;
        D_800D199C = NULL;
    }
}

s32 func_15080CF4(void) {
    if (D_800D1941 == 0) {
        return 1;
    }
    return 0;
}
