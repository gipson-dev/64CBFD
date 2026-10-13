#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/61490.s. */

s32 func_1502DB20(s32 type);

extern u8 D_800CC2D4[];
void func_1503B9BC(s32 index);

extern u8 D_800CC2D0[];
extern u8 D_800BEAC0;
extern s32 D_800D121C;

s32 func_15033FE0() {
    return 0;
}

s32 func_150341BC() {
    return 0;
}

u8 *func_15034340(u8 *arg0, s32 arg1) {
    s8 *record = (s8 *)&D_800CC2D0[arg1 * 0x32C];

    if (record[0x1D1] != 0) {
        *(s16 *)arg0 = 6;
        arg0 += 4;
        *(s16 *)(arg0 - 2) = record[0x1D1] * 200;
    }

    return arg0;
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_61490/func_150343B0.s")

/* Original mounted-gun bone command writer; OGL Note 653. */
#pragma GLOBAL_ASM("asm/nonmatchings/generated_61490/func_15034420.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_61490/func_150344A0.s")

void func_1503453C(s32 index) {
    switch (D_800CC2D4[(u32)index * 0x32C]) {
        case 0:
        case 1:
        case 2:
        case 3:
        case 4:
        case 0x80:
        case 0xB0:
            func_1503B9BC(index);
            break;
    }
}

s32 func_150345E4() {
    return 0;
}

void func_15034728(u8 *actor) {
    s32 last;
    s32 bone;
    s32 row;
    s32 offset;
    u32 buffer;

    if (*(u32 *)(actor + 0x1D4) == 0 || *(u32 *)(actor + 0x9C) == 0) {
        return;
    }
    last = (s32)((u32)func_1502DB20(actor[4]) - 1);
    buffer = *(u32 *)(actor + 0x1D4);
    bone = 31;
    if (last < 31) {
        bone = last;
    }
    for (; bone >= 0; bone--) {
        if (*(u32 *)(actor + 0x9C) & (1U << bone)) {
            u32 matrix = buffer + bone * 64;
            for (row = 0; row < 3; row++) {
                u32 vector = matrix + (row << 4);
                for (offset = 0; offset < 12; offset += 4) {
                    *(f32 *)(vector + offset) = 0.0f;
                }
            }
        }
    }
}

void func_150347E8(void) {
    u8 *record = D_800CC2D0;

    if (D_800BEAC0 == 0) {
        u8 *end = (u8 *)&D_800D121C;

        do {
            if ((*(s32 *)record != 0) && (*(s32 *)(record + 0x9C) != 0)) {
                func_15034728(record);
            }
            record += 0x32C;
        } while (record != end);
    }
}
