#include <ultra64.h>

extern u8 *D_800BE628;
extern u8 D_80089470[];
extern u8 D_800BE9C0;
extern u8 *D_800DC2A0[];
extern f32 D_800D35E0;
extern f32 D_800D35E4;
extern f32 D_800D9AC0[][3];
extern u8 D_800D9AF0;
extern u8 *D_800DBFF0;
extern u8 D_800C35EA, D_800C3662, D_800BEBA0, D_800BEAAA, D_800DBE62;
extern u16 D_800D18A0;
extern s32 D_800BE9F0, D_800DCD7C;
extern u8 D_800D9B90[], D_800D9BD0[], D_800D9C10[];
extern s32 D_800D9E10[];
extern u8 D_800D9E20, D_800D9E21, D_800D9E28[];
extern Gfx *D_800B0E00, *D_800B0E04, *D_800B0E08;

extern void func_1510CB10(s16);
extern Gfx *func_1510CDB8(Gfx *, s32, s32, s32);
extern Gfx *func_151733D8(Gfx *, s32);
extern Gfx *func_150C8600(Gfx *);
extern Gfx *func_15100464(Gfx *);
extern Gfx *func_150DFBD0(Gfx *);
extern Gfx *func_150CF5E8(Gfx *);
extern Gfx *func_150D765C(Gfx *);
extern void func_1510F800(s32);
extern Gfx *func_1515D914(Gfx *, s32, s32, s32, s32, s32, s32, s32,
                         u8 *, u8 *, s32, s32, s32, u8 *);
extern Gfx *func_150A5378(Gfx *, Gfx *, u8 *, s32, s32, u32);
extern Gfx *func_1512E5F0(Gfx *, u8 *);
extern Gfx *func_1515E544(Gfx *, s32, s32, s32, u8 *);
extern Gfx *func_151742EC(Gfx *, s16);

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

Gfx *func_1510B9D0(Gfx *arg0, s16 arg1) {
    s32 offset = arg1 * 0x9A0;
    u8 *actor = D_800DBFF0 + offset;
    u8 mode = D_800C35EA;
    s32 suppressed;
    u32 slotMask;
    u8 *light;
    s32 *value;

    D_800BEBA0 = 1;
    suppressed = mode == 1 && D_800C3662 != 0;
    slotMask = 1U << ((u32) arg1 & 31);
    if (D_800D18A0 & slotMask) {
        suppressed = 1;
    }
    arg0 = func_1510B7B4(arg0, arg1);
    gSPLookAtX(arg0++, D_800D9B90 + D_800BE9C0 * 0x20);
    gSPLight(arg0++, D_800D9B90 + D_800BE9C0 * 0x20 + 0x10, 1);
    func_1510CB10(arg1);
    arg0 = func_1510CDB8(arg0, 255, 255, arg1);
    arg0 = func_151733D8(arg0, 1);
    gSPMatrix(arg0++, D_80089470, G_MTX_MODELVIEW | G_MTX_LOAD | G_MTX_NOPUSH);
    if (!suppressed) {
        if (D_800BE9F0 == 0x14) {
            arg0 = func_150C8600(arg0);
        } else if (D_800BE9F0 == 0x1A) {
            arg0 = func_15100464(arg0);
        } else if (D_800BE9F0 == 0x13) {
            arg0 = func_150DFBD0(arg0);
        } else if (D_800BE9F0 == 0x35) {
            arg0 = func_150CF5E8(arg0);
        } else if (D_800BE9F0 == 0x33) {
            arg0 = func_150D765C(arg0);
        }
    }
    func_1510F800(0);
    if (D_800DCD7C == 0) {
        gDma2p(arg0++, G_MOVEMEM, D_800D9BD0 + arg1 * 0x10 + D_800BE9C0 * 8,
               48, G_MV_LIGHT, 96);
    }
    light = D_800D9BD0 + arg1 * 0x10;
    value = D_800D9E10 + arg1;
    {
        u8 *current = D_800DBFF0 + offset;
        arg0 = func_1515D914(arg0, arg1, (s32) *(f32 *) (current + 0x2F8),
                            (s32) *(f32 *) (current + 0x2FC),
                            (s32) *(f32 *) (current + 0x300), 0, *value,
                            D_800D9E20, light + D_800BE9C0 * 8, &D_800D9E21,
                            1, 0, 0x25, D_800D9E28);
    }
    if (!suppressed) {
        if (D_800BE9F0 != 5) {
            if (D_800BEAAA != 0) {
                gDPPipeSync(arg0++);
                if (D_800DBE62 != 0) {
                    if (D_800BE9F0 != 0x14 && D_800BE9F0 != 0x33 && D_800BE9F0 != 0x32) {
                        arg0 = func_150A5378(D_800B0E00, arg0, D_800D9C10 + arg1 * 0x40,
                                            0, 0, slotMask);
                    } else {
                        gSPDisplayList(arg0++, D_800B0E00);
                    }
                    if (D_800B0E04 != 0) {
                        gDPPipeSync(arg0++);
                        arg0 = func_1510CDB8(arg0, 255, 255, arg1);
                        arg0 = func_151733D8(arg0, 1);
                        if (D_800BE9F0 == 0x35) {
                            arg0 = func_150CF5E8(arg0);
                        }
                        gSPDisplayList(arg0++, D_800B0E04);
                    }
                    D_800BEBA0 = 0;
                    if (actor[0x8B8] != 0 && (*(u32 *) (actor + 0x84) & 8)) {
                        arg0 = func_1512E5F0(arg0, actor);
                        gDPPipeSync(arg0++);
                    }
                } else {
                    gSPDisplayList(arg0++, D_800B0E00);
                }
            } else {
                gSPDisplayList(arg0++, D_800B0E00);
            }
        }
        arg0 = func_1515E544(arg0, *value, D_800D9E20, D_800D9E21,
                            light + D_800BE9C0 * 8);
        if (D_800B0E08 != 0) {
            gDPPipeSync(arg0++);
            arg0 = func_1510CDB8(arg0, 255, 255, arg1);
            gSPDisplayList(arg0++, D_800B0E08);
        }
    }
    arg0 = func_151742EC(arg0, arg1);
    gDPPipeSync(arg0++);
    return arg0;
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
