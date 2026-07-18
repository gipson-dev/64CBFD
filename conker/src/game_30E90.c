#include <ultra64.h>

#include "functions.h"
#include "variables.h"

/* Generated placeholder declarations. */
s32 func_150039E0();
s32 func_150045C4();
s32 func_150049A4();
s32 func_15004AAC();
s32 func_15004BF0();
/* End generated placeholder declarations. */

/* Non-matching C placeholders for asm/nonmatchings/game_30E90/func_150039E0.s. */
s32 func_150039E0() {
    return 0;
}

// FIXME: matches but something isnt right
void func_15004574(void) {
    if (D_800DBF88 != 0xFF) {
        D_800DBF8C = D_800DBEF4[D_800DBF88].unk1C;
        D_800DBF90 = D_800DBEF4[D_800DBF88].unk28;
    }
}

void func_150045BC(void) {
}

/* Non-matching C placeholders for asm/nonmatchings/game_30E90/func_150045C4.s. */
s32 func_150045C4() {
    return 0;
}
/* Non-matching C placeholders for asm/nonmatchings/game_30E90/func_150049A4.s. */
s32 func_150049A4() {
    return 0;
}
// NON-MATCHING: not this...
void func_15004A4C(void) {
    s32 i;

    for (i = 0; i < D_800DBEF0; i++) {
        D_800DBEF8[i] = 0;
        D_800DBEFC[i] = 0;
    }
}

/* Non-matching C placeholders for asm/nonmatchings/game_30E90/func_15004AAC.s. */
s32 func_15004AAC() {
    return 0;
}
/* Non-matching C placeholders for asm/nonmatchings/game_30E90/func_15004BF0.s. */
s32 func_15004BF0() {
    return 0;
}
void func_15004CE0(u8 *arg0, s32 arg1) {
    u8 *cur;

    for (cur = arg0; cur[0] != 0xDF; cur += 8) {
        if ((cur[0] == 0xDC) && (cur[3] == 0xE) && (*(u32 *)(cur + 4) < 0x80000000U)) {
            *(u32 *)(cur + 4) += arg1;
        }
    }
}
