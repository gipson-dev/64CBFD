#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/C3E20.s. */

extern s32 D_800D2DB4;
extern u8 D_800D2DC0[];
extern u8 D_800C35EA;

s32 func_15096A68(s32);

s32 func_15096970(void) {
    bzero(D_800D2DC0, 0x6C);
    D_800D2DB4 = 0;
}

s32 func_150969A0() {
    return 0;
}

s32 func_15096A68(s32 arg0) {
    return 0;
}

void func_15096D08(void) {
    s32 i;
    u8 *entry;

    i = 0;
    if (D_800C35EA != 1) {
        entry = D_800D2DC0;
        while (i != 3) {
            if ((*entry != 0) && (func_15096A68(i) != 0)) {
                break;
            }
            i++;
            entry += 0x24;
        }
    }
}

s32 func_15096D78() {
    return 0;
}

s32 func_1509759C() {
    return 0;
}

s32 func_15097798() {
    return 0;
}
