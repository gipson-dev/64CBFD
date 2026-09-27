#include <ultra64.h>
extern u8 D_800CC2D0[];

/* Non-matching placeholders for the text-only asm slice asm/FE850.s. */

s32 func_150D13A0() {
    return 0;
}

void func_150D1410(u8 *arg0) {
    u8 *temp_v0 = (u8 *) func_151149AC(0xF9);

    if (temp_v0 != 0) {
        if ((arg0 - D_800CC2D0) / 0x32C == 0) {
            temp_v0[0x6E] = 1;
        } else {
            temp_v0[0x6E] = 0;
        }
    }
}

void func_150D146C(u8 arg0) {
    u8 *temp_v0 = (u8 *) func_151149AC(0xF9);

    if (temp_v0 != 0) {
        temp_v0[0x6E] = 1;
    }
}

s32 func_150D149C() {
    return 0;
}
