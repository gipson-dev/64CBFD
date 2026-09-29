#include <ultra64.h>
void func_1502EA98(u8 *arg0, u8 arg1, u8 arg2, u8 arg3, u8 arg4,
                   s32 arg5, u8 arg6);

/* Non-matching placeholders for the text-only asm slice asm/1199D0.s. */

s32 func_150EC520() {
    return 0;
}

s32 func_150EC6B0() {
    return 0;
}

s32 func_150ECA68() {
    return 0;
}

void func_150ECB4C(u8 *arg0, s32 arg1, u8 arg2) {
    func_15169850(arg1, arg2, (s32) (arg0 + 0x28), (s32) (arg0 + 0x2C), (s32) arg0);
}

void func_150ECB8C(u8 *arg0) {
    u8 *sub = arg0 + 0x28;
    u8 *target = *(u8 **) sub;

    if ((*(s32 *) target == 0) || (sub[4] != target[0x3B])) {
        *(s16 *) (arg0 + 0xE) = -1;
        return;
    }
    func_1502EA98(target, sub[5], sub[6], sub[7], sub[8], 0, sub[9]);
}

void func_150ECC00(u8 *arg0, volatile u8 arg1, s32 arg2) {
    func_151C9AC0(arg0, arg1, arg2);
    func_150ECA68(arg0, 0, 0xFF, 0, 0xFF, 4, -1, arg1, arg2);
}

s32 func_150ECC70() {
    return 0;
}
