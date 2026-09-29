#include <ultra64.h>
extern u8 *D_800CC5EC;
s32 func_1517F08C();
void *func_15167A68(s32, s32, s32, s32, u8, u8);

/* Non-matching placeholders for the text-only asm slice asm/131620.s. */

void func_15104170(s32 arg0, s32 arg1, s32 arg2) {
    u8 *temp_v0 = func_15167A68(0x64, 0, 0x20, 0, 0xFF, 1);

    if (temp_v0 != NULL) {
        *(s16 *) (temp_v0 + 0x18) = 0xF;
        temp_v0[0x1A] = 0;
        temp_v0[0x1B] = 0;
        *(s32 *) (temp_v0 + 0x10) = arg1;
        *(s32 *) (temp_v0 + 0x14) = arg2;
        temp_v0[0x1C] = arg0;
    }
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
