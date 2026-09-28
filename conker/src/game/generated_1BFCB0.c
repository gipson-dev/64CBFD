#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/1BFCB0.s. */

s32 func_15192800() {
    return 0;
}

s32 func_151928B0(u8 *arg0, s32 *arg1) {
    s32 result = 0;

    switch (arg0[4]) {
        case 0:
        case 1:
        case 2:
        case 3:
        case 4:
            result = 1;
            *arg1 = 0;
            break;
        case 0x53:
            result = 1;
            *arg1 = 1;
            break;
    }

    return result;
}
