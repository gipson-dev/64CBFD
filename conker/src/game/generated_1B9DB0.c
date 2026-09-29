#include <ultra64.h>

extern u8 D_800DF7D0[];
extern s16 *D_800DF9B8[];
extern s32 *D_800E0148[];

void func_1510D630(s16 *);
void func_100043B4(s32 *, u32);

/* Non-matching placeholders for the text-only asm slice asm/1B9DB0.s. */

s32 func_1518C900() {
    return 0;
}

void func_1518CA04(s32 arg0) {
    if (arg0 == 0x1E4) {
        return;
    }

    if ((D_800DF7D0[arg0] != 0) && (--D_800DF7D0[arg0] == 0)) {
        func_1510D630(D_800DF9B8[arg0]);
        func_100043B4(D_800E0148[arg0], 4);
    }
}
