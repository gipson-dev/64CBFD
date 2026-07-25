#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/61D10.s. */

extern u8 D_800C3F00;

s32 func_15034860() {
    return 0;
}

s32 func_15034EB4() {
    return 0;
}

void func_15034F20(void) {
    D_800C3F00 = 0;
}

s32 func_15034F30() {
    return 0;
}

u8 *func_150356C8(void) {
    extern u8 D_800C3F08[];
    u8 val = D_800C3F00;
    u8 next;

    if (val == 15) {
        return 0;
    }
    next = val + 1;
    D_800C3F00 = next;
    return D_800C3F08 + (next - 1) * 12;
}

s32 func_15035714() {
    return 0;
}

s32 func_15035808() {
    return 0;
}

s32 func_15035D6C() {
    return 0;
}

s32 func_15035FE8() {
    return 0;
}

s32 func_15036148() {
    return 0;
}
