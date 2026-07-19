#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/E8C10.s. */

s32 func_150BB760() {
    return 0;
}

s32 func_150BBB5C() {
    return 0;
}

s32 func_150BC488() {
    return 0;
}

s32 func_150BCBBC() {
    return 0;
}

s32 func_150BCFB8() {
    return 0;
}

s32 func_150BD070() {
    return 0;
}

s32 func_150BD740() {
    return 0;
}

s32 func_150BD954() {
    return 0;
}

s32 func_150BDB3C(u8 *arg0) {
    u8 *temp_v0 = *(u8 **) (arg0 + 0x98);
    s32 temp_v1 = *(s16 *) (arg0 + 0x1C);

    if ((temp_v1 << 3) < *(temp_v0 + 0x1B)) {
        *(temp_v0 + 0x1B) = temp_v1 << 3;
    }
    return 1;
}
