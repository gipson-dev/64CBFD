#include <ultra64.h>

extern f32 D_800BE9A4;
extern f32 D_800A2470, D_800A2474, D_800A2478, D_800A247C;
f32 func_15144B68(f32);
f32 sinf(f32);
void func_15108B80(u8 *);
void func_15108BC0(u8 *);

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

/* Advance the two phases and derive their sine-scaled offsets.
 * Refresh the owner timer and lookup value, then keep the callback active. */
s32 func_15108AB4(u8 *owner) {
    f32 *delta = &D_800BE9A4;
    f32 *state = (f32 *)(owner + *(s32 *)(owner + 0x50) + 0xF8);

    state[2] += D_800A2470 * *delta;
    state[3] += D_800A2474 * *delta;
    state[2] = func_15144B68(state[2]);
    state[3] = func_15144B68(state[3]);
    state[0] = sinf(state[2]) * D_800A2478;
    state[1] = sinf(state[3]) * D_800A247C;
    func_15108B80(owner);
    func_15108BC0(owner);
    return 1;
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

extern f32 D_800A2490;
extern u8 D_800BE9C0;
void func_150A8050(f32 matrix[4][4],f32 x,f32 y,f32 z);
/* Scale the owner's rotation matrix, retain its height and publish the active slot. */
s32 func_15108D24(u8 *owner, s32 view) {
    f32 matrix[4][4];
    u8 *state;
    state = owner + *(s32 *)(owner + 0x50) + 0xF8;
    func_150A8050(matrix, *(f32 *)state, 0.0f, *(f32 *)(state + 4));
    matrix[3][1] = *(f32 *)(state + 0x10);
    matrix[0][0] *= D_800A2490;
    matrix[0][1] *= D_800A2490;
    matrix[0][2] *= D_800A2490;
    matrix[1][0] *= D_800A2490;
    matrix[1][1] *= D_800A2490;
    matrix[1][2] *= D_800A2490;
    matrix[2][0] *= D_800A2490;
    matrix[2][1] *= D_800A2490;
    matrix[2][2] *= D_800A2490;
    guMtxF2L(matrix, (Mtx *)(owner + ((u32)D_800BE9C0 << 6) + 0x78));
    return 1;
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
