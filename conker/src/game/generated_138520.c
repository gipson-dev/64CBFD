#include <ultra64.h>

extern u8 *D_800BE628;
extern u8 D_80089470[];
extern u8 D_800BE9C0;
extern u8 *D_800DC2A0[];
extern f32 D_800D35E0;
extern f32 D_800D35E4;
extern f32 D_800D9AC0[][3];
extern u8 D_800D9AF0;

/* Non-matching placeholders for the text-only asm slice asm/138520.s. */

s32 func_1510B070() {
    return 0;
}

s32 func_1510B128() {
    return 0;
}

// Eight guards preserve retail's five-word float ABI and register sequence.
s32 func_1510B32C(s32 arg0, f32 arg1, f32 arg2, f32 arg3) {
    func_1510B128(arg0, *(s32 *)&arg1, *(s32 *)&arg2, *(s32 *)&arg3, 0);
    D_800D9AC0[arg0][0] = arg3;
    D_800D9AC0[arg0][1] = arg1;
    D_800D9AC0[arg0][2] = arg2;
    D_800D9AF0 = 1;
}

s32 func_1510B3B0() {
    return 0;
}

s32 func_1510B458() {
    return 0;
}

s32 func_1510B51C() {
    return 0;
}

s32 func_1510B5F8() {
    return 0;
}

s32 func_1510B690() {
    return 0;
}

Gfx *func_1510B7B4(Gfx *arg0, s32 arg1) {
    gDPPipeSync(arg0++);
    gDPSetBlendColor(arg0++, 0, 0, 0, 1);
    gSPMatrix(arg0++, D_80089470, G_MTX_MODELVIEW | G_MTX_LOAD | G_MTX_NOPUSH);
    gSPPerspNormalize(arg0++, *(u16 *) (D_800BE628 + arg1 * 0x180 + 0xB8));
    gSPClipRatio(arg0++, FRUSTRATIO_3);
    gSPClearGeometryMode(arg0++, G_LOD);
    gSPMatrix(arg0++, (u32) D_800BE628 + arg1 * 0x180 + D_800BE9C0 * 0x40 + 0x100,
              G_MTX_PROJECTION | G_MTX_LOAD | G_MTX_NOPUSH);
    gSPMatrix(arg0++, D_800DC2A0[D_800BE9C0] + arg1 * 0x40,
              G_MTX_PROJECTION | G_MTX_MUL | G_MTX_NOPUSH);
    gDPSetOtherMode(arg0++, 0x082C3F, 0x552230);
    return arg0;
}

void func_1510B958(s32 arg0) {
    u8 *record = D_800BE628 + arg0 * 0x180;

    D_800D35E0 = *(f32 *) (record + 0x64) +
                 ((*(f32 *) (record + 0x74) /
                   *(f32 *) (record + 0x6C)) - 1.0f) * -1.0f;
    D_800D35E4 = *(f32 *) (record + 0x68) +
                 ((*(f32 *) (record + 0x78) /
                   *(f32 *) (record + 0x70)) - 1.0f) * -1.0f;
}

s32 func_1510B9D0() {
    return 0;
}

s32 func_1510BF60() {
    return 0;
}

s32 func_1510C4AC() {
    return 0;
}

s32 func_1510C8A8() {
    return 0;
}
