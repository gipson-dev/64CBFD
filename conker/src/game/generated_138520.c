#include <ultra64.h>

extern u8 *D_800BE628;
extern f32 D_800D35E0;
extern f32 D_800D35E4;

/* Non-matching placeholders for the text-only asm slice asm/138520.s. */

s32 func_1510B070() {
    return 0;
}

s32 func_1510B128() {
    return 0;
}

s32 func_1510B32C() {
    return 0;
}

s32 func_1510B3B0() {
    return 0;
}

s32 func_1510B458() {
    return 0;
}

s32 func_1510B51C() {
    return 0;
}

s32 func_1510B5F8() {
    return 0;
}

s32 func_1510B690() {
    return 0;
}

s32 func_1510B7B4() {
    return 0;
}

void func_1510B958(s32 arg0) {
    u8 *record = D_800BE628 + arg0 * 0x180;

    D_800D35E0 = *(f32 *) (record + 0x64) +
                 ((*(f32 *) (record + 0x74) /
                   *(f32 *) (record + 0x6C)) - 1.0f) * -1.0f;
    D_800D35E4 = *(f32 *) (record + 0x68) +
                 ((*(f32 *) (record + 0x78) /
                   *(f32 *) (record + 0x70)) - 1.0f) * -1.0f;
}

s32 func_1510B9D0() {
    return 0;
}

s32 func_1510BF60() {
    return 0;
}

s32 func_1510C4AC() {
    return 0;
}

s32 func_1510C8A8() {
    return 0;
}
