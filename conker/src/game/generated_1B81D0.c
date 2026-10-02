#include <ultra64.h>
s32 func_1518B2A8(s32, f32, f32, s32, s32, s32, s32);

typedef struct {
    u8 pad0[0x3C];
    f32 unk3C;
    u8 pad40[0x24];
    s16 unk64;
    u8 pad66[0xA];
    s8 unk70;
    u8 pad71[0xFF];
    f32 unk170;
} Func1518B1D8Object;

/* Non-matching placeholders for the text-only asm slice asm/1B81D0.s. */

s32 func_1518AD20() {
    return 0;
}

s32 func_1518B1AC(u8 *arg0) {
    if (*(f32 *) (arg0 + 0x3C) < *(f32 *) (arg0 + 0x170)) {
        return 0;
    }
    return 1;
}

s32 func_1518B1D8(Func1518B1D8Object *arg0) {
    f32 delta = arg0->unk3C - arg0->unk170;
    s32 candidate;
    s32 delta_half;
    s32 selected;

    if (delta < 0.0f) {
        return 0;
    }

    candidate = arg0->unk64 << 2;
    if (candidate >= 0x100) {
        candidate = 0xFF;
    }

    delta_half = (s32) delta >> 1;
    selected = candidate;
    if (delta_half >= 0x100) {
        delta_half = 0xFF;
    }
    if (delta_half < candidate) {
        selected = delta_half;
    }

    if (selected < 0) {
        return 0;
    }
    arg0->unk70 = selected;
    return 1;
}

void func_1518B264(s32 arg0, f32 arg1, f32 arg2, s32 arg3, u8 arg4) {
    func_1518B2A8(arg0, arg1, arg2, arg3, 4, 0xFF, arg4);
}

s32 func_1518B2A8(s32 arg0, f32 arg1, f32 arg2, s32 arg3, s32 arg4, s32 arg5, s32 arg6) {
    return 0;
}
