#include <ultra64.h>

#include "functions.h"
#include "variables.h"

/* Generated placeholder declarations. */
s32 func_15141A7C();
s32 func_15141C0C();
s32 func_15141CC0();
s32 func_15141E38(s32 arg0, s32 arg1);
s32 func_15141F78();
s32 func_15142180();
s32 func_151424F4();
s32 func_15142600();
s32 func_15142838();
s32 func_15142E24();
s32 func_1514306C();
s32 func_15143134();
s32 func_151432BC();
s32 func_151438D8();
s32 func_15143E94();
s32 func_1514401C();
s32 func_151441A4();
s32 func_151442FC();
s32 func_1514470C();
s32 func_15144CEC();
s32 func_15144E80();
s32 func_151451F0();
s32 func_151452C4();
s32 func_15145740();
s32 func_15145AD8();
s32 func_15145EA4();
s32 func_15146078();
s32 func_151462C8();
s32 func_1514654C();
/* End generated placeholder declarations. */

extern u8 D_800C3E90;
extern s16 D_800DD1C8;
extern s16 D_800DD1CA;
extern s16 D_800DD1CC;
extern s16 D_800DD1CE;
extern s16 D_800DD204;
extern s16 D_800DD206;
extern s16 D_800DD1C0;
extern s16 D_800DD1C2;
extern s16 D_800DD1C4;
extern s16 D_800DD1C6;
extern u32 D_800DD1FC;
extern u32 D_800DD200;
extern s32 D_800A5200[6];

s32 func_150A2AEC(s32 arg0, s32 arg1, s32 *arg2);
s32 func_1514563C(struct17 *arg0, struct17 *arg1, struct17 *arg2, struct17 *arg3, f32 *arg4);
void func_150A7960(f32 mtx[4][4], f32 arg1, f32 arg2, f32 arg3, f32 *arg4, f32 *arg5, f32 *arg6);


void func_15141970(struct37 *arg0) {
    func_1514EDF0(arg0, arg0->unk2C);
}

void func_15141990(void *arg0) {
    func_15141970(arg0);
}

void func_151419B0(void *arg0) {
    func_15141970(arg0);
}

void func_151419D0(u8 *arg0, u8 *arg1, u8 arg2) {
    u8 *dst = arg0 + 0x28;
    s32 current;

    if (arg2 == 0) {
        if ((*(s32 *)arg1 == *(s32 *)(dst + 4)) || (arg1[4] == dst[8])) {
            func_1516972C(arg0);
        }
    } else if (arg2 == 0x2D) {
        current = *(s32 *)(dst + 4);
        if (*(s32 *)arg1 == current) {
            *(s32 *)(dst + 4) = *(s32 *)(arg1 + 4);
            dst[8] = arg1[9];
        } else if (*(s32 *)(arg1 + 4) == current) {
            *(s32 *)(dst + 4) = *(s32 *)arg1;
            dst[8] = arg1[8];
        }
    }
}
/* Non-matching C placeholders for asm/nonmatchings/game_16EE20/func_15141A7C.s. */
s32 func_15141A7C() {
    return 0;
}
// requires jump table
/* Non-matching C placeholders for asm/nonmatchings/game_16EE20/func_15141C0C.s. */
s32 func_15141C0C() {
    return 0;
}
/* Non-matching C placeholders for asm/nonmatchings/game_16EE20/func_15141CC0.s. */
s32 func_15141CC0() {
    return 0;
}
void func_15141DA4(void *arg0, s32 arg1, s32 arg2) {
    if ((arg1 < 12) && (arg1 >= 0) &&
        (arg2 < 20) && (arg2 >= 0) &&
        (D_800BE616 == 0) &&
        (D_8008A084[arg1] != 0) && (arg2 != -1)) {
        if ((D_8008A0B4[arg2].unk0 != 0) && (D_8008A0B4[arg2].unk4 > 0)) {
            func_15141E38(arg0, arg2);
        }
    }
}
/* Non-matching C placeholders for asm/nonmatchings/game_16EE20/func_15141E38.s. */
s32 func_15141E38(s32 arg0, s32 arg1) {
    return 0;
}
/* Non-matching C placeholders for asm/nonmatchings/game_16EE20/func_15141F78.s. */
s32 func_15141F78() {
    return 0;
}
// NON-MATCHING: need to determine arguments
// void func_1513C650(s32, s32, s32, u16, s32, s32, s32, f32, f32, s32, s32, s32, s32, s32, u8, s32);
// s32 func_1513C650(s32 arg0, u8 arg1, u8 arg2, s32 arg3, f32 arg4, f32 arg5, f32 arg6, f32 arg7, f32 arg8, u8 arg9, u8 argA, s32 argB, s32 argC, s32 argD, u8 argE, s32 argF);
// void func_15141F78(u8 arg0, struct157 *arg1, f32 arg2, s32 arg3, struct157 *arg4, u8 arg5) {
//     struct157 tmp;
//     f32 temp_f2;
//     s32 phi_v0;
//
//     tmp.unk6 = arg0;
//     tmp.unk7 = 0;
//     tmp.unk0 = 0x6F701;
//     tmp.unk4 = (func_150ADA20() % 61U) + 100;
//     tmp.unk8 = 0;
//     tmp.unkC = 0;
//     tmp.unk10 = (func_150ADA20() & 0x7F) + 128;
//     tmp.unk11 = 0xFF;
//     tmp.unk12 = 0xFF;
//     tmp.unk13 = 0xFF;
//     tmp.unk14 = 0xFF;
//     tmp.unk15 = 0xFF;
//     tmp.unk18 = 0x3B0002;
//     tmp.unk16 = 0;
//     tmp.unk17 = 7;
//     tmp.unk20 = 0xFF;
//     tmp.unk1C = arg1->unk18;
//     tmp.unk22 = 0x28;
//     tmp.unk24 = 6;
//     temp_f2 = ((func_150ADA68() * 5.0f) + 10.0f) * arg2;
//     // --- matching to here ---
//     if (arg5 == 2) {
//         phi_v0 = 1;
//     } else {
//         phi_v0 = 0;
//     }
//     func_1513C650(&tmp, 0, 0, arg1->unk4, arg4->unk0, arg1->unk0, arg4->unk8, temp_f2, temp_f2, arg3, phi_v0, 3, 1, 0, 0xFF, 1);
// }

s32 func_151420F8(struct127 *arg0) {
    s32 tmp[6];

    tmp[0] = D_800A5200[0];
    tmp[1] = D_800A5200[1];
    tmp[2] = D_800A5200[2];
    tmp[3] = D_800A5200[3];
    tmp[4] = D_800A5200[4];
    tmp[5] = D_800A5200[5];

    return func_150A2AEC(((s32)arg0 - (s32)D_800CC2D0) / sizeof(struct127), 6, tmp) != -1;
}
/* Non-matching C placeholders for asm/nonmatchings/game_16EE20/func_15142180.s. */
s32 func_15142180() {
    return 0;
}
s32 func_151422C0(s32 arg0, s32 arg1, s32 arg2, s32 arg3) {
    return (arg3 + arg2) >> 1;
}

s32 func_151422DC(s32 arg0, s32 arg1, s32 arg2, s32 arg3, s32 arg4, s32 arg5, s32 arg6) {
    return arg4;
}

s32 func_151422F8(s32 arg0, s32 arg1, s32 arg2, s32 arg3, s32 arg4) {
    return arg4;
}

void func_15142314(u8 *arg0, s32 arg1, f32 *arg2) {
    u8 *ptr = arg0 + (arg1 << 6);
    f32 scale = 1.0f / 65536.0f;

    if (D_800C3E90 != 0) {
        arg2[0] = (f32)(((*(s16 *)(ptr + 0x18)) << 16) + *(s16 *)(ptr + 0x38)) * scale;
        arg2[1] = (f32)(((*(s16 *)(ptr + 0x1A)) << 16) + *(s16 *)(ptr + 0x3A)) * scale;
        arg2[2] = (f32)(((*(s16 *)(ptr + 0x1C)) << 16) + *(s16 *)(ptr + 0x3C)) * scale;
    } else {
        arg2[0] = *(f32 *)(ptr + 0x30);
        arg2[1] = *(f32 *)(ptr + 0x34);
        arg2[2] = *(f32 *)(ptr + 0x38);
    }
}
f32 func_151423D8(u8 arg0) {
    s32 idx;
    s32 quadrant;

    if (arg0 & 0x40) {
        idx = 0x40 - (arg0 & 0x3F);
    } else {
        idx = arg0 & 0x3F;
    }

    quadrant = arg0 & 0xC0;
    if ((quadrant == 0) || (quadrant == 0xC0)) {
        return D_8009A220[idx];
    }
    return -D_8009A220[idx];
}
void *func_15142444(u8 arg0, u8 *arg1) {
    u8 *found;

    if (arg0 == 0xFF) {
        if (*(s32 *)(arg1 + 0x1D4) != 0) {
            return arg1;
        }
        return NULL;
    }

    if ((arg1 != NULL) && (*(s32 *)arg1 != 0) && (arg0 == arg1[0x3B])) {
        if (*(s32 *)(arg1 + 0x1D4) != 0) {
            return arg1;
        }
        return NULL;
    }

    found = (u8 *)func_15083E90(arg0);
    if (found == NULL) {
        return NULL;
    }
    if (*(s32 *)(found + 0x1D4) == 0) {
        return NULL;
    }
    return found;
}
/* Non-matching C placeholders for asm/nonmatchings/game_16EE20/func_151424F4.s. */
s32 func_151424F4() {
    return 0;
}
/* Non-matching C placeholders for asm/nonmatchings/game_16EE20/func_15142600.s. */
s32 func_15142600() {
    return 0;
}
/* Non-matching C placeholders for asm/nonmatchings/game_16EE20/func_15142838.s. */
s32 func_15142838() {
    return 0;
}
void func_15142914(f32 *arg0, f32 arg1, f32 arg2, f32 arg3, f32 arg4, f32 arg5, f32 arg6, f32 arg7, f32 arg8) {
    func_150A8050((f32 (*)[4])arg0, arg3, arg4, arg5);

    arg0[12] = arg6;
    arg0[13] = arg7;
    arg0[14] = arg8;

    arg0[0] *= arg1;
    arg0[1] *= arg1;
    arg0[2] *= arg1;
    arg0[4] *= arg2;
    arg0[5] *= arg2;
    arg0[6] *= arg2;
    arg0[8] *= arg1;
    arg0[9] *= arg1;
    arg0[10] *= arg1;
}

void func_151429E0(u8 arg0, u8 *arg1, u8 *arg2, u8 *arg3) {
    u8 *tmp = &D_8008A160[((func_150ADA20() & 3) * 3) + (arg0 * 12)];

    *arg1 = tmp[0];
    *arg2 = tmp[1];
    *arg3 = tmp[2];
}
// NON-MATCHING: ported from ects_proto (ECTS ROM build), not yet byte-verified for us
s32 func_15142A5C(s32 *arg0) {
    s32 *p = *(s32**)((u8*)arg0 + 0x2D0);
    s32 v0 = 0;
    if (*(s16*)((u8*)p + 0x3C) > 0) {
        return 1;
    }
    return v0;
}
f32 func_15142A80(f32 arg0) {
    return (1.0f - arg0) * (arg0 - 2.0f) * arg0 * D_800A5624;
}
f32 func_15142AC0(f32 arg0) {
    return (arg0 + 1.0f) * (arg0 - 1.0f) * (arg0 - 2.0f) * 0.5f;
}
f32 func_15142B04(f32 arg0) {
    return (2.0f - arg0) * (arg0 + 1.0f) * arg0 * 0.5f;
}
f32 func_15142B44(f32 arg0) {
    return (arg0 + 1.0f) * (arg0 - 1.0f) * arg0 * D_800A5628;
}
Gfx *func_15142B7C(Gfx *arg0, u32 arg1, u32 arg2) {
    if (((~D_800DD200) & arg2) != 0) {
        arg0->words.w0 = 0xD9000000 | ((~arg2) & 0xFFFFFF);
        arg0->words.w1 = 0;
        arg0++;
        D_800DD200 |= arg2;
    }

    if (((~D_800DD1FC) & arg1) != 0) {
        arg0->words.w0 = 0xD9FFFFFF;
        arg0->words.w1 = arg1;
        arg0++;
        D_800DD1FC |= arg1;
    }
    return arg0;
}

Gfx *func_15142C10(Gfx *arg0, s32 arg1, s32 arg2, s32 arg3, s32 arg4, u8 *arg5) {
    if ((arg1 == D_800DD1C8) && (arg2 == D_800DD1CA) && (arg3 == D_800DD1CC) && (arg4 == D_800DD1CE)) {
        return arg0;
    }

    if (*arg5 == 1) {
        gDPPipeSync(arg0++);
        *arg5 = 0;
    }

    arg0->words.w0 = 0xFB000000;
    arg0->words.w1 = ((arg1 & 0xFF) << 24) | ((arg2 & 0xFF) << 16) | ((arg3 & 0xFF) << 8) | (arg4 & 0xFF);
    arg0++;

    D_800DD1C8 = arg1;
    D_800DD1CA = arg2;
    D_800DD1CC = arg3;
    D_800DD1CE = arg4;
    return arg0;
}

Gfx *func_15142CF0(Gfx *arg0, s32 arg1, s32 arg2, s32 arg3, s32 arg4, s32 arg5, s32 arg6, u8 *arg7) {
    if ((arg1 == D_800DD204) && (arg2 == D_800DD206) && (arg3 == D_800DD1C0) &&
        (arg4 == D_800DD1C2) && (arg5 == D_800DD1C4) && (arg6 == D_800DD1C6)) {
        return arg0;
    }

    if (*arg7 == 1) {
        gDPPipeSync(arg0++);
        *arg7 = 0;
    }

    arg0->words.w0 = 0xFA000000 | ((arg1 & 0xFF) << 8) | (arg2 & 0xFF);
    arg0->words.w1 = ((arg3 & 0xFF) << 24) | ((arg4 & 0xFF) << 16) | ((arg5 & 0xFF) << 8) | (arg6 & 0xFF);
    arg0++;

    D_800DD204 = arg1;
    D_800DD206 = arg2;
    D_800DD1C0 = arg3;
    D_800DD1C2 = arg4;
    D_800DD1C4 = arg5;
    D_800DD1C6 = arg6;
    return arg0;
}
/* Non-matching C placeholders for asm/nonmatchings/game_16EE20/func_15142E24.s. */
s32 func_15142E24() {
    return 0;
}
Gfx *func_15142FBC(Gfx *arg0, u32 arg1, u32 arg2, u8 *arg3) {
    if ((arg1 == D_800DD218) && (arg2 == D_800DD21C)) {
        return arg0;
    }

    if (*arg3 == 1) {
        gDPPipeSync(arg0++);
        *arg3 = 0;
    }

    arg0->words.w0 = 0xEF000000 | ((arg1 | 0xF) & 0xFFFFFF);
    arg0->words.w1 = arg2;
    arg0++;
    D_800DD218 = arg1;
    D_800DD21C = arg2;
    return arg0;
}
s16 func_15143044(u8 arg0, s32 arg1) {
    return (s16)(0x7FFF - arg0);
}
/* Non-matching C placeholders for asm/nonmatchings/game_16EE20/func_1514306C.s. */
s32 func_1514306C() {
    return 0;
}
/* Non-matching C placeholders for asm/nonmatchings/game_16EE20/func_15143134.s. */
s32 func_15143134() {
    return 0;
}/* Non-matching C placeholders for asm/nonmatchings/game_16EE20/func_151432BC.s. */
s32 func_151432BC() {
    return 0;
}
// void func_151432BC(struct208 *arg0, f32 *arg1, f32 *arg2, f32 *arg3, f32 *arg4) {
//     struct209 tmp;
//     f32 temp_f2;
//     f32 temp_f6;
//     f32 temp_ret;
//     s32 temp_t6;
//     u8 temp_a0;
//
//     temp_t6 = (arg0->unk15) & 3;
//     if (temp_t6 == 0) {
//         tmp.unk1B = func_150ADA20();
//         tmp.unk14 = func_151423D8((tmp.unk1B - 64) & 0xFF);
//         tmp.unk10 = func_151423D8(tmp.unk1B);
//         temp_ret = func_150ADA68();
//         temp_f2 = temp_ret * arg0->unk6;
//         *arg1 = (arg0->unk0 + (temp_f2 * tmp.unk10));
//         *arg2 = (arg0->unk4 - (temp_f2 * tmp.unk14));
//         *arg3 = (arg0->unk2 + arg0->unk8);
//         *arg4 = arg0->unk2;
//     } else if (temp_t6 != 1) {
//         if (temp_t6 == 2) {
//             tmp.unk2F = (u32) (arg0->unk10 * D_800A5644); // 0.7111111283302307
//             tmp.unk28 = func_151423D8((tmp.unk2F - 64));
//             tmp.unk24 = func_151423D8(tmp.unk2F);
//             tmp.unk20 = (func_150ADA68() * (2.0f * (f32) arg0->unk6)) + (f32) -(s32) arg0->unk6;
//             temp_f2 = (func_150ADA68() * (2.0f * (f32) arg0->unkA)) + (f32) -(s32) arg0->unkA;
//             temp_f6 = temp_f2 * tmp.unk24;
//             *arg1 = (arg0->unk0 + ((tmp.unk20 * tmp.unk24) + (temp_f2 * tmp.unk28)));
//             *arg2 = (arg0->unk4 + (temp_f6 - (tmp.unk20 * tmp.unk28)));
//             *arg3 = (arg0->unk2 + arg0->unk8);
//             *arg4 = arg0->unk2;
//         } else {
//             *arg1 = arg0->unk0;
//             *arg2 = arg0->unk4;
//             *arg3 = (arg0->unk2 + arg0->unk8);
//             *arg4 = (arg0->unk2 - arg0->unk8);
//         }
//     } else {
//         tmp.unkB = func_150ADA20();
//         tmp.unk4 = func_151423D8((tmp.unkB - 64));
//         tmp.unk0 = func_151423D8(tmp.unkB);
//         temp_ret = func_150ADA68();
//         temp_f2 = temp_ret * (f32) arg0->unk6;
//         *arg1 = (arg0->unk0 + (temp_f2 * tmp.unk0));
//         *arg2 = (arg0->unk4 - (temp_f2 * tmp.unk4));
//         *arg3 = (arg0->unk2 + arg0->unk8);
//         *arg4 = (arg0->unk2 - arg0->unk8);
//     }
// }


void func_151436B4(f32 arg0, f32 arg1, f32 arg2, vertex *arg3) {
    f32 cos0 = cosf(arg0);
    f32 sin0 = sinf(arg0);
    f32 cos1 = cosf(arg1);
    f32 temp = arg2 * cos1;

    arg3->x = temp * sin0;
    arg3->y = -arg2 * sinf(arg1);
    arg3->z = temp * cos0;
}
void func_1514373C(f32 arg0, f32 arg1, f32 *arg2, f32 *arg3) {
    f32 tmp = cosf(arg0);
    f32 sin0 = sinf(arg0);

    *arg2 = arg1 * sin0;
    *arg3 = arg1 * tmp;
}
// NON-MATCHING: only differs from us by the jal target address of the still-unmatched
// func_151423D8 (called 4 times here) - this function's own code is verified
// byte-identical otherwise.
void func_15143794(s16 arg0, s16 arg1, f32 arg2, vertex *arg3) {
    f32 sinArg0 = func_151423D8((u8) arg0);
    f32 sinArg0m = func_151423D8((u8) (arg0 - 0x40));
    f32 sinArg1 = func_151423D8((u8) arg1);
    f32 sinArg1m = func_151423D8((u8) (arg1 - 0x40));
    f32 temp = arg2 * sinArg1;

    arg3->x = temp * sinArg0m;
    arg3->y = -arg2 * sinArg1m;
    arg3->z = temp * sinArg0;
}
// NON-MATCHING: only differs from us by the jal target address of func_15143794
// (verified byte-identical above except for its own dependency on func_151423D8) -
// this function's own code is verified byte-identical otherwise.
void func_15143834(s16 arg0, s16 arg1, f32 arg2, vertex *arg3) {
    func_15143794(arg0, arg1, arg2, arg3);
}
void func_15143874(u8 arg0, f32 arg1, f32 *arg2, f32 *arg3) {
    f32 tmp = func_151423D8(arg0);

    *arg2 = arg1 * func_151423D8((arg0 - 0x40) & 0xFF);
    *arg3 = arg1 * tmp;
}
/* Non-matching C placeholders for asm/nonmatchings/game_16EE20/func_151438D8.s. */
s32 func_151438D8() {
    return 0;
}
void func_15143D18(s32 *arg0, s32 *arg1, s32 arg2, s32 arg3) {
    s32 tmp;

    if (arg3 < arg2) {
        tmp = arg2;
        arg2 = arg3;
        arg3 = tmp;
    }

    if (*arg1 < *arg0) {
        tmp = *arg0;
        *arg0 = *arg1;
        *arg1 = tmp;
    }

    if (*arg0 < arg2) {
        *arg0 = arg2;
    }

    if (arg3 < *arg1) {
        *arg1 = arg3;
    }
}
s32 func_15143DA8(s32 *arg0, s32 arg1, s32 arg2) {
    s32 tmp;

    if (arg2 < arg1) {
        tmp = arg1;
        arg1 = arg2;
        arg2 = tmp;
    }

    if (*arg0 < arg1) {
        *arg0 = arg1;
        return 1;
    }

    if (arg2 < *arg0) {
        *arg0 = arg2;
        return 2;
    }

    return 0;
}

s32 func_15143E08(struct127 *arg0) {
    return (((s32) arg0->unk7A >> 8) + 64) & 0xFF;
}

s16 func_15143E24(struct127 *arg0) {
    struct126 *temp = arg0->unk31C;

    if (temp != NULL) {
        return (arg0->unk7A - temp->unk12) >> 8;
    }
    return arg0->unk7A >> 8;
}
f32 func_15143E64(f32 *arg0) {
    f32 x = arg0[0];
    f32 y = arg0[1];
    f32 z = arg0[2];
    return sqrtf(x * x + y * y + z * z);
}
/* Non-matching C placeholders for asm/nonmatchings/game_16EE20/func_15143E94.s. */
s32 func_15143E94() {
    return 0;
}
/* Non-matching C placeholders for asm/nonmatchings/game_16EE20/func_1514401C.s. */
s32 func_1514401C() {
    return 0;
}
/* Non-matching C placeholders for asm/nonmatchings/game_16EE20/func_151441A4.s. */
s32 func_151441A4() {
    return 0;
}
/* Non-matching C placeholders for asm/nonmatchings/game_16EE20/func_151442FC.s. */
s32 func_151442FC() {
    return 0;
}
u32 func_151444DC(s32 arg0, s32 arg1, s32 arg2) {
    s32 step;

    if (arg1 < arg0) {
        step = arg1 - arg2 + 1;
        arg0 -= step;
        while (arg1 < arg0) {
            arg0 -= step;
        }
    }

    if (arg0 < arg2) {
        step = arg1 - arg2 + 1;
        arg0 += step;
        while (arg0 < arg2) {
            arg0 += step;
        }
    }

    return arg0;
}
f32 func_15144528(f32 arg0, f32 arg1, f32 arg2) {
    f32 step = arg1 - arg2;

    while (arg1 < arg0) {
        arg0 -= step;
    }

    while (arg0 < arg2) {
        arg0 += step;
    }

    return arg0;
}
f32 func_15144598(struct134 *arg0) {
    f32 ret;

    switch (arg0->unk16 & 3) {
        case 0:
        case 1:
            ret = arg0->unk6 * arg0->unk6 * D_800A5694;
            break;
        case 2:
            ret = arg0->unk6 * arg0->unkA * 4.0f;
            break;
        default:
            ret = 1.0f;
            break;
    }

    return ret;
}
/* Non-matching C placeholders for asm/nonmatchings/game_16EE20/func_1514462C.s. */
f32 func_1514462C(s32 arg0) {
    return 0.0f;
}
/* Non-matching C placeholders for asm/nonmatchings/game_16EE20/func_1514470C.s. */
s32 func_1514470C() {
    return 0;
}
f32 func_15144A74(f32 *arg0, f32 *arg1) {
    return arg0[0] * arg1[0] + arg0[1] * arg1[1] + arg1[2] * arg0[2];
}
f32 func_15144AA8(s32 arg0) {
    f32 ret = D_800DBFF0[arg0].unk380;

    while (ret > 360.0f) {
        ret -= 360.0f;
    }

    while (ret < 0.0f) {
        ret += 360.0f;
    }

    return ret;
}
f32 *func_15144B34(s32 arg0) {
    return &D_800DBFF0[arg0].unk2F8;
}
f32 func_15144B68(f32 arg0) {
    while (D_800A56A4 < arg0) {
        arg0 -= D_800A56A4;
    }

    while (arg0 < 0.0f) {
        arg0 += D_800A56A4;
    }

    return arg0;
}

f32 func_15144BC8(f32 arg0) {
    while (360.0f < arg0) {
        arg0 -= 360.0f;
    }

    while (arg0 < 0.0f) {
        arg0 += 360.0f;
    }

    return arg0;
}

s32 func_15144C2C(s16 arg0) {
    s16 tmp1 = arg0;

    while (tmp1 >= 256)
    {
        tmp1 -= 255;
    }
    while (tmp1 < 0)
    {
        tmp1 += 255;
    }

    return tmp1;
}

f32 func_15144C8C(f32 arg0, f32 arg1) {
    f32 tmp;

    arg0 = func_15144B68(arg0);
    tmp = fabsf(arg0 - func_15144B68(arg1));
    if (D_800A56A8 < tmp) {
        tmp = D_800A56AC - tmp;
    }
    return tmp;
}
/* Non-matching C placeholders for asm/nonmatchings/game_16EE20/func_15144CEC.s. */
s32 func_15144CEC() {
    return 0;
}
/* Non-matching C placeholders for asm/nonmatchings/game_16EE20/func_15144E80.s. */
s32 func_15144E80() {
    return 0;
}
void func_151450B4(struct17 *arg0, struct17 *arg1, struct17 *arg2) {
    arg2->unk0 = arg0->unk4 * arg1->unk8 - arg0->unk8 * arg1->unk4;
    arg2->unk4 = arg0->unk8 * arg1->unk0 - arg0->unk0 * arg1->unk8;
    arg2->unk8 = arg0->unk0 * arg1->unk4 - arg0->unk4 * arg1->unk0;
}

s32 func_15145128(struct17 *arg0, struct17 *arg1, f32 *arg2, f32 *arg3) {
    f32 local;
    f32 len;
    f32 inv_len;

    if (arg3 == NULL) {
        arg3 = &local;
    }

    len = (arg0->unk0 * arg0->unk0) + (arg0->unk4 * arg0->unk4) + (arg0->unk8 * arg0->unk8);
    if (len == 0.0f) {
        return 0;
    }

    len = sqrtf(len);
    inv_len = 1.0f / len;
    if (arg2 != NULL) {
        *arg2 = len;
    }
    *arg3 = inv_len;

    arg1->unk0 = arg0->unk0 * *arg3;
    arg1->unk4 = arg0->unk4 * *arg3;
    arg1->unk8 = arg0->unk8 * *arg3;
    return 1;
}
/* Non-matching C placeholders for asm/nonmatchings/game_16EE20/func_151451F0.s. */
s32 func_151451F0() {
    return 0;
}
/* Non-matching C placeholders for asm/nonmatchings/game_16EE20/func_151452C4.s. */
s32 func_151452C4() {
    return 0;
}
s32 func_151454BC(u8 arg0, f32 arg1, struct17 *arg2) {
    f32 tmp1;
    f32 tmp2;
    f32 tmp3;
    struct17 *temp_v0;

    temp_v0 = func_15144B34(arg0);
    tmp1 = arg2->unk0 - temp_v0->unk0;
    tmp2 = arg2->unk4 - temp_v0->unk4;
    tmp3 = arg2->unk8 - temp_v0->unk8;

    if ((arg1 * arg1) < ((tmp1 * tmp1) + (tmp2 * tmp2) + (tmp3 * tmp3))) {
        return 0;
    }
    return 1;
}

void func_15145548(struct17 *arg0, struct17 *arg1, struct17 *arg2, struct17 *arg3, f32 *arg4) {
    f32 local;

    if (arg4 == NULL) {
        arg4 = &local;
    }

    if (func_1514563C(arg0, arg1, arg2, arg3, arg4) != 0) {
        if (*arg4 < 0.0f) {
            arg3->unk0 = arg0->unk0;
            arg3->unk4 = arg0->unk4;
            arg3->unk8 = arg0->unk8;
        } else if (*arg4 > 1.0f) {
            arg3->unk0 = arg0->unk0 + arg1->unk0;
            arg3->unk4 = arg0->unk4 + arg1->unk4;
            arg3->unk8 = arg0->unk8 + arg1->unk8;
        }
    } else {
        arg3->unk0 = arg0->unk0;
        arg3->unk4 = arg0->unk4;
        arg3->unk8 = arg0->unk8;
    }
}

s32 func_1514563C(struct17 *arg0, struct17 *arg1, struct17 *arg2, struct17 *arg3, f32 *arg4) {
    f32 local;
    f32 mag_sq;
    f32 dot0;
    f32 dot1;
    f32 amount;

    if (arg4 == NULL) {
        arg4 = &local;
    }

    mag_sq = (arg1->unk0 * arg1->unk0) + (arg1->unk4 * arg1->unk4) + (arg1->unk8 * arg1->unk8);
    if (mag_sq == 0.0f) {
        return 0;
    }

    dot0 = (arg0->unk0 * arg1->unk0) + (arg0->unk4 * arg1->unk4) + (arg0->unk8 * arg1->unk8);
    dot1 = (arg2->unk0 * arg1->unk0) + (arg2->unk4 * arg1->unk4) + (arg2->unk8 * arg1->unk8);
    amount = (dot1 - dot0) / mag_sq;
    *arg4 = amount;

    arg3->unk0 = arg0->unk0 + (amount * arg1->unk0);
    arg3->unk4 = arg0->unk4 + (*arg4 * arg1->unk4);
    arg3->unk8 = arg0->unk8 + (*arg4 * arg1->unk8);
    return 1;
}
/* Non-matching C placeholders for asm/nonmatchings/game_16EE20/func_15145740.s. */
s32 func_15145740() {
    return 0;
}
// NON-MATCHING: 90% there
// void func_15145740(struct127 *arg0, struct17 *arg1, struct17 *arg2, struct17 *arg3, f32 arg4) {
//     struct194 tmp;
//     f32 temp_f6;
//     s16 phi_v1;
//     s16 phi_t0;
//
//     if ((arg0->unk4 == 0x96) && ((arg0->unk31C->unk7D != 0))) {
//         phi_t0 = arg0->unk7A + arg0->unk31C->unk80;
//     } else {
//         if (arg0->unk31C != 0) {
//             phi_t0 = arg0->unk7A - arg0->unk31C->unk12;
//         } else {
//             phi_t0 = arg0->unk7A;
//         }
//     }
//     if ((arg0->unk4 == 0x96) && (arg0->unk31C->unk7D != 0)) {
//         phi_v1 = arg0->unk31C->unk82 + 1024;
//     } else {
//         phi_v1 = arg0->unk1D1 * 200;
//     }
//     tmp.unk14 = phi_t0;
//     tmp.unk10 = phi_v1 * 0.005493164f;
//     tmp.unk0 = tmp.unk10 * D_800A56B4;
//     func_1505A184(phi_t0, 2000.0f, tmp.unk10, &arg1->unk0, &arg1->unk8, &arg1->unk4);
//     if (arg2 != 0) {
//         arg2->unk4 = cosf(tmp.unk0) * 1000.0f;
//         temp_f6 = sinf(tmp.unk0) * 1000.0f;
//         tmp.unk8 = temp_f6;
//         tmp.unk4 = phi_t0 * D_800A56B8;
//         arg2->unk0 = cosf(tmp.unk4) * tmp.unk8;
//         arg2->unk8 = sinf(tmp.unk4) * -temp_f6;
//         if (arg3 != 0) {
//             tmp.unkC = tmp.unk0 + arg4;
//             arg3->unk4 = cosf(tmp.unkC) * 1000.0f;
//             tmp.unk8 = sinf(tmp.unkC) * 1000.0f;
//             arg3->unk0 = cosf(tmp.unk4) * tmp.unk8;
//             arg3->unk8 = sinf(tmp.unk4) * -tmp.unk8;
//         }
//     }
// }

void func_15145974(struct17 *arg0, f32 *arg1, f32 *arg2) {
    *arg1 = func_150484A0(arg0->unk0, arg0->unk8) * D_800A56BC;
    if (arg2 != NULL) {
        *arg2 = (func_150484A0(sqrtf(arg0->unk0 * arg0->unk0 + arg0->unk8 * arg0->unk8), arg0->unk4) * D_800A56C0) - 90.0f;
    }
}

f32 func_15145A0C(f32 arg0, f32 arg1, f32 arg2) {
    return D_800A548C[(s32)(arg0 * arg2 * 100.0f)] * arg1;
}


void func_15145A50(struct127 *arg0) {
    arg0->unk5 = 3;
    if (D_800BE9F0 != 51) {
        if ((D_800BE616 != 0) || (arg0->interaction_state == 5) || (arg0->interaction_state == 1) || (arg0->interaction_state == 21)) {
            arg0->interaction_state = 5;
            if (arg0->unk31C != NULL) {
                arg0->unk31C->unk78 = 0;
            }
        } else {
            func_15053694(arg0);
        }
    }
}
/* Non-matching C placeholders for asm/nonmatchings/game_16EE20/func_15145AD8.s. */
s32 func_15145AD8() {
    return 0;
}
u8 func_15145C90(s32 arg0) {
    if (arg0 < 0) {
        return 1;
    } else {
        return (D_800DBEF4[arg0].unk6F & 0x80) == 0x80;
    }
}

void func_15145CD0(u8 *arg0, struct17 **arg1, struct17 **arg2, s32 arg3) {
    f32 mtx[4][4];
    struct17 *src;
    struct17 *dst;

    func_150A8050(mtx, *(f32 *)(arg0 + 0), *(f32 *)(arg0 + 4), *(f32 *)(arg0 + 8));
    mtx[3][0] = *(s16 *)(arg0 + 0x10);
    mtx[3][1] = *(s16 *)(arg0 + 0x12);
    mtx[3][2] = *(s16 *)(arg0 + 0x14);

    while (arg3 > 0) {
        src = *arg1;
        dst = *arg2;
        func_150A7960(mtx, src->unk0, src->unk4, src->unk8, &dst->unk0, &dst->unk4, &dst->unk8);
        arg3--;
        arg1++;
        arg2++;
    }
}

void func_15145DB4(u8 *arg0, struct17 *arg1, struct17 *arg2, s32 arg3) {
    f32 mtx[4][4];

    func_150A8050(mtx, *(f32 *)(arg0 + 0), *(f32 *)(arg0 + 4), *(f32 *)(arg0 + 8));
    mtx[3][0] = *(s16 *)(arg0 + 0x10);
    mtx[3][1] = *(s16 *)(arg0 + 0x12);
    mtx[3][2] = *(s16 *)(arg0 + 0x14);

    while (arg3 > 0) {
        func_150A7960(mtx, arg1->unk0, arg1->unk4, arg1->unk8, &arg2->unk0, &arg2->unk4, &arg2->unk8);
        arg3--;
        arg1++;
        arg2++;
    }
}
/* Non-matching C placeholders for asm/nonmatchings/game_16EE20/func_15145EA4.s. */
s32 func_15145EA4() {
    return 0;
}
/* Non-matching C placeholders for asm/nonmatchings/game_16EE20/func_15146078.s. */
s32 func_15146078() {
    return 0;
}
/* Non-matching C placeholders for asm/nonmatchings/game_16EE20/func_151462C8.s. */
s32 func_151462C8() {
    return 0;
}
s32 func_151464B8(s16 *arg0) {
    s32 i;
    s16 mask = 0;

    for (i = 0; i <= D_80082FA0; i++) {
        mask |= 1 << i;
    }

    return (arg0[1] & mask) == 0;
}

void func_15146508(struct127 *arg0, struct127 *arg1) {
    struct193 tmp;

    tmp.unk0 = arg0;
    tmp.unk4 = arg1;
    tmp.unk8 = arg0->unique_id;
    tmp.unk9 = arg1->unique_id;
    func_15169040(&tmp, 45, arg0, arg1);
}
/* Non-matching C placeholders for asm/nonmatchings/game_16EE20/func_1514654C.s. */
s32 func_1514654C() {
    return 0;
}
// NON-MATCHING: JUSTREG: first 3 statements are out of order
s32 func_1514672C(struct17 *arg0) {
    if ((D_800A56C4 < fabsf(arg0->unk0)) || (D_800A56C4 < fabsf(arg0->unk8)) || (D_800A56C4 < arg0->unk4) || (arg0->unk4 < D_800A56C8)) {
        return 0;
    } else {
        return 1;
    }
}

void func_151467A4(f32 *arg0, f32 arg1, f32 *arg2, f32 arg3, f32 arg4, f32 arg5, f32 arg6, f32 *arg7) {
    *arg0 = *arg0 - D_800BE9A4;
    if (*arg0 < 0.0f) {
        *arg0 = func_150ADA68() * arg1;
        if ((func_150ADA20() & 3) != 0) {
            *arg2 = (func_150ADA68() * (arg4 - arg3)) + arg3;
        } else {
            *arg2 = (func_150ADA68() * (arg5 - arg4)) + arg4;
        }
    }
    *arg7 = ((*arg2 - *arg7) * arg6) + *arg7;
}
