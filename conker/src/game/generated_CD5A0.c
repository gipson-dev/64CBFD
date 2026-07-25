#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/CD5A0.s. */

s32 func_150A00F0() {
    return 0;
}

s32 func_150A019C() {
    return 0;
}

s32 func_150A0264() {
    return 0;
}

s32 func_150A02D0() {
    return 0;
}

s32 func_150A0374(s32 arg0, s32 arg1, s32 arg2) {
    extern u8 D_800D3014[];

    if (arg1 == 3) {
        return *(s32 *) (D_800D3014 + arg0 * 12);
    }
    return 0;
}
