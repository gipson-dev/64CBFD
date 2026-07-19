#include <ultra64.h>
extern u8 *D_800CC5EC;

/* Non-matching placeholders for the text-only asm slice asm/131620.s. */

s32 func_15104170() {
    return 0;
}

s32 func_151041E4() {
    return 0;
}

s32 func_1510448C() {
    return 0;
}

s32 func_151044F4(void) {
    u8 *temp_v1 = D_800CC5EC;

    if (temp_v1 != 0) {
        return temp_v1[0x7D];
    }
    return 0;
}
