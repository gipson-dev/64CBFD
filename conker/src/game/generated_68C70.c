#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/68C70.s. */

extern u8 D_800CC5CB[];

s32 func_1503B7C0() {
    return 0;
}

s32 func_1503B840() {
    return 0;
}

s32 func_1503B95C(s32 arg0, u8 *arg1) {
    s32 flags = D_800CC5CB[arg0 * 0x32C];

    if (flags & 2) {
        arg1[0x4E] = 0;
        return 0;
    }
    if (flags & 1) {
        return 0;
    }
    return 1;
}

s32 func_1503B9BC() {
    return 0;
}

s32 func_1503CB98() {
    return 0;
}
