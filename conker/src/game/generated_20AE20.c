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
extern s32 D_800E0AF0;
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

extern u8 D_800D2E40;
extern u8 D_8008FDA4;
extern u8 D_800BEAC1;
extern s16 D_8008FDCC;
extern s32 D_800BE9E4;
extern s32 D_800E0A88;
extern s8 D_800E0BE9;
extern s8 *D_8008FDD4;
extern s8 D_8008FE54[23];
s8 D_800E0BE0[23];
extern u8 D_800AB570[];
extern u8 D_800E0B95;

void func_151E557C(void);
void func_151E6BFC(void);
s32 func_151E55A8();

void func_151DD970(void) {
    s32 i;

    for (i = 0; i < 23; i++) {
        D_800E0BE0[i] = D_8008FE54[i];
    }
}

s32 func_151DD9E4() {
    return 0;
}

s32 func_151DDB94(s32 arg0) {
    return ~arg0;
}

void func_151DDBA0(void) {
    D_800D2E40 = 0;
    func_1501C730(6, 0x1D, 0, 0, 1);
    D_800E0B94 = 3;
    D_8008FDA4 = 0;
    D_800BEAC1 = 0;
    func_151E557C();
    func_1000F1A8();
    func_1000E934();
    D_8008FD8C = 1;
    D_8008FD90 = 1;
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

void func_151E4E00(void) {
    D_8008FDCC = 0;
    func_151E557C();
    D_800E0B94 = 3;
    D_8008FDA4 = 0;
    D_8008FD80 = 0;
    D_800D2E40 = 0;
    func_1501C730(6, 0x1D, 0, 0, 1);
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

void func_151E50C8(void) {
    s32 i;

    for (i = 0; i < 23; i++) { D_800E0BE0[i] = D_8008FE54[i]; }

    D_800E0A90 = 0;
    func_151E6BFC();

    if (D_8008FDD4 == NULL) {
        D_8008FDD4 = (s8 *)&D_800E0AF0;
        func_151E5034();

        if ((D_8008FDD4[0x3E] == 1) ^ 0) {
            D_8008FDD4[0x2C] = D_800AB570[D_8008FDD4[0x2C]];
        }
    }

    func_15017790();
    D_800E0B94 = 11;
    D_800D2E40 = 0;
    func_1501C730(6, 0x25, 0, 0, 1);
    D_800E0B95 = D_800E0B94;
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

void func_151E7E9C(void) {
    s8 var;

    var = D_800E0BE9;
    if (var == 2) {
        func_10017870(1);
        return;
    }
    if (var == 0) {
        func_10017870(2);
        return;
    }
    func_10017870(4);
}

void func_151E7EF8(void) {
    s32 *iter;
    s32 sum;

    func_151E7E9C();
    sum = 0;
    for (iter = (s32 *)&func_151DDC20; iter < (s32 *)&func_151DE7D4; iter++) {
        sum += *iter;
    }
    if (sum != 0xBFC924E3) {
        *(s32 *)&osSpTaskLoad = 0;
    }
}

s32 func_151E7F60() {
    return 0;
}

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
