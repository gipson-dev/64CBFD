#include <ultra64.h>
extern u8 *D_800DBEF4;

/* Non-matching placeholders for the text-only asm slice asm/F4D20.s. */

s32 func_150C7870() {
    return 0;
}

s32 func_150C78E0() {
    return 0;
}

void func_150C7930(u8 *arg0) {
    u8 *temp_v0 = D_800DBEF4;

    *(u32 *) (arg0 + 0x3C) = *(u32 *) (temp_v0 + 0x21C) & 0xFFFF0000;
    func_151150BC(arg0, temp_v0 + 0x1E0);
}

s32 func_150C7968() {
    return 0;
}

s32 func_150C79BC() {
    return 0;
}

s32 func_150C7C90() {
    return 0;
}

s32 func_150C7D7C() {
    return 0;
}
