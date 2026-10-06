#include <ultra64.h>

#include "functions.h"
#include "variables.h"

/* Generated placeholder declarations. */
s32 func_1513C060();
s32 func_1513CBF0();
s32 func_1513CFE4();
s32 func_1513DB00();
s32 func_1513DF9C();
s32 func_1513E6E8();
s32 func_1513E83C();
s32 func_1513EAD8(s32 arg0, s32 arg1, s32 arg2);
s32 func_1513EE14();
s32 func_1513F114();
s32 func_1513F4E4();
s32 func_1513F728();
s32 func_1513FAB4(s32 arg0, s32 arg1, s32 arg2, s32 arg3);
void func_1513FFF4(u8 *out, u8 index, u8 variant);
void func_151400D0(u8 *out, u8 *input);
Vtx *func_15140190(u8 *actor, s16 view);
Vtx *func_15140410(u8 *actor, f32 *widthAxis, f32 *heightAxis, s16 view);
s32 func_151406AC();
/* End generated placeholder declarations. */

void func_151D5D60(void *, s16, s32, Vtx **, u8 *);
void func_150A7960(f32 *, f32, f32, f32, f32 *, f32 *, f32 *);

/* Non-matching C placeholders for asm/nonmatchings/game_169510/func_1513C060.s. */
s32 func_1513C060() {
    return 0;
}/* Non-matching C placeholders for asm/nonmatchings/game_169510/func_1513C350.s. */
#pragma GLOBAL_ASM("asm/nonmatchings/game_169510/func_1513C350.s")
// NON-MATCHING: JUSTREG: final 3 lines :(
// struct210 *func_1513C350(struct210 *arg0, s32 arg1, u8 arg2, u8 arg3, u8 arg4, s32 arg5, s32 arg6, struct167 *arg7, s32 arg8, u8 arg9, s32 argA) {
//     struct210 *temp_v0;
//     u8 phi_v0;
//     s32 i;
//
//     if (arg1 == 0) {
//         arg1 = &D_800A4AA0;
//     }
//     if (arg0->unk0 & 0x40000) {
//         phi_v0 = 0x4A;
//     } else {
//         phi_v0 = 0x1B;
//     }
//     temp_v0 = func_15167A68(phi_v0, argA, arg8 + 0xB0, 1, arg9, 1);
//     if (temp_v0 == 0) {
//         return NULL;
//     }
//     memcpy(&temp_v0->unk18.i.unk0, arg0, 0x28); // memcpy
//     func_1513FFF4(&temp_v0->unk40, temp_v0->unk1E, arg4);
//     func_151400D0(&temp_v0->unk40, arg1);
//     temp_v0->unk80 = arg2;
//     temp_v0->unk81 = arg3;
//     temp_v0->unk84 = arg5;
//     temp_v0->unk10 = 1;
//     temp_v0->unk14 = 0;
//     temp_v0->unkA0 = arg6;
//     for (i = 0; i < 4; i++) {
//         temp_v0->unk8C[i] = 0;
//     }
//
//     temp_v0->unk9C = 0;
//     if (arg5) {
//         for (i = 0; i <= D_80082FA0; i++) {
//             temp_v0->unk8C[i] = func_1515D480(arg5);
//         }
//         temp_v0->unk9C = func_1515D440();
//     }
//     if (arg7) {
//         temp_v0->unkA4[0] = arg7->unk0;
//         temp_v0->unkA4[1] = arg7->unk4;
//         temp_v0->unkA4[2] = arg7->unk8;
//     }
//     return temp_v0;
// }

struct210 *func_1513C4EC(s32 arg0, s32 arg1, u8 arg2, u8 arg3, f32 arg4, f32 arg5, f32 arg6, f32 arg7, f32 arg8, u8 arg9, u8 argA, s32 argB, s32 argC, s32 argD, u8 argE, s32 argF) {
    s32 temp_v0;
    struct17 tmp;

    tmp.unk0 = arg4;
    tmp.unk4 = arg5;
    tmp.unk8 = arg6;
    temp_v0 = func_1513C350(arg0, arg1, arg2, arg3, argA, argB, argC, &tmp, argD, argE, argF);
    if (temp_v0 == 0) {
        return 0;
    }
    func_1513E13C(temp_v0, arg4, arg5, arg6, arg7, arg8, arg9);
    return temp_v0;
}

struct210 *func_1513C5B0(s32 arg0, s32 arg1, u8 arg2, u8 arg3, f32 arg4, f32 arg5, f32 arg6, f32 arg7, f32 arg8, u8 arg9, u8 argA, s32 argB, u8 argC, s32 argD) {
    s32 tmp = func_1513C350(arg0, arg1, arg2, arg3, argA, 0, 0, 0, argB, argC, argD);
    if (tmp == 0) {
        return 0;
    }
    func_1513E13C(tmp, arg4, arg5, arg6, arg7, arg8, arg9);
    return tmp;
}

struct210 *func_1513C650(s32 arg0, u8 arg1, u8 arg2, s32 arg3, f32 arg4, f32 arg5, f32 arg6, f32 arg7, f32 arg8, u8 arg9, u8 argA, s32 argB, s32 argC, s32 argD, u8 argE, s32 argF) {
    s32 temp_v0;
    struct17 tmp;

    tmp.unk0 = arg4;
    tmp.unk4 = arg5;
    tmp.unk8 = arg6;

    temp_v0 = func_1513C350(arg0, 0, arg1, arg2, argA, argB, argC, &tmp, argD, argE, argF);
    if (temp_v0 == 0) {
        return 0;
    }

    if (func_1513E2AC(temp_v0, 0, arg3, arg4, arg5, arg6, arg7, arg8, arg9) == 0) {
        func_1516972C(temp_v0);
        return 0;
    }
    return temp_v0;
}

struct210 *func_1513C73C(s32 arg0, u8 arg1, u8 arg2, s32 arg3, f32 arg4, f32 arg5, f32 arg6, f32 arg7, f32 arg8, u8 arg9, u8 argA, s32 argB, u8 argC, s32 argD) {
    s32 tmp = func_1513C350(arg0, 0, arg1, arg2, argA, 0, 0, 0, argB, argC, argD);
    if (tmp == 0) {
        return 0;
    }

    if (func_1513E2AC(tmp, 0, arg3, arg4, arg5, arg6, arg7, arg8, arg9) == 0) {
        func_1516972C(tmp);
        return 0;
    }
    return tmp;
}

struct210 *func_1513C804(s32 arg0, s32 arg1, u8 arg2, u8 arg3, s32 arg4, f32 arg5, f32 arg6, f32 arg7, f32 arg8, f32 arg9, u8 argA, u8 argB, s32 argC, u8 argD, s32 argE) {
    s32 tmp = func_1513C350(arg0, 0, arg2, arg3, argB, 0, 0, 0, argC, argD, argE);
    if (tmp == 0) {
        return 0;
    }
    if (func_1513E2AC(tmp, 0, arg4, arg5, arg6, arg7, arg8, arg9, argA) == 0) {
        func_1516972C(tmp);
        return 0;
    }
    return tmp;
}

void func_1513C8D4(struct210 *arg0) {
    func_1513C92C(arg0);
    func_15169804(arg0);
}

void func_1513C900(struct210 *arg0) {
    func_1513C92C(arg0);
    func_15169824(arg0);
}

void func_1513C92C(struct210 *arg0) {
    s32 i;

    for (i = 0; i <= D_80082FA0; i++) {
        if (arg0->unk8C[i]) {
            func_100043B4(arg0->unk8C[i], 4);
        }
    }
    if (arg0->unk9C != 0) {
        func_100043B4(arg0->unk9C, 4);
    }
}

void func_1513C9B0(struct210 *arg0) {
    s32 idx;
    if ((arg0->unk18.i.unk0 & 0x1000) != 0) {
        idx = arg0->unk1F;
    } else {
        idx = 0;
    }
    D_80089EE8[idx]();
}

void func_1513C9FC(struct210 *arg0) {
    s32 idx;
    if ((arg0->unk18.i.unk0 & 0x1000) != 0) {
        idx = arg0->unk1F;
    } else {
        idx = 0;
    }
    D_80089EF0[idx]();
}

void func_1513CA48(struct210 *arg0) {
    func_151D5E30(&arg0->unk100);
}

void func_1513CA6C(struct210 *arg0) {
    func_1513CA48(arg0);
    func_1513CAD4(arg0);
    func_15169804(arg0);
}

void func_1513CAA0(struct210 *arg0) {
    func_1513CA48(arg0);
    func_1513CAD4(arg0);
    func_15169824(arg0);
}

void func_1513CAD4(struct210 *arg0) {
    s32 i;

    for (i = 0; i <= D_80082FA0; i++) {
        if (arg0->unkA4[i]) {
            func_100043B4(arg0->unkA4[i], 4);
        }
    }
    if (arg0->unkB4 != 0) {
        func_100043B4(arg0->unkB4, 4);
    }
}

// is this really struct210?
void func_1513CB58(struct210 *arg0) {
    s32 idx;
    if ((arg0->unk58 & 0x400000) != 0) {
        idx = arg0->unk18.b.unk1; //unk19;
    } else {
        idx = 0;
    }
    D_80089EF8[idx]();
}

void func_1513CBA4(struct210 *arg0) {
    s32 idx;
    if ((arg0->unk58 & 0x400000) != 0) {
        idx = arg0->unk18.b.unk1; //unk19;
    } else {
        idx = 0;
    }
    D_80089F2C[idx]();
}
/* Non-matching C placeholders for asm/nonmatchings/game_169510/func_1513CBF0.s. */
s32 func_1513CBF0() {
    return 0;
}
void func_1513CF9C(s32 arg0, s32 arg1, u8 arg2) {
    D_80089F60[0](arg0, arg1, arg2);
}

void func_1513CFD0(s32 arg0, s32 arg1, s32 arg2) {
}
/* Non-matching C placeholders for asm/nonmatchings/game_169510/func_1513CFE4.s. */
s32 func_1513CFE4() {
    return 0;
}/* Non-matching C placeholders for asm/nonmatchings/game_169510/func_1513D2F0.s. */
void *func_1513D2F0(void *descriptor, s32 table, u8 kind, u8 mode, u8 first,
                      u8 setup, u8 variant, s32 resource, s32 extra, s32 payload,
                      u8 channel, s32 context) {
    extern f32 D_800A5184;
    extern void *func_15167A68(s32, s32, s32, s32, u8, u8);
    extern u8 *func_1515D480(s32);
    extern u8 *func_1515D440(void);
    u8 *result;
    u32 flags;
    s32 category;
    u8 allocationMode;
    s32 i;

    flags = *(u32 *)((u8 *)descriptor + 0x40);
    if ((flags & 0x800000) != 0) {
        category = 0x56;
    } else if ((flags & 0x2000000) != 0) {
        category = 0x49;
    } else {
        category = 0x1C;
    }
    allocationMode = (flags & 0x80000000) != 0 ? 2 : 1;
    result = func_15167A68(category, context, payload + 0x110, 1, channel, allocationMode);
    if (result == NULL) {
        return NULL;
    }
    memcpy(result + 0x18, descriptor, 0x58);
    result[0x70] = kind;
    result[0x71] = mode;
    result[0x72] = first;
    result[0x73] = setup;
    result[0x74] = 0;
    bzero(result + 0x100, 0x10);
    func_1513FFF4(result + 0xC0, result[0x18], variant);
    func_151400D0(result + 0xC0, (u8 *)table);
    *(s32 *)(result + 0x10) = 1;
    *(s32 *)(result + 0x14) = 0;
    *(f32 *)(result + 0x78) = D_800A5184;
    *(s32 *)(result + 0x98) = 0;
    result[0x95] = 0;
    result[0x94] = 0;
    *(s32 *)(result + 0x90) = 0;
    *(s32 *)(result + 0x9C) = resource;
    *(s32 *)(result + 0xB8) = extra;
    result[0xA0] = 0;
    for (i = 0; i < 4; i++) {
        *(u8 **)(result + 0xA4 + i * 4) = NULL;
    }
    *(u8 **)(result + 0xB4) = NULL;
    if (resource != 0) {
        for (i = 0; i <= D_80082FA0; i++) {
            *(u8 **)(result + 0xA4 + i * 4) = func_1515D480(resource);
        }
        *(u8 **)(result + 0xB4) = func_1515D440();
    }
    return result;
}
void func_1513D4B8(s32 arg0, s32 arg1, u8 arg2, u8 arg3, u8 arg4, u8 arg5, u8 arg6, s32 arg7, u8 arg8, s32 arg9) {
    func_1513D2F0(arg0, arg1, arg2, arg3, arg4, arg5, arg6, 0, 0, arg7, arg8, arg9);
}

void func_1513D524(s32 arg0, u8 arg1, u8 arg2, u8 arg3, u8 arg4, u8 arg5, s32 arg6, u8 arg7, s32 arg8) {
    func_1513D2F0(arg0, &D_800A4AA0, arg1, arg2, arg3, arg4, arg5, 0, 0, arg6, arg7, arg8);
}

s32 func_1513D594(s32 arg0, s32 arg1, u8 arg2, u8 arg3, u8 arg4, u8 arg5, s16 arg6, f32 arg7, f32 arg8, s32 arg9, s32 argA, s32 argB, s32 argC, u8 argD, s32 argE, u8 argF, s32 arg10) {
    struct210 *temp_v0;

    if (arg1 == 0) {
        arg1 = &D_800A4AA0;
    }
    temp_v0 = func_1513D2F0(arg0, arg1, arg2, arg3, arg4, 0xC, arg5, argB, argC, argE + 0x18, argF, arg10);
    if ((temp_v0 != 0) && (func_1513D6FC(&temp_v0->unk110, arg6, arg7, arg8, arg9, argA, argD) == 0)) {
        func_1516972C(temp_v0);
        return 0;
    }
    return temp_v0;
}

void func_1513D668(s32 arg0, s32 arg1, u8 arg2, u8 arg3, u8 arg4, u8 arg5, s16 arg6, f32 arg7, f32 arg8, s32 arg9, s32 argA, u8 argB, s32 argC, u8 argD, s32 argE) {
    func_1513D594(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, argA, 0, 0, argB, argC, argD, argE);
}
/* Non-matching C placeholders for asm/nonmatchings/game_169510/func_1513D6FC.s. */
s32 func_1513D6FC(struct211 *arg0, s16 arg1, f32 arg2, f32 arg3, s32 arg4, s32 arg5, u8 arg6) {
    return 0;
}
// s32 func_1513D6FC(struct211 *arg0, s16 arg1, f32 arg2, f32 arg3, s32 arg4, s32 arg5, u8 arg6) {
//     f32 spBC;
//     f32 spB8;
//     f32 spB4;
//     s32 spB0;
//     f32 spAC;
//     s32 spA8;
//     f32 spA4;
//     s32 spA0;
//     s32 sp9C;
//     s32 sp98;
//     s32 sp94;
//     s32 sp90;
//     f32 sp8C;
//     f32 sp88;
//     f32 sp84;
//     s32 sp80;
//     f32 sp7C;
//     f32 sp78;
//     f32 sp74;
//     f32 sp70;
//     f32 sp6C;
//     f32 sp68;
//     f32 sp64;
//     f32 sp60;
//     s32 sp5C;
//     s32 sp58;
//     s32 sp54; // ?
//     s32 sp50; // ?
//     s32 sp4C; // ?
//     s32 sp48; // ?
//     s32 sp44; // ?
//     s32 sp40; // ?
//     s32 sp3C; // ?
//     s32 sp38; // ?
//     s32 sp34; // ?
//     s32 sp30; // ?
//     f32 sp2C;
//     f32 sp28;
//     f32 sp24;
//
//     f32 temp_f0;
//     f32 temp_f16;
//     f32 temp_f18;
//     f32 phi_f12;
//     f32 phi_f14;
//     f32 phi_f12_2;
//
//     if (arg6 != 0) {
//         spB4 = func_151423D8(arg1 - 64);
//         temp_f0 = func_151423D8(arg1);
//         spAC = arg2 * temp_f0;
//         spA4 = arg3 * temp_f0;
//         if (func_1510E388(arg4, arg5, &spBC, &spB8) == 0) {
//             return 0;
//         }
//         temp_f18 = spA4 * spB8;
//         sp2C = fabsf(spA4);
//         temp_f16 = arg3 * spB4;
//         sp28 = sqrtf((spA4 * spA4) + (temp_f18 * temp_f18));
//         if (temp_f16 != 0.0f) {
//             sp8C = temp_f16 * spBC;
//             sp88 = fabsf(temp_f16) / sqrtf((temp_f16 * temp_f16) + (sp8C * sp8C));
//         } else {
//             sp8C = 0.0f;
//             sp88 = 0.0f;
//         }
//         if (spA4 != 0.0f) {
//             sp84 = temp_f18;
//             phi_f12 = sp2C / sp28;
//         } else {
//             sp84 = 0.0f;
//             phi_f12 = 0.0f;
//         }
//         arg0->unk0 = sp88 * temp_f16;
//         arg0->unk8 = phi_f12 * spA4;
//         arg0->unk4 = (sp88 * sp8C) + (phi_f12 * sp84) + 0.5f;
//         temp_f18 = -(arg2 * spB4);
//         temp_f16 = temp_f18 * spB8;
//         sp28 = fabsf(temp_f18);
//         sp2C = temp_f16;
//         sp24 = sqrtf((temp_f18 * temp_f18) + (temp_f16 * temp_f16));
//         if (spAC != 0.0f) {
//             temp_f0 = spAC * spBC;
//             sp8C = temp_f0;
//             phi_f14 = fabsf(spAC) / sqrtf((spAC * spAC) + (temp_f0 * temp_f0));
//         } else {
//             sp8C = 0.0f;
//             sp88 = 0.0f;
//             phi_f14 = 0.0f;
//         }
//         if (temp_f18 != 0.0f) {
//             sp84 = sp2C;
//             phi_f12_2 = sp28 / sp24;
//         } else {
//             sp84 = 0.0f;
//             phi_f12_2 = 0.0f;
//         }
//         arg0->unkC = phi_f14 * spAC;
//         arg0->unk14 = phi_f12_2 * temp_f18;
//         arg0->unk10 = (phi_f14 * sp8C) + (phi_f12_2 * sp84) + 0.5f;
//     } else {
//         sp7C = func_151423D8(arg1 - 64);
//         sp78 = func_151423D8(arg1);
//         if (func_15144E80(arg5, &sp6C, &sp60, &sp54) == 0) {
//             return 0;
//         }
//         if (func_15145128(&sp6C, &sp6C, &sp50, &sp4C) == 0) {
//             return 0;
//         }
//         if (func_15145128(&sp60, &sp60, &sp50, &sp4C) == 0) {
//             return 0;
//         }
//         temp_f0 = arg2 * sp78;
//         temp_f18 = arg2 * sp7C;
//         arg0->unk0 = (temp_f0 * sp6C) + (temp_f18 * sp60);
//         arg0->unk4 = (temp_f0 * sp70) + (temp_f18 * sp64);
//         arg0->unk8 = (temp_f0 * sp74) + (temp_f18 * sp68);
//         temp_f0 = -arg3 * sp7C;
//         temp_f18 = arg3 * sp78;
//         arg0->unkC = (temp_f0 * sp6C) + (temp_f18 * sp60);
//         arg0->unk10 = (temp_f0 * sp70) + (temp_f18 * sp64);
//         arg0->unk14 = (temp_f0 * sp74) + (temp_f18 * sp68);
//     }
//     return 1;
// }
/* Non-matching C placeholders for asm/nonmatchings/game_169510/func_1513DB00.s. */
s32 func_1513DB00() {
    return 0;
}
// jump table
/* Non-matching C placeholders for asm/nonmatchings/game_169510/func_1513DF9C.s. */
s32 func_1513DF9C() {
    return 0;
}
void func_1513E070(s32 arg0, s32 arg1, s32 arg2) {
}

void func_1513E084(struct210 *arg0, struct212 *arg1, u8 arg2) {
    struct212 *temp_v0 = &arg0->unk110;
    if (arg2 == 0x1A) {
        if ((temp_v0->unk0 == arg1->unk0) || (temp_v0->unk4.b.unk0 == arg1->unk4.b.unk0)) {
            func_1516972C(arg0);
        }
    } else {
        temp_v0 = &arg0->unk110;
        if (arg2 == 0x2D) {
            if (temp_v0->unk0 == arg1->unk0) {
                temp_v0->unk0 = arg1->unk4.i.unk0;
                temp_v0->unk4.b.unk0 = arg1->unk9;
            } else if (temp_v0->unk0 == arg1->unk4.i.unk0) {
                temp_v0->unk0 = arg1->unk0;
                temp_v0->unk4.b.unk0 = arg1->unk8;
            }
        }
    }
}

void func_1513E134(void) {
}

// NON-MATCHING: register scheduling only
void func_1513E13C(struct210 *arg0, f32 arg1, f32 arg2, f32 arg3, f32 arg4, f32 arg5, u8 arg6) {
    f32 sp48;
    f32 sp30;
    f32 sp1C;

    f32 temp_f0;
    f32 temp_f12;
    f32 temp_f14;
    f32 temp_f16;
    f32 temp_f18;
    f32 temp_f2;
    s32 temp_f10;

    sp48 = func_151423D8((arg6 - 0x40));
    temp_f0 = func_151423D8(arg6);
    temp_f12 = arg5 * sp48;
    temp_f14 = arg4 * temp_f0;
    temp_f18 = arg1 + temp_f14;
    arg0->unk40 = temp_f18 - temp_f12;
    temp_f10 = arg2;
    arg0->unk42 = temp_f10;
    temp_f16 = arg5 * temp_f0;
    temp_f2 = arg4 * sp48;
    sp1C = arg3 + temp_f16;
    sp30 = arg1 - temp_f14;
    arg0->unk44 = sp1C + temp_f2;
    arg0->unk52 = temp_f10;
    arg0->unk50 = sp30 - temp_f12;
    arg0->unk54 = sp1C - temp_f2;
    arg0->unk62 = temp_f10;
    arg0->unk60 = sp30 + temp_f12;
    arg0->unk72 = temp_f10;
    arg0->unk70 = temp_f18 + temp_f12;
    sp30 = arg3 - temp_f16;
    arg0->unk64 = sp30 - temp_f2;
    arg0->unk74 = sp30 + temp_f2;
}

void func_1513E2A4(void) {
}
/* Non-matching C placeholders for asm/nonmatchings/game_169510/func_1513E2AC.s. */
#pragma GLOBAL_ASM("asm/nonmatchings/game_169510/func_1513E2AC.s")
/* Non-matching C placeholders for asm/nonmatchings/game_169510/func_1513E6E8.s. */
s32 func_1513E6E8() {
    return 0;
}
// s32 func_1513E6E8(void *arg0) {
//     void *temp_v0;
//     void *temp_v0_2;
//     void *temp_v0_3;
//     void *temp_v0_4;
//     s32 phi_v1;
//     s32 phi_v1_2;
//
//     if ((arg0->unk58 & 0x20) != 0) {
//         temp_v0 = arg0->unk110;
//         temp_v0->unkC = (f32) (temp_v0->unkC + (temp_v0->unk2C * D_800BE9A4));
//     }
//     phi_v1 = arg0->unk58;
//     if ((arg0->unk58 & 0x40) != 0) {
//         temp_v0_2 = arg0->unk110;
//         arg0->unk34 = (f32) (arg0->unk34 + (temp_v0_2->unk8 * D_800BE9A4));
//         arg0->unk38 = (f32) (arg0->unk38 + (temp_v0_2->unkC * D_800BE9A4));
//         arg0->unk3C = (f32) (arg0->unk3C + (temp_v0_2->unk10 * D_800BE9A4));
//         phi_v1 = arg0->unk58;
//     }
//     temp_v0_3 = arg0->unk110;
//     phi_v1_2 = phi_v1;
//     if ((phi_v1 & 0x80) != 0) {
//         arg0->unk40 = (f32) (arg0->unk40 + (temp_v0_3->unk14 * D_800BE9A4));
//         arg0->unk44 = (f32) (arg0->unk44 + (temp_v0_3->unk18 * D_800BE9A4));
//         arg0->unk48 = (f32) (arg0->unk48 + (temp_v0_3->unk1C * D_800BE9A4));
//         phi_v1_2 = arg0->unk58;
//     }
//     temp_v0_4 = arg0->unk110;
//     if ((phi_v1_2 & 0x100) != 0) {
//         arg0->unk4C = (f32) (arg0->unk4C + (temp_v0_4->unk20 * D_800BE9A4));
//         arg0->unk50 = (f32) (arg0->unk50 + (temp_v0_4->unk24 * D_800BE9A4));
//         arg0->unk54 = (f32) (arg0->unk54 + (temp_v0_4->unk28 * D_800BE9A4));
//     }
//     arg0->unk5D = (u8)0xFF;
//     return 1;
// }
/* Non-matching C placeholders for asm/nonmatchings/game_169510/func_1513E83C.s. */
s32 func_1513E83C() {
    return 0;
}
// ???
/* Non-matching C placeholders for asm/nonmatchings/game_169510/func_1513EAD8.s. */
s32 func_1513EAD8(s32 arg0, s32 arg1, s32 arg2) {
    return 0;
}
void func_1513EDB4(s32 arg0, s16 arg1) {
    func_1513EAD8(arg0, 0, arg1);
}

void func_1513EDE4(s32 arg0, s16 arg1) {
    func_1513EAD8(arg0, 1, arg1);
}
/* Non-matching C placeholders for asm/nonmatchings/game_169510/func_1513EE14.s. */
s32 func_1513EE14() {
    return 0;
}/* Non-matching C placeholders for asm/nonmatchings/game_169510/func_1513F114.s. */
s32 func_1513F114() {
    return 0;
}
void func_1513F4B0(struct210 *arg0, s16 arg1) {
    func_15140410((u8 *)arg0, (f32 *)((u8 *)arg0 + 0x110),
                 (f32 *)((u8 *)arg0 + 0x11C), arg1);
}
/* Non-matching C placeholders for asm/nonmatchings/game_169510/func_1513F4E4.s. */
s32 func_1513F4E4() {
    return 0;
}
void func_1513F680(struct171 *arg0, u8 arg1, u8 arg2, u8 arg3, u8 arg4) {
    arg0->unk70 = arg1;
    arg0->unk71 = arg2;
    arg0->unk72 = arg3;
    arg0->unk73 = arg4;
}

void func_1513F6C0(struct210 *arg0, u8 arg1, u8 arg2) {
    arg0->unk80 = arg1;
    arg0->unk81 = arg2;
}

// NON-MATCHING: stackless retail scheduling
s32 func_1513F6E8(struct210 *arg0) {
    arg0->unk2C += arg0->unk128 * D_800BE9A4;
    arg0->unk30 += arg0->unk128 * D_800BE9A4;
    return 1;
}
/* Non-matching C placeholders for asm/nonmatchings/game_169510/func_1513F728.s. */
s32 func_1513F728() {
    return 0;
}
void func_1513FA2C(struct210 *arg0, s16 arg1) {
    f32 tmp[2];

    tmp[0] = 1.0f;
    tmp[1] = 1.0f;
    func_1513FAB4(arg0, 0, tmp, arg1);
}

void func_1513FA70(struct210 *arg0, s16 arg1) {
    f32 tmp[2];

    tmp[0] = 1.0f;
    tmp[1] = 1.0f;
    func_1513FAB4(arg0, 1, tmp, arg1);
}
/* Non-matching C placeholders for asm/nonmatchings/game_169510/func_1513FAB4.s. */
s32 func_1513FAB4(s32 arg0, s32 arg1, s32 arg2, s32 arg3) {
    return 0;
}

void func_1513FFF4(u8 *out, u8 index, u8 variant) {
    typedef struct {
        u8 prefix[6];
        u16 width;
        u16 height;
        u8 tail[2];
    } ViewDimensions169510;
    extern ViewDimensions169510 D_80090B60[];
    ViewDimensions169510 *record;
    u16 width, height;
    s32 coordinate;

    if (index != 255) {
        record = &D_80090B60[index];
        width = record->width - 1;
        height = record->height - 1;
        coordinate = (variant & 1) ? width << 6 : 0;
        *(s16 *)(out + 0x38) = coordinate;
        *(s16 *)(out + 0x08) = coordinate;
        coordinate = (variant & 1) ? 0 : width << 6;
        *(s16 *)(out + 0x28) = coordinate;
        *(s16 *)(out + 0x18) = coordinate;
        coordinate = (variant & 2) ? height << 6 : 0;
        *(s16 *)(out + 0x1A) = coordinate;
        *(s16 *)(out + 0x0A) = coordinate;
        coordinate = (variant & 2) ? 0 : height << 6;
        *(s16 *)(out + 0x3A) = coordinate;
        *(s16 *)(out + 0x2A) = coordinate;
    }
}
void func_151400D0(u8 *out, u8 *input) {
    s32 i;
    for (i = 0; i < 4; i++) {
        *(u16 *)(out + 6) = *(u16 *)(input + 8);
        out[12] = *(s16 *)(input + 0);
        out[13] = *(s16 *)(input + 2);
        out[14] = *(s16 *)(input + 4);
        out[15] = *(s16 *)(input + 6);
        *(u16 *)(out + 6) = 0;
        out += 16;
        input += 10;
    }
}
Vtx *func_15140190(u8 *actor, s16 view) {
    Vtx *cursor;
    Vtx *first;
    f32 matrix[4][4];
    f32 points[4][3];
    u8 i;
    u8 fresh;
    func_151D5D60(actor + 0x100, view, 0x40, &cursor, &fresh);
    first = cursor;
    if (cursor != NULL) {
        if (fresh) {
            memcpy(*(u8 **)(actor + 0x100 + view * 4), actor + 0xC0, 0x40);
            memcpy(*(u8 **)(actor + 0x100 + view * 4) + 0x40, actor + 0xC0, 0x40);
        }
    } else {
        return NULL;
    }
    points[0][2] = 0.0f;
    points[0][0] = *(f32 *)(actor + 0x2C);
    points[0][1] = *(f32 *)(actor + 0x30);
    points[1][0] = -*(f32 *)(actor + 0x2C);
    points[1][1] = *(f32 *)(actor + 0x30);
    points[1][2] = 0.0f;
    points[2][0] = -*(f32 *)(actor + 0x2C);
    points[2][1] = -*(f32 *)(actor + 0x30);
    points[2][2] = 0.0f;
    points[3][0] = *(f32 *)(actor + 0x2C);
    points[3][1] = -*(f32 *)(actor + 0x30);
    points[3][2] = 0.0f;
    func_150A8050(matrix, *(f32 *)(actor + 0x40), *(f32 *)(actor + 0x44), *(f32 *)(actor + 0x48));
    matrix[3][0] = *(f32 *)(actor + 0x34);
    matrix[3][1] = *(f32 *)(actor + 0x38);
    matrix[3][2] = *(f32 *)(actor + 0x3C);
    for (i = 0; i < 4; i++) {
        f32 *point = points[i];
        func_150A7960((f32 *)matrix, point[0], point[1], 0.0f,
                     &point[0], &point[1], &point[2]);
        cursor->v.ob[0] = (s32)point[0];
        cursor->v.ob[1] = (s32)point[1];
        cursor->v.ob[2] = (s32)point[2];
        cursor->v.flag = 0;
        cursor++;
    }
    return first;
}
void func_151403A8(s32 arg0, u8 arg1) {
    func_15169260(&D_800A5168, 4, arg0, arg1);
}

void func_151403DC(s32 arg0, u8 arg1) {
    func_15169260(&D_800A5178, 3, arg0, arg1);
}
Vtx *func_15140410(u8 *actor, f32 *widthAxis, f32 *heightAxis, s16 view) {
    Vtx *cursor;
    Vtx *first;
    f32 wx, wy, wz, hx, hy, hz;
    u8 fresh;
    func_151D5D60(actor + 0x100, view, 0x40, &cursor, &fresh);
    first = cursor;
    if (cursor != NULL) {
        if (fresh) {
            memcpy(*(u8 **)(actor + 0x100 + view * 4), actor + 0xC0, 0x40);
            memcpy(*(u8 **)(actor + 0x100 + view * 4) + 0x40, actor + 0xC0, 0x40);
        }
    } else {
        return NULL;
    }
    wx = *(f32 *)(actor + 0x2C) * widthAxis[0];
    wy = *(f32 *)(actor + 0x2C) * widthAxis[1];
    wz = *(f32 *)(actor + 0x2C) * widthAxis[2];
    hx = *(f32 *)(actor + 0x30) * heightAxis[0];
    hy = *(f32 *)(actor + 0x30) * heightAxis[1];
    hz = *(f32 *)(actor + 0x30) * heightAxis[2];
    cursor[0].v.ob[0] = (s32)((*(f32 *)(actor + 0x34) + wx) + hx);
    cursor[0].v.ob[1] = (s32)((*(f32 *)(actor + 0x38) + wy) + hy);
    cursor[0].v.ob[2] = (s32)((*(f32 *)(actor + 0x3C) + wz) + hz);
    cursor[0].v.flag = 0;
    cursor[1].v.ob[0] = (s32)((*(f32 *)(actor + 0x34) - wx) + hx);
    cursor[1].v.ob[1] = (s32)((*(f32 *)(actor + 0x38) - wy) + hy);
    cursor[1].v.ob[2] = (s32)((*(f32 *)(actor + 0x3C) - wz) + hz);
    cursor[1].v.flag = 0;
    cursor[2].v.ob[0] = (s32)((*(f32 *)(actor + 0x34) - wx) - hx);
    cursor[2].v.ob[1] = (s32)((*(f32 *)(actor + 0x38) - wy) - hy);
    cursor[2].v.ob[2] = (s32)((*(f32 *)(actor + 0x3C) - wz) - hz);
    cursor[2].v.flag = 0;
    cursor[3].v.ob[0] = (s32)((*(f32 *)(actor + 0x34) + wx) - hx);
    cursor[3].v.ob[1] = (s32)((*(f32 *)(actor + 0x38) + wy) - hy);
    cursor[3].v.ob[2] = (s32)((*(f32 *)(actor + 0x3C) + wz) - hz);
    cursor[3].v.flag = 0;
    return first;
}
/* Non-matching C placeholders for asm/nonmatchings/game_169510/func_151406AC.s. */
s32 func_151406AC() {
    return 0;
}
