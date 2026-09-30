#include <ultra64.h>
extern u8 *D_800DBFF0;
extern f32 D_800A1980;
extern f32 D_800A1984;

void *func_15149130(s16 arg0, s8 arg1, s8 arg2, s8 arg3, u8 arg4,
                    u8 arg5, s32 arg6, u8 arg7, s32 arg8);

typedef struct {
    u8 *owner;
    u8 owner_id;
    u8 state;
    u8 pad6[2];
    f32 value;
    u8 mode;
    u8 padD[3];
} Generated11FF10Payload;

/* Non-matching placeholders for the text-only asm slice asm/11FF10.s. */

s32 func_150F2A60() {
    return 0;
}

void func_150F2C8C(u8 *arg0) {
    Generated11FF10Payload payload;
    u8 *object;

    payload.owner = arg0;
    payload.owner_id = arg0[0x3B];
    payload.state = 0;
    payload.value = 0.0f;
    payload.mode = 0;

    object = func_15149130(0x12C, -1, 0x5C, -1, 0, 0x44,
                           sizeof(payload), 0xFF, 1);
    if (object != NULL) {
        memcpy(object + 0x28, &payload, sizeof(payload));
    }
}

s32 func_150F2D14() {
    return 0;
}

void func_150F3194(u8 *arg0, s32 arg1, u8 arg2) {
    func_15169850(arg1, arg2, (s32) (arg0 + 0x28), (s32) (arg0 + 0x2C), (s32) arg0);
}

void func_150F31D4(u8 *arg0, s32 arg1, u8 arg2) {
    func_15169850(arg1, arg2, (s32) (arg0 + 0x110), (s32) (arg0 + 0x114), (s32) arg0);
}

s32 func_150F3214() {
    return 0;
}

void func_150F337C(u8 *arg0, s16 arg1) {
    func_15140410(arg0, arg0 + 0x12C, arg0 + 0x138, arg1);
}

// Matched with guarded set-bit temporary register normalization.
void func_150F33B0(u8 *arg0) {
    if (*(f32 *) (D_800DBFF0 + 0x300) < -2000.0f) {
        *(arg0 + 0x4F) &= 0xFFFE;
    } else {
        *(arg0 + 0x4F) |= 1;
    }
}

s32 func_150F33F8() {
    return 0;
}

f32 func_150F34A0(u8 *arg0, f32 arg1) {
    f32 result;

    if (arg1 < -5.0f) {
        result = arg1 * D_800A1980 + D_800A1984;
    } else {
        result = 0.75f;
    }
    return result;
}

s32 func_150F34F4() {
    return 0;
}

s32 func_150F43F0() {
    return 0;
}
