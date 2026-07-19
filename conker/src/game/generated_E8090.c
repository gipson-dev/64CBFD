#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/E8090.s. */

s32 func_150BABE0() {
    return 0;
}

s32 func_150BAFEC() {
    return 0;
}

s32 func_150BB260() {
    return 0;
}

void func_150BB408(u8 *arg0) {
    *(u32 *) (arg0 + 0x18) |= 1;
    *(s16 *) (arg0 + 0x1C) = 0x32;
    *(s16 *) (arg0 + 0xB0) = *(s16 *) (arg0 + 0x1C);
    *(s16 *) (arg0 + 0xB2) = 5;
    func_1513F6C0(arg0, 6, *(arg0 + 0x81));
}

s32 func_150BB450(u8 *arg0) {
    s32 temp_v0 = *(s16 *) (arg0 + 0x1C);

    if (temp_v0 < *(s16 *) (arg0 + 0xB0)) {
        s32 temp_v1 = (s16) ((u32) *(s16 *) (arg0 + 0xB2) * temp_v0);

        if (temp_v1 < *(arg0 + 0x28)) {
            *(arg0 + 0x28) = temp_v1;
        }
    }
    return 1;
}

s32 func_150BB498() {
    return 0;
}
