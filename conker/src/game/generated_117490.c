#include <ultra64.h>
extern u8 *D_800DBEF4;

/* Non-matching placeholders for the text-only asm slice asm/117490.s. */

s32 func_150E5AE0();

#pragma GLOBAL_ASM("asm/nonmatchings/generated_117490/func_150E9FE0.s")

s32 func_150EA10C(u8 *arg0) {
    *(s32 *)(arg0 + 0x80) = 0;
    return 1;
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_117490/func_150EA11C.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_117490/func_150EA490.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_117490/func_150EA500.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_117490/func_150EA5CC.s")

void func_150EA8E0(s32 arg0) {
    func_150E5AE0();
}

// Matched with guarded base/index and byte-update register lifetimes.
void func_150EA904(u8 arg0, s32 arg1) {
    u8 *temp_v0 = D_800DBEF4 + arg1 * 0xA0;

    if (*(temp_v0 + 0x72) == 0xE0) {
        *(temp_v0 + 0x73) |= 3;
    }
}

s32 func_150EA944() {
    return 0;
}

s32 func_150EAB10() {
    return 0;
}

s32 func_150EAE24() {
    return 0;
}
