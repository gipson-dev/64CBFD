#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/1A1B40.s. */

extern s32 D_800BE9E4;

s32 func_15174690() {
    return 0;
}

void func_15174920(u8 *arg0) {
    s32 remaining = arg0[0x3F];
    s32 motion;

    if (remaining >= 201) {
        remaining = 200;
    }
    remaining -= (u32)D_800BE9E4 * *(u32 *)(arg0 + 0x18);
    if (remaining < 0) {
        *(s16 *)(arg0 + 0x38) = 0;
        return;
    }

    motion = *(s32 *)(arg0 + 0x14);
    arg0[0x3F] = remaining;
    *(s16 *)(arg0 + 0x34) += motion;
    *(s16 *)(arg0 + 0x36) += (motion << 3) / 7;
}
