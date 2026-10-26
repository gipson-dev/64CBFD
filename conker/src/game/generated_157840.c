#include <ultra64.h>
#include "structs.h"

/* Non-matching placeholders for the text-only asm slice asm/157840.s. */

s32 func_1512A390() {
    return 0;
}

s32 func_1512ABF8() {
    return 0;
}

s32 func_1512AD54() {
    return 0;
}

extern u8 D_800BEAC0;
extern u8 D_800C3671;

/* Request the fixed state unless the actor can use its normal handler. */
void func_1512B100(u8 *actor) {
    s32 type = *(s32 *)(actor + 0x2C);

    if ((type & ~0x100) && !D_800BEAC0 && !D_800C3671) {
        if ((type != 0x40) && (*(s32 *)(actor + 0x84) & 8) &&
            !(*(s32 *)(actor + 0x84) & 0x200) && !actor[0x23C] &&
            !(*(s32 *)(actor + 0x5F0) & 0x80) && !(*(s32 *)(actor + 0x5F0) & 0x40)) {
            func_1512AD54(actor);
        } else {
            *(s16 *)(actor + 0x5F8) = 1;
            *(u16 *)(actor + 0x5FC) = 2;
            *(s16 *)(actor + 0x5FE) = 60;
        }
    }
}

s32 func_1512B1B8() {
    return 0;
}

s32 func_1512B53C() {
    return 0;
}

void func_1512B5FC(u8 *arg0, s32 arg1, s32 arg2) {
    *(arg0 + 2) = *(arg0 + 1);
    if (*(s32 *) (arg0 + 4) < arg1) {
        *(arg0 + 1) = 0;
    } else {
        *(arg0 + 1) = 1;
    }
    *(s32 *) (arg0 + 8) = arg2;
    *(s32 *) (arg0 + 4) = arg1;
}

s32 func_1512B630() {
    return 0;
}

s32 func_1512B730() {
    return 0;
}

s32 func_1512BB10() {
    return 0;
}

s32 func_1512C068() {
    return 0;
}

extern f32 D_800A3694, D_800A3698;
f32 func_15048A70(f32 current, f32 target);

/* Advance the angle blend, then mark completion or apply one wrapped delta. */
void func_1512C150(struct108 *actor) {
    f32 delta;

    actor->unk5CC += D_800A3694;
    actor->unk5CC = actor->unk5CC > 1.0f ? 1.0f : actor->unk5CC;
    if (actor->unk5CC == 1.0f) {
        actor->unk384 = D_800A3698;
        actor->unk240 &= ~2;
    } else {
        delta = func_15048A70(actor->unk384, actor->unk37C);
        actor->unk384 += delta * actor->unk5CC;
    }
}

void func_1512C200(s32 arg0) {
}

s32 func_1512C20C() {
    return 0;
}

s32 func_1512C47C(s32 arg0) {
    return 1;
}
