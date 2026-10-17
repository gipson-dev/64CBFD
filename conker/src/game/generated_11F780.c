#include <ultra64.h>
extern f32 D_800BE9A4;
f32 func_15144B68(f32);
#include "structs.h"

void func_151C329C(struct17 *arg0, s32 arg1, s32 arg2);
void func_150A8050(f32 mtx[4][4], f32 arg1, f32 arg2, f32 arg3);
extern u8 D_800BE9C0;
void func_150F2994(u8 *actor, s32 value);
s32 func_15123934(u8 *, s32, s32, s32, s32);
void func_15124B18(u8 *);
void func_15128774(u8 *, u8 *);
void func_151239CC(u8 *, s32);
s32 func_1509BE40(s32, s32, s32, s32);
void func_1509BFB0(s32, s32, s32);
extern u8 *D_800D2E4C;

void func_150A7960(f32 matrix[4][4], f32 x, f32 y, f32 z, f32 *outX, f32 *outY, f32 *outZ);

extern f32 D_800A1920[3];
void func_15143134(f32 *point, f32 *output, u8 *matrix);


/* Non-matching placeholders for the text-only asm slice asm/11F780.s. */

/* Transform the selector's indexed actor record into the output point. */
s32 func_150F22D0(struct17 *output, u8 *actor, u8 selector) {
    s32 index;

    switch (selector) {
        case 3: index = 0x29; break;
        case 4: index = 0x2D; break;
        case 5: index = 0x31; break;
        case 6: index = 0x35; break;
        case 7: index = 0x39; break;
        case 8: index = 0x3D; break;
        default: return 0;
    }
    func_15143134(D_800A1920, (f32 *)output,
                 *(u8 **)(actor + 0x1D4) + (index << 6));
    return 1;
}

s32 func_150F237C(s32 arg0, s32 arg1) {
    return 0xE;
}

void func_150F2390(u8 *arg0, s32 arg1, s32 arg2) {
    struct17 value;

    if (*(s32 *)(arg0 + 0x1D4) != 0) {
        func_150F22D0(&value, arg0, (u8)arg1);
        func_151C329C(&value, 0xFF, 0);
    }
}

/* Update actor offsets from fixed sine state, then advance both phases. */
s32 func_150F23E0(u8 *actor) {
    f32 *state = (f32 *)(actor + 0x170);

    *(f32 *)(actor + 0x20) = state[4] * sinf(state[0]);
    *(f32 *)(actor + 0x28) = state[5] * sinf(state[1]);
    state[0] = func_15144B68(state[2] * D_800BE9A4 + state[0]);
    state[1] = func_15144B68(state[3] * D_800BE9A4 + state[1]);
    return 1;
}

/* Update sine outputs, then advance and wrap both phases. */
s32 func_150F2480(u8 *actor) {
    f32 *state;

    state = (f32 *)(actor + *(s32 *)(actor + 0x50) + 0xF8);
    state[9] = state[4] * sinf(state[0]);
    state[10] = state[5] * sinf(state[1]);
    state[0] = func_15144B68(state[2] * D_800BE9A4 + state[0]);
    state[1] = func_15144B68(state[3] * D_800BE9A4 + state[1]);
    return 1;
}

s32 func_150F2518(u8 *arg0, s32 arg1) {
    f32 matrix[4][4];
    u8 *entry;

    entry = arg0 + *(s32 *)(arg0 + 0x50) + 0xF8;
    func_150A8050(matrix, *(f32 *)(entry + 0x24), 0.0f,
                   *(f32 *)(entry + 0x28));
    matrix[3][0] = *(f32 *)(entry + 0x18);
    matrix[3][1] = *(f32 *)(entry + 0x1C);
    matrix[3][2] = *(f32 *)(entry + 0x20);
    guMtxF2L(matrix, (Mtx *)(arg0 + (D_800BE9C0 << 6) + 0x78));
    return 1;
}

/* Transform the owner-relative point into the destination's signed halfwords. */
s32 func_150F25A0(u8 *record) {
    u8 **owner = (u8 **)(record + 0x18);
    f32 point[3];
    f32 matrix[4][4];

    func_150A8050(matrix, *(f32 *)(*owner + 0x20) * 3.0f, 0.0f,
                 *(f32 *)(*owner + 0x28) * 3.0f);
    matrix[3][0] = *(f32 *)(*owner + 0x38);
    matrix[3][1] = *(f32 *)(*owner + 0x3C);
    matrix[3][2] = *(f32 *)(*owner + 0x40);
    func_150A7960(matrix, 0.0f, -495.0f, 0.0f, &point[0], &point[1], &point[2]);
    *(s16 *)(*(u8 **)(record + 0x14) + 0x0E) = (s32)point[0];
    *(s16 *)(*(u8 **)(record + 0x14) + 0x10) = (s32)point[1];
    *(s16 *)(*(u8 **)(record + 0x14) + 0x12) = (s32)point[2];
    return 1;
}

/* Update actor movement state and refresh its event-controlled flags. */
void func_150F26A0(u8 *actor) {
    u8 *state = *(u8 **)(actor + 0x3D0);

    if (state[0x102] && !state[0x104]) {
        func_150F2994(actor, 1);
        if (*(s32 *)(actor + 0x2C) != 0x100 && !*(s32 *)(actor + 0x6C8)) {
            if (func_15123934(actor, 0x80, 0, 0, 3)) {
                *(u32 *)(actor + 0x84) |= 0x300400;
                *(u32 *)(actor + 0x84) &= ~6;
                *(s16 *)(actor + 0x1B4) = 1;
                *(s16 *)(actor + 0x1E0) = 3;
                func_15124B18(actor);
            }
            *(f32 *)(actor + 0x348) = 29.0f;
            *(f32 *)(actor + 0x34C) = 29.0f;
            *(f32 *)(actor + 0x374) = 200.0f;
            *(f32 *)(actor + 0x190) = -19.0f;
            if (!actor[0x3E8] && 0.5f * *(f32 *)(actor + 0x374) <
                    *(f32 *)(actor + 0x370) - *(f32 *)(actor + 0x374)) {
                func_15128774(actor, *(u8 **)(actor + 0x3D0));
            }
        }
    } else {
        state[7] = 0xFF;
        if (actor[0x23E] == 0x3B) {
            func_150F2994(actor, 1);
            if (*(s32 *)(actor + 0x2C) != 0x100 && !*(s32 *)(actor + 0x6C8)) {
                if (func_15123934(actor, 8, 0, 0, 3)) {
                    *(u32 *)(actor + 0x84) |= 0x300000;
                    *(u32 *)(actor + 0x84) &= ~4;
                    *(s16 *)(actor + 0x1B4) = 1;
                    *(s16 *)(actor + 0x1E0) = 3;
                }
                *(s32 *)(actor + 0x134) = 0;
                *(f32 *)(actor + 0x348) = 125.0f;
                *(f32 *)(actor + 0x34C) = 125.0f;
                *(f32 *)(actor + 0x374) = 220.0f;
                *(f32 *)(actor + 0x190) = 30.0f;
            }
        } else {
            if ((*(s32 *)(actor + 0x2C) == 8 || *(s32 *)(actor + 0x2C) == 0x80) &&
                    !*(s32 *)(actor + 0x6C8)) {
                func_151239CC(actor, 3);
            }
            if (*(s16 *)(actor + 0x1B4) == 1) {
                *(s16 *)(actor + 0x1B4) = 2;
                func_15124B18(actor);
            }
            func_150F2994(actor, 0);
        }
    }
    if (func_1509BE40(1, 0x405A, 6, 0x9000)) {
        *(u32 *)(actor + 0x84) |= 0x80000000;
    } else {
        *(u32 *)(actor + 0x84) &= 0x7FFFFFFF;
    }
    if (func_1509BE40(1, 0x405E, 6, 0x9000)) {
        *(u32 *)(actor + 0x84) |= 0x10000;
    } else {
        *(u32 *)(actor + 0x84) &= 0xFFFEFFFF;
    }
    if (func_1509BE40(1, 0x405F, 6, 0x2000)) {
        *(u32 *)(actor + 0x84) |= 0x10;
    } else {
        *(u32 *)(actor + 0x84) &= ~0x10;
    }
}

/* Apply the shared event value, including optional player-state events. */
void func_150F2994(u8 *actor, s32 value) {
    s32 i;

    for (i = 0; i < 14; i++) {
        func_1509BFB0(0, i + 0x4016, value);
    }
    func_1509BFB0(0, 0x405D, value);
    func_1509BFB0(0, 0x405F, value);
    if (D_800D2E4C[0x15] & 8) {
        func_1509BFB0(0, 0x4063, value);
        func_1509BFB0(0, 0x4064, value);
        func_1509BFB0(0, 0x4065, value);
    }
}
