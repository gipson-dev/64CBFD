#include <ultra64.h>
extern u8 *D_800DC2B0;

/* Non-matching placeholders for the text-only asm slice asm/15AA10.s. */

s32 func_1512D560() {
    return 0;
}

/* Note 385: guards preserve one closed IDO register-allocation cycle. */
u8 *func_1512D604(u8 *arg0) {
    u32 temp_a3;
    u8 *temp_v0;
    u8 *temp_v1;
    s32 temp_a1;

    temp_a3 = 0xB0;
    temp_v0 = D_800DC2B0 + *(arg0 + 0x23D) * temp_a3;
    temp_a1 = *(s32 *) (temp_v0 + 0xA8);
    *(s32 *) (temp_v0 + 0xA8) = temp_a1 + 1;
    temp_v1 = temp_v0 + temp_a1 * 8;
    temp_v0 = D_800DC2B0 + *(arg0 + 0x23D) * temp_a3;
    if (*(s32 *) (temp_v0 + 0xA8) == 20) {
        *(s32 *) (temp_v0 + 0xA8) = 0;
    }
    return temp_v1;
}

void func_1512D66C(u8 *arg0) {
    u32 stride = 0xB0;

    *(s32 *) (D_800DC2B0 + *(arg0 + 0x23D) * stride + 0xA8) = 0;
    *(s32 *) (D_800DC2B0 + *(arg0 + 0x23D) * stride + 0xAC) = 0;
}

/* Note 318: guarded temporaries preserve retail record-index register lifetimes. */
s32 func_1512D6B0(u8 *arg0) {
    u8 *temp_v1 = D_800DC2B0 + *(arg0 + 0x23D) * 0xB0;

    return *(s32 *) (temp_v1 + 0xA8) == *(s32 *) (temp_v1 + 0xAC);
}
