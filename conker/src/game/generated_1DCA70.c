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

typedef struct { f32 x, y, z; } EffectPoint151AFC88;
typedef struct RadialPacket151AFC88 {
    u32 field00, field04;
    s16 field08, field0A;
    u32 field0C, field10;
    u8 field14, field15, field16, field17;
    u8 field18, field19, field1A, field1B;
    u8 field1C, field1D;
    s16 field1E, field20, field22;
    f32 field24, field28, field2C;
    f32 position[3];
    f32 field3C, field40, field44;
    EffectPoint151AFC88 direction;
    f32 field54;
    u32 flags;
    u8 reserved5C[4];
    u8 field60, field61, field62;
    s8 field63;
    u8 reserved64[16];
} RadialPacket151AFC88;
extern f32 D_800AA110, D_800AA114, D_800AA118, D_800AA11C;
void func_15143794(s16, s16, f32, EffectPoint151AFC88 *);
void *func_15130374(void *, u8, s32, u8, s32);
void *memcpy(void *, const void *, size_t);
s32 func_150ADA20(void);
f32 func_150ADA68(void);

/* Submit the randomized radial descriptor and retain its damping value. */
s32 func_151AFC88(s32 kind, s16 index, f32 x, f32 y, f32 z,
                    f32 unused5, f32 unused6, f32 unused7, s16 heading, u8 unused9,
                    f32 unused10, s32 unused11, f32 unused12, s32 unused13, u8 slot) {
    RadialPacket151AFC88 packet;
    f32 sample;
    f32 bonus;
    void *allocated;
    u32 random;
    packet.field1D = 41;
    packet.field08 = 0xE03;
    packet.field00 = 0x200005;
    packet.field04 = 0;
    packet.field0A = ((u32)func_150ADA20() & 15) + 25;
    packet.field0C = 0;
    packet.field10 = 0;
    packet.field18 = 176;
    packet.field19 = 160;
    packet.field1A = 42;
    packet.field14 = 64;
    packet.field15 = 11;
    packet.field16 = 106;
    packet.field17 = 255;
    packet.field1B = (u32)func_150ADA20() % 156U + 100;
    packet.field1C = 255;
    packet.field60 = 3;
    packet.field61 = 3;
    sample = func_150ADA68();
    packet.position[0] = x;
    packet.position[1] = y;
    packet.position[2] = z;
    packet.field28 = packet.field2C = sample * 202.0f + 101.0f;
    random = func_150ADA20();
    sample = func_150ADA68();
    func_15143794(heading, (s16)(random % 21U - 20), (sample * D_800AA110 + 500.0f) * D_800AA114, &packet.direction);
    packet.flags = 0xE05;
    packet.field54 = 0.0f;
    if (func_150ADA20() & 1) packet.flags |= 0x40;
    if (func_150ADA20() & 1) packet.flags |= 0x80;
    packet.field62 = 6;
    packet.field63 = -1;
    packet.field1E = 15;
    packet.field20 = 17;
    packet.field22 = 25;
    packet.field24 = D_800AA118;
    bonus = D_800AA11C;
    allocated = func_15130374(&packet, 1, 4, slot, 1);
    if (allocated != NULL) memcpy((u8 *)allocated + 0xA8, &bonus, 4);
    return 1;
}

extern s32 D_800BE9E4;
typedef struct {
    u8 reserved00[0x58];
    f32 x;
    u8 reserved5C[4];
    f32 z;
    u8 reserved64[0x44];
    f32 damping;
} DampingState151AFEA4;

/* Damp both horizontal velocity components once per simulation tick. */
s32 func_151AFEA4(DampingState151AFEA4 *state, void *context) {
    f32 *factor = &state->damping;
    u32 ticks;

    for (ticks = (u32)D_800BE9E4; ticks != 0; ticks--) {
        state->x *= *factor;
        state->z *= *factor;
    }
    return 1;
}
