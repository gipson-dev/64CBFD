#include <ultra64.h>
extern u8 *D_800D2E4C;
extern u8 *D_800DBEF4;
void func_1511650C(s32 arg0, s32 arg1, s32 arg2, f32 arg3);

/* Non-matching placeholders for the text-only asm slice asm/F4D20.s. */

void func_150C7870(s32 arg0) {
    if ((D_800D2E4C[0xA] & 8) == 0) {
        if ((D_800DBEF4[0x73] & 4) == 0) {
            func_1511650C(arg0, 1, 0x353, 1000.0f);
        } else {
            func_1511650C(arg0, 1, 0x43, 400.0f);
        }
    }
}

void func_150C78E0(u8 *arg0) {
    if (!(*(arg0 + 0x73) & 4)) {
        u8 *temp_v0 = D_800DBEF4;

        *(u32 *) (arg0 + 0x3C) = -(s32) (*(u32 *) (temp_v0 + 0x21C) & 0xFFFF0000) & 0xFFFF0000;
        func_151150BC(arg0);
    }
}

// Retail materializes and discards temp_v0 + 0x1E0 before the call.
#pragma GLOBAL_ASM("asm/nonmatchings/generated_F4D20/func_150C7930.s")

void func_150C7968(u8 *arg0) {
    func_15116110(arg0);
    if (!(*(arg0 + 0x73) & 4)) {
        u8 *state = D_800DBEF4;
        u8 *record = *(u8 **)(arg0 + 0x7C);
        s16 value = *(s16 *)(state + 0x21C);

        state += 0x1E0;
        if (record != NULL) {
            *(record + 0x13) = value >> 4;
        }
    }
}

s32 func_150C79BC() {
    return 0;
}

s32 func_150C7C90() {
    return 0;
}

s32 func_150C7D7C() {
    return 0;
}
