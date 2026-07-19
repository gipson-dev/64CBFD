#include <ultra64.h>
extern u8 D_800BE93C[];
extern u8 D_80084060[];

/* Non-matching placeholders for the text-only asm slice asm/48FD0.s. */

s32 func_1501BB20() {
    return 0;
}

s32 func_1501BBB8() {
    return 0;
}

s32 func_1501C010() {
    return 0;
}

s32 func_1501C0F0() {
    return 0;
}

void func_1501C17C(arg0)
u8 arg0;
{
    u8 idx = D_80084060[arg0];

    if (idx < 4) {
        D_800BE93C[idx] = 0;
    }
}

s32 func_1501C1B0() {
    return 0;
}

void func_1501C53C(void) {
    s32 i = 0;

    do {
        func_1501C17C(i & 0xFF);
        i += 1;
        i = i & 0xFF;
    } while (i < 4);
}

s32 func_1501C57C() {
    return 0;
}
