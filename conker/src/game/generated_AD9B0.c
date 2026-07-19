#include <ultra64.h>
extern u8 D_800D1941;

/* Non-matching placeholders for the text-only asm slice asm/AD9B0.s. */

s32 func_15080500() {
    return 0;
}

s32 func_15080620() {
    return 0;
}

s32 func_150806A8() {
    return 0;
}

void func_15080718(register s32 arg0, s32 *arg1, s32 *arg2) {
    *arg2 = 1 << (arg0 & 7);
    *arg1 = arg0 >> 3;
}

s32 func_15080738() {
    return 0;
}

s32 func_15080784() {
    return 0;
}

void func_150807F4(u8 arg0, u8 arg1, s32 arg2) {
    if (arg2 == 0x20) {
        func_15080784();
    }
}

s32 func_15080828() {
    return 0;
}

s32 func_15080BE8() {
    return 0;
}

s32 func_15080C64() {
    return 0;
}

s32 func_15080CF4(void) {
    if (D_800D1941 == 0) {
        return 1;
    }
    return 0;
}
