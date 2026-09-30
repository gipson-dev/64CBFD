#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/1DCA70.s. */

extern f32 D_800BE9A4;

typedef struct {
    s16 threshold;
    u8 pad2[2];
    f32 rate;
} Generated1DCA70MotionRecord;

typedef struct {
    u8 pad0[0x1C];
    s16 value;
    u8 pad1E[0xE];
    f32 accumulator0;
    f32 accumulator1;
    u8 pad34[0x24];
    s32 flags;
    u8 limit;
    u8 pad5D[0xCB];
    Generated1DCA70MotionRecord motion;
} Generated1DCA70MotionObject;

s32 func_151AF5C0() {
    return 0;
}

s32 func_151AF6C0(s32 arg0, s32 arg1) {
    return 0xC;
}

s32 func_151AF6D4() {
    return 0;
}

s32 func_151AFBD4(u8 *arg0) {
    s32 temp_v0 = *(s16 *)(arg0 + 0x1C);

    if (temp_v0 < 0x20) {
        s32 temp_v1 = temp_v0 << 3;
        if (temp_v1 < *(u8 *)(arg0 + 0x28)) {
            *(u8 *)(arg0 + 0x28) = temp_v1;
        }
    }
    return 1;
}

/* Note 536: flag-gated motion threshold and paired accumulator update. */
s32 func_151AFC08(Generated1DCA70MotionObject *arg0) {
    s32 scaled;
    s32 value;
    f32 delta;

    if (arg0->flags & 1) {
        Generated1DCA70MotionRecord *record;

        value = arg0->value;
        if (value < 0x20) {
            scaled = value << 3;
            if (scaled < arg0->limit) {
                arg0->limit = scaled;
                value = arg0->value;
            }
        }

        record = &arg0->motion;
        if (record->threshold < value) {
            delta = record->rate * D_800BE9A4;
            arg0->accumulator0 += delta;
            arg0->accumulator1 += delta;
        }
    }
    return 1;
}

s32 func_151AFC88() {
    return 0;
}

s32 func_151AFEA4() {
    return 0;
}
