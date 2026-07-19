#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/1CA420.s. */

extern s32 D_800E0920;
s32 func_1514933C();

void func_1519CF70(u8 arg0) {
    u8 value = arg0;

    func_15147D64(&value, 6);
}

void func_1519CFA0(u8 *arg0) {
    u8 *temp_v0 = *(u8 **) (arg0 + 0x98);

    *(u16 *) (arg0 + 0x1E) &= 0xFFFD;
    *(arg0 + 0x30) = 0;
    *(temp_v0 + 6) |= 1;
    *(temp_v0 + 6) |= 4;
}

void func_1519CFD0(u8 *arg0) {
    u8 *temp_v0 = *(u8 **) (arg0 + 0x98);

    func_1514EDF0(arg0, *(s32 *) temp_v0);
    func_151478F4(arg0);
}

void func_1519D000(u8 *arg0) {
    u8 *temp_v0 = *(u8 **) (arg0 + 0x98);

    func_1514EDF0(arg0, *(s32 *) temp_v0);
    func_15147928(arg0);
}

s32 func_1519D030() {
    return 0;
}

s32 func_1519D240() {
    return 0;
}

s32 func_1519D454() {
    return 0;
}

s32 func_1519D9F4() {
    return 0;
}

s32 func_1519E1F4() {
    return 0;
}

s32 func_1519E304() {
    return 0;
}

s32 func_1519E3BC() {
    return 0;
}

s32 func_1519E464() {
    return 0;
}

s32 func_1519E570() {
    return 0;
}

s32 func_1519E61C() {
    return 0;
}

void func_1519E65C(u8 arg0) {
    func_1519CF70(3);
    func_1519CF70(4);
}

void func_1519E688(void) {
    func_1519CF70(3);
    func_1519CF70(4);
    func_15147D64(0, 9);
}

s32 func_1519E6BC() {
    return 0;
}

s32 func_1519E754() {
    return 0;
}

s32 func_1519E818() {
    return 0;
}

s32 func_1519E8CC(u8 *arg0) {
    func_1514EDF0(arg0, *(s32 *)(arg0 + 0x28));
    func_1514933C(arg0);
}

s32 func_1519E8F8(u8 *arg0) {
    func_1514EDF0(arg0, *(s32 *)(arg0 + 0x28));
    func_15149368(arg0);
}

void func_1519E924(void) {
    D_800E0920 = 0;
    func_1514933C();
}

void func_1519E948(void) {
    D_800E0920 = 0;
    func_15149368();
}
