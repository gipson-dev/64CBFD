#include <ultra64.h>
extern u8 *D_800DC2B0;

/* Non-matching placeholders for the text-only asm slice asm/15AA10.s. */

s32 func_1512D560() {
    return 0;
}

s32 func_1512D604() {
    return 0;
}

void func_1512D66C(u8 *arg0) {
    u32 stride = 0xB0;

    *(s32 *) (D_800DC2B0 + *(arg0 + 0x23D) * stride + 0xA8) = 0;
    *(s32 *) (D_800DC2B0 + *(arg0 + 0x23D) * stride + 0xAC) = 0;
}

s32 func_1512D6B0(u8 *arg0) {
    u8 *temp_v1 = D_800DC2B0 + *(arg0 + 0x23D) * 0xB0;

    return *(s32 *) (temp_v1 + 0xA8) == *(s32 *) (temp_v1 + 0xAC);
}
