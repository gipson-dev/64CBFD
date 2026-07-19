#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/1E0560.s. */

extern void (*D_8008FB68[])(u8 *, s32, u8);

s32 func_151B30B0() {
    return 0;
}

s32 func_151B3184() {
    return 0;
}

s32 func_151B32C8() {
    return 0;
}

void func_151B3A34(u8 *arg0, s32 arg1, u8 arg2) {
    void (*callback)(u8 *, s32, u8) = D_8008FB68[arg0[0x44]];

    if (callback != NULL) {
        callback(arg0, arg1, arg2);
    }
}

s32 func_151B3A7C() {
    return 0;
}

s32 func_151B3CF0() {
    return 0;
}

s32 func_151B3F28() {
    return 0;
}

s32 func_151B3FDC() {
    return 0;
}

s32 func_151B42A4() {
    return 0;
}

s32 func_151B47D8() {
    return 0;
}

s32 func_151B48DC() {
    return 0;
}

s32 func_151B498C() {
    return 0;
}

s32 func_151B4A14() {
    return 0;
}

s32 func_151B4B78() {
    return 0;
}

s32 func_151B4C1C() {
    return 0;
}

s32 func_151B4C6C(s32 arg0) {
    func_151B4C1C(arg0);
    func_15169824(arg0);
}

s32 func_151B4C98(s32 arg0) {
    func_151B4C1C(arg0);
    func_15169824(arg0);
}
