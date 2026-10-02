#include <ultra64.h>

#include "functions.h"
#include "variables.h"

/* Generated placeholder declarations. */
s32 func_1513B5E0();
void func_1513B798(u8 *arg0);
s32 func_1513B83C();
s32 func_1513BAE8();
s32 func_1513BBFC();
s32 func_1513BEB0();
s32 func_15109064(struct132 *, s32, u8);
s32 func_151BA468(struct132 *, s32, u8);
/* End generated placeholder declarations. */

extern s32 (*D_80089C18[])();

/* Non-matching C placeholders for asm/nonmatchings/game_168A90/func_1513B5E0.s. */
s32 func_1513B5E0() {
    return 0;
}
void func_1513B798(u8 *arg0) {
    s32 remove = 0;
    s8 callbackIndex;

    if ((arg0[0x10] & 1) != 0) {
        *(s16 *)(arg0 + 0x14) -= D_800BE9E4;
        if (*(s16 *)(arg0 + 0x14) < 0) {
            remove = 1;
        }
    }

    if (remove == 0) {
        callbackIndex = *(s8 *)(arg0 + 0x11);
        if ((callbackIndex != -1) && (D_80089C18[callbackIndex]() == 0)) {
            remove = 1;
        }
    }

    if (remove != 0) {
        func_1516972C((struct102 *)arg0);
    }
}
/* Non-matching C placeholders for asm/nonmatchings/game_168A90/func_1513B83C.s. */
s32 func_1513B83C() {
    return 0;
}

s32 func_1513B968(s32 arg0, s32 arg1) {
    // FIXME: &arg0->unk_120[D_800BE9C0]
    func_150A7B80(arg0 + 120 + (D_800BE9C0 << 6));
    return 1;
}

void func_1513B9A8(struct132 *arg0) {
    func_100043B4(arg0->unk4C, 4);
    func_15169804(arg0);
}

void func_1513B9DC(struct132 *arg0) {
    func_100043B4(arg0->unk4C, 4);
    func_15169824(arg0);
}

void func_1513BA10(struct132 *arg0) {
    D_80089C44[arg0->unk48]();
}

void func_1513BA44(struct132 *arg0) {
    D_80089C54[arg0->unk48]();
}

void func_1513BA78(struct132 *arg0, s32 arg1, u8 arg2) {
    switch (arg0->unk48) {
        case 1:
            func_15109064(arg0, arg1, arg2);
            break;
        case 2:
            func_151BA468(arg0, arg1, arg2);
            break;
    }
}

s32 func_1513BAD4(s32 arg0, s32 arg1) {
    return 0;
}

/* Non-matching C placeholders for asm/nonmatchings/game_168A90/func_1513BAE8.s. */
s32 func_1513BAE8() {
    return 0;
}
/* Non-matching C placeholders for asm/nonmatchings/game_168A90/func_1513BBFC.s. */
s32 func_1513BBFC() {
    return 0;
}
/* Non-matching C placeholders for asm/nonmatchings/game_168A90/func_1513BEB0.s. */
s32 func_1513BEB0() {
    return 0;
}
