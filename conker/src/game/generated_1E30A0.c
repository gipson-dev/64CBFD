#include <ultra64.h>
void func_100111C8(u16 arg0);

/* Non-matching placeholders for the text-only asm slice asm/1E30A0.s. */

s32 func_151B5BF0() {
    return 0;
}

s32 func_151B5E94() {
    return 0;
}

void func_151B5FCC(u8 *arg0) {
    s32 temp_v0 = *(s32 *) (arg0 + 0x88);

    if (temp_v0 != 0) {
        func_100111C8(temp_v0);
        *(s32 *) (arg0 + 0x88) = 0;
    }
}
