#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/19A8B0.s. */

s32 func_1516D400() {
    return 0;
}

s32 func_1516D4E8() {
    return 0;
}

s32 func_1516D678() {
    return 0;
}

s32 func_1516D738() {
    return 0;
}

s32 func_1516D99C() {
    return 0;
}

s32 func_1516DB90() {
    return 0;
}

s32 func_1516E778() {
    return 0;
}

s32 func_1516E8CC() {
    return 0;
}

s32 func_1516ECAC() {
    return 0;
}

s32 func_1516ED68() {
    return 0;
}

s32 func_1516EED4() {
    return 0;
}

s32 func_1516F024() {
    return 0;
}

s32 func_1516F1C0() {
    return 0;
}

s32 func_1516F2F8() {
    return 0;
}

s32 func_1516F548() {
    return 0;
}

s32 func_1516F864() {
    return 0;
}

void func_1516F8EC(u8 *arg0, u32 arg1) {
    s32 val = *(s8 *) (arg0 + 0x26);

    val = (val << 8) + *(arg0 + 0x27);
    val = val * arg1;
    *(s8 *) (arg0 + 0x26) = (val >> 8) >> 8;
    *(arg0 + 0x27) = val >> 8;
}

void func_1516F91C(u8 *arg0, u32 arg1) {
    s32 val = *(s8 *) (arg0 + 0x28);

    val = (val << 8) + *(arg0 + 0x29);
    val = val * arg1;
    *(s8 *) (arg0 + 0x28) = (val >> 8) >> 8;
    *(arg0 + 0x29) = val >> 8;
}

void func_1516F94C(u8 *arg0, u32 arg1) {
    func_1516F8EC(arg0, arg1);
    func_1516F91C(arg0, arg1);
}

void func_1516F984(u8 *arg0, u32 arg1) {
    func_1516F94C(arg0, arg1);
    *(s16 *) (arg0 + 0x18) = (s32) (*(s16 *) (arg0 + 0x18) * arg1) >> 8;
}

s32 func_1516F9C4() {
    return 0;
}

s32 func_1516FA88() {
    return 0;
}

s32 func_1516FBCC() {
    return 0;
}

s32 func_1516FD50() {
    return 0;
}

s32 func_1516FE1C() {
    return 0;
}

s32 func_15170034() {
    return 0;
}

s32 func_151700D8() {
    return 0;
}

s32 func_15170500() {
    return 0;
}

s32 func_151707E0() {
    return 0;
}

s32 func_151709B4() {
    return 0;
}
