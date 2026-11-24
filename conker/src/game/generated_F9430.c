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

#include "structs.h"

typedef struct {
    u32 field00,field04; u16 field08; s16 lifetime;
    u32 field0C,field10;
    u8 field14,field15,field16,field17;
    u8 field18,field19,field1A,field1B;
    u8 field1C,kind; s16 field1E,field20,field22;
    f32 field24,sizeStart,sizeEnd;
    vertex position;
    f32 field3C,field40,field44;
    vertex direction;
    f32 field54; u32 flags;
    u8 reserved5C[4]; u8 field60,field61; s8 field62,field63;
    u8 reserved64[12];
} RadialParticle150CC6B8;
s32 func_150ADA20(void);
f32 func_150ADA68(void);
void func_15143794(s16,s16,f32,vertex *);
void *func_15130374(void *,u8,s32,u8,s32);
void *memcpy(void *,const void *,unsigned int);

extern f32 D_800A06CC,D_800A06D0,D_800A06D4,D_800A06D8;

/* Emit a kind-0x29 radial particle and retain its damping payload on success. */
s32 func_150CC6B8(s32 source,s16 index,f32 x,f32 y,f32 z,
    f32 originX,f32 originY,f32 originZ,s16 angle,u8 start,f32 radius,
    s32 style,f32 extra,s32 context,u8 slot) {
    RadialParticle150CC6B8 packet;
    s16 pitch;
    f32 damping;
    f32 sample;
    s32 pitchDraw;
    void *result;
    packet.kind = 0x29;
    packet.field08 = 0xE03;
    packet.field00 = 0x200005;
    packet.field04 = 0;
    packet.lifetime = (u32)func_150ADA20() % 16U + 20;
    packet.field0C = 0;
    packet.field10 = 0;
    packet.field18 = 0xB0;
    packet.field19 = 0xA0;
    packet.field1A = 0x2A;
    packet.field14 = 0x40;
    packet.field15 = 0x0B;
    packet.field16 = 0x6A;
    packet.field17 = 255;
    packet.field1B = (u32)func_150ADA20() % 156U + 100;
    packet.field1C = 255;
    packet.field60 = 3;
    packet.field61 = 3;
    sample = func_150ADA68();
    packet.sizeStart = packet.sizeEnd = sample * D_800A06CC + 300.0f;
    packet.position.x = x;
    packet.position.y = y;
    packet.position.z = z;
    pitchDraw = func_150ADA20();
    sample = func_150ADA68();
    pitch = (u32)pitchDraw % 21U - 25;
    func_15143794(angle,pitch,
        (sample * 200.0f + 350.0f) * D_800A06D0,&packet.direction);
    packet.field54 = 0.0f;
    packet.flags = 0xE05;
    if (func_150ADA20() & 1) packet.flags |= 0x40;
    if (func_150ADA20() & 1) packet.flags |= 0x80;
    packet.field62 = 8;
    packet.field63 = -1;
    packet.field1E = 10;
    packet.field20 = 25;
    packet.field22 = 27;
    packet.field24 = D_800A06D4;
    damping = D_800A06D8;
    result = func_15130374(&packet,1,4,slot,1);
    if (result != 0) memcpy((u8 *)result + 0xA8,&damping,4);
    return 1;
}



extern s32 D_800BE9E4;
typedef struct { u8 pad00[0x58]; f32 x, pad5C, z; u8 pad64[0x44]; f32 damping; } DampingState150CC8D4;
/* Apply one damping step for each elapsed tick. */
s32 func_150CC8D4(DampingState150CC8D4 *state, s32 unused) {
    u32 ticks;
    f32 *factor = &state->damping;
    for (ticks = (u32)D_800BE9E4; ticks != 0; ticks--) {
        state->x *= *factor;
        state->z *= *factor;
    }
    return 1;
}

s32 func_150CCA7C() {
    return 0;
}

typedef struct {
    u8 pad0[0x20];
    f32 rotation[3];
    u8 pad2C[0xC];
    f32 position[3];
    f32 velocity[3];
    f32 angularVelocity[3];
    f32 verticalAcceleration;
} GeneratedF9430KinematicObject;

/* Advance position and rotation, including vertical acceleration over the timestep. */
s32 func_150CCCB4(GeneratedF9430KinematicObject *object) {
    object->position[0] += object->velocity[0] * D_800BE9A4;
    object->position[1] += object->velocity[1] * D_800BE9A4 +
        object->verticalAcceleration * D_800BE9A4 * D_800BE9A4 * 0.5f;
    object->position[2] += object->velocity[2] * D_800BE9A4;
    object->velocity[1] += object->verticalAcceleration * D_800BE9A4;
    object->rotation[0] += object->angularVelocity[0] * D_800BE9A4;
    object->rotation[1] += object->angularVelocity[1] * D_800BE9A4;
    object->rotation[2] += object->angularVelocity[2] * D_800BE9A4;
    return 1;
}
