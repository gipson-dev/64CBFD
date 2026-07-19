#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/1DD500.s. */

s32 func_151B0050() {
    return 0;
}

s32 func_151B01B8() {
    return 0;
}

s32 func_151B03B8() {
    return 0;
}

s32 func_151B09BC() {
    return 0;
}

s32 func_151B0B88() {
    return 0;
}

s32 func_151B118C() {
    return 0;
}

s32 func_151B1478(u8 *arg0) {
    s32 temp_v0 = *(s16 *)(arg0 + 0x1C);

    if (temp_v0 < 0x20) {
        s32 temp_v1 = temp_v0 << 3;
        if (temp_v1 < *(u8 *)(arg0 + 0x5C)) {
            *(u8 *)(arg0 + 0x5C) = temp_v1;
        }
    }
    return 1;
}

s32 func_151B14AC() {
    return 0;
}

s32 func_151B1828() {
    return 0;
}

s32 func_151B1918() {
    return 0;
}

s32 func_151B19A4() {
    return 0;
}

s32 func_151B1A58(s32 arg0) {
    func_151B1918(arg0);
    func_1514933C(arg0);
}

s32 func_151B1A84(s32 arg0) {
    func_151B1918(arg0);
    func_15149368(arg0);
}

s32 func_151B1AB0() {
    return 0;
}

s32 func_151B1B34() {
    return 0;
}

s32 func_151B1FAC() {
    return 0;
}
