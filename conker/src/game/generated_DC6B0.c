#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/DC6B0.s. */

s32 func_15131828();
s32 func_15131958();

s32 func_150AF200() {
    return 0;
}

s32 func_150AF2E0() {
    return 0;
}

s32 func_150AF328() {
    return 0;
}

s32 func_150AF6E4(u8 *arg0, s32 arg1) {
    u8 *temp_a2 = arg0 + 0xA8;

    func_15131828(arg0, arg0 + 0xAC, temp_a2, arg0 + 0xAA);
    func_15131958(arg0 + 0x58, *(s32 *) (temp_a2 + 0xC));
    return 1;
}

s32 func_150AF738() {
    return 0;
}

s32 func_150AF790() {
    return 0;
}

s32 func_150AF7C4() {
    return 0;
}

s32 func_150AFBF4() {
    return 0;
}

s32 func_150AFC68() {
    return 0;
}

s32 func_150AFDB0() {
    return 0;
}

s32 func_150AFE64() {
    return 0;
}

s32 func_150B003C() {
    return 0;
}

s32 func_150B0094() {
    return 0;
}

s32 func_150B02C0(u8 *arg0) {
    u8 *temp_a1 = arg0;

    if (*(s32 volatile *)(temp_a1 + 0x170) != 0) {
        func_1516972C(*(s32 volatile *)(temp_a1 + 0x170));
    }
}

s32 func_150B02F0(s32 arg0) {
    func_150B02C0(arg0);
    func_15132570(arg0);
}

s32 func_150B031C(s32 arg0) {
    func_150B02C0(arg0);
    func_1513259C(arg0);
}

s32 func_150B0348() {
    return 0;
}

s32 func_150B060C() {
    return 0;
}
