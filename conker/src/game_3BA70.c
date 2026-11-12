#include <ultra64.h>

#include "functions.h"
#include "variables.h"

/* Generated placeholder declarations. */
void func_1500E5C0(void);
s32 func_1500E738();
s32 func_1500E8C0();
/* End generated placeholder declarations. */

void func_15012470(void);
extern void *D_800D9894;
extern void *D_800D98D0[4];
extern u8 *D_80088870;

/* Reset the game session counters, records, and related state.
 * Keep the compact store layout: IDO scheduling depends on this source shape.
 */
void func_1500E5C0(void) {
    s32 i;
    func_15012470();
    func_15008A10();
    func_15012770();
    for (i = 0; i < 20; i += 4) { D_800E0950[i+1] = 0; D_800E0950[i+2] = 0; D_800E0950[i+3] = 0; D_800E0950[i] = 0; }
    D_800D9921 = 0;
    D_800D9920 = 0;
    D_800D9928 = 0;
    D_800D9938 = 0;
    D_800D9929 = 0;
    D_800D9939 = 0;
    { u8 *p = D_800D992A; u8 *q = D_800D993A; do { p[1]=0; q[1]=0; p[2]=0; q[2]=0; p[3]=0; q[3]=0; p[0]=0; q[0]=0; p+=4; q+=4; } while (p != D_800D992A + 12); }
    D_800D9890 = 0;
    D_800D9894 = NULL;
    D_800D98D0[3] = NULL; D_800D98D0[2] = NULL; D_800D98D0[1] = NULL; D_800D98D0[0] = NULL;
    D_80088870 = NULL;
    bzero(D_800BE500, 5);
    D_800D9950[2] = 0;
    D_800D9950[1] = 0;
    D_800D9950[0] = 0;
    D_80088980 = 0;
    D_800D9AA0[0] = NULL;
    D_800D9AA0[1] = NULL;
    D_800D9AA0[2] = NULL;
    D_800BE4F0 = NULL;
    D_80088B40 = 0;
}

void func_1500E70C(s32 arg0) {
    if (arg0 == 0x2B) {
        func_15011C70();
    }
}

/* Non-matching C placeholders for asm/nonmatchings/game_3BA70/func_1500E738.s. */
s32 func_1500E738() {
    return 0;
}

void func_1500E890(void) {
    func_15008E00();
    func_15008E10(0);
    func_15008E10(1);
}

/* Non-matching C placeholders for asm/nonmatchings/game_3BA70/func_1500E8C0.s. */
s32 func_1500E8C0() {
    return 0;
}
// NON-MATCHING: fair bit to figure out
// void func_1500E8C0(void) {
//     struct145 tmp;
//     s32 phi_v0;
//
//     func_15195AA8(D_800B0E00[0], D_800902E8, 0, -1, 0, 0, 0, -6);
//     func_15195AA8(D_800B0E00[1], D_800902E8, 0, -1, 0, 1, 0, -6);
//     tmp.unk28 = D_80096210; // 0.2142857164144516
//     tmp.unk30 = 5.0f;
//     tmp.unk34 = 6.0f;
//     tmp.unk20 = 8.0f;
//     tmp.unk24 = 7.0f;
//     tmp.unk14 = 0.0f;
//     tmp.unk18 = 0.0f;
//     tmp.unk2C = 0.0f;
//     tmp.unk48 = 3;
//     tmp.unk4C = 2;
//     tmp.unk0 = 0x34;
//     tmp.unk2 = 0x12;
//     tmp.unk4 = -0x28;
//     tmp.unk6 = 0xF;
//     tmp.unk38 = 0x9B;
//     tmp.unk3A = 0x64;
//     tmp.unk44 = 0x29;
//     tmp.unk46 = 0x29;
//     tmp.unk10 = 400.0f;
//     tmp.unk1C = 900.0f - 400.0f;
//     tmp.unk3C = D_80096214; // 0.6000000238418579
//     tmp.unk40 = D_80096218;
//     tmp.unkC = D_8009621C;
//     tmp.unk8 = 800.0f;
//     func_15189900(&tmp, 1);
//     if (D_800BE9F0 == 6) {
//         phi_v0 = 52;
//     } else {
//         phi_v0 = 7;
//     }
//     func_1000FA64(1567, (s16)phi_v0, 0, 0, 12000, 1000, 400, func_1000EF40, 0, 0, 72, 0);
// }

void func_1500EAA0(void) {
    func_15195AA8(D_800B0E00[0], D_80090320, 0, -1, 0, 0, 0, -8);
    func_15195AA8(D_800B0E00[1], D_80090320, 0, -1, 0, 1, 0, -8);
}
