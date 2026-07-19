#include <ultra64.h>
extern void (*D_80089670[])();
extern u8 *D_800B0DF0;

/* Non-matching placeholders for the text-only asm slice asm/15D6E0.s. */

void func_15130230(s32 arg0, s32 arg1) {
    u8 temp_v0 = *(D_800B0DF0 + 0xF);

    if (temp_v0 != 0) {
        D_80089670[temp_v0]();
    }
}
