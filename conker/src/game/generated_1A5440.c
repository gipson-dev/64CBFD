#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/1A5440.s. */

extern u8 *D_800DCF38;

s32 func_15177F90() {
    return 0;
}

s32 func_15178268() {
    return 0;
}

s32 func_15178750() {
    return 0;
}

s32 func_151787AC() {
    return 0;
}

s32 func_15178B98(u8 arg0) {
    u8 *node = D_800DCF38;

    while (node != NULL) {
        if (node[0x34] == arg0) {
            return (s32) node;
        }

        node = *(u8 **) (node + 8);
    }

    return 0;
}

s32 func_15178BE4() {
    return 0;
}

s32 func_15178C34() {
    return 0;
}

s32 func_15178C9C() {
    return 0;
}

s32 func_15178DA4(s32 arg0) {
    return 0;
}

void func_15178E14(u8 arg0) {
    func_15178DA4(func_15178B98(arg0));
}
