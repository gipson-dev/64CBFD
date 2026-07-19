#include <ultra64.h>

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
    u16 temp_t6 = *(u16 *)(arg0 + 0x1E);
    u8 *temp_v0 = *(u8 **)(arg0 + 0x98);
    s32 temp_t8;
    s32 temp_t0;
    s32 temp_t1;

    *(u8 *)(arg0 + 0x30) = 0;
    *(u16 *)(arg0 + 0x1E) = temp_t6 & 0xFFFD;
    temp_t8 = *(u8 *)(temp_v0 + 0x30);
    temp_t0 = temp_t8 | 1;
    temp_t1 = temp_t0 | 4;
    *(u8 *)(temp_v0 + 0x30) = temp_t0;
    *(u8 *)(temp_v0 + 0x30) = temp_t1;
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

s32 func_151A5130() {
    return 0;
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

s32 func_151A561C() {
    return 0;
}
