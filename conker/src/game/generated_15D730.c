#include <ultra64.h>
typedef struct { s32 a, b, c; } ThreeWord15D730;
void func_15169260(void *, s32, s32, u8);
extern u8 D_800A37F0[];
extern void (*D_80089844[])();
extern void (*D_80089814[])();
extern s32 D_800BE9E4;

/* Non-matching placeholders for the text-only asm slice asm/15D730.s. */

void func_151318E8(f32 *, f32);

s32 func_15131918();
s32 func_15131958();

s32 func_151319C4();


#pragma GLOBAL_ASM("asm/nonmatchings/generated_15D730/func_15130280.s")


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

    func_151318E8((f32 *)(temp_a2 + 0x58), *(f32 *)(temp_a2 + 0xA8));
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

void func_1513175C(u8 *arg0) {
    func_15169824(arg0);
}

s32 func_1513177C(u8 *arg0) {
    s32 idx = (*(u32 *) (arg0 + 0x68) & 0x4000) ? *(arg0 + 0x75) : 0;

    D_80089814[idx]();
}

s32 func_151317C8(u8 *arg0) {
    s32 idx = (*(u32 *) (arg0 + 0x68) & 0x4000) ? *(arg0 + 0x75) : 0;

    D_80089844[idx]();
}

s32 func_15131814(s32 arg0, s32 arg1) {
    return 0;
}

s32 func_15131828() {
    return 0;
}

/* The mixed pointer/float ABI carries arg1's raw bits in a1. */
void func_151318E8(f32 *arg0, f32 arg1) {
    s32 count = D_800BE9E4;

    while (count > 0) {
        arg0[1] *= arg1;
        count--;
    }
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

void func_15131D4C(s32 arg0, u8 arg1) {
    ThreeWord15D730 tmp;

    tmp = *(ThreeWord15D730 *) D_800A37F0;
    func_15169260(&tmp, 3, arg0, arg1);
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_15D730/func_15131D9C.s")

s32 func_15131DEC() {
    return 0;
}

s32 func_15131EE4() {
    return 0;
}
