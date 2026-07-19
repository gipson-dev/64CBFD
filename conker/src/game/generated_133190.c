#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/133190.s. */

extern void (*D_80088C28[])(u8 *, s32, u8);

s32 func_15105CE0() {
    return 0;
}

s32 func_1510608C() {
    return 0;
}

s32 func_151061E0(s32 arg0) {
    return arg0 + 0x88;
}

u8 *func_151061EC(u8 *arg0) {
    return arg0 + *(s32 *) (arg0 + 0x48) * 0x34 + 0x88;
}

s32 func_15106214() {
    return 0;
}

s32 func_151064B4() {
    return 0;
}

s32 func_151064DC() {
    return 0;
}

s32 func_15106510() {
    return 0;
}

f32 func_15106540(register f32 arg0) {
    return arg0 * arg0 * arg0;
}

s32 func_15106558() {
    return 0;
}

s32 func_15106584() {
    return 0;
}

s32 func_151065BC() {
    return 0;
}

s32 func_151065EC() {
    return 0;
}

s32 func_15106610() {
    return 0;
}

s32 func_151067B8() {
    return 0;
}

s32 func_15106E78() {
    return 0;
}

s32 func_15106EF8(s32 arg0) {
    func_15106E78(arg0);
    func_15169804(arg0);
}

s32 func_15106F24(s32 arg0) {
    func_15106E78(arg0);
    func_15169824(arg0);
}

void func_15106F50(u8 *arg0, s32 arg1, u8 arg2) {
    void (*callback)(u8 *, s32, u8) = D_80088C28[arg0[0x5C]];

    if (callback != NULL) {
        callback(arg0, arg1, arg2);
    }
}

s32 func_15106F98() {
    return 0;
}

s32 func_151070F8() {
    return 0;
}

s32 func_151072BC() {
    return 0;
}

void func_15107604(u8 *arg0) {
    u8 *temp_v0 = *(u8 **)(arg0 + 0x60);
    u8 *temp_v1 = *(u8 **)temp_v0 + 0x28;

    *(s32 *)(temp_v1 + 8) = 0;
}

s32 func_1510761C(u8 *arg0) {
    u8 *temp_a1 = arg0;

    if (*(s32 volatile *)(temp_a1 + 0x30) != 0) {
        func_1516972C(*(s32 volatile *)(temp_a1 + 0x30));
    }
}

s32 func_1510764C(s32 arg0) {
    func_1510761C(arg0);
    func_1514933C(arg0);
}

s32 func_15107678(s32 arg0) {
    func_1510761C(arg0);
    func_15149368(arg0);
}

s32 func_151076A4() {
    return 0;
}

s32 func_15107700() {
    return 0;
}

void func_151078E4(u8 *arg0, s32 arg1, u8 arg2) {
    u8 *target = *(u8 **) (arg0 + 0x60);

    func_15169850(arg1, arg2, (s32) target, (s32) (target + 4), (s32) arg0);
}

s32 func_15107924() {
    return 0;
}

s32 func_15107A20() {
    return 0;
}

s32 func_15107AE0() {
    return 0;
}

s32 func_15107B78() {
    return 0;
}

s32 func_15107C1C() {
    return 0;
}

s32 func_15107E48() {
    return 0;
}

s32 func_15107F54() {
    return 0;
}

s32 func_15107F98() {
    return 0;
}
