#include <ultra64.h>
extern u8 *D_800DD0E0;

/* Non-matching placeholders for the text-only asm slice asm/1FFB70.s. */

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1FFB70/func_151D26C0.s")

void func_151D2718(arg0)
s16 arg0;
{
    u8 *ptr = D_800DD0E0;
    s32 val = -2;

    if (ptr != 0) {
        do {
            if (arg0 == *(s16 *) (ptr + 0x10)) {
                *(s8 *) (ptr + 0x16) = val;
            }
            ptr = *(u8 **) (ptr + 8);
        } while (ptr != 0);
    }
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1FFB70/func_151D275C.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1FFB70/func_151D2830.s")
