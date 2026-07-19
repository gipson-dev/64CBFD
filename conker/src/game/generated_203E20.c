#include <ultra64.h>
extern s32 D_800BE9F0;

/* Non-matching placeholders for the text-only asm slice asm/203E20.s. */

void func_151D6970(u8 *arg0, s32 arg1) {
    s32 temp_v0 = D_800BE9F0;

    if ((temp_v0 == 0x32) || (temp_v0 == 0x33)) {
        func_150D6730(arg0, 0xFF, 1);
    }
}

s32 func_151D69B4() {
    return 0;
}

s32 func_151D6BFC() {
    return 0;
}

s32 func_151D6E60() {
    return 0;
}

s32 func_151D7000() {
    return 0;
}

void func_151D70CC(u8 *arg0, s32 arg1, u8 arg2) {
    u8 *target = *(u8 **) (arg0 + 0x48);

    func_15169850(arg1, arg2, (s32) target, (s32) (target + 4), (s32) arg0);
}

s32 func_151D710C() {
    return 0;
}
