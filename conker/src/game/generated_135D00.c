#include <ultra64.h>
extern u8 D_800C35EA;
extern u8 *D_800C3958;
void func_15169260(void *, s32, s32, u8);
extern u8 D_80088C58[];
typedef struct { s32 a, b; } TwoWord135D00;
typedef struct { s32 a, b; u8 c; } EventPayload135D00;
extern s32 D_800BE9E4;
extern u8 D_80088C50[];

/* Non-matching placeholders for the text-only asm slice asm/135D00.s. */

s32 func_15108850() {
    return 0;
}

s32 func_15108AB4() {
    return 0;
}

void func_15108B80(u8 *arg0) {
    s32 end = 0x3E7;
    u8 *temp_v0 = arg0 + *(s32 *) (arg0 + 0x50) + 0xF8;

    if (end != *(s32 *) (temp_v0 + 0x14)) {
        s32 t = *(s32 *) (temp_v0 + 0x1C) - D_800BE9E4;

        *(s32 *) (temp_v0 + 0x1C) = t;
        if (t < 0) {
            *(s32 *) (temp_v0 + 0x14) = end;
        }
    }
}

void func_15108BC0(u8 *arg0) {
    u8 *sub = arg0 + *(s32 *) (arg0 + 0x50) + 0xF8;
    s32 index = *(s32 *) (sub + 0x14);

    if (index == 0x3E7) {
        *(f32 *) (sub + 0x10) = 226.0f;
    } else {
        if (D_800C35EA == 1) {
            *(f32 *) (sub + 0x10) = *(f32 *) (D_800C3958 + index * 0x44 + 4);
        } else {
            *(f32 *) (sub + 0x10) = 226.0f;
        }
    }
}

s32 func_15108C38() {
    return 0;
}

s32 func_15108D24() {
    return 0;
}

s32 func_15108E10() {
    return 0;
}

void func_15108FFC(s32 arg0, s32 arg1, u8 arg2) {
    EventPayload135D00 payload;
    TwoWord135D00 tmp = *(TwoWord135D00 *) D_80088C50;

    payload.a = arg0;
    payload.b = arg1;
    payload.c = arg2;
    func_15169260(&tmp, 2, (s32) &payload, 0x1D);
}

void func_15109064(u8 *arg0, u8 *arg1, u8 arg2) {
    u8 *sub = arg0 + *(s32 *) (arg0 + 0x50) + 0xF8;

    switch (arg2) {
        case 0x1D:
            *(s32 *) (sub + 0x14) = *(s32 *) arg1;
            sub[0x18] = arg1[8];
            *(s32 *) (sub + 0x1C) = *(s32 *) (arg1 + 4);
            break;
        case 0x1E:
            if (sub[0x20] != 0) {
                sub[0x20] = 0;
            } else {
                sub[0x20] = 1;
            }
            break;
    }
}

void func_151090DC(void) {
    TwoWord135D00 tmp = *(TwoWord135D00 *) D_80088C58;

    func_15169260(&tmp, 2, 0, 0x1E);
}

s32 func_15109120() {
    return 0;
}
