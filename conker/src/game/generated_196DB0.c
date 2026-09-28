#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/196DB0.s. */

void *func_15167A68(s32 arg0, s32 arg1, s32 arg2, s32 arg3, u8 arg4, u8 arg5);

void *func_15169900(void *arg0, s32 arg1) {
    void *ret;

    ret = func_15167A68(0x5E, 0, 0x4C, 0, arg1, 1);
    if (ret != NULL) {
        bcopy(arg0, (u8 *) ret + 0x10, 0x3C);
    }

    return ret;
}

void func_15169968(register void *arg0) {
    func_15169900(arg0, 0xFF);
}

s32 func_15169988() {
    return 0;
}

s32 func_15169A48() {
    return 0;
}
