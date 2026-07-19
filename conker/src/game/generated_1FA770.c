#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/1FA770.s. */

s32 func_151D10E4();
s32 func_151D13E0();

s32 func_151CD2C0() {
    return 0;
}

void func_151CD35C(s32 arg0) {
    s32 value;

    if ((arg0 >= 0) && (arg0 < 4)) {
        value = arg0;
        func_151494E0(&value, 0x17);
    }
}

void func_151CD394(s32 arg0) {
    s32 value;

    if ((arg0 >= 0) && (arg0 < 4)) {
        value = arg0;
        func_151494E0(&value, 0x18);
    }
}

s32 func_151CD3CC() {
    return 0;
}

s32 func_151CD4C0() {
    return 0;
}

s32 func_151CD674() {
    return 0;
}

s32 func_151CD7BC() {
    return 0;
}

s32 func_151CDB94() {
    return 0;
}

s32 func_151CDE20() {
    return 0;
}

void func_151CE47C(u8 *arg0) {
    *(u8 *)(arg0 + 0x30) = 0;
    *(u16 *)(arg0 + 0x1E) &= ~2;
    *(u16 *)(arg0 + 0x1E) |= 8;
}

void func_151CE49C(u8 *arg0) {
    s32 value = *(s32 *) (*(u8 **) (arg0 + 0x98) + 0x48);

    func_151494E0(&value, 0x23);
    func_151478F4(arg0);
}

void func_151CE4DC(u8 *arg0) {
    s32 value = *(s32 *) (*(u8 **) (arg0 + 0x98) + 0x48);

    func_151494E0(&value, 0x23);
    func_15147928(arg0);
}

s32 func_151CE51C() {
    return 0;
}

s32 func_151CE634() {
    return 0;
}

s32 func_151CE6D0() {
    return 0;
}

s32 func_151CEA20() {
    return 0;
}

s32 func_151CEAAC() {
    return 0;
}

s32 func_151CEC10() {
    return 0;
}

s32 func_151CEC54() {
    return 0;
}

s32 func_151CF120() {
    return 0;
}

s32 func_151CF380() {
    return 0;
}

s32 func_151CF844() {
    return 0;
}

s32 func_151CF898() {
    return 0;
}

s32 func_151CFA4C() {
    return 0;
}

s32 func_151D0024(u8 *arg0) {
    struct { u8 *ptr; u8 value; } temp;

    temp.ptr = arg0;
    temp.value = *(u8 *)(arg0 + 0x3B);
    func_151494E0(&temp, 0x18);
}

s32 func_151D0058() {
    return 0;
}

void func_151D0128(u8 *arg0) {
    u8 *temp_v0 = *(u8 **)(arg0 + 0x28);
    u16 temp_t7 = *(u16 *)(arg0 + 0x2E);
    s16 temp_t8 = -1;

    if (*(u16 *)(temp_v0 + 0x84) != temp_t7) {
        *(s16 *)(arg0 + 0xE) = temp_t8;
    }
}

s32 func_151D014C() {
    return 0;
}

s32 func_151D08F0() {
    return 0;
}

s32 func_151D09A8() {
    return 0;
}

s32 func_151D0ED8(u8 *arg0) {
    u8 *temp_a1 = arg0;

    if (*(s32 *)(temp_a1 + 0xA8) != 0) {
        func_1516972C(*(s32 *)(temp_a1 + 0xA8));
    }
}

s32 func_151D0F08(s32 arg0) {
    func_151D0ED8(arg0);
    func_1513173C(arg0);
}

s32 func_151D0F34(s32 arg0) {
    func_151D0ED8(arg0);
    func_1513175C(arg0);
}

s32 func_151D0F60() {
    return 0;
}

s32 func_151D1074() {
    return 0;
}

void func_151D10A4(s32 arg0, s32 arg1) {
    func_151D10E4(arg0, arg1, 0);
}

void func_151D10C4(s32 arg0, s32 arg1) {
    func_151D10E4(arg0, arg1, 1);
}

s32 func_151D10E4() {
    return 0;
}

s32 func_151D1138() {
    return 0;
}

void func_151D1328(u8 *arg0, s32 arg1, u8 arg2) {
    func_15169850(arg1, arg2, (s32) (arg0 + 0x28), (s32) (arg0 + 0x2C), (s32) arg0);
}

void func_151D1368() {
    func_151D13E0();
}

s32 func_151D1388(s32 arg0) {
    func_151D1368(arg0);
    func_1514933C(arg0);
}

s32 func_151D13B4(s32 arg0) {
    func_151D1368(arg0);
    func_15149368(arg0);
}

s32 func_151D13E0() {
    return 0;
}

s32 func_151D1448() {
    return 0;
}

s32 func_151D15D0() {
    return 0;
}

s32 func_151D197C() {
    return 0;
}

s32 func_151D1C98() {
    return 0;
}

void func_151D223C(u8 *arg0) {
    u8 *temp_v0 = *(u8 **)(arg0 + 0x98);
    u8 *temp_v1 = *(u8 **)temp_v0;

    if (temp_v1 != NULL) {
        *(s32 *)(temp_v1 + 0x30) = 0;
    }
}

s32 func_151D2258(s32 arg0) {
    func_151D223C(arg0);
    func_151478F4(arg0);
}

s32 func_151D2284(s32 arg0) {
    func_151D223C(arg0);
    func_15147928(arg0);
}

s32 func_151D22B0() {
    return 0;
}
