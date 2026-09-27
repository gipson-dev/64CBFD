#include <ultra64.h>
s32 func_15131C84(void *, void *, s32, void *, void *, void *);

/* Non-matching placeholders for the text-only asm slice asm/1BF090.s. */

s32 func_15191BE0() {
    return 0;
}

s32 func_15191D54() {
    return 0;
}

s32 func_1519203C() {
    return 0;
}

s32 func_15192308(u8 *arg0, s32 arg1) {
    func_15131C84(arg0 + 0xAC, arg0 + 0xAE, *(s32 *)(arg0 + 0xA8),
                  arg0 + 0xB0, arg0 + 0x38, arg0 + 0x3C);
    return 1;
}

s32 func_15192358() {
    return 0;
}

s32 func_1519257C(s32 arg0, s32 arg1) {
    s32 call_result = func_15192308(arg0, arg1);
    u8 result = call_result;

    if (call_result != 0) {
        result = func_15192358(arg0, arg1);
    }

    return result;
}

s32 func_151925C4() {
    return 0;
}

void func_1519277C(u8 *arg0, s32 arg1, u8 arg2) {
    func_15169850(arg1, arg2, arg0 + 0x28, arg0 + 0x2C, arg0);
}
