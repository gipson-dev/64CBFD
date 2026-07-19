#include <ultra64.h>
void func_15169260(s32, s32, s32, u8);
extern u8 D_800A8D70[];
typedef struct { s32 val; } OneWord1D0840;
extern void (*D_8008F900[])();

/* Non-matching placeholders for the text-only asm slice asm/1D0840.s. */

extern void (*D_8008F904[])(u8 *, s32, u8);

s32 func_151A3390() {
    return 0;
}

s32 func_151A3504() {
    return 0;
}

s32 func_151A361C() {
    return 0;
}

s32 func_151A37C0() {
    return 0;
}

s32 func_151A3BE4() {
    return 0;
}

s32 func_151A4590() {
    return 0;
}

s32 func_151A4638() {
    return 0;
}

s32 func_151A483C() {
    return 0;
}

s32 func_151A4900() {
    return 0;
}

s32 func_151A499C() {
    return 0;
}

s32 func_151A4A38() {
    return 0;
}

s32 func_151A4CE0() {
    return 0;
}

s32 func_151A4D88() {
    return 0;
}

s32 func_151A4E34() {
    return 0;
}

void func_151A4E9C(u8 *arg0) {
    u8 *temp_v0 = *(u8 **) (arg0 + 0x98);

    *(u16 *) (arg0 + 0x1E) &= 0xFFFD;
    *(arg0 + 0x30) = 0;
    *(temp_v0 + 0x30) |= 1;
    *(temp_v0 + 0x30) |= 4;
}

s32 func_151A4ECC() {
    return 0;
}

s32 func_151A4F7C() {
    return 0;
}

s32 func_151A4FD0() {
    return 0;
}

s32 func_151A5070() {
    return 0;
}

void func_151A5130(arg0, arg1, arg2)
s32 arg0;
u8 *arg1;
s16 arg2;
{
    D_8008F900[*(arg1 + 0x14)]();
}

s32 func_151A5170() {
    return 0;
}

void func_151A55D4(u8 *arg0, s32 arg1, u8 arg2) {
    void (*callback)(u8 *, s32, u8) = D_8008F904[arg0[0x19]];

    if (callback != NULL) {
        callback(arg0, arg1, arg2);
    }
}

void func_151A561C(s32 arg0, u8 arg1) {
    OneWord1D0840 tmp;

    tmp = *(OneWord1D0840 *) D_800A8D70;
    func_15169260(&tmp, 1, arg0, arg1);
}
