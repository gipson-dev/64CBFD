#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/1ED0F0.s. */

s32 func_151BFC40() {
    return 0;
}

s32 func_151BFDA0() {
    return 0;
}

s32 func_151BFE84() {
    return 0;
}

s32 func_151C0098() {
    return 0;
}

s32 func_151C02E4() {
    return 0;
}

s32 func_151C0360() {
    return 0;
}

s32 func_151C0418() {
    return 0;
}

s32 func_151C04F8() {
    return 0;
}

s32 func_151C05A4() {
    return 0;
}

s32 func_151C05F0() {
    return 0;
}

s32 func_151C0644() {
    return 0;
}

s32 func_151C0698() {
    return 0;
}

s32 func_151C110C() {
    return 0;
}

s32 func_151C1180() {
    return 0;
}

s32 func_151C1570() {
    return 0;
}

s32 func_151C15FC(s32 arg0) {
    func_151C1570(arg0);
    func_15132570(arg0);
}

s32 func_151C1628(s32 arg0) {
    func_151C1570(arg0);
    func_1513259C(arg0);
}

s32 func_151C1654() {
    return 0;
}

s32 func_151C1798() {
    return 0;
}

void func_151C1814(u8 *arg0, s32 *arg1, u8 arg2) {
    u8 *temp_v0 = arg0 + 0x170;

    if (arg2 == 0x2D) {
        s32 temp_v1 = arg1[0];
        s32 temp_a2 = *(s32 *) (temp_v0 + 0x6C);

        if (temp_v1 == temp_a2) {
            *(s32 *) (temp_v0 + 0x6C) = arg1[1];
            return;
        }
        if (temp_a2 == arg1[1]) {
            *(s32 *) (temp_v0 + 0x6C) = temp_v1;
        }
    }
}

s32 func_151C1860() {
    return 0;
}

void func_151C1940(s32 arg0, s32 arg1, s32 *arg2) {
    func_151C02E4(arg0, arg1, arg2[0], &arg2[1]);
}

s32 func_151C196C() {
    return 0;
}

s32 func_151C1D5C() {
    return 0;
}

s32 func_151C1FB8() {
    return 0;
}
