#include <ultra64.h>
extern u8 *D_800CC5EC;
s32 func_1517F08C();

/* Non-matching placeholders for the text-only asm slice asm/131620.s. */

s32 func_15104170() {
    return 0;
}

s32 func_151041E4() {
    return 0;
}

s32 func_1510448C(s32 arg0, u8 *arg1, s16 arg2) {
    s16 gate = arg2;
    u8 **record = &arg1;
    s32 value;

    if ((gate != 0) || ((value = (*record)[0x1B]) == 0)) {
        return arg0;
    }
    return func_1517F08C(arg0, ((value << 6) - value) >> 8, 0, 0, 0, arg2);
}

s32 func_151044F4(void) {
    u8 *temp_v1 = D_800CC5EC;

    if (temp_v1 != 0) {
        return temp_v1[0x7D];
    }
    return 0;
}
