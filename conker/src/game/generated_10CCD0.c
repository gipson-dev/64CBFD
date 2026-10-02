#include <ultra64.h>
#include "functions.h"
#include "structs.h"

extern f32 D_800A0F60;
extern f32 D_800A0F64;

void func_150DF820(struct108 *arg0) {
    s32 flags;

    *(volatile s32 *)&arg0->unk84 = flags = arg0->unk84 & ~0x4000;
    *(volatile s32 *)&arg0->unk84 = flags = flags | 4;
    *(volatile s32 *)&arg0->unk84 = flags = flags & ~0x1010;
    flags |= 0x1010;

    if (arg0->unk3D0->in_water != 0) {
        arg0->unk84 = flags;
        flags &= ~4;
        *(volatile s32 *)&arg0->unk84 = flags;
        arg0->unk374 = D_800A0F60;
    } else if (arg0->unk374 == D_800A0F64) {
        arg0->unk1B4 = 3;
        func_15124B18(arg0);
    }
}
