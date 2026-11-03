#include <ultra64.h>

typedef struct HeightResult71820 HeightResult71820;
typedef struct HeightActor71820 HeightActor71820;
extern f32 D_800AA0F0[];
extern f32 D_800AA0FC[];
void func_15143134(f32 *, f32 *, u8 *);
void func_1504715C(HeightResult71820 *, HeightActor71820 *);
s32 func_15046C80(f32 *, u16, f32, HeightResult71820 *);

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

/* Transform the selected actor offset and optionally query its height interval. */
s32 func_151AF5C0(f32 *position, u8 *actor, HeightResult71820 *result, u8 mode) {
    f32 start[3];
    f32 *point;
    u8 *matrix;

    if (mode != 1 && mode != 2) {
        return 0;
    }
    if (mode == 1) {
        point = D_800AA0FC;
    } else {
        point = D_800AA0F0;
    }
    if (mode == 1) {
        matrix = *(u8 **)(actor + 0x1D4) + 0x800;
    } else {
        matrix = *(u8 **)(actor + 0x1D4) + 0x640;
    }
    func_15143134(point, position, matrix);
    if (result == NULL) {
        return 1;
    }
    start[0] = position[0];
    start[1] = position[1] + 100.0f;
    start[2] = position[2];
    func_1504715C(result, (HeightActor71820 *)actor);
    return func_15046C80(start, 0, position[1] - 500.0f, result);
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
