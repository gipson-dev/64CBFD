#include <ultra64.h>
extern f32 D_800BE9A4;


/* Non-matching placeholders for the text-only asm slice asm/F5800.s. */

s32 func_150C8350() {
    return 0;
}

s32 func_150C84F4() {
    return 0;
}

s32 func_150C851C() {
    return 0;
}

s32 func_150C8600() {
    return 0;
}

s32 func_150C8730() {
    return 0;
}

s32 func_150C88D0() {
    return 0;
}

s32 func_150C8A68() {
    return 0;
}

s32 func_150C8DB8() {
    return 0;
}

s32 func_150C99B4() {
    return 0;
}

s32 func_150C9BDC() {
    return 0;
}

s32 func_150C9DC4() {
    return 0;
}

/* Integrate position and angles, retaining the original single-precision grouping. */
s32 func_150CA07C(u8 *record) {
    f32 acceleration = *(f32 *)(record + 0x5C);
    f32 verticalVelocity = *(f32 *)(record + 0x48);
    *(f32 *)(record + 0x38) += *(f32 *)(record + 0x44) * D_800BE9A4;
    *(f32 *)(record + 0x3C) += verticalVelocity * D_800BE9A4
        + acceleration * D_800BE9A4 * D_800BE9A4 * 0.5f;
    *(f32 *)(record + 0x40) += *(f32 *)(record + 0x4C) * D_800BE9A4;
    { f32 delta = acceleration * D_800BE9A4;
    *(f32 *)(record + 0x48) = verticalVelocity + delta; }
    *(f32 *)(record + 0x20) += *(f32 *)(record + 0x50) * D_800BE9A4;
    *(f32 *)(record + 0x24) += *(f32 *)(record + 0x54) * D_800BE9A4;
    *(f32 *)(record + 0x28) += *(f32 *)(record + 0x58) * D_800BE9A4;
    return 1;
}

s32 func_150CA150() {
    return 0;
}

#include "structs.h"
s32 func_150ADA20(void);
f32 func_150ADA68(void);
void func_1514C678(f32, f32, f32, f32, s16, s16, s16, u8, s32, f32, void *, u8);

/* Submit a randomized type-19 burst at the point after both RNG calls. */
void func_150CA930(struct17 *point) {
    s16 count = (u32)func_150ADA20() % 21U + 10;
    f32 scale = func_150ADA68() * 59.0f + 170.0f;

    func_1514C678(point->unk0, point->unk4, point->unk8, scale,
        0, 255, count, 0x13, 0, 0.0f, 0, 255);
}

s32 func_150CA9D0(u8 *arg0) {
    s32 temp_v0 = *(s16 *)(arg0 + 0x1C);

    if (temp_v0 < 0x20) {
        s32 temp_v1 = temp_v0 << 3;
        if (temp_v1 < *(u8 *)(arg0 + 0x28)) {
            *(u8 *)(arg0 + 0x28) = temp_v1;
        }
    }
    return 1;
}

s32 func_150CAA04() {
    return 0;
}

s32 func_150CAC28() {
    return 0;
}

s32 func_150CADD0() {
    return 0;
}

s32 func_150CB008() {
    return 0;
}
