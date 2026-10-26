#include <ultra64.h>

typedef struct { u8 red, green, blue; } EnvironmentColorBytes;
extern EnvironmentColorBytes D_800BE530[];
extern s16 D_800BE550[];
extern u8 D_800BE564;

extern u8 D_800DF9B3[];
extern u8 D_800DF7D3[];
extern u8 D_800DF7D0[];

/* Non-matching placeholders for the text-only asm slice asm/3FC60.s. */

s32 func_150127B0() {
    return 0;
}

s32 func_15012C84() {
    return 0;
}

/* Collect environment RGB values and command indices up to the end-list opcode. */
s32 func_15012ED8(u32 *displayList) {
    s32 index = 0;
    s32 opcode = (s8)(displayList[0] >> 24);
    u32 *cursor = displayList;
    s32 slot;
    u32 payload;

    while (opcode != -33) {
        if (opcode == -5) {
            slot = D_800BE564;
            D_800BE550[slot] = index;
            D_800BE530[slot].red = cursor[1] >> 24;
            D_800BE530[slot].green = cursor[1] >> 16;
            payload = cursor[1];
            D_800BE564 = slot + 1;
            D_800BE530[slot].blue = payload >> 8;
        }
        index++;
        cursor += 2;
        opcode = (s8)(cursor[0] >> 24);
    }
    return index;
}

void func_15012F90(void) {
    s32 i;

    for (i = 0; i < 0x1E3; i++) {
        D_800DF7D0[i] = 0;
    }
}
