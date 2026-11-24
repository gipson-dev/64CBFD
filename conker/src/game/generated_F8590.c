#include <ultra64.h>
#include "variables.h"

typedef struct HeightResult71820 HeightResult71820;
typedef struct HeightActor71820 HeightActor71820;
extern f32 D_800A05E0[];
extern f32 D_800A05EC[];
void func_15143134(f32 *, f32 *, u8 *);
void func_1504715C(HeightResult71820 *, HeightActor71820 *);
s32 func_15046C80(f32 *, u16, f32, HeightResult71820 *);

/* Non-matching placeholders for the text-only asm slice asm/F8590.s. */

/* Transform the selected actor offset and optionally query its height interval. */
s32 func_150CB0E0(f32 *position, u8 *actor, HeightResult71820 *result, u8 mode) {
    f32 start[3];
    f32 *point;
    u8 *matrix;

    if (mode != 1 && mode != 2) {
        return 0;
    }
    if (mode == 1) {
        point = D_800A05EC;
    } else {
        point = D_800A05E0;
    }
    if (mode == 1) {
        matrix = *(u8 **)(actor + 0x1D4) + 0xA00;
    } else {
        matrix = *(u8 **)(actor + 0x1D4) + 0xBC0;
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

s32 func_150CB1E0(s32 arg0, s32 arg1) {
    return 0xB;
}

s32 func_150CB1F4() {
    return 0;
}

s32 func_150CB7CC(u8 *arg0) {
    s32 temp_v0 = *(s16 *)(arg0 + 0x1C);

    if (temp_v0 < 0x20) {
        s32 temp_v1 = temp_v0 << 3;
        if (temp_v1 < *(u8 *)(arg0 + 0x28)) {
            *(u8 *)(arg0 + 0x28) = temp_v1;
        }
    }
    return 1;
}

typedef struct {
    f32 field00,field04,sizeStart,sizeEnd;
    vertex rotation,scale,position,direction;
    f32 field40,field44,field48,field4C;
    u32 field50; s16 lifetime,field56;
    u8 field58,reserved59[3]; u32 field5C;
    u8 field60,field61,field62,field63,field64,field65,field66,field67,field68;
    u8 reserved69,field6A,reserved6B; u32 field6C;
    u8 field70,reserved71; s16 field72,field74; u8 reserved76[6];
} RadialSprite150CB800;
s32 func_150ADA20(void);
f32 func_150ADA68(void);
void func_15143794(s16,s16,f32,vertex *);
void *func_15132A4C(void *,s32,s32,s32,u8,s32);

extern f32 D_800A0604,D_800A0608,D_800A060C,D_800A0610;
extern f32 D_800A0618,D_800A061C,D_800A0614,D_800A0620;

/* Emit a rotating radial sprite with randomized velocity and lifetime. */
s32 func_150CB800(s32 source,s16 index,f32 x,f32 y,f32 z,
    f32 originX,f32 originY,f32 originZ,s16 angle,u8 start,f32 radius,
    s32 style,f32 extra,s32 context,u8 slot) {
    RadialSprite150CB800 packet;
    s16 pitch;
    f32 sample;
    s32 pitchDraw;
    packet.position.x = x;
    packet.position.y = y;
    packet.position.z = z;
    packet.scale.z = packet.scale.y = packet.scale.x = 1.0f;
    packet.field50 = 0x29E8;
    packet.rotation.z = packet.rotation.y = packet.rotation.x = 0.0f;
    packet.field44 = 0.0f;
    packet.field00 = 1.0f;
    packet.field56 = 32;
    packet.field04 = D_800A0604;
    pitchDraw = func_150ADA20();
    sample = func_150ADA68();
    pitch = (u32)pitchDraw % 36U - 55;
    func_15143794(angle,pitch,(sample * 200.0f + 200.0f) * D_800A0608,&packet.direction);
    packet.field40 = (func_150ADA68() * 300.0f + -149.0f) * D_800A060C;
    packet.field48 = (func_150ADA68() * 300.0f + -149.0f) * D_800A0610;
    packet.lifetime = (u32)func_150ADA20() % 33U + 32;
    packet.field4C = (func_150ADA68() * D_800A0614 + D_800A0618) * D_800A061C;
    sample = (func_150ADA68() * 300.0f + 101.0f) * D_800A0620;
    packet.sizeEnd = packet.sizeStart = sample;
    packet.field58 = 0;
    packet.field5C = 0;
    packet.field60 = (u32)func_150ADA20() % 101U + 155;
    packet.field61 = 2;
    packet.field62 = 0;
    packet.field63 = 0;
    packet.field64 = 0;
    packet.field65 = 0;
    packet.field66 = 0;
    packet.field67 = 0;
    packet.field68 = 0;
    packet.field6A = 2;
    packet.field6C = 0;
    packet.field70 = 0;
    packet.field72 = 32;
    packet.field74 = 7;
    func_15132A4C(&packet,3,255,0,slot,0);
    return 1;
}


s32 func_150CBA30(u8 *arg0) {
    s32 value;
    f32 delta;

    *(s16 *)(arg0 + 0x128) -= D_800BE9E4;
    if (*(s16 *)(arg0 + 0x128) > 0) {
        delta = *(f32 *)(arg0 + 0x12C) * D_800BE9A4;
        *(f32 *)(arg0 + 0x2C) += delta;
        *(f32 *)(arg0 + 0x30) += delta;
    }

    if ((*(u32 *)(arg0 + 0x58) & 1) != 0) {
        value = *(s16 *)(arg0 + 0x1C);
        if ((value < 0x20) && ((value << 3) < *(u8 *)(arg0 + 0x5C))) {
            *(u8 *)(arg0 + 0x5C) = value << 3;
        }
    }

    return 1;
}

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
} RadialParticle150CBABC;
s32 func_150ADA20(void);
f32 func_150ADA68(void);
void func_15143794(s16,s16,f32,vertex *);
void *func_15130374(void *,u8,s32,u8,s32);
void *memcpy(void *,const void *,unsigned int);

extern f32 D_800A0624,D_800A0628,D_800A062C,D_800A0630;

/* Emit a kind-0x29 radial particle and retain its damping payload on success. */
s32 func_150CBABC(s32 source,s16 index,f32 x,f32 y,f32 z,
    f32 originX,f32 originY,f32 originZ,s16 angle,u8 start,f32 radius,
    s32 style,f32 extra,s32 context,u8 slot) {
    RadialParticle150CBABC packet;
    s16 pitch;
    f32 damping;
    f32 sample;
    s32 pitchDraw;
    void *result;
    packet.kind = 0x29;
    packet.field08 = 0xE03;
    packet.field00 = 0x200005;
    packet.field04 = 0;
    packet.lifetime = (u32)func_150ADA20() % 41U + 40;
    packet.field0C = 0;
    packet.field10 = 0;
    packet.field18 = 0xB0;
    packet.field19 = 0xA0;
    packet.field1A = 0x2A;
    packet.field14 = 0x40;
    packet.field15 = 0x0B;
    packet.field16 = 0x6A;
    packet.field17 = 255;
    packet.field1B = (u32)func_150ADA20() % 157U + 100;
    packet.field1C = 255;
    packet.field60 = 3;
    packet.field61 = 3;
    sample = func_150ADA68();
    packet.sizeStart = packet.sizeEnd = sample * D_800A0624 + 300.0f;
    packet.position.x = x;
    packet.position.y = y;
    packet.position.z = z;
    pitchDraw = func_150ADA20();
    sample = func_150ADA68();
    pitch = (u32)pitchDraw % 26U - 25;
    func_15143794(angle,pitch,
        (sample * 500.0f + 1000.0f) * D_800A0628,&packet.direction);
    packet.field54 = 0.0f;
    packet.flags = 0xE05;
    if (func_150ADA20() & 1) packet.flags |= 0x40;
    if (func_150ADA20() & 1) packet.flags |= 0x80;
    packet.field62 = 7;
    packet.field63 = -1;
    packet.field1E = 25;
    packet.field20 = 10;
    packet.field22 = 60;
    packet.field24 = D_800A062C;
    damping = D_800A0630;
    result = func_15130374(&packet,1,4,slot,1);
    if (result != 0) memcpy((u8 *)result + 0xA8,&damping,4);
    return 1;
}



extern s32 D_800BE9E4;
typedef struct { u8 pad00[0x58]; f32 x, pad5C, z; u8 pad64[0x44]; f32 damping; } DampingState150CBCE0;
/* Apply one damping step for each elapsed tick. */
s32 func_150CBCE0(DampingState150CBCE0 *state, s32 unused) {
    u32 ticks;
    f32 *factor = &state->damping;
    for (ticks = (u32)D_800BE9E4; ticks != 0; ticks--) {
        state->x *= *factor;
        state->z *= *factor;
    }
    return 1;
}

/* Integrate position and angles, retaining the original single-precision grouping. */
s32 func_150CBE88(u8 *record) {
    f32 acceleration = *(f32 *)(record + 0x5C);
    f32 verticalVelocity = *(f32 *)(record + 0x48);
    *(f32 *)(record + 0x38) += *(f32 *)(record + 0x44) * D_800BE9A4;
    *(f32 *)(record + 0x3C) += verticalVelocity * D_800BE9A4
        + acceleration * D_800BE9A4 * D_800BE9A4 * 0.5f;
    *(f32 *)(record + 0x40) += *(f32 *)(record + 0x4C) * D_800BE9A4;
    {
        f32 delta = acceleration * D_800BE9A4;

        *(f32 *)(record + 0x48) = verticalVelocity + delta;
    }
    *(f32 *)(record + 0x20) += *(f32 *)(record + 0x50) * D_800BE9A4;
    *(f32 *)(record + 0x24) += *(f32 *)(record + 0x54) * D_800BE9A4;
    *(f32 *)(record + 0x28) += *(f32 *)(record + 0x58) * D_800BE9A4;
    return 1;
}

void func_150CBF5C(u8 *arg0) {
    *(u32 *)(arg0 + 0x58) |= 1;
    *(s16 *)(arg0 + 0x1C) = 0x20;
}
