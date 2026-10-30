#include <ultra64.h>

#include "functions.h"
#include "variables.h"

u32 func_1502B8E0(void *buffer, u32 cap, u32 depth, ...);

typedef struct { u8 values[2][3]; } EffectSelectorTable36680;
typedef struct {
    f32 unk0;
    f32 unk4;
    u8 *record;
    f32 unkC;
    f32 unk10;
    f32 unk14;
} UnkB060C;
extern EffectSelectorTable36680 D_80082BEC;
extern s32 D_800BE9F0;
s32 func_150B060C(u8, UnkB060C *);
struct225 *func_1516037C(Header *, struct226 *, s32, u8, s32);
void *memcpy(void *, const void *, u32);

typedef struct { u8 values[6]; } EffectPointIds36680;
extern EffectPointIds36680 D_80082BF4;
u8 *func_151149AC(u8);

/* Generated placeholder declarations. */
s32 func_15009334(s32 arg0);
void func_1500A6D8(struct226 *actor, s32 command);
void func_1500A7E8(struct226 *actor, s32 command);
s32 func_1500AC14();
s32 func_1500AD84();
s32 func_1500AF08();
s32 func_1500B1F4();
s32 func_1500B3B0();
s32 func_1500B714();
s32 func_1500B8F4();
s32 func_1500BAB8();
s32 func_1500BC7C();
s32 func_1500BEC0();
/* End generated placeholder declarations. */

void func_150091D0(void) {
    int tmp0 = 127;

    D_800DCD78 = 0;
    D_800DCD7C = 1;
    D_800DCD80 = 0;
    D_800DCD84 = 0;

    func_1515D4D4(255, 255, 255, 0);

    D_800DCD24[0] = 0;
    D_800DCD24[1] = 0;
    D_800DCD24[2] = 0;

    D_800DCD28[0] = 255;
    D_800DCD28[1] = 255;
    D_800DCD28[2] = 255;

    if (0) {};

    D_800DCD30 = tmp0;
    D_800DCD31 = 0;
    D_800DCD32 = 0;

    D_800DCD33 = tmp0;
    D_800DCD34 = 0;
    D_800DCD35 = 0;

    D_800DCD36 = tmp0;
    D_800DCD37 = 0;
    D_800DCD38 = 0;

    D_800DCD39 = tmp0;
    D_800DCD3A = 0;
    D_800DCD3B = 0;
    D_800DCD3C = 0;
    D_800DCD3D = 0;
    bzero(&D_800DCD40, 56);
}

void func_150092DC(void) {
    u32 i;
    for (i = 0; i < D_800D3094; i++) {
        func_15009334(i);
    }
}

// requires jumptable
/* Non-matching C placeholders for asm/nonmatchings/game_36680/func_15009334.s. */
#pragma GLOBAL_ASM("asm/nonmatchings/game_36680/func_15009334.s")

void func_150095D8(s32 arg0, s32 arg1) {
    func_1516127C(arg0, 0xFF, 1);
}

void func_15009600(s32 arg0, s32 arg1) {
    func_15161334(arg0, 0xFF, 1);
}

void func_15009628(s32 arg0, s32 arg1) {
    struct220 tmp;
    u8 sp24[4] = D_80082BE0; // {1, 2, 3, 4};
    tmp.unk0 = 0;
    tmp.unk1 = -1;
    tmp.unk2 = 300;
    tmp.unk4 = sp24[arg1 - 3];

    func_1516037C((Header *)&tmp, (struct226 *)arg0, 0, 255, 1);
}

void func_1500969C(s32 arg0, s32 arg1) {
    func_15161408(arg0, 0xFF, 1);
}

void func_150096C4(s32 arg0, s32 arg1) {
    struct220 tmp;
    u8 sp24[5] =  D_80082BE4; // {10, 9, 12, 11, 7};
    tmp.unk0 = 0;
    tmp.unk1 = -1;
    tmp.unk2 = 300;
    tmp.unk4 = sp24[arg1 - 8];

    func_1516037C((Header *)&tmp, (struct226 *)arg0, 0, 255, 1);
}

void func_15009740(s32 arg0, s32 arg1) {
    func_15161494(arg0, 0xFF, 1);
}

void func_15009768(s32 arg0, s32 arg1) {
    func_151615F8(arg0, 0, 0, 0xE, 0xFF, 1);
}

void func_150097A4(s32 arg0, s32 arg1) {
    func_15161540(arg0, 0xFF, 1);
}

void func_150097CC(s32 arg0, s32 arg1) {
    s32 temp_v0 = func_151615F8(arg0, 0, 2, 0xE, 0xFF, 1);
    if (temp_v0 != 0) {
        func_150121C0(temp_v0);
    }
}

void func_15009818(s32 arg0, s32 arg1) {
    func_151B8DB0(arg0, 0, 0xFF, 1);
}

void func_15009844(s32 arg0, s32 arg1) {
    func_151B8DB0(arg0, 1, 0xFF, 1);
}

void func_15009870(s32 arg0, s32 arg1) {
    func_15108850(arg0);
}

void func_15009894(s32 arg0, s32 arg1) {
    func_151615F8(arg0, 1, 0, 0xE, 0xFF, 1);
}

void func_150098D0(s32 arg0, s32 arg1) {
    func_15162034(arg0, 0xFF, 1);
}

void func_150098F8(s32 arg0, s32 arg1) {
    func_151623F4(arg0, 1, 22, 0, -1, 300, 0xFF, 1);
}

void func_15009944(s32 arg0, s32 arg1) {
    func_15162740(arg0, 1, 6, 0, 300, 2, 0xFF, 1);
}

void func_15009990(s32 arg0, s32 arg1) {
    struct132 * temp_v0;
    u8 sp40[4];

    sp40[0] = D_80095B50[arg1];
    temp_v0 = func_1516295C(arg0, D_80095B48[arg1], D_80095B4C[arg1], 2, 300, 12, -1, 0, -1, 1, 1, 255, 1);
    if (temp_v0 != 0) {
        memcpy(&temp_v0->unk48, &sp40, 1);
    }
}

void func_15009A38(s32 arg0, s32 arg1) {
    struct220 tmp;

    tmp.unk0 = 2;
    tmp.unk1 = -1;
    tmp.unk2 = 300;
    tmp.unk4 = D_80095B27[arg1];
    func_1516037C((Header *)&tmp, (struct226 *)arg0, 0, 255, 1);
}

void func_15009AA0(s32 arg0, s32 arg1) {
    func_15162FAC(arg0, 1, 0, 2, 300, 0xD, 0xFF, 1);
}

void func_15009AEC(s32 arg0, s32 arg1) {
    func_15162740(arg0, 2, 6, 0, 300, 2, 0xFF, 1);
}

void func_15009B38(s32 arg0, s32 arg1) {
    func_15162740(arg0, 20, 6, 0, 300, 2, 0xFF, 1);
}

void func_15009B84(s32 arg0, s32 arg1) {
    func_15162740(arg0, 3, 6, 0, 300, 2, 0xFF, 1);
}

void func_15009BD0(s32 arg0, s32 arg1) {
    struct00 *temp_v0; // dummy
    struct221 tmp;

    tmp.unk4 = 0.0f;
    tmp.unk8 = 90.0f;
    tmp.unk0 = func_15187EC0(0, 0.0f, 0, 0, 0, 220, 220, 255);
    temp_v0 = func_1516387C(arg0, 2, 16, 300, 0, 12, 255, 1);
    if (temp_v0 != 0) {
        memcpy(&temp_v0->unk18, &tmp, 12);
    }
}

void func_15009C7C(s32 arg0, s32 arg1) {
    struct00 *temp_v0; // dummy
    struct221 tmp;

    tmp.unk4 = 0.0f;
    tmp.unk8 = 50.0f;
    tmp.unk0 = func_15187EC0(0, 0.0f, 0, 0, 0, 220, 220, 255);
    temp_v0 = func_1516387C(arg0, 2, 16, 300, 0, 12, 255, 1);
    if (temp_v0 != 0) {
        memcpy(&temp_v0->unk18, &tmp, 12);
    }
}

void func_15009D28(s32 arg0, s32 arg1) {
    func_15163604(arg0, 1, 5, 300, 0, 0, 255, 1);
}

void func_15009D6C(s32 arg0, s32 arg1) {
    func_15163604(arg0, 2, 5, 300, 0, 0, 255, 1);
}

void func_15009DB0(s32 arg0, s32 arg1) {
    func_15162740(arg0, 4, 6, 0, 300, 2, 255, 1);
}

void func_15009DFC(s32 arg0, s32 arg1) {
    func_15162740(arg0, 5, 6, 0, 300, 2, 255, 1);
}

void func_15009E48(s32 arg0, s32 arg1) {
    func_151615F8(arg0, 1, 1, 14, 255, 1);
}

void func_15009E84(s32 arg0, s32 arg1) {
    func_15163604(arg0, 3, 5, 300, 0, 0, 255, 1);
}

void func_15009EC8(s32 arg0, s32 arg1) {
    func_1516381C(arg0, 32, 255, 1);
}

void func_15009EF4(s32 arg0, s32 arg1) {
    func_151615F8(arg0, 1, 3, 35, 255, 1);
}

void func_15009F30(s32 arg0, s32 arg1) {
    func_15163604(arg0, 4, 36, 300, 0, 0, 255, 1);
}

void func_15009F74(s32 arg0, s32 arg1) {
    struct00 *temp_v0; // dummy
    struct221 tmp;

    tmp.unk4 = 0.0f;
    tmp.unk8 = 60.0f;
    tmp.unk0 = func_15187EC0(1, 0.1f, 100, 100, 100, 255, 100, 100);
    temp_v0 = func_1516387C(arg0, 2, 16, 300, 0, 12, 255, 1);
    if (temp_v0 != 0) {
        memcpy(&temp_v0->unk18, &tmp, 12);
    }
}

void func_1500A028(s32 arg0, s32 arg1) {
    func_15163604(arg0, 5, 5, 300, 0, 0, 255, 1);
}

void func_1500A06C(s32 arg0, s32 arg1) {
    func_15163604(arg0, 6, 5, 300, 0, 0, 255, 1);
}

void func_1500A0B0(s32 arg0, s32 arg1) {
    func_15162740(arg0, 7, 6, 0, 300, 2, 255, 1);
}

void func_1500A0FC(s32 arg0, s32 arg1) {
    func_15162740(arg0, 9, 6, 0, 300, 2, 255, 1);
}

void func_1500A148(s32 arg0, s32 arg1) {
    func_15162740(arg0, 10, 6, 0, 300, 2, 255, 1);
}

void func_1500A194(s32 arg0, s32 arg1) {
    func_15162740(arg0, 11, 38, 0, 300, 2, 255, 1);
}

void func_1500A1E0(s32 arg0, s32 arg1) {
    func_151615F8(arg0, 1, 4, 14, 255, 1);
}

void func_1500A21C(s32 arg0, s32 arg1) {
    func_15163604(arg0, 7, 5, 300, 0, 0, 255, 1);
}

void func_1500A260(s32 arg0, s32 arg1) {
    func_15162FAC(arg0, 2, 0, 2, 300, 13, 255, 1);
}

void func_1500A2AC(s32 arg0, s32 arg1) {
    u8 sp1C[4] = D_80095B70;

    func_151B8DB0(arg0, sp1C[arg1 - 0x33], 0xFF, 1);
}

void func_1500A2F4(s32 arg0, s32 arg1) {
    u8 sp1C[2] = D_80095B74;
    func_15164208(arg0, sp1C[arg1 - 0x38], 0xFF, 1);
}

void func_1500A33C(s32 arg0, s32 arg1) {
    func_15163604(arg0, 8, 5, 300, 0, 0, 255, 1);
}

void func_1500A380(s32 arg0, s32 arg1) {
    func_15163604(arg0, 9, 0x28, 300, 0, 0, 255, 1);
}

void func_1500A3C4(s32 arg0, s32 arg1) {
    func_15162740(arg0, 15, 6, 0, 300, 2, 255, 1);
}

void func_1500A410(s32 arg0, s32 arg1) {
    func_15163604(arg0, 10, 5, 300, 0, 0, 255, 1);
}

void func_1500A454(s32 arg0, s32 arg1) {
    func_151615F8(arg0, 0, 5, 14, 255, 1);
}

void func_1500A490(s32 arg0, s32 arg1) {
    func_15163604(arg0, 11, 5, 300, 0, 0, 255, 1);
}

void func_1500A4D4(s32 arg0, s32 arg1) {
    func_15163604(arg0, 12, 41, 300, 0, 0, 255, 1);
}

void func_1500A518(s32 arg0, s32 arg1) {
    func_15163604(arg0, 13, 41, 300, 0, 0, 255, 1);
}

void func_1500A55C(s32 arg0, s32 arg1) {
    func_151623F4(arg0, 1, 22, 0, -1, 300, 255, 1);
}

void func_1500A5A8(s32 arg0, s32 arg1) {
    func_15162740(arg0, 17, 6, 0, 300, 2, 255, 1);
}

void func_1500A5F4(s32 arg0, s32 arg1) {
    func_15162740(arg0, 18, 6, 0, 300, 2, 255, 1);
}

void func_1500A640(s32 arg0, s32 arg1) {
    func_15162740(arg0, 19, 6, 0, 300, 2, 255, 1);
}

void func_1500A68C(s32 arg0, s32 arg1) {
    func_15162740(arg0, 21, 6, 0, 300, 2, 255, 1);
}

/* Select the category-specific payload for commands 0x49..0x4B and spawn it. */
void func_1500A6D8(struct226 *actor, s32 command) {
    Header header;
    UnkB060C payload;
    s32 variant = 0;
    EffectSelectorTable36680 ids = D_80082BEC;
    struct225 *effect;

    if (D_800BE9F0 == 6) {
        variant = 1;
    } else {
        variant = 0;
    }
    if (func_150B060C(ids.values[variant][command - 0x49], &payload) != 0) {
        header.unk0 = 0;
        header.unk1 = 23;
        header.unk2 = 300;
        header.unk4 = 0;
        effect = func_1516037C(&header, actor, sizeof(payload), 255, 1);
        if (effect != NULL) {
            memcpy((u8 *)effect + 0x18, &payload, sizeof(payload));
        }
    }
}
void func_1500A79C(s32 arg0, s32 arg1) {
    func_15162740(arg0, 22, 6, 0, 300, 2, 255, 1);
}

/* Resolve commands 0x50..0x55's record and spawn its coordinate payload. */
void func_1500A7E8(struct226 *actor, s32 command) {
    Header header;
    UnkB060C payload;
    struct225 *effect;
    EffectPointIds36680 ids = D_80082BF4;

    payload.record = func_151149AC(ids.values[command - 0x50]);
    if (payload.record != NULL) {
        payload.unk0 = -400.0f;
        payload.unk4 = 4.0f;
        payload.unkC = (f32)*(s16 *)(payload.record + 0x10);
        payload.unk10 = (f32)*(s16 *)(payload.record + 0x12);
        payload.unk14 = (f32)*(s16 *)(payload.record + 0x14);
        header.unk0 = 0;
        header.unk1 = 23;
        header.unk2 = 300;
        header.unk4 = 0;
        effect = func_1516037C(&header, actor, sizeof(payload), 255, 1);
        if (effect != NULL) {
            memcpy((u8 *)effect + 0x18, &payload, sizeof(payload));
        }
    }
}
void func_1500A8C8(s32 arg0, s32 arg1) {
    func_151615F8(arg0, 0, 6, 0xE, 255, 1);
}

void func_1500A904(s32 arg0, s32 arg1) {
    u8 tmp = arg1 - 80;
    func_151615F8(arg0, 1, tmp, 0xE, 255, 1);
}

void func_1500A94C(s32 arg0, s32 arg1) {
    if ((arg1 > 0) && (arg1 < 89)) {
        if (D_80082BFC[arg1]) {
            D_80082BFC[arg1](arg0);
        }
    }
}

void func_1500A990(s32 arg0) {
    struct164 tmp;
    f32 phi_f18;
    struct164 *temp_v0;

    tmp.unk0 = 35.0f;
    tmp.unk4 = 35.0f;
    tmp.unk8 = 60.0f;
    tmp.unkC = 34.0f;
    tmp.unk10 = 30.0f;
    tmp.unk14 = 50.0f;

    phi_f18 = (u32)(osGetCount() * func_150ADA20()) & 0xFFFF;
    phi_f18 *= D_80095BB8;
    tmp.unk18 = (phi_f18 + phi_f18) * D_80095BBC;

    phi_f18 = (u32)(osGetCount() * func_150ADA20()) & 0xFFFF;
    phi_f18 *= D_80095BC0;
    tmp.unk1C = (phi_f18 + phi_f18) * D_80095BC4;

    phi_f18 = (u32)(osGetCount() * func_150ADA20()) & 0xFFFF;
    phi_f18 *= D_80095BC8;

    tmp.unk20 = (phi_f18 + phi_f18) * D_80095BCC;
    tmp.unk24 = D_80095BD0;
    tmp.unk28 = D_80095BD4;
    tmp.unk2C = D_80095BD8;

    temp_v0 = func_15149130(300, -1, 45, -1, 0, 0, 48, 255, 1);
    if (temp_v0 != NULL) {
        memcpy(&temp_v0->unk28, &tmp, 48);
    }
}

void func_1500AB5C(s32 arg0) {
    if ((arg0 > 0) && (arg0 < 6)) {
        if (D_80082D60[arg0] != 0) {
            D_80082D60[arg0]();
        }
    }
}

void func_1500ABA0(s32 arg0) {
    bzero(&D_800BE4A0, 60);
    func_1502B8E0(&D_800BE4A0, 60, 3, 12, arg0, 10);
    bzero(&D_800DDA90, 240);
    bzero(&D_800DD478, 1560);
}

/* Non-matching C placeholders for asm/nonmatchings/game_36680/func_1500AC14.s. */
s32 func_1500AC14() {
    return 0;
}
// GOTO hell
/* Non-matching C placeholders for asm/nonmatchings/game_36680/func_1500AD84.s. */
s32 func_1500AD84() {
    return 0;
}
/* Non-matching C placeholders for asm/nonmatchings/game_36680/func_1500AF08.s. */
s32 func_1500AF08() {
    return 0;
}
/* Non-matching C placeholders for asm/nonmatchings/game_36680/func_1500B1F4.s. */
s32 func_1500B1F4() {
    return 0;
}
/* Non-matching C placeholders for asm/nonmatchings/game_36680/func_1500B3B0.s. */
s32 func_1500B3B0() {
    return 0;
}
/* Non-matching C placeholders for asm/nonmatchings/game_36680/func_1500B714.s. */
s32 func_1500B714() {
    return 0;
}
/* Non-matching C placeholders for asm/nonmatchings/game_36680/func_1500B8F4.s. */
s32 func_1500B8F4() {
    return 0;
}
/* Non-matching C placeholders for asm/nonmatchings/game_36680/func_1500BAB8.s. */
s32 func_1500BAB8() {
    return 0;
}
/* Non-matching C placeholders for asm/nonmatchings/game_36680/func_1500BC7C.s. */
s32 func_1500BC7C() {
    return 0;
}

void func_1500BE40(s32 arg0) {
    D_800DDD10[0] = 0;
    D_800DDD10[1] = 0;
    D_800DDD0C = 110;
}

void func_1500BE68(void) {
    D_800DDD1C = 0;
    D_8008CEB0 = 0;
    D_800DDC04 = D_800DDC00 = D_800DDC08 = 0;
    D_800DDD20 = 0;
    func_1500BE40(0);
}


/* Non-matching C placeholders for asm/nonmatchings/game_36680/func_1500BEC0.s. */
s32 func_1500BEC0() {
    return 0;
}
