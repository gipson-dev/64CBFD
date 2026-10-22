#include <ultra64.h>

#include "functions.h"
#include "variables.h"

/* Generated placeholder declarations. */
s32 func_150039E0();
s32 func_150045C4();
void func_150049A4(s8 *, u32, u32);
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
/* Relocate vertex/data and matrix command addresses in place. */
void func_150049A4(s8 *commands, u32 dataOffset, u32 matrixOffset) {
    s32 index;
    s8 *command;
    s32 opcode;

    for (index = 0; commands[index << 3] != (s8)G_ENDDL; index++) {
        command = commands + (index << 3);
        opcode = command[0];
        switch (opcode) {
            /* Retail keeps this positive comparison after the signed load. */
            case G_DL:
                *(u32 *)(command + 4) += dataOffset;
                break;
            case G_VTX:
                *(u32 *)(command + 4) += dataOffset;
                break;
            case (s8)G_MOVEMEM:
                if ((u8)command[3] == G_MV_MATRIX) {
                    *(u32 *)(command + 4) += matrixOffset;
                }
                break;
        }
    }
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
void func_15004CE0(s8 *arg0, s32 arg1) {
    s32 i = 0;
    s8 *cur = arg0;
    s32 opcode;

    if (cur[0] != -0x21) {
        opcode = *(volatile s8 *)cur;
        do {
            if ((opcode == -0x24) && ((u8)cur[3] == 0xE) && (*(u32 *)(cur + 4) < 0x80000000U)) {
                *(u32 *)(cur + 4) += arg1;
            }
            i++;
            cur = (s8 *)((u32)arg0 + (i << 3));
            opcode = cur[0];
        } while (opcode != -0x21);
    }
}
