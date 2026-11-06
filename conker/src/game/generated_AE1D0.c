#include <ultra64.h>
#include "structs.h"
extern u8 D_800CC2D0[], D_800D121C[], D_8009BD30[];
s32 func_1508108C(u8 *);


/* Non-matching placeholders for the text-only asm slice asm/AE1D0.s. */

s32 func_15080D20(u8 *origin, u8 *target, s32 part, f32 forwardOffset, f32 radius, s32 queryMode) {
    return 0;
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_AE1D0/func_1508108C.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_AE1D0/func_1508114C.s")

/* Find the first loaded actor of this type that passes the spatial query. */
s32 func_15081574(struct127 *origin, f32 forwardOffset, f32 radius,
    s32 *foundActorAddress, s32 queryMode, s32 actorType) {
    u8 *actor;
    s32 part;
    s32 value;

    *foundActorAddress = 0;
    actor = D_800CC2D0;
    do {
        if (*(s32 *)actor != 0 && *(void **)(actor + 0x1D4) != NULL &&
            actor[4] == actorType) {
            part = func_1508108C(actor);
            if (part != -1) {
                value = func_15080D20((u8 *)origin, actor, D_8009BD30[part * 4 + 2],
                    forwardOffset, radius, queryMode);
                if (value != 0) {
                    *foundActorAddress = (s32)actor;
                    return value;
                }
            }
        }
        actor += 0x32C;
    } while (actor != D_800D121C);
    return 0;
}
