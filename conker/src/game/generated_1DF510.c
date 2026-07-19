#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/1DF510.s. */

s32 func_151B222C();

s32 func_151B2060() {
    return 0;
}

s32 func_151B2100() {
    return 0;
}

void func_151B220C() {
    func_151B222C();
}

s32 func_151B222C() {
    return 0;
}

s32 func_151B229C(s32 arg0) {
    func_151B220C(arg0);
    func_1514933C(arg0);
}

s32 func_151B22C8(s32 arg0) {
    func_151B220C(arg0);
    func_15149368(arg0);
}

s32 func_151B22F4() {
    return 0;
}

s32 func_151B2348() {
    return 0;
}

s32 func_151B2690() {
    return 0;
}

void func_151B2950(u8 *arg0) {
    u8 *temp_v0 = *(u8 **)(arg0 + 0x178);

    if (temp_v0 != NULL) {
        *(s32 *)(temp_v0 + (*(u8 *)(arg0 + 0x17C) * 4) + 0x38) = 0;
    }
}

s32 func_151B2974() {
    return 0;
}

void func_151B2EC4(u8 *arg0, s32 arg1, u8 arg2) {
    func_15169850(arg1, arg2, (s32) (arg0 + 0x28), (s32) (arg0 + 0x2C), (s32) arg0);
}

s32 func_151B2F04() {
    return 0;
}

s32 func_151B2FA0() {
    return 0;
}

void func_151B2FD0(u8 *arg0) {
    u8 *temp_v0 = *(u8 **)(arg0 + 0x4C);

    if (temp_v0 != NULL) {
        *(s32 *)(temp_v0 + 0x44) = 0;
    }
}

s32 func_151B2FE8(s32 arg0) {
    func_151B2FD0(arg0);
    func_1514933C(arg0);
}

s32 func_151B3014(s32 arg0) {
    func_151B2FD0(arg0);
    func_15149368(arg0);
}

s32 func_151B3040() {
    return 0;
}
