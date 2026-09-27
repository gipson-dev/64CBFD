#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/FFBA0.s. */

s32 func_150D26F0() {
    return 0;
}

s32 func_150D278C() {
    return 0;
}

s32 func_150D2924() {
    return 0;
}

s32 func_150D2D6C() {
    return 0;
}

s32 func_150D317C() {
    return 0;
}

void func_150D32FC(u8 *arg0, u8 *arg1, u8 arg2) {
    u8 *record = arg0 + 0x28;

    if (arg2 == 0x34 && *arg1 == record[0x51]) {
        func_150D278C(*(s32 *) record, record + 0x10, arg0[0xC], arg0[1]);
    }
}
