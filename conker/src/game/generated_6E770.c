#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/6E770.s. */

extern u8 D_800848D0[];

s32 func_150412C0() {
    return 0;
}

s32 func_150413FC() {
    return 0;
}

s32 func_15041480(u8 arg0) {
    s32 i;

    for (i = 0; i != 0x50; i += 4) {
        if (arg0 == D_800848D0[i]) {
            return i;
        }
        if (arg0 == D_800848D0[i + 1]) {
            return i + 1;
        }
        if (arg0 == D_800848D0[i + 2]) {
            return i + 2;
        }
        if (arg0 == D_800848D0[i + 3]) {
            return i + 3;
        }
    }
    return i;
}

s32 func_15041508() {
    return 0;
}

s32 func_150415E0() {
    return 0;
}

s32 func_150417AC() {
    return 0;
}

s32 func_150428D4() {
    return 0;
}

s32 func_15042C40() {
    return 0;
}
