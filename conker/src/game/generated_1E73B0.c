#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/1E73B0.s. */

extern s32 D_800BE9E4;
extern f32 D_800AA860;
extern f32 D_800AA864;
extern f32 D_800AA82C;
extern s32 D_800AA760;
extern s32 D_800AA76C;

s32 func_15160CDC(s32 arg0, s32 arg1, s32 *arg2, s32 *arg3, f32 arg4, s32 arg5, s32 arg6, s32 arg7, s32 arg8, s32 arg9, s32 arg10, s32 arg11, s32 arg12, s32 arg13, s32 arg14, s32 arg15);

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

s32 func_151BC074(s32 arg0) {
    if (arg0 != 0) {
        return func_15160CDC(arg0, 1, &D_800AA760, &D_800AA76C, D_800AA82C, 2, 0x12C, 0xFF, 0xFF, 0xFF, 0xFF, 1, 0, 0, 0xFF, 1);
    }
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

s32 func_151BD2BC(u8 *arg0) {
    u8 *temp_v0 = *(u8 **) (arg0 + 0x28);

    if (*(s32 *) temp_v0 == 0) {
        return 0;
    }
    if (*(arg0 + 0x2C) != *(temp_v0 + 0x3B)) {
        return 0;
    }
    return 1;
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

f32 func_151BD750(u8 *arg0) {
    s16 temp_v0 = *(s16 *)(arg0 + 0x80);
    f32 result = (f32) temp_v0 * 2.0f * D_800AA860 + D_800AA864;

    *(s16 *)(arg0 + 0x80) = temp_v0 + D_800BE9E4;
    return result;
}

s32 func_151BD79C(u8 *arg0) {
    u8 *temp_v0 = *(u8 **)(arg0 + 0xB0);

    if (*(s32 *) temp_v0 != 0 && *(u8 *)(temp_v0 + 4) != 0xFF) {
        *(f32 *)(arg0 + 0x4C) = *(f32 *)(temp_v0 + 0x14);
        *(f32 *)(arg0 + 0x50) = *(f32 *)(temp_v0 + 0x18);
        *(f32 *)(arg0 + 0x54) = *(f32 *)(temp_v0 + 0x1C);
    }
    return func_1513170C(arg0);
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

s32 func_151BE0AC(u8 *arg0, u8 *arg1, u8 arg2) {
    if (arg2 == 0x3B) {
        if (*(s32 *)(arg0 + 0x28) == *(s32 *)(arg1 + 0) || *(u8 *)(arg0 + 0x2C) == *(u8 *)(arg1 + 4)) {
            func_1516972C(arg0);
        }
    } else {
        func_15169850(arg1, arg2, (s32) (arg0 + 0x28), (s32) (arg0 + 0x2C), (s32) arg0);
    }
}

s32 func_151BE138(u8 *arg0) {
    if (*(s32 *)(arg0 + 0x30) != 0) {
        func_1516972C(*(s32 *)(arg0 + 0x30));
    }
    if (*(s32 *)(arg0 + 0x34) != 0) {
        func_1516972C(*(s32 *)(arg0 + 0x34));
    }
    if (*(s32 *)(arg0 + 0x38) != 0) {
        func_1516972C(*(s32 *)(arg0 + 0x38));
    }
    if (*(s32 *)(arg0 + 0x3C) != 0) {
        func_1516972C(*(s32 *)(arg0 + 0x3C));
    }
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

s32 func_151BEE94(u8 *arg0) {
    s32 temp_v0 = 0xFF;

    if (temp_v0 == *(arg0 + 0x127)) {
        return 0;
    }
    if (*(s32 *) arg0 == 0) {
        return 0;
    }
    if (temp_v0 == *(arg0 + 4)) {
        return 0;
    }
    return 1;
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

s32 func_151BFB2C(u8 *arg0) {
    s32 i;

    if (*(s32 *)(arg0 + 0x28) != 0) {
        func_1516972C(*(s32 *)(arg0 + 0x28));
    }
    for (i = 0; i < 2; i++) {
        if (*(s32 *)(arg0 + 0x2C + i * 4) != 0) {
            func_1516972C(*(s32 *)(arg0 + 0x2C + i * 4));
        }
    }
}

s32 func_151BFBA4(s32 arg0) {
    func_151BFB2C(arg0);
    func_1514933C(arg0);
}

s32 func_151BFBD0(s32 arg0) {
    func_151BFB2C(arg0);
    func_15149368(arg0);
}

void func_151BFBFC(u8 *arg0, u8 arg1, u8 arg2) {
    if (arg2 == 0x57) {
        func_1516972C(arg0);
    }
}
