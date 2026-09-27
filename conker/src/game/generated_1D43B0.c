#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/1D43B0.s. */

s32 func_151A6F00() {
    return 0;
}

s32 func_151A73EC(u8 *arg0) {
    u8 *entry = arg0 + 0x170;

    if (*(s16 *)(arg0 + 0x64) < 0x20) {
        if (*(u32 *)(entry + 4) != 0) {
            func_1516972C(*(u32 *)(entry + 4));
            *(u32 *)(entry + 4) = 0;
        }
    }
    return 1;
}

s32 func_151A743C() {
    return 0;
}

s32 func_151A7610() {
    return 0;
}

s32 func_151A77C0() {
    return 0;
}

s32 func_151A787C() {
    return 0;
}

void func_151A7908(u8 *arg0) {
    u8 *temp_v0 = arg0 + 0x170;

    if (*(s32 *) (arg0 + 0x174) != 0) {
        func_1516972C(*(u32 *) (temp_v0 + 4));
        *(u32 *) (temp_v0 + 4) = 0;
    }
}
