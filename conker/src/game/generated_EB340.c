#include <ultra64.h>
extern f32 D_800BE9A4;
extern u8 D_800CC2D0[];

/* Non-matching placeholders for the text-only asm slice asm/EB340.s. */

s32 func_150BDE90() {
    return 0;
}

s32 func_150BDF0C() {
    return 0;
}

void func_150BE150(u8 *arg0, u8 **arg1, u8 arg2) {
    if (arg2 == 0x21) {
        if (*(u8 **) (arg0 + 0x28) == *arg1) {
            func_1516972C(arg0);
        }
    } else if (arg2 == 0) {
        u8 *payload = *arg1;

        if (*(u8 **) (arg0 + 0x28) == *(u8 **) (payload + 0x318)) {
            func_1516972C(arg0);
        }
    }
}

s32 func_150BE1C4(u8 *arg0) {
    *(f32 *) (arg0 + 0x14) = *(f32 *) (arg0 + 0x80) * D_800BE9A4 + *(f32 *) (arg0 + 0x14);
    if (120.0f < *(f32 *) (arg0 + 0x14)) {
        return 0;
    }
    return 1;
}

s32 func_150BE210() {
    return 0;
}

s32 func_150BE2E8() {
    return 0;
}

u8 *func_150BE438(u8 *arg0, s32 arg1) {
    u8 *entry = D_800CC2D0 + arg1 * 0x32C;
    s16 *dst = (s16 *) arg0;

    dst[0] = 0x68;
    dst[1] = *(s32 *) (entry + 0x2E8);
    dst[2] = 0xE;
    dst[3] = *(s32 *) (entry + 0x2E4);
    return arg0 + 8;
}

s32 func_150BE494() {
    return 0;
}
