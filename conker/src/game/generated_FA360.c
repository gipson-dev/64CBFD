#include <ultra64.h>
extern f32 D_800A07A4;
extern u8 *D_80088870;

/* Non-matching placeholders for the text-only asm slice asm/FA360.s. */

s32 func_150CCEB0() {
    return 0;
}

s32 func_150CD17C() {
    return 0;
}

s32 func_150CD59C() {
    return 0;
}

s32 func_150CD7F8() {
    return 0;
}

void func_150CDB6C(s32 arg0) {
    if (arg0 >= 0) {
        if (arg0 < 0x100) {
            u8 *temp_v0 = D_80088870;

            if (temp_v0 != 0) {
                u8 *temp_v1 = temp_v0 + 0x28;

                *(f32 *) (temp_v1 + 4) = arg0 * D_800A07A4;
            }
        }
    }
}
