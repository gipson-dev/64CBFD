#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/13AE20.s. */

s32 func_1510D970() {
    return 0;
}

s32 func_1510DA84() {
    return 0;
}

s32 func_1510E120() {
    return 0;
}

s32 func_1510E388() {
    return 0;
}

u8 *func_1510E634(u8 *arg0, s32 arg1, s32 arg2) {
    extern u32 D_80089470;
    u8 *ptr = arg0;

    *(u32 *) (ptr + 0) = 0xda380003;
    *(u32 *) (ptr + 4) = (u32) &D_80089470;
    arg0 = arg0 + 8;
    return arg0;
}
