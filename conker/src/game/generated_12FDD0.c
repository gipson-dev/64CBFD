#include <ultra64.h>
#include "structs.h"

/* Non-matching placeholders for the text-only asm slice asm/12FDD0.s. */

#pragma GLOBAL_ASM("asm/nonmatchings/generated_12FDD0/func_15102920.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_12FDD0/func_15102B38.s")

void func_15102D50(u8 *arg0, s32 arg1, u8 arg2) {
    func_15169850(arg1, arg2, (s32) (arg0 + 0x110), (s32) (arg0 + 0x114), (s32) arg0);
}

typedef struct { u8 pad00[0x34]; struct17 input[2]; u8 pad4C[0xC4]; struct127 *actor; u8 identity; u8 pad115[3]; s32 matrixOffset; s16 descriptorId; u8 pad11E[2]; s32 descriptorIndex; u8 flags; u8 pad125[3]; struct17 output[2]; } LinkOwner15102D90;
struct126 *func_1503195C(struct127 *, s32, s32);
s32 func_1514654C(struct127 *, u8 *, s32, struct17 **, struct17 **, s32);
void func_15145EA4(struct17 **, struct17 **, u8 *, s32);
/* Validate the linked actor and transform two input vectors into the owner. */
s32 func_15102D90(LinkOwner15102D90 *owner) {
    struct127 *actor = owner->actor;
    struct17 *input[2], *output[2];
    struct126 *descriptor;
    owner->flags &= ~1;
    if (owner->identity != actor->unique_id || actor->interaction_state == 0) return 0;
    if (actor->unk1D4 == 0 || (actor->unk74 & 0xF) == 0xF) return 1;
    input[0] = &owner->input[0]; input[1] = &owner->input[1];
    output[0] = &owner->output[0]; output[1] = &owner->output[1];
    if (owner->descriptorId != -1) {
        descriptor = func_1503195C(actor, owner->descriptorId, 0);
        if (descriptor == 0) return 0;
        if (!func_1514654C(actor, (u8 *)descriptor, owner->descriptorIndex, input, output, 2)) return 0;
    } else {
        func_15145EA4(input, output, (u8 *)actor->unk1D4 + owner->matrixOffset, 2);
    }
    owner->flags |= 1;
    return 1;
}

s32 func_15102EB8() {
    return 0;
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_12FDD0/func_15103254.s")
