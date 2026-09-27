#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/50D20.s. */

extern u8 *D_800C35F0[];
extern u8 *func_1505EEF4(s32 arg0);

void func_15023870(s32 arg0, s32 arg1, s32 arg2, s32 arg3) {
    if ((arg0 == 0xB) && (arg1 == 2)) {
        u8 *temp_v0 = func_1505EEF4(arg3);

        if (temp_v0 != 0) {
            D_800C35F0[arg2][0x2A] = temp_v0[0x3B];
        }
    }
}
