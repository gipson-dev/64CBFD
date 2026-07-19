#include <ultra64.h>
void func_15169260(s32, s32, s32, u8);
extern u8 D_800A3860[];
typedef struct { s32 a, b; } TwoWord15F680;

/* Non-matching placeholders for the text-only asm slice asm/15F680.s. */


s32 func_15133EEC();

s32 func_151321D0() {
    return 0;
}

s32 func_151323AC() {
    return 0;
}

s32 func_151323F8() {
    return 0;
}

s32 func_15132444() {
    return 0;
}

s32 func_15132570(s32 arg0) {
    func_15132444(arg0);
    func_15169804(arg0);
}

s32 func_1513259C(s32 arg0) {
    func_15132444(arg0);
    func_15169824(arg0);
}

s32 func_151325C8() {
    return 0;
}

s32 func_1513264C() {
    return 0;
}

void func_15132A4C(s32 arg0, s32 arg1, s32 arg2, s32 arg3, u8 arg4, s32 arg5) {
    func_1513264C(arg0, arg1, arg2, 0, arg3, arg4, arg5);
}

s32 func_15132A88() {
    return 0;
}

s32 func_15132B80() {
    return 0;
}

s32 func_15132DDC() {
    return 0;
}

s32 func_151332DC() {
    return 0;
}

s32 func_15133510() {
    return 0;
}

s32 func_15133588() {
    return 0;
}

s32 func_151336A8() {
    return 0;
}

s32 func_15133760() {
    return 0;
}

s32 func_151337C0() {
    return 0;
}

s32 func_15133894() {
    return 0;
}

s32 func_151339D4() {
    return 0;
}

s32 func_15133A50(u8 *arg0, s32 arg1, s32 arg2, s32 arg3, f32 arg4) {
    *(f32 *) (arg0 + 0x44) = 0.0f;
    *(f32 *) (arg0 + 0x48) = 0.0f;
    *(f32 *) (arg0 + 0x3C) = *(f32 *) (arg0 + 0x10) + arg4;
    *(f32 *) (arg0 + 0x4C) = 0.0f;
    *(f32 *) (arg0 + 0x50) = 0.0f;
    *(f32 *) (arg0 + 0x54) = 0.0f;
    *(f32 *) (arg0 + 0x58) = 0.0f;
    return 1;
}

s32 func_15133A94() {
    return 0;
}

s32 func_15133B98() {
    return 0;
}

s32 func_15133C58() {
    return 0;
}

s32 func_15133D20() {
    return 0;
}

s32 func_15133DE8() {
    return 0;
}

void func_15133E3C(s32 arg0, u8 arg1) {
    s32 tmp[2];

    tmp[0] = *(s32 *) D_800A3860;
    tmp[1] = *(s32 *) (D_800A3860 + 4);
    func_15169260(tmp, 2, arg0, arg1);
}

s32 func_15133E84(s32 arg0, u8 *arg1, s32 arg2) {
    func_15133EEC(arg0, *(u16 *)(arg1 + 0x170), *(u8 *)(arg1 + 0x172), *(s32 *)(arg1 + 0x174));
}

s32 func_15133EB8(s32 arg0, u8 *arg1, s32 arg2) {
    func_15133EEC(arg0, *(u16 *)(arg1 + 0x174), *(u8 *)(arg1 + 0x176), *(s32 *)(arg1 + 0x178));
}

s32 func_15133EEC() {
    return 0;
}

s32 func_15133FD8() {
    return 0;
}
