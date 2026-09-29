#include <ultra64.h>

#include "structs.h"
#include "variables.h"

/* Non-matching placeholders for the text-only asm slice asm/156160.s. */

typedef struct {
    u16 unk0;
    s16 unk2;
    f32 unk4;
    f32 unk8;
    u8 padC[0x18];
} Generated156160Slot;

extern f32 D_800A3610;
extern Generated156160Slot D_800DC028[];

s32 func_15128CB0() {
    return 0;
}

void func_151298C0(struct108 *arg0, s32 arg1) {
    if (D_80089550 != 0) {
        D_800DC028[arg0->unk23D].unk2 = 0;
        D_800DC028[arg0->unk23D].unk4 = -1.0f;
        D_800DC028[arg0->unk23D].unk8 = D_800A3610;
    }
}

s32 func_15129934() {
    return 0;
}
