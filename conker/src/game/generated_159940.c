#include <ultra64.h>
extern s32 D_800BE9E4;
extern s32 D_800DC290[];

/* Non-matching placeholders for the text-only asm slice asm/159940.s. */

s32 func_1512C490() {
    return 0;
}

s32 func_1512D070() {
    return 0;
}

s32 func_1512D238() {
    return 0;
}

void func_1512D2E4(u8 *arg0, s32 arg1) {
    *(s32 *)(arg0 + 0x850) = arg1;
    *(u8 *)(arg0 + 0x84D) = 1;
}

void func_1512D2F8(u8 *arg0) {
    switch (*(u8 *) (arg0 + 0x84D)) {
        case 1:
            *(u8 *) (arg0 + 0x84E) = 0;
            *(u8 *) (arg0 + 0x84D) = 2;
            return;
        case 2:
            *(u8 *) (arg0 + 0x84E) += D_800BE9E4;
            if (*(u8 *) (arg0 + 0x84E) >= D_800DC290[*(s32 *) (arg0 + 0x850)]) {
                *(u8 *) (arg0 + 0x84D) = 0;
            }
            return;
        default:
            return;
    }
}

void func_1512D368(s32 arg0) {
}
