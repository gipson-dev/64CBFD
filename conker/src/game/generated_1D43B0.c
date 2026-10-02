#include <ultra64.h>

extern s32 D_800BE9E4;

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

void func_151A787C(u8 *arg0) {
    u8 *params = arg0 + 0x50;
    s32 value = *(s16 *)(arg0 + 0x38);
    s32 delta;
    s32 intensity;

    if (value < *(s16 *)(params + 4)) {
        arg0[0x3F] = value * (u32)*(s16 *)(params + 6);
    }

    if (value < *(s16 *)(params + 8)) {
        delta = *(s16 *)(params + 0xA) * (u32)D_800BE9E4;
        *(s16 *)(arg0 + 0x34) += delta;
        *(s16 *)(arg0 + 0x36) += delta;
        value = *(s16 *)(arg0 + 0x38);
    }

    intensity = value * (u32)*(s16 *)(params + 2);
    arg0[0x42] = intensity;
    arg0[0x41] = intensity;
    arg0[0x40] = intensity;
}

void func_151A7908(u8 *arg0) {
    u8 *temp_v0 = arg0 + 0x170;

    if (*(s32 *) (arg0 + 0x174) != 0) {
        func_1516972C(*(u32 *) (temp_v0 + 4));
        *(u32 *) (temp_v0 + 4) = 0;
    }
}
