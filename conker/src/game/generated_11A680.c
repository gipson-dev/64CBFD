#include <ultra64.h>
u16 func_1505A630(f32, f32, s32);
f32 func_150ED1D0(f32, f32);

/* Non-matching placeholders for the text-only asm slice asm/11A680.s. */

#pragma GLOBAL_ASM("asm/nonmatchings/game_11A680/func_150ED1D0.s")

/* Query the heading helper using relative X/Z and the actor scalar at 0x40. */
f32 func_150ED234(void *actor, void *other) {
    return func_150ED1D0((f32) (func_1505A630((*(f32 *)((char *)(other) + 0x14)) - (*(f32 *)((char *)(actor) + 0x14)), (*(f32 *)((char *)(actor) + 0x1C)) - (*(f32 *)((char *)(other) + 0x1C)), 0) + 0x4000) * 0.005493164f, (*(f32 *)((char *)(actor) + 0x40)));
}

#pragma GLOBAL_ASM("asm/nonmatchings/game_11A680/func_150ED298.s")

#pragma GLOBAL_ASM("asm/nonmatchings/game_11A680/func_150ED578.s")

#pragma GLOBAL_ASM("asm/nonmatchings/game_11A680/func_150ED638.s")

#pragma GLOBAL_ASM("asm/nonmatchings/game_11A680/func_150ED748.s")

#pragma GLOBAL_ASM("asm/nonmatchings/game_11A680/func_150EEC84.s")

#pragma GLOBAL_ASM("asm/nonmatchings/game_11A680/func_150EEDA8.s")
