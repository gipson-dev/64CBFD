#include <ultra64.h>
#include "structs.h"
extern s8 D_800DD190;
extern struct102 *D_800DCE94;
extern void *D_800DD198[];
extern u8 D_800C3E78;
void func_1516972C(struct102 *);
extern s32 D_800BE9F0;
s32 func_150AF200(s32, u8);
s32 func_15179008(s32);
void func_151CF898(s32, f32, f32);
extern f32 D_800BE9A4;
f32 func_15144B68(f32);
u8 *func_151149AC(u8);

/* Non-matching placeholders for the text-only asm slice asm/DC6B0.s. */

s32 func_15131828();
s32 func_15131958();
s32 func_1515FF74();

typedef struct {
    s8 unk0;
    s8 unk1;
    s8 unk2;
    u8 pad3;
    s16 unk4;
    s8 unk6;
} UnkAF738;

typedef struct {
    f32 unk0;
    f32 unk4;
    f32 unk8;
    f32 unkC;
} UnkAFBF4Values;

typedef struct {
    u8 pad0[0x10];
    f32 unk10;
    u8 pad14[0x5C];
    UnkAFBF4Values values;
} UnkAFBF4;

typedef struct {
    f32 unk0;
    f32 unk4;
    u8 *record;
    f32 unkC;
    f32 unk10;
    f32 unk14;
} UnkB060C;

#pragma GLOBAL_ASM("asm/nonmatchings/generated_DC6B0/func_150AF200.s")

// Matched with guarded commutative-add normalization.
void func_150AF2E0(s32 arg0, u8 *arg1) {
    s32 temp_v0 = *(s16 *) (arg1 + 2);

    func_151CF898(arg0, (f32) (*(s16 *) (arg1 + 8) + temp_v0), (f32) temp_v0);
}

s32 func_150AF328() {
    return 0;
}

s32 func_150AF6E4(u8 *arg0, s32 arg1) {
    u8 *temp_a2 = arg0 + 0xA8;

    func_15131828(arg0, arg0 + 0xAC, temp_a2, arg0 + 0xAA);
    func_15131958(arg0 + 0x58, *(s32 *) (temp_a2 + 0xC));
    return 1;
}

void func_150AF738(s16 arg0, u8 arg1, s32 arg2) {
    UnkAF738 sp18;

    sp18.unk0 = 1;
    sp18.unk1 = -1;
    sp18.unk2 = 2;
    sp18.unk4 = arg0;
    sp18.unk6 = 0;
    func_1515FF74(&sp18, 0, arg1, arg2);
}

void func_150AF790(u8 arg0, u8 *arg1) {
    func_150B1DB0(arg1, arg1 + 0x1ECC0);
}

s32 func_150AF7C4() {
    return 0;
}

s32 func_150AFBF4(UnkAFBF4 *arg0, register UnkAFBF4Values *values) {
    arg0->values.unk8 += arg0->values.unkC * D_800BE9A4;
    values = &arg0->values;
    values->unk8 = func_15144B68(values->unk8);
    arg0->unk10 = sinf(values->unk8) * values->unk4 + values->unk0;
    return 1;
}

s32 func_150AFC68() {
    return 0;
}

/* Release list nodes owned by the current object, preserving nested iterators. */
void func_150AFDB0(void) {
    struct102 *node;

    D_800DD190++;
    node = D_800DCE94;
    while (node != NULL) {
        D_800DD198[D_800DD190] = (struct102 *)node->unk8;
        if (D_800C3E78 == node->pad3E[1]) {
            func_1516972C(node);
        }
        node = D_800DD198[D_800DD190];
    }
    D_800DD190--;
}

s32 func_150AFE64() {
    return 0;
}

/* Select the command pair, with the extra setup call in category 6. */
void func_150B003C(s32 unused) {
    if (D_800BE9F0 == 6) {
        func_15179008(0);
        func_150AF200(0xE2, 0xE1U);
        return;
    }
    func_150AF200(0xDF, 0xDEU);
}

s32 func_150B0094() {
    return 0;
}

s32 func_150B02C0(u8 *arg0) {
    u8 *temp_a1 = arg0;

    if (*(s32 volatile *)(temp_a1 + 0x170) != 0) {
        func_1516972C((struct102 *)*(s32 volatile *)(temp_a1 + 0x170));
    }
}

s32 func_150B02F0(s32 arg0) {
    func_150B02C0(arg0);
    func_15132570(arg0);
}

s32 func_150B031C(s32 arg0) {
    func_150B02C0(arg0);
    func_1513259C(arg0);
}

s32 func_150B0348() {
    return 0;
}

s32 func_150B060C(u8 arg0, UnkB060C *arg1) {
    arg1->record = func_151149AC(arg0);
    if (arg1->record == NULL) {
        return 0;
    }

    arg1->unk0 = -150.0f;
    arg1->unk4 = 4.5f;
    arg1->unkC = (f32)*(s16 *)(arg1->record + 0x10);
    arg1->unk10 = (f32)*(s16 *)(arg1->record + 0x12);
    arg1->unk14 = (f32)*(s16 *)(arg1->record + 0x14);
    return 1;
}
