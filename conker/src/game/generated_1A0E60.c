#include <ultra64.h>
extern u8 *D_800DBEF4;

u8 *func_151149AC(u8);

/* Non-matching placeholders for the text-only asm slice asm/1A0E60.s. */

s32 func_151739B0() {
    return 0;
}

void func_15173C60(s32 arg0, s32 arg1) {
    func_151739B0(0, 0, arg0, arg1, 0);
}

void func_15173C90(s32 arg0, s32 arg1, s32 arg2) {
    u8 *record = func_151149AC(arg2);

    if (record != NULL) {
        func_151739B0(
            *(u16 *) (record + 0x54) & ~0x8000,
            1,
            arg0,
            arg1,
            (record - D_800DBEF4) / 0xA0);
    }
}
