#include <ultra64.h>
extern u8 D_800C35E8;
extern u8 D_800C35EA;
extern s32 (*D_8008ADA8)();

/* Non-matching placeholders for the text-only asm slice asm/F21D0.s. */

s32 func_150C4D20() {
    return 0;
}

s32 func_150C4E9C() {
    return 0;
}

s32 func_150C522C() {
    return 0;
}

s32 func_150C5280(void) {
    if (D_800C35EA == 1) {
        u8 temp_v0 = D_800C35E8;

        if ((temp_v0 == 0xB) || (temp_v0 == 0xC) || (temp_v0 == 0xD)) {
            return 1;
        }
    }
    return 0;
}

s32 func_150C52CC(u8 *arg0) {
    if (func_150C5280() != 0) {
        return 0;
    }
    return D_8008ADA8(arg0);
}

s32 func_150C5310() {
    return 0;
}
