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

void *func_15167A68(s32, s32, s32, s32, u8, u8);
void func_1517E05C(s32, s32, s32);
/* Initialize two quads and publish the effect's world-coordinate origin. */
void func_15166118(s32 first, s32 second, s32 x, s32 y, s32 z,
                   s32 step, s32 lifetime, s32 mode, u8 selector, s32 category) {
    u8 *created;
    u8 *vertices;
    s32 quad;

    created = (u8 *)func_15167A68(4, category, 0xA8, 1, selector, 1);
    if (created != NULL) {
        created[0x95] = 2;
        vertices = created;
        quad = 0;
        do {
            quad++;
            vertices += 0x40;
            *(s16 *)(vertices - 0x28) = 0x2000;
            *(s16 *)(vertices - 0x26) = 0x2000;
            *(s16 *)(vertices - 0x18) = 0x2800;
            *(s16 *)(vertices - 0x16) = 0x2000;
            *(s16 *)(vertices - 0x8) = 0x2800;
            *(s16 *)(vertices - 0x6) = 0x2800;
            *(s16 *)(vertices + 0x8) = 0x2000;
            *(s16 *)(vertices + 0xA) = 0x2800;
        } while (quad != 2);
        *(s16 *)(created + 0x9E) = 1;
        created[0x92] = lifetime;
        created[0x93] = lifetime;
        *(s16 *)(created + 0x98) = x;
        *(s16 *)(created + 0x9A) = y;
        *(s16 *)(created + 0x9C) = z;
        *(s16 *)(created + 0x96) = step;
        created[0x94] = mode;
        created[0xA0] = first;
        created[0xA1] = second;
        func_1517E05C(x, y, z);
    }
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
