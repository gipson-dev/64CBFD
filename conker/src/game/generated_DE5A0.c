#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/DE5A0.s. */

s32 func_150B10F0() {
    return 0;
}

#include "structs.h"
extern s32 *D_800D2104;
extern f32 D_8009F8BC, D_8009F8C0;
void func_15058EA4(struct127 *, f32, f32, f32, f32, f32, f32);
s32 func_15056B08(s32);
void func_15059140(struct127 *);
s32 func_150535F4(struct127 *);
s32 func_1502178C();

/* Apply vertical limits, then smooth the wrapped movement-angle correction. */
void func_150B12FC(struct127 *actor) {
    s16 oldAngle;
    s16 angleChange;
    f32 height;
    f32 correction;
    f32 previous;

    oldAngle = (s16)actor->unk76;
    actor->unk80 = 10;
    height = (f32)((s16 *)D_800D2104[actor->unk13F])[1];
    func_15058EA4(actor, height, 1.0f, height, D_8009F8BC, 12.0f, -16.0f);
    func_15056B08((s32)actor);
    angleChange = (oldAngle - actor->unk76) * 6;
    previous = actor->unkC4;
    correction = angleChange * (1.0f / 256.0f) - previous;
    if (correction > 6.0f) correction = 6.0f;
    else if (correction < -6.0f) correction = -6.0f;
    actor->unk148 += (correction - actor->unk148) * D_8009F8C0;
    actor->unkC4 += actor->unk148;
    actor->unk40 = (s16)(actor->unk7A + 0x4000) * 0.0054931640625f;
    func_15059140(actor);
    if (!func_150535F4(actor)) func_1502178C(actor, 0, -1);
}


s32 func_150B1484() {
    return 0;
}

s32 func_150B17DC() {
    return 0;
}

s32 func_150B19E0() {
    return 0;
}
