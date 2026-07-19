#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/1E73B0.s. */

s32 func_151B9F00() {
    return 0;
}

s32 func_151BA084() {
    return 0;
}

s32 func_151BA468() {
    return 0;
}

s32 func_151BA518() {
    return 0;
}

s32 func_151BB044() {
    return 0;
}

s32 func_151BB0E0() {
    return 0;
}

s32 func_151BB61C() {
    return 0;
}

s32 func_151BBA9C() {
    return 0;
}

s32 func_151BBEE4() {
    return 0;
}

s32 func_151BBFBC() {
    return 0;
}

s32 func_151BC074() {
    return 0;
}

s32 func_151BC104() {
    return 0;
}

s32 func_151BC370() {
    return 0;
}

s32 func_151BC580(u8 *arg0) {
    s32 *temp_v0 = *(s32 **) (arg0 + 0x40);

    if (*temp_v0 == 0) {
        return 0;
    }
    return 1;
}

s32 func_151BC5A4() {
    return 0;
}

s32 func_151BC64C() {
    return 0;
}

s32 func_151BC794() {
    return 0;
}

s32 func_151BCA90() {
    return 0;
}

s32 func_151BD21C() {
    return 0;
}

s32 func_151BD2BC() {
    return 0;
}

s32 func_151BD2F8() {
    return 0;
}

s32 func_151BD42C(u8 *arg0) {
    *(s16 *)(arg0 + 0x80) = 0;
    return 1;
}

s32 func_151BD43C() {
    return 0;
}

s32 func_151BD750() {
    return 0;
}

s32 func_151BD79C() {
    return 0;
}

s32 func_151BD7F4(u8 *arg0) {
    struct { u8 *ptr; u8 value; } temp;

    temp.ptr = arg0;
    temp.value = *(u8 *)(arg0 + 0x3B);
    func_151494E0(&temp, 0x3B);
}

s32 func_151BD828() {
    return 0;
}

s32 func_151BDD8C() {
    return 0;
}

s32 func_151BE0AC() {
    return 0;
}

s32 func_151BE138() {
    return 0;
}

s32 func_151BE1B8(s32 arg0) {
    func_151BE138(arg0);
    func_1514933C(arg0);
}

s32 func_151BE1E4(s32 arg0) {
    func_151BE138(arg0);
    func_15149368(arg0);
}

s32 func_151BE210() {
    return 0;
}

s32 func_151BE4B8() {
    return 0;
}

s32 func_151BE558() {
    return 0;
}

void func_151BE604(u8 *arg0, s32 arg1, u8 arg2) {
    func_15169850(arg1, arg2, (s32) (arg0 + 0x110), (s32) (arg0 + 0x114), (s32) arg0);
}

void func_151BE644(u8 *arg0) {
    u8 *temp_v0 = arg0 + 0x110;

    if (*(s32 *)(arg0 + 0x160) != 0) {
        u8 *temp_v1 = *(u8 **)(temp_v0 + 0x50) + 0x28;
        *(s32 *)(temp_v1 + (*(u8 *)(temp_v0 + 5) * 4) + 8) = 0;
    }
}

s32 func_151BE674(s32 arg0) {
    func_151BE644(arg0);
    func_1513CA6C(arg0);
}

s32 func_151BE6A0(s32 arg0) {
    func_151BE644(arg0);
    func_1513CAA0(arg0);
}

s32 func_151BE6CC() {
    return 0;
}

void func_151BE788(u8 *arg0, s32 arg1, u8 arg2) {
    func_15169850(arg1, arg2, (s32) (arg0 + 0x180), (s32) (arg0 + 0x184), (s32) arg0);
}

void func_151BE7C8(u8 *arg0) {
    u8 *temp_v0 = arg0 + 0x170;

    if (*(s32 *)(arg0 + 0x178) != 0) {
        u8 *temp_v1 = *(u8 **)(temp_v0 + 8) + 0x28;
        *(s32 *)(temp_v1 + (*(u8 *)(temp_v0 + 0xC) * 4) + 0x10) = 0;
    }
}

s32 func_151BE7F8(s32 arg0) {
    func_151BE7C8(arg0);
    func_151411A4(arg0);
}

s32 func_151BE824(s32 arg0) {
    func_151BE7C8(arg0);
    func_151411C4(arg0);
}

s32 func_151BE850() {
    return 0;
}

s32 func_151BEB20() {
    return 0;
}

s32 func_151BEC94(s32 arg0, s32 arg1, s32 arg2, s32 arg3, u8 *arg4) {
    *arg4 = 1;
    return arg0;
}

s32 func_151BECB8() {
    return 0;
}

s32 func_151BEE94() {
    return 0;
}

s32 func_151BEEE0() {
    return 0;
}

s32 func_151BF0C8() {
    return 0;
}

s32 func_151BF340() {
    return 0;
}

s32 func_151BF81C() {
    return 0;
}

s32 func_151BFB2C() {
    return 0;
}

s32 func_151BFBA4(s32 arg0) {
    func_151BFB2C(arg0);
    func_1514933C(arg0);
}

s32 func_151BFBD0(s32 arg0) {
    func_151BFB2C(arg0);
    func_15149368(arg0);
}

s32 func_151BFBFC() {
    return 0;
}
