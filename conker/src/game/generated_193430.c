#include <ultra64.h>
typedef struct {
    u32 unk0;
    u8 unk4;
    u8 pad5;
    u16 unk6;
    u16 unk8;
    u8 unkA;
    u8 unkB;
} structC1D70Source;
extern s16 D_800DCE40;
extern s32 D_800DD220, D_800DD224;
extern u8 *D_800DD228;
extern u8 D_800DD230[], D_800903F4[];
extern u32 D_800D2C9C, D_800A4AC8[];
s32 func_15094F70(s32, structC1D70Source *, s32, u8 *, s32, s32, s32, s32, s32);
Gfx *func_15142FBC(Gfx *, u32, u32, u8 *);


extern s32 D_800BE9E4;
extern void func_1516972C(void *arg0);

/* Non-matching placeholders for the text-only asm slice asm/193430.s. */

s32 func_15165F80() {
    return 0;
}

s32 func_15166118() {
    return 0;
}

void func_15166204(u8 *arg0) {
    s32 timer = arg0[0x92];

    *(s16 *)(arg0 + 0x9E) += *(s16 *)(arg0 + 0x96) * D_800BE9E4;
    timer -= D_800BE9E4;
    if (timer <= 0) {
        func_1516972C(arg0);
    } else {
        arg0[0x92] = timer;
    }
}

s32 func_15166268() {
    return 0;
}

/* Advance the signed ring offset and submit its display-list packet. */
Gfx *func_151668B8(Gfx *commands, s32 unusedIndex, s32 unusedPacked, s32 unusedHighHalf) {
    u8 sync;

    D_800DD228 = D_800903F4;
    D_800DD220 = D_800DCE40;
    D_800DCE40 += 0x80;
    sync = 1;
    if (D_800DCE40 >= 0x500) {
        D_800DCE40 = 0;
    }
    D_800DD224 = 1;
    commands = (Gfx *)func_15094F70((s32)commands, (structC1D70Source *)D_800DD228,
                                  D_800DD220, D_800DD230, 0, 0, 0, D_800DD224, 3);
    return func_15142FBC(commands, D_800D2C9C | 0x80000 | 0x2CA0,
                         D_800A4AC8[7] | D_800A4AC8[6], &sync);
}
