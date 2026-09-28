#include <ultra64.h>
#include "variables.h"
extern s16 D_8008FDCC;
extern u8 D_800E0B94;
extern u8 D_800BE616;
extern u8 D_800BE740;
extern s8 D_8008FD90;
extern s8 D_800E0BD3;
extern u8 **D_800E0BD8;
extern s32 (*D_8008FFF4[])(s32);
extern Gfx *(*D_8008FFC0[])(Gfx *);
extern s32 D_80090058;
extern s16 D_800E0C78;
extern s32 D_800BEBA4;
extern Gfx *D_800BE9C8[];
extern f32 D_8008FE1C;
extern f32 D_8008FE20;
s32 func_151ED1E0(void);

/* Non-matching placeholders for the text-only asm slice asm/215960.s. */

s32 func_151E84B0(void) {
    /* Retain retail's local-slot gap under IDO's debug layout. */
    s32 stack_pad;
    s32 result;
    s32 index = 0;
    s32 (*callback)(s32);

    D_8003C8E0 = 0x09000001;
    result = func_151ED1E0();
    callback = D_8008FFF4[D_800E0B94];
    if (callback != NULL) {
        result = callback(result);
    }

    if (D_80000300 != 0) {
        if ((D_800BE616 != 0) && (D_8008FD90 >= 2)) {
            if ((D_800BE740 & 0xF) == 0) {
                if (D_800E0BD3 == 1) {
                    index = 0x33;
                } else if (D_800E0BD3 == 2) {
                    index = 0x16;
                }
            }
        } else if ((D_800BE740 & 1) == 0) {
            if (D_800E0BD3 == 1) {
                index = 0x32;
            } else if (D_800E0BD3 == 2) {
                index = 0x15;
            }
        }
    }

    if (index != 0) {
        func_1504332C(0xFF, 0xFF, 0xFF, 0xFF);
        func_15042D94(0x94, 0xC8, 0x81, D_800E0BD8[index]);
    }

    D_8003C8E0 = 0;
    return result;
}

Gfx *func_151E8620(Gfx *value) {
    s32 mode;
    Gfx *original;
    Gfx *(*callback)(Gfx *);
    s32 overflow;

    mode = D_800E0B94;
    callback = D_8008FFC0[mode];
    original = value;
    D_8003C8E0 = 0x09000000;
    if (callback != NULL) {
        value = callback(value);
        mode = D_800E0B94;
    }

    if (mode != 0) {
        D_80090058 = 0;
        D_800E0C78 = 0;
    }

    D_8003C8E0 = 0;
    if (D_800BEBA4 < (value - D_800BE9C8[D_800BE9C0])) {
        overflow = 1;
    } else {
        overflow = 0;
    }
    if (overflow != 0) {
        return original;
    }
    return value;
}

Gfx *func_151E86E4(Gfx *display_list, s32 ulx, s32 uly, s32 lrx, s32 lry,
                   s32 tile, s32 s, s32 t, s32 dsdx, s32 dtdy) {
    if (D_8008FE1C != 1.0f) {
        ulx = (s32) ((f32) ulx * D_8008FE1C);
        lrx = (s32) ((f32) lrx * D_8008FE1C);
        uly = (s32) ((f32) uly * D_8008FE20);
        lry = (s32) ((f32) lry * D_8008FE20);
        dsdx = (s32) ((f32) dsdx / D_8008FE1C);
        dtdy = (s32) ((f32) dtdy / D_8008FE20);
    }

    gSPScisTextureRectangle(display_list++, ulx, uly, lrx, lry, tile,
                            s, t, dsdx, dtdy);
    return display_list;
}

s32 func_151E89A0() {
    return 0;
}

s32 func_151E966C() {
    return 0;
}

s32 func_151E9D18() {
    return 0;
}

s32 func_151EA15C() {
    return 0;
}

s32 func_151EADFC() {
    return 0;
}

s32 func_151EB06C() {
    return 0;
}

u8 *func_151EB930(u8 *arg0) {
    s16 temp = D_8008FDCC;

    if (temp != 0) {
        arg0 = (u8 *) func_151EA15C(arg0, 0x6A, temp, 0);
    }
    return arg0;
}

s32 func_151EB96C() {
    return 0;
}

s32 func_151EBB50() {
    return 0;
}

s32 func_151EC178() {
    return 0;
}

s32 func_151EC1F0() {
    return 0;
}

s32 func_151EC3E8() {
    return 0;
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_215960/func_151EC648.s")

s32 func_151ED09C() {
    return 0;
}

s32 func_151ED1E0() {
    return 0;
}

s32 func_151ED29C() {
    return 0;
}

s32 func_151ED430() {
    return 0;
}

s32 func_151ED90C() {
    return 0;
}

s32 func_151EDB58() {
    return 0;
}

s32 func_151EDBDC() {
    return 0;
}

s32 func_151EDF4C() {
    return 0;
}

s32 func_151EE184() {
    return 0;
}

s32 func_151EEBE8() {
    return 0;
}

void func_151EEFF0(void) {
    D_800E9D00 = 0;
}
