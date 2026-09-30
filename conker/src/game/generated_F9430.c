#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/F9430.s. */

typedef struct {
    s16 threshold;
    u8 pad2[2];
    f32 rate;
} GeneratedF9430MotionRecord;

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
    GeneratedF9430MotionRecord motion;
} GeneratedF9430MotionObject;

extern f32 D_800BE9A4;

s32 func_150CBF80() {
    return 0;
}

/* Note 527: flag-gated motion threshold and paired accumulator update. */
s32 func_150CC638(GeneratedF9430MotionObject *arg0) {
    s32 scaled;
    s32 value;
    f32 delta;

    if (arg0->flags & 1) {
        GeneratedF9430MotionRecord *record;

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

s32 func_150CC6B8() {
    return 0;
}

s32 func_150CC8D4() {
    return 0;
}

s32 func_150CCA7C() {
    return 0;
}

s32 func_150CCCB4() {
    return 0;
}
