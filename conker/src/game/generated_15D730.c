#include <ultra64.h>
extern s32 D_800BE9E4;

/* Non-matching placeholders for the text-only asm slice asm/15D730.s. */

s32 func_151318E8();

s32 func_15131918();
s32 func_15131958();

s32 func_151319C4();

s32 func_15130280() {
    return 0;
}

s32 func_15130374(s32 arg0, u8 arg1, s32 arg2, s32 arg3, s32 arg4) {
    return 0;
}

void func_151303BC(s32 arg0, u8 arg1, s32 arg2) {
    func_15130374(arg0, arg1, arg2, 0xFF, 0);
}

s32 func_151303EC() {
    return 0;
}

s32 func_15130A9C() {
    return 0;
}

s32 func_1513137C() {
    return 0;
}

s32 func_15131514() {
    return 0;
}

s32 func_1513164C() {
    return 0;
}

s32 func_151316AC(u8 *arg0, s32 arg1) {
    u8 *temp_a2 = arg0;

    func_151318E8(temp_a2 + 0x58, *(s32 *)(temp_a2 + 0xA8));
    return 1;
}

s32 func_151316DC(u8 *arg0, s32 arg1) {
    u8 *temp_a2 = arg0;

    func_15131918(temp_a2 + 0x58, *(s32 *)(temp_a2 + 0xA8));
    return 1;
}

s32 func_1513170C(u8 *arg0, s32 arg1) {
    u8 *temp_a2 = arg0;

    func_15131958(temp_a2 + 0x58, *(s32 *)(temp_a2 + 0xA8));
    return 1;
}

void func_1513173C() {
    func_15169804();
}

void func_1513175C() {
    func_15169824();
}

s32 func_1513177C() {
    return 0;
}

s32 func_151317C8() {
    return 0;
}

s32 func_15131814(s32 arg0, s32 arg1) {
    return 0;
}

s32 func_15131828() {
    return 0;
}

/* Retail signature is (f32 *, f32) but exact caller func_151316AC passes raw
   s32 bits and must not see that prototype; keep a placeholder in this TU. */
s32 func_151318E8() {
    return 0;
}

s32 func_15131918() {
    return 0;
}

s32 func_15131958() {
    return 0;
}

void func_151319A4(register u8 *arg0, register s32 arg1) {
    func_151319C4(arg0, arg1, arg0 + 0xA8);
}

s32 func_151319C4() {
    return 0;
}

void func_15131AFC(u8 *arg0, s32 arg1) {
    func_15131958(arg0 + 0x58, *(s32 *) (arg0 + 0xA8));
    func_151319C4(arg0, arg1, arg0 + 0xB0);
}

void func_15131B3C(u8 *arg0, s32 arg1) {
    func_15131918(arg0 + 0x58, *(s32 *) (arg0 + 0xA8));
    func_151319C4(arg0, arg1, arg0 + 0xB0);
}

s32 func_15131B7C() {
    return 0;
}

s32 func_15131C2C() {
    return 0;
}

s32 func_15131C84() {
    return 0;
}

s32 func_15131D4C() {
    return 0;
}

s32 func_15131D9C() {
    return 0;
}

s32 func_15131DEC() {
    return 0;
}

s32 func_15131EE4() {
    return 0;
}
