#include <ultra64.h>
extern s8 D_8008FD90;
extern s8 D_8008FD8C;
extern s8 D_800E0BEB;
extern s8 D_800E0C00[];
extern u8 D_800BE616;
extern u8 D_8008FE28;
extern u8 D_800E0B98;
extern u8 D_800E0B97;
extern s32 D_800E0A90;
extern u8 D_800E0B96;
extern u8 D_8008FD74;
extern s8 D_8008FE30;
extern u8 D_8008FD80;
extern u8 D_8008FD84;
extern s32 D_800E0BA8[];
extern s32 D_800E0BA0[];
extern u8 D_80084060[];

/* Non-matching placeholders for the text-only asm slice asm/20AE20.s. */

s32 func_151E43DC();
s32 func_151E530C();
s32 func_151DE85C();

extern s16 D_800E0B9A;
extern u8 D_800E0B94;

extern s8 D_8008FDC8;
extern s32 D_8008FDD8;
extern u8 D_800E0A8C;
extern u8 D_800E0B94;
extern u8 D_800E0BD3;
extern s32 D_800E0BD4;

s32 func_151DD970() {
    return 0;
}

s32 func_151DD9E4() {
    return 0;
}

s32 func_151DDB94(s32 arg0) {
    return ~arg0;
}

s32 func_151DDBA0() {
    return 0;
}

s32 func_151DDC20() {
    return 0;
}

s32 func_151DE6D4() {
    return 0;
}

void func_151DE7D4(void) {
    D_800E0A90 = 0;
    D_800E0B97 = 0;
    D_800E0B98 = 0;
    D_800E0A8C = 0;
    D_8008FE28 = 2;
    func_151DE85C();
}

void func_151DE81C(void) {
    D_8008FD74 = 4;
    D_800E0B96 = 0;
    if (D_8008FE30 == 0) {
        func_1500764C();
    }
}

s32 func_151DE85C() {
    return 0;
}

void func_151DE8E8() {
}

s32 func_151DE8F0() {
    return 0;
}

s32 func_151DF1BC() {
    return 0;
}

s32 func_151DF574() {
    return 0;
}

s32 func_151DFF38() {
    return 0;
}

s32 func_151E0424() {
    return 0;
}

s32 func_151E09DC() {
    return 0;
}

s32 func_151E0B70() {
    return 0;
}

s32 func_151E1214() {
    return 0;
}

s32 func_151E1744() {
    return 0;
}

void func_151E2284(void) {
    D_8008FD80 = 3;
    func_151E530C();
    func_151E43DC();
    D_8008FD80 = 0;
}

s32 func_151E22BC() {
    return 0;
}

s32 func_151E2404() {
    return 0;
}

s32 func_151E24F0() {
    return 0;
}

s32 func_151E2834() {
    return 0;
}

s32 func_151E30C4() {
    return 0;
}

s32 func_151E327C() {
    return 0;
}

s32 func_151E3344() {
    return 0;
}

s32 func_151E4264() {
    return 0;
}

s32 func_151E4314() {
    return 0;
}

s32 func_151E43DC() {
    return 0;
}

s32 func_151E4BD8() {
    return 0;
}

void func_151E4DC4() {
    D_800E0B94 = 10;
}

void func_151E4DD8() {
    if (D_800E0B9A & 0x8020) {
        D_800E0B94 = 4;
    }
}

s32 func_151E4E00() {
    return 0;
}

s32 func_151E4E64() {
    return 0;
}

s32 func_151E4EE8() {
    return 0;
}

s32 func_151E5034() {
    return 0;
}

s32 func_151E50C8() {
    return 0;
}

s32 func_151E51EC() {
    return 0;
}

s32 func_151E530C() {
    return 0;
}

s32 func_151E53E8() {
    return 0;
}

void func_151E557C(void) {
    D_80084060[0] = 0;
    D_80084060[1] = 1;
    D_80084060[2] = 2;
    D_80084060[3] = 3;
}

s32 func_151E55A8() {
    return 0;
}

void func_151E562C(void) {
    if (D_800E0A8C != 0) {
        D_800E0A8C = 0;
    }
}

s32 func_151E564C() {
    return D_8008FDC8;
}

s32 func_151E565C() {
    return 0;
}

s32 func_151E5F64(s32 arg0) {
    s8 temp_v1;

    if (D_800BE616 == 0) {
        if (D_800E0B94 == 0) {
            return arg0;
        }
    }
    temp_v1 = D_800E0C00[arg0];
    if (temp_v1 < 0) {
        temp_v1 = 0;
    }
    return temp_v1;
}

s32 func_151E5FAC(void) {
    if (D_800E0BEB != 0) {
        s8 temp_v1 = D_8008FD8C;

        if (temp_v1 < 5) {
            return temp_v1;
        }
    }
    return D_8008FD90;
}

s32 func_151E5FF4() {
    return 0;
}

s32 func_151E6964() {
    return 0;
}

void func_151E6BFC(void) {
    D_800E0BD3 = 0;
    D_800E0BD4 = 0;
    D_8008FDD8 = 0;
}

s32 func_151E6C1C() {
    return 0;
}

s32 func_151E7DC0() {
    return 0;
}

s32 func_151E7E9C() {
    return 0;
}

s32 func_151E7EF8() {
    return 0;
}

s32 func_151E7F60() {
    return 0;
}

/* Retail pairs lui- stores across TU-local data symbols; not
   reproducible with extern declarations, so keep a placeholder. */
s32 func_151E81EC() {
    return 0;
}

s32 func_151E8214() {
    return 0;
}

s32 func_151E82B8() {
    return 0;
}

s32 func_151E83E8() {
    return 0;
}
