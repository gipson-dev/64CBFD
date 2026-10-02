#include <ultra64.h>
extern u8 *D_800CC5EC;
u8 *func_151149AC(u8);
void func_15117798(u8 *);

/* Non-matching placeholders for the text-only asm slice asm/FC550.s. */

void func_150CF0A0(u8 *arg0) {
    u8 *object;

    if ((arg0[0x73] & 3) != 2) {
        if (((arg0[0x4F] & 4) != 0) && (D_800CC5EC[0x57] != 0)) {
            object = func_151149AC(0xFE);
            object[0x73] &= ~3;
            object[0x73] |= 2;
            object = func_151149AC(0xFD);
            object[0x73] &= ~3;
            object[0x73] |= 2;
        }
    } else {
        func_15117798(arg0);
    }
}
