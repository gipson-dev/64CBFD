#include <ultra64.h>

/* Recovered routines and remaining placeholders for asm/1A6360.s. */

extern u8 *D_800DBFF0;
extern s16 D_800DD436;
extern u8 **D_800DD440;

s32 func_15178EB0() {
    return 0;
}

s32 func_15178EFC() {
    return 0;
}

s32 func_15179008() {
    return 0;
}

#include "structs.h"
#include <math.h>

extern u8 *D_800DBFF0;
f32 func_150AD78C(f32);
f32 func_150AD780(f32);
extern s16 D_800DD438[3];

/* Build the offset point from truncated camera coordinates and two live angles. */
void func_151794C8(void) {
    s32 x;
    s32 y;
    s32 z;
    f32 zero;
    f32 vertical;
    f32 horizontal;
    f32 sine;
    f32 angle;

    zero = 0.0f;
    x = (s32)((struct108 *)D_800DBFF0)->unk2F8;
    y = (s32)((struct108 *)D_800DBFF0)->unk2FC;
    z = (s32)((struct108 *)D_800DBFF0)->unk300;
    angle = ((struct108 *)D_800DBFF0)->unk398;
    sine = func_150AD78C(angle);
    horizontal = func_150AD780(angle);
    vertical = 500.0f * sine;
    horizontal = -500.0f * horizontal;
    angle = ((struct108 *)D_800DBFF0)->unk3A0;
    sine = func_150AD78C(angle);
    angle = func_150AD780(angle);
    x = (s32)((f32)x + (zero + horizontal * sine));
    z = (s32)((f32)z + (horizontal * angle - zero));
    y = (s32)((f32)y + vertical);
    D_800DD438[0] = x;
    D_800DD438[2] = z;
    D_800DD438[1] = y;
}

s32 func_15179600() {
    return 0;
}

s32 func_151797B0() {
    return 0;
}

void func_15179AB8(void) {
    s32 i;
    u8 *object;
    u32 flags;

    for (i = D_800DD436 - 1; i >= 0; i--) {
        object = D_800DD440[i];
        if (object != NULL) {
            flags = *(u32 *) (object + 0x90);
            if (!(flags & 2)) {
                *(u32 *) (object + 0x90) = flags | 2;
                return;
            }
        }
    }
}

s32 func_15179B14() {
    return 0;
}

/* Derive the record opacity byte from planar viewer distance. */
void func_15179CB0(u8 *record) {
    f32 dx;
    f32 dz;
    f32 distance;
    u8 *viewer;

    viewer = D_800DBFF0;
    dx = (f32)*(s16 *)(record + 0xA0) - *(f32 *)(viewer + 0x300);
    dz = (f32)*(s16 *)(record + 0x9C) - *(f32 *)(viewer + 0x2F8);
    distance = sqrtf(dx * dx + dz * dz);
    record[0xB4] = (u32)(255.0f - distance * 160.0f / 1000.0f);
}
