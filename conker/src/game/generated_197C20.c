#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/197C20.s. */

s32 func_1516A770() {
    return 0;
}

s32 func_1516A7B0() {
    return 0;
}

s32 func_1516AA70() {
    return 0;
}

s32 func_1516B6BC() {
    return 0;
}

s32 func_1516C878() {
    return 0;
}

s32 func_1516C934() {
    return 0;
}

s32 func_1516CC58() {
    return 0;
}

s32 func_1516D0CC() {
    return 0;
}

void func_1516D2E0(u8 *arg0) {
    if (arg0 != 0) {
        if (*arg0 == 0x51) {
            *(*(u8 **) (arg0 + 0x10) + 8) = 0;
            func_1516972C(arg0);
            *(arg0 + 0x15) = 0;
        }
    }
}

s32 func_1516D328() {
    return 0;
}

s32 func_1516D378() {
    return 0;
}

u8 *func_1516D3C4(u8 *arg0) {
    u8 *temp_v1;

    if ((arg0 != 0) && (*arg0 == 0x51)) {
        temp_v1 = *(u8 **) (arg0 + 0x10);
        *(u32 *) temp_v1 |= 0x500;
        return arg0;
    }
    return 0;
}
