#include <ultra64.h>
#include "structs.h"

extern struct127 D_800CC2D0[];
void func_150836CC(struct127 *arg0, s32 arg1);
u8 *func_15083568(u8 *, s32, f32, s32);
void func_1505E650(u8 *, u16, f32, f32, f32, f32, s32);

/* Non-matching placeholders for the text-only asm slice asm/90840.s. */

#pragma GLOBAL_ASM("asm/nonmatchings/generated_90840/func_15063390.s")

/* Set nested state 9, start requests 0x1D/0x1E, and reset its counters. */
void func_15063404(struct127 *actor) {
    struct127 *entry = &D_800CC2D0[(u32)(((s32)actor -
        (s32)D_800CC2D0) / (s32)sizeof(struct127))];

    entry->unk31C->unk78 = 9;
    func_15083568((u8 *)actor, 0x1D, 1.0f, 0);
    func_15083568((u8 *)actor, 0x1E, 1.0f, 0);
    actor->disable_jump = 20;
    actor->disable_run = 0;
    actor->unk83 = 0;
    *(s16 *)((u8 *)entry->unk31C + 0x24) = 60;
    entry->unk31C->unk11A = 2;
    func_1505E650((u8 *)actor, 0x7F, 1.0f, 0.0f, 0.0f, 0.0f, 0);
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

/* Start the actor's transition state and its animation providers. */
void func_15063570(struct127 *actor) {
    s32 index = ((s32)actor - (s32)D_800CC2D0) / (s32)sizeof(struct127);
    struct127 *entry = &D_800CC2D0[(u32)index];

    entry->unk31C->unk78 = 0x3B;
    entry->unk31C->unk11A = 2;
    func_15083568((u8 *)actor, 0x89, 1.0f, 0);
    actor->disable_jump = 20;
    actor->disable_run = 0;
    actor->unk83 = 0;
    func_1505E650((u8 *)actor, 0x221, 1.0f, 0.0f, 0.0f, 0.0f, 0);
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
