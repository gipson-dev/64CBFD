#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/F2820.s. */

extern void (*D_800887C8[])(u8 *, s32, u8);

s32 func_150C5370() {
    return 0;
}

void func_150C5430() {
    func_15169804();
}

void func_150C5450() {
    func_15169824();
}

s32 func_150C5470() {
    return 0;
}

s32 func_150C54C0() {
    return 0;
}

s32 func_150C5510(u8 *arg0) {
    func_1514EDF0(arg0, *(s32 *)(arg0 + 0xC8));
    func_150C5430(arg0);
}

s32 func_150C553C(u8 *arg0) {
    func_1514EDF0(arg0, *(s32 *)(arg0 + 0xC8));
    func_150C5450(arg0);
}

s32 func_150C5568() {
    return 0;
}

s32 func_150C56A4() {
    return 0;
}

s32 func_150C5B88() {
    return 0;
}

s32 func_150C5BD4() {
    return 0;
}

s32 func_150C5C74(s32 arg0) {
    func_1514D3B0(arg0, 0x15, 1, 0);
}

s32 func_150C5C9C(s32 arg0) {
    func_1514D3B0(arg0, 0x15, 2, 0);
}

void func_150C5CC4(u8 *arg0, s32 arg1, u8 arg2) {
    void (*callback)(u8 *, s32, u8) = D_800887C8[arg0[0x38]];

    if (callback != NULL) {
        callback(arg0, arg1, arg2);
    }
}

s32 func_150C5D0C() {
    return 0;
}
