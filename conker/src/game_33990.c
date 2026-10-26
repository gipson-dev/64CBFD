#include <ultra64.h>

#include "functions.h"
#include "variables.h"

/* Generated placeholder declarations. */
s32 func_15006590();
s32 func_15006BEC();
s32 func_1500707C();
s32 func_15007168();
s32 func_1500727C();
s32 func_15007360();
s32 func_15007440();
s32 func_15007558();
/* End generated placeholder declarations. */

void func_150064E0(void) {
    s32 i = 0;
    func_15017790();

    do {
        D_800C3A60[i++] = 0;
    } while (i < 69);

    D_800BE3DF = 24;
    D_800BE3E8 = 0;
    D_800D2E45 = 1;
}

/* Non-matching C placeholders for asm/nonmatchings/game_33990/func_15006590.s. */
s32 func_15006590() {
    return 0;
}
/* Non-matching C placeholders for asm/nonmatchings/game_33990/func_15006BEC.s. */
s32 func_15006BEC() {
    return 0;
}
/* Non-matching C placeholders for asm/nonmatchings/game_33990/func_1500707C.s. */
s32 func_1500707C() {
    return 0;
}
// requires jump table
/* Non-matching C placeholders for asm/nonmatchings/game_33990/func_15007168.s. */
s32 func_15007168() {
    return 0;
}
/* Non-matching C placeholders for asm/nonmatchings/game_33990/func_1500727C.s. */
s32 func_1500727C() {
    return 0;
}
/* Non-matching C placeholders for asm/nonmatchings/game_33990/func_15007360.s. */
s32 func_15007360() {
    return 0;
}
/* Non-matching C placeholders for asm/nonmatchings/game_33990/func_15007440.s. */
s32 func_15007440() {
    return 0;
}
/* Non-matching C placeholders for asm/nonmatchings/game_33990/func_15007558.s. */
s32 func_15007558() {
    return 0;
}

void func_15007644(void) {
}

void func_1500764C(void) {
    D_80082BB4 = (u8)6;
    D_800BE3EC = (u8)0;
}

void func_15007668(void) {
    D_80082BB4 = (u8)7;
    D_800BE3EC = (u8)0;
}

void func_15007684(void) {
    D_80082BB4 = (u8)4;
    D_800BE3EC = (u8)0;
}

void func_150076A0(void) {
    D_80082BB4 = (u8)5;
    D_800BE3EC = (u8)0;
}

void func_150076BC(s32 arg0) {
    if (arg0 < 0) {
        func_150064E0();
    }
    if ((arg0 >= 0) && (arg0 < 4) && (D_800BE616 == 0)) {
        D_80082BB4 = (u8)1;
        D_800BE3EC = arg0;
    }
}

void func_15007718(s32 arg0) {
    if ((arg0 >= 0) && (arg0 < 3) && (D_800BE616 == 0)) {
        D_80082BB4 = (u8)2;
        D_800BE3EC = arg0;
    }
}

void func_15007750(s32 arg0) {
    if ((arg0 >= 0) && (arg0 < 3)) {
        D_80082BB4 = (u8)3;
        D_800BE3EC = arg0;
    }
}

/* Reset inline record sentinels, the pointed-to bytes and local selection bytes. */
void func_15007778(void) {
    s32 i;
    u8 *cursor;

    D_800BE3F8.unk8 = -1;
    D_800BE3F8.unk18 = -1;
    D_800BE3F8.unk28 = -1;
    D_800BE3F8.unkE = -1;
    D_800BE3F8.unk1E = -1;
    D_800BE3F8.unk2E = -1;
    D_800BE3DC = -1;
    D_800BE3DE = 0;
    D_80082BC0 = 1;

    i = 0;
    for (;;) {
        ((u8 *)D_800D2E4C)[i++] = 0;
        if (i >= 27) {
            break;
        }
    }

    cursor = D_800D2E60;
    do {
        *cursor++ = 0;
    } while (cursor < D_800D2E60 + 9);

    D_800BE3D8.byte0 = D_800BE3D8.byte1 = D_800BE3D8.byte2 = D_800BE3D8.byte3 = -1;
}
