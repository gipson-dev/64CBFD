#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/1228D0.s. */

s32 func_150F55C8();

s32 func_15179008();

s32 func_150F5420() {
    return 0;
}

void func_150F5590(u8 *arg0) {
    s32 val = 0x1000 - (*(s16 *) (arg0 + 0x24) << 2);

    *(s16 *) (arg0 + 0x38) = val;
    *(s16 *) (arg0 + 0x3A) = *(s16 *) (arg0 + 0x38);
    func_150F55C8(arg0);
}

s32 func_150F55C8() {
    return 0;
}

void func_150F568C(s32 arg0) {
    func_15179008(0);
}

s32 func_150F56B0() {
    return 0;
}

s32 func_150F5A54() {
    return 0;
}

s32 func_150F5C08() {
    return 0;
}

s32 func_150F5C98() {
    return 0;
}

void func_150F6138(u8 *arg0, s32 arg1, u8 arg2) {
    func_15149514(arg1, arg2, (s32) (arg0 + 0x28), (s32) (arg0 + 0x2C), (s32) arg0);
}

s32 func_150F6178() {
    return 0;
}

s32 func_150F631C() {
    return 0;
}

s32 func_150F6368(s32 arg0) {
    func_150F631C(arg0);
    func_1514933C(arg0);
}

s32 func_150F6394(s32 arg0) {
    func_150F631C(arg0);
    func_15149368(arg0);
}

void func_150F63C0(u8 *arg0, s32 arg1, u8 arg2) {
    func_15169850(arg1, arg2, (s32) (arg0 + 0x28), (s32) (arg0 + 0x2C), (s32) arg0);
}

void func_150F6400(u8 *arg0) {
    u8 *temp_v0;

    if (*(u8 * volatile *)(arg0 + 0x160) != NULL) {
        temp_v0 = *(u8 * volatile *)(arg0 + 0x160) + 0x28;
        *(s32 *)(temp_v0 + 8) = 0;
    }
}

s32 func_150F6420(s32 arg0) {
    func_150F6400(arg0);
    func_1513CA6C(arg0);
}

s32 func_150F644C(s32 arg0) {
    func_150F6400(arg0);
    func_1513CAA0(arg0);
}

void func_150F6478(s32 arg0) {
}

s32 func_150F6484(s32 arg0) {
    func_150F6478(arg0);
    func_151411A4(arg0);
}

s32 func_150F64B0(s32 arg0) {
    func_150F6478(arg0);
    func_151411C4(arg0);
}

s32 func_150F64DC() {
    return 0;
}

void func_150F6850(u8 *arg0, s32 arg1, u8 arg2) {
    func_15169850(arg1, arg2, (s32) (arg0 + 0x28), (s32) (arg0 + 0x2C), (s32) arg0);
}

s32 func_150F6890() {
    return 0;
}

s32 func_150F695C() {
    return 0;
}
