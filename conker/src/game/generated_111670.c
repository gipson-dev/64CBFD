#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/111670.s. */

#include "structs.h"
#include <math.h>

extern struct108 *D_800DBFF0;
extern s16 D_800D99F0[3];

/* Build the offset point from truncated camera coordinates and two live angles. */
void func_150E41C0(void) {
    s32 x;
    s32 y;
    s32 z;
    f32 zero;
    f32 vertical;
    f32 horizontal;
    f32 sine;
    f32 angle;

    zero = 0.0f;
    x = (s32)D_800DBFF0->unk2F8;
    y = (s32)D_800DBFF0->unk2FC;
    z = (s32)D_800DBFF0->unk300;
    angle = D_800DBFF0->unk398;
    sine = sinf(angle);
    horizontal = cosf(angle);
    vertical = 500.0f * sine;
    horizontal = -500.0f * horizontal;
    angle = D_800DBFF0->unk3A0;
    sine = sinf(angle);
    angle = cosf(angle);
    x = (s32)((f32)x + (zero + horizontal * sine));
    z = (s32)((f32)z + (horizontal * angle - zero));
    y = (s32)((f32)y + vertical);
    D_800D99F0[0] = x;
    D_800D99F0[2] = z;
    D_800D99F0[1] = y;
}

s32 func_150E42F8() {
    return 0;
}

void func_150E4514(s32 arg0) {
    func_150E41C0();
    func_150E42F8(arg0 / 0x1E);
}

s32 func_150E4550() {
    return 0;
}

s32 func_150E4928() {
    return 0;
}

s32 func_150E4CBC() {
    return 0;
}

s32 func_150E4E04() {
    return 0;
}

s32 func_150E5558() {
    return 0;
}

s32 func_150E5810() {
    return 0;
}
