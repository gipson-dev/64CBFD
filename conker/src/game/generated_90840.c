#include <ultra64.h>
#include "structs.h"

extern struct127 D_800CC2D0[];
void func_150836CC(struct127 *arg0, s32 arg1);

/* Non-matching placeholders for the text-only asm slice asm/90840.s. */

#pragma GLOBAL_ASM("asm/nonmatchings/generated_90840/func_15063390.s")

s32 func_15063404() {
    return 0;
}

void func_150634E4(struct127 *arg0) {
    s32 index = ((s32)arg0 - (s32)D_800CC2D0) / (s32)sizeof(struct127);
    struct127 *entry = &D_800CC2D0[(u32)index];

    entry->unk31C->unk78 = 0;
    entry->unk31C->unk11A = 0;
    func_150836CC(arg0, 0x1D);
    func_150836CC(arg0, 0x1E);
    arg0->disable_jump = 0;
    arg0->disable_run = 0;
    arg0->unk83 = 0;
}

s32 func_15063570() {
    return 0;
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_90840/func_15063628.s")

// Matched with guarded nested-pointer register normalization.
void func_150636A4(u8 *arg0) {
    u8 *temp_v0 = *(u8 **) (*(u32 *) (arg0 + 0x31C) + 0xB0);

    if (temp_v0 != 0) {
        u8 *temp_a1 = *(u8 **) (temp_v0 + 0x31C);

        if (temp_a1 != 0) {
            *(temp_a1 + 0x195) = 0x1E;
            *(u8 *) (*(u32 *) (temp_v0 + 0x31C) + 0x196) =
                (arg0 - (u8 *)D_800CC2D0) / 0x32C;
        }
    }
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_90840/func_150636F0.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_90840/func_150639BC.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_90840/func_15063A38.s")

#pragma GLOBAL_ASM("asm/nonmatchings/game_90840/func_15063B64.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_90840/func_15063C60.s")

#pragma GLOBAL_ASM("asm/nonmatchings/game_90840/func_15063E84.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_90840/func_15063FA0.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_90840/func_150641D8.s")

s32 func_150642AC() {
    return 0;
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_90840/func_150649A0.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_90840/func_15064A14.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_90840/func_15064B94.s")

s32 func_15065A5C() {
    return 0;
}
