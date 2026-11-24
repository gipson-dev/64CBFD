#include <ultra64.h>
#include <string.h>

#include "functions.h"
#include "variables.h"

typedef struct PacketEF410 {
    f32 *x;
    f32 *y;
    f32 *z;
    f32 parameter0;
    f32 parameter1;
    s16 delta;
    u8 flags;
    u8 byte17;
    u8 byte18;
    s8 sentinel;
} PacketEF410;

extern f32 D_800A0280;
extern f32 D_800A0284;
extern f32 D_800A0268;
extern f32 D_800A026C;
typedef struct {
    s16 kind;
    s16 mode;
    s16 offset;
    s16 eventCode;
} EffectBandDescriptor150C2700;

typedef struct {
    f32 x;
    f32 y;
    f32 z;
    s16 type;
    s16 variant;
    f32 width;
    f32 height;
    s16 lifetime;
    s16 zero;
    f32 parameter0;
    f32 parameter1;
    u8 opacity;
    u8 scale;
    u8 reserved26[2];
    f32 parameter2;
    f32 velocity;
    u8 active;
    u8 classId;
    u8 reserved32[2];
    f32 acceleration;
    u8 loop;
    u8 reserved39[3];
    f32 phase;
} EffectBandPayload150C2700;

typedef struct {
    EffectBandDescriptor150C2700 descriptor;
    EffectBandPayload150C2700 payload;
} EffectBandLocals150C2700;

extern f32 D_800A0274;
extern f32 D_800A0278;
extern f32 D_800A027C;
void func_15150178(void *, void *, s32, u8, s32);

void func_1514C470(f32, f32, f32, f32, f32, f32, f32, s32, s32, f32, void *, u8);
f32 *func_15144B34(s32);
void *func_15134908(void *arg0, s32 arg1, u8 arg2, s32 arg3);

void *func_151D9014(void *, f32 *, u8, f32, s16, u8, f32, u8,
                    f32, f32, u8, s32, u8, u8, u8, s32);

typedef struct {
    f32 x, y, z;
    f32 size0, delta0, size1, delta1, delta2;
    s16 code0, code1, duration;
    u8 firstColor[3], alpha;
    u16 flags2A;
    u8 secondColor[3], enabled;
    s32 zero30;
    u8 kind34;
    u8 reserved35[3];
    f32 zero38, value3C, value40, value44;
} RadialEffectPacket150C29F0;

extern f32 D_800A02A0, D_800A02A4, D_800A02A8, D_800A02AC;
extern f32 D_800A02B0, D_800A02B4, D_800A02B8, D_800A02BC;
void *func_15149550(RadialEffectPacket150C29F0 *, u8, u8, s32, u8, s32);

void func_1514373C(f32, f32, f32 *, f32 *);

extern f32 D_800A0320, D_800A0324, D_800A0328;
extern f32 D_800A032C, D_800A0330;
void func_1505A250(f32, f32, f32, f32 *, f32 *);
void func_1505A3A8(f32, void *, f32, f32, u8);
void func_15056B08(void *);
void func_150562FC(void *);
void func_150599C8(void *, s32, u16);
void func_1001091C(struct127 *, s32);
f32 sqrtf(f32);

extern f32 D_800A0334;
void func_151B9BF0(s32, s32, s16, s16, s16, s16, s16, s16,
                   s16, s16, s16, s16, s16, u32, u8, s32);
void func_15188810(u8 *, s32, s32);
void func_150C1660(f32, f32, f32, u8);
void func_1506AC8C(void *, s32, s32);

extern f32 D_800A0338;
s32 func_151EF040(s32, s32);
void func_15171200(s32, s32, f32, f32, f32, f32, f32, f32,
                   f32, s32, s32, f32, u8, s32);
/* The current spray implementation accepts full-width coordinate words. */
void func_151709B4(s32, s32, s32, s32, f32, u8, s32);
void func_1516D99C(
    s16, s16, s16, u8, u8, u8, u8, u8, u8, u8, u8, u8, u8,
    u8, u8, u8, u8, u8, u8, u8, u8, u8, u8, u8, u8, u8, u8,
    s16, s16, s16, s16, u16, u8, u8, u8, u8, s16, u16, u16,
    u8, u8, u8, u8, u8, s32, u8, u8, s32, s32);
struct225 *func_151602C0(Header *, Header2 *, s32, s32, s32, s32,
                         u8, u8, s32, u8, s32);

typedef struct {
    f32 x, y, z, field0C, field10, field14, field18, field1C, field20;
    s16 field24, field26, field28, field2A, field2C, field2E;
    s16 field30, field32, field34, field36;
    u8 field38, field39, field3A, reserved3B;
    u32 field3C, field40, field44, field48, field4C, field50;
    u8 field54, field55, field56, reserved57;
    u32 field58, field5C, field60, field64, field68;
    u32 field6C, field70, field74, field78;
    u8 field7C, field7D, reserved7E[2];
    s16 field80, field82;
    u32 retained84;
} FixedSpray150C2290;
extern f32 D_800A0258, D_800A025C, D_800A0260, D_800A0264;
extern f32 D_800A0270;
void func_15151A38(void *, u8, s32);

typedef struct { f32 x, y, z; } OpeningPointEF410;
typedef struct {
    OpeningPointEF410 position;
    f32 field0C, field10, field14, field18, field1C, field20;
    s16 field24, field26, field28, field2A, field2C, field2E;
    s16 field30, field32, field34, field36;
    u8 field38, field39, field3A, reserved3B;
    u32 field3C, field40, field44, field48, field4C, field50;
    u8 field54, field55, field56, reserved57;
    u32 field58, field5C, field60, field64, field68;
    u32 field6C, field70, field74, field78;
    u8 field7C, field7D, reserved7E[2];
    s16 field80, field82;
    u32 retained84;
} OpeningSprayEF410;
typedef struct {
    s16 angle0Base, angle0Range, angle1Base, angle1Range;
} OpeningBandHeaderEF410;
typedef struct {
    OpeningPointEF410 position;
    s16 countBase, countRange;
    f32 speedBase, speedRange;
    s16 lifeBase, lifeRange;
    f32 sizeBase, sizeRange;
    u8 opacityBase, opacityRange, reserved26[2];
    f32 extentBase, extentRange;
    u8 field30, kind, reserved32[2];
    f32 chance0;
    u8 field38, reserved39[3];
    f32 chance1;
} OpeningBandEF410;
typedef struct {
    OpeningBandHeaderEF410 header;
    OpeningBandEF410 band;
    OpeningSprayEF410 spray;
} OpeningLocalsEF410;
extern f32 D_800A0230, D_800A0234, D_800A0238, D_800A023C;
extern f32 D_800A0240, D_800A0244, D_800A0248, D_800A024C;
extern f32 D_800A0250, D_800A0254;

/* Generated placeholder declarations. */
void func_150C1F60(u8);
void func_150C2290(u8);
s32 func_150C2558(
        s32 unusedKind, s16 unusedIndex, f32 x, f32 y, f32 z,
        f32 unusedX, f32 unusedY, f32 unusedZ, u8 unusedAngle, u8 unusedStart,
        f32 unusedRadius, s32 unusedContext, f32 unusedParameter,
        s32 unusedFlags, u8 channel);
s32 func_150C2700(
        void *unusedOwner, s32 unusedEvent, f32 x, f32 y, f32 z,
        s32 unused5, s32 unused6, s32 unused7, s32 unused8, s32 unused9,
        s32 unused10, s32 unused11, s32 unused12, s32 unused13, u8 channel);
void func_150C2804(f32 *x, f32 *y, f32 *z, s16 delta, u8 channel, s32 context);
s32 func_150C308C(u8 *);
Gfx *func_150C3160(Gfx *, u8 *);
void func_150C3230();
void func_150C3D5C(u8 *);
/* End generated placeholder declarations. */

/* Submit two sprays, then a band using the second provider's live position. */
void func_150C1F60(u8 channel) {
    OpeningLocalsEF410 locals;

    locals.spray.position.x = D_800A0230;
    locals.spray.position.y = 40.0f;
    locals.spray.field24 = 12;
    locals.spray.field26 = 13;
    locals.spray.field28 = -160;
    locals.spray.field2C = -60;
    locals.spray.field2A = 69;
    locals.spray.field2E = 67;
    locals.spray.field30 = 3;
    locals.spray.field32 = 5;
    locals.spray.field34 = 50;
    locals.spray.field36 = 31;
    locals.spray.field38 = 11;
    locals.spray.field39 = 1;
    locals.spray.field3A = 40;
    locals.spray.field3C = 1;
    locals.spray.field40 = 4;
    locals.spray.field44 = 0;
    locals.spray.field48 = 0;
    locals.spray.field4C = 0;
    locals.spray.field50 = 0;
    locals.spray.field54 = 255;
    locals.spray.field55 = 255;
    locals.spray.field56 = 0;
    locals.spray.field58 = 3;
    locals.spray.field5C = 255;
    locals.spray.field60 = 0;
    locals.spray.field64 = 0x220005;
    locals.spray.field68 = 0x1D0600;
    locals.spray.field6C = 1;
    locals.spray.field70 = 59;
    locals.spray.field74 = 128;
    locals.spray.field78 = 32;
    locals.spray.field7C = 0;
    locals.spray.field7D = 7;
    locals.spray.field80 = 12;
    locals.spray.field82 = 21;
    locals.spray.position.z = D_800A0234;
    locals.spray.field1C = D_800A0238;
    locals.spray.field20 = D_800A023C;
    locals.spray.field0C = 9.0f;
    locals.spray.field10 = D_800A0240;
    locals.spray.field14 = D_800A0244;
    locals.spray.field18 = 0.5f;
    func_15151A38(&locals.spray, channel, 1);

    locals.spray.field24 = 2;
    locals.spray.field26 = 3;
    locals.spray.field28 = -108;
    locals.spray.field2C = -22;
    locals.spray.field2A = 21;
    locals.spray.field2E = 22;
    locals.spray.field30 = 7;
    locals.spray.field32 = 0;
    locals.spray.field34 = 48;
    locals.spray.field36 = 21;
    locals.spray.field1C = 100.0f;
    locals.spray.field20 = 57.5f;
    locals.spray.field0C = D_800A0248;
    locals.spray.field10 = 39.0f;
    locals.spray.field14 = D_800A024C;
    locals.spray.field18 = 1.0f;
    func_15151A38(&locals.spray, channel, 1);

    locals.band.position = locals.spray.position;
    locals.band.countBase = 25;
    locals.band.countRange = 18;
    locals.header.angle0Base = -159;
    locals.header.angle0Range = 68;
    locals.header.angle1Base = -52;
    locals.header.angle1Range = 38;
    locals.band.speedBase = 40.0f;
    locals.band.speedRange = 35.0f;
    locals.band.lifeBase = 25;
    locals.band.lifeRange = 25;
    locals.band.sizeBase = D_800A0250;
    locals.band.sizeRange = D_800A0254;
    locals.band.opacityBase = 155;
    locals.band.opacityRange = 100;
    locals.band.extentBase = 1152.0f;
    locals.band.extentRange = 848.0f;
    locals.band.field30 = 1;
    locals.band.kind = 6;
    locals.band.chance0 = 0.0f;
    locals.band.field38 = 1;
    locals.band.chance1 = 0.0f;
    func_15150178(&locals.header, &locals.band, 0, channel, 1);
}

/* Submit the fixed spray request. Retail leaves reserved bytes and retained84 unwritten. */
void func_150C2290(u8 channel) {
    FixedSpray150C2290 descriptor;

    descriptor.x = D_800A0258;
    descriptor.y = 40.0f;
    descriptor.field24 = 2;
    descriptor.field26 = 3;
    descriptor.field28 = -0x29;
    descriptor.field2C = -0x16;
    descriptor.field2A = 0x15;
    descriptor.field2E = 0x16;
    descriptor.field30 = 7;
    descriptor.field32 = 0;
    descriptor.field34 = 0x30;
    descriptor.field36 = 0x15;
    descriptor.field38 = 0xB;
    descriptor.field39 = 1;
    descriptor.field3A = 0x28;
    descriptor.field3C = 1;
    descriptor.field40 = 4;
    descriptor.field44 = 0;
    descriptor.field48 = 0;
    descriptor.field4C = 0;
    descriptor.field50 = 0;
    descriptor.field54 = 0xFF;
    descriptor.field55 = 0xFF;
    descriptor.field56 = 0;
    descriptor.field58 = 3;
    descriptor.field5C = 0xFF;
    descriptor.field60 = 0;
    descriptor.field64 = 0x220005;
    descriptor.field68 = 0x1D0600;
    descriptor.field6C = 1;
    descriptor.field70 = 0x3B;
    descriptor.field74 = 0x80;
    descriptor.field78 = 0x20;
    descriptor.field7C = 0;
    descriptor.field7D = 7;
    descriptor.field80 = 0xC;
    descriptor.field82 = 0x15;
    descriptor.z = D_800A025C;
    descriptor.field1C = 100.0f;
    descriptor.field20 = 57.5f;
    descriptor.field0C = D_800A0260;
    descriptor.field10 = 39.0f;
    descriptor.field14 = D_800A0264;
    descriptor.field18 = 1.0f;
    func_15151A38(&descriptor, channel, 1);
}

/* Emit both randomized effect bands used by event 0x2E. */
void func_150C2424(u8 channel) {
    func_1514C470(D_800A0268, -490.0f, -328.0f, D_800A0268,
                 -490.0f, 328.0f, func_150ADA68() * 8.0f + 8.0f,
                 1, 0, 0.0f, NULL, channel);
    func_1514C470(D_800A026C, -560.0f, -580.0f, 8117.0f,
                 -560.0f, -580.0f, func_150ADA68() * 3.0f + 4.0f,
                 3, 0, 0.0f, NULL, channel);
}
// NON-MATCHING: ported from ects_proto (ECTS ROM build), not yet byte-verified for us
s32 func_150C251C(struct202 *arg0) {
    u8 *p;
    s32 val;

    p = (u8 *) arg0->unk98;
    val = arg0->unk1C * 8;
    if (val >= 0x100) {
        val = 0xFF;
    }
    p[0x1B] = val;
    if ((u8) val < 0) {
        return 0;
    }
    return 1;
}
/* Submit the event spray with a randomized Z coordinate and derived angle. */
s32 func_150C2558(
        s32 unusedKind, s16 unusedIndex, f32 x, f32 y, f32 z,
        f32 unusedX, f32 unusedY, f32 unusedZ, u8 unusedAngle, u8 unusedStart,
        f32 unusedRadius, s32 unusedContext, f32 unusedParameter,
        s32 unusedFlags, u8 channel) {
    FixedSpray150C2290 descriptor;

    descriptor.x = x;
    descriptor.y = y;
    descriptor.z = z + 15.0f - func_150ADA68() * 30.0f;
    descriptor.field24 = 1;
    descriptor.field26 = 0;
    descriptor.field28 = (u32)(s32)(descriptor.z * D_800A0270) - 64u;
    descriptor.field2A = 9;
    descriptor.field2C = 0;
    descriptor.field2E = 0;
    descriptor.field30 = 3;
    descriptor.field32 = 3;
    descriptor.field34 = 40;
    descriptor.field36 = 21;
    descriptor.field38 = 11;
    descriptor.field39 = 1;
    descriptor.field3A = 40;
    descriptor.field3C = 1;
    descriptor.field40 = 4;
    descriptor.field44 = 0;
    descriptor.field48 = 0;
    descriptor.field4C = 0;
    descriptor.field50 = 0;
    descriptor.field54 = 255;
    descriptor.field55 = 255;
    descriptor.field56 = 0;
    descriptor.field58 = 3;
    descriptor.field5C = 255;
    descriptor.field60 = 0;
    descriptor.field64 = 0x220005;
    descriptor.field68 = 0x1D0600;
    descriptor.field6C = 1;
    descriptor.field70 = 59;
    descriptor.field74 = 128;
    descriptor.field78 = 32;
    descriptor.field7C = 0;
    descriptor.field7D = 7;
    descriptor.field80 = 12;
    descriptor.field82 = 21;
    descriptor.field1C = 200.0f;
    descriptor.field20 = 150.0f;
    descriptor.field0C = 22.0f;
    descriptor.field14 = 0.0f;
    descriptor.field18 = 0.0f;
    descriptor.field10 = 44.0f;
    func_15151A38(&descriptor, channel, 1);
    return 1;
}

/* Submit the fixed effect-band descriptor and caller position packet. */
s32 func_150C2700(
        void *unusedOwner, s32 unusedEvent, f32 x, f32 y, f32 z,
        s32 unused5, s32 unused6, s32 unused7, s32 unused8, s32 unused9,
        s32 unused10, s32 unused11, s32 unused12, s32 unused13, u8 channel) {
    EffectBandLocals150C2700 locals;

    locals.descriptor.kind = 0x6B;
    locals.descriptor.mode = 0x46;
    locals.descriptor.offset = -0x1F;
    locals.descriptor.eventCode = 0x2E;
    locals.payload.x = x;
    locals.payload.y = y;
    locals.payload.z = z;
    locals.payload.type = 6;
    locals.payload.variant = 5;
    locals.payload.width = 30.0f;
    locals.payload.height = 35.0f;
    locals.payload.lifetime = 100;
    locals.payload.zero = 0;
    locals.payload.parameter0 = D_800A0274;
    locals.payload.parameter1 = D_800A0278;
    locals.payload.opacity = 0x9B;
    locals.payload.scale = 100;
    locals.payload.parameter2 = D_800A027C;
    locals.payload.velocity = 0.0f;
    locals.payload.active = 1;
    locals.payload.classId = 6;
    locals.payload.acceleration = 0.0f;
    locals.payload.loop = 1;
    locals.payload.phase = 0.0f;
    func_15150178(&locals.descriptor, &locals.payload, 0, channel, 1);
    return 1;
}

/* Float-reference effect packet dispatch. */
void func_150C2804(f32 *x, f32 *y, f32 *z, s16 delta, u8 channel, s32 context) {
    PacketEF410 packet;

    packet.parameter0 = D_800A0280;
    packet.x = x;
    packet.y = y;
    packet.z = z;
    packet.parameter1 = D_800A0284;
    packet.delta = delta;
    packet.flags = 5;
    packet.byte17 = 6;
    packet.byte18 = 3;
    packet.sentinel = -1;
    func_15134908(&packet, 0, channel, context);
}
/* Emit a randomized effect opposite the incoming direction. */
void func_150C2898(f32 x, f32 y, f32 z, f32 dx, f32 dy, f32 dz, u8 *owner) {
    f32 position[3];
    f32 velocity[3];
    f32 speed, second;
    u32 secondValue, firstValue;
    f32 first;

    position[0] = x;
    position[1] = y;
    position[2] = z;
    speed = (func_150ADA68() * 112.0f + 247.0f) * D_800A0288;
    velocity[0] = -dx * speed;
    velocity[1] = -dy * speed;
    velocity[2] = -dz * speed;
    first = func_150ADA68();
    firstValue = func_150ADA20();
    secondValue = func_150ADA20();
    second = func_150ADA68();
    func_151D9014(position, velocity, 6,
        first * D_800A028C + D_800A0290,
        (firstValue & 15U) + 25, secondValue % 101U + 155,
        second * 119.0f + 129.0f, 0, 1.0f, 1.0f,
        1, 0, 1, 0, owner[0xC], owner[1]);
}
/* Submit a randomized radial effect and refresh the owner's timer. */
void func_150C29F0(u8 *volatile owner) {
    u8 *position;
    RadialEffectPacket150C29F0 packet;
    f32 firstScale, secondScale;
    u8 angle;
    f32 directionX, directionZ, radius;

    angle = func_150ADA20();
    directionX = func_151423D8((u8)(angle - 64));
    directionZ = func_151423D8(angle);
    radius = func_150ADA68();
    position = owner;
    radius = radius * *(f32 *)(position + 0x30);
    packet.code0 = 0x6231;
    packet.code1 = 0x1A4D;
    packet.firstColor[0] = 0;
    packet.firstColor[1] = 0;
    packet.firstColor[2] = 0;
    packet.alpha = 255;
    packet.secondColor[0] = 255;
    packet.secondColor[1] = 255;
    packet.zero30 = 0;
    packet.flags2A = 1;
    packet.secondColor[2] = 0;
    packet.enabled = 1;
    position += 0x28;
    packet.duration = (u32)func_150ADA20() % 201U + 100;
    packet.kind34 = 15;
    packet.zero38 = 0.0f;
    packet.value40 = D_800A02A0;
    packet.value44 = D_800A02A4;
    packet.x = *(f32 *)position + radius * directionX;
    packet.y = *(f32 *)(position + 12);
    packet.z = *(f32 *)(position + 4) + radius * directionZ;
    packet.value3C = D_800A02A8;
    firstScale = func_150ADA68();
    firstScale = firstScale * 0.5f + 1.0f;
    secondScale = func_150ADA68();
    secondScale = secondScale * 0.5f + 1.0f;
    packet.size0 = D_800A02AC * firstScale;
    packet.size1 = D_800A02B0 * firstScale;
    packet.delta0 = D_800A02B4 * secondScale;
    packet.delta1 = D_800A02B8 * secondScale;
    packet.delta2 = D_800A02BC * secondScale;
    position = owner;
    func_15149550(&packet, 10, 1, 0, position[0xC], position[1]);
    *(s16 *)(owner + 0xE) = (u32)func_150ADA20() % 51U + 25;
}
/* Consume motion-gated emission attempts and copy each successful heading. */
void func_150C2C00(u8 *owner) {
    f32 firstScale, secondScale;
    f32 *accumulator;
    RadialEffectPacket150C29F0 packet;
    f32 *motion;
    f32 heading;
    f32 angleLimit, headingBase, headingScale, effectScale;
    void *created;

    accumulator = (f32 *)(owner + 0x28);
    firstScale = func_150ADA68();
    *accumulator +=
        (((firstScale * 20.0f) * 9.99999972e-10f) * D_800BE9A4) * 36447764.0f;
    if (1.0f < *accumulator) {
        motion = func_15144B34(D_80082FA4);
        /* Reuse the draw scalars for the motion gate before their size values. */
        secondScale = motion[0];
        firstScale = motion[2];
        secondScale = secondScale * secondScale + firstScale * firstScale;
        if (2500000.0f < secondScale) {
            packet.y = -390.0f;
            packet.value40 = 0.0450000018f;
            packet.value44 = 0.699999988f;
            angleLimit = 0.400000006f;
            headingBase = 0.957203984f;
            headingScale = 5.86594248f;
            packet.value3C = 0.0f;
            packet.code0 = 0x6231;
            packet.code1 = 0x1A4D;
            packet.firstColor[0] = 0;
            packet.firstColor[1] = 0;
            packet.firstColor[2] = 0;
            packet.alpha = 255;
            packet.secondColor[1] = 255;
            packet.secondColor[2] = 20;
            packet.enabled = 1;
            /* This packet variant uses word 0x30 as mode four. */
            packet.zero30 = 4;
            packet.flags2A = 1;
            packet.kind34 = 25;
            effectScale = 0.00100000005f;
            do {
                heading = func_150ADA68();
                heading = heading * headingScale + headingBase;
                secondScale = func_150484A0(motion[0], motion[2]);
                secondScale = func_15144C8C(secondScale, heading);
                if (secondScale < angleLimit) {
                    secondScale = func_150ADA68();
                    func_1514373C(heading,
                        secondScale * 1278.0f + 3900.0f,
                        &packet.x, &packet.z);
                    firstScale = func_150ADA68();
                    firstScale = (firstScale * 1991.0f + 1985.0f) * effectScale;
                    secondScale = func_150ADA68();
                    packet.size0 = 22.6000004f * firstScale;
                    packet.size1 = 13.7860003f * firstScale;
                    secondScale = (secondScale * 1493.0f + 3000.0f) * effectScale;
                    packet.delta0 = 57.9690018f * secondScale;
                    packet.delta1 = 42.7140007f * secondScale;
                    packet.delta2 = 118.763f * secondScale;
                    packet.duration = (u32)func_150ADA20() % 151U + 50;
                    secondScale = func_150ADA68();
                    packet.zero38 = (secondScale * 500.0f) * effectScale;
                    packet.secondColor[0] = (u32)func_150ADA20() % 156U + 100;
                    created = func_15149550(&packet, 10, 1, 0, owner[0xC], owner[1]);
                    if (created != 0) {
                        memcpy((u8 *)created + 0x160, &heading, sizeof(heading));
                    }
                }
                *accumulator -= 1.0f;
            } while (1.0f < *accumulator);
        } else {
            do {
                *accumulator -= 1.0f;
            } while (1.0f < *accumulator);
        }
    }
}
/* Apply damping and vertical acceleration; report whether both extents remain valid. */
s32 func_150C2FCC(void *effect) {
    *(f32 *) ((char *) effect + 0x2C) -= *(f32 *) ((char *) effect + 0x2C) * *(f32 *) ((char *) effect + 0x150);
    *(f32 *) ((char *) effect + 0x30) -= *(f32 *) ((char *) effect + 0x30) * *(f32 *) ((char *) effect + 0x150);
    *(f32 *) ((char *) effect + 0x38) += *(f32 *) ((char *) effect + 0x50) * D_800BE9A4 + 0.5f * *(f32 *) ((char *) effect + 0x4C) * D_800BE9A4 * D_800BE9A4;
    *(f32 *) ((char *) effect + 0x50) += *(f32 *) ((char *) effect + 0x4C) * D_800BE9A4;
    if (*(f32 *) ((char *) effect + 0x2C) < 10.0f || *(f32 *) ((char *) effect + 0x30) < 10.0f) {
        return 0;
    }
    return 1;
}
/* Move an active actor to state five when either motion test succeeds. */
s32 func_150C308C(u8 *actor) {
    u8 stop = 0;
    f32 *motion;
    f32 x, z;

    if (*(s16 *)(actor + 0x1C) >= 6) {
        motion = func_15144B34(D_80082FA4);
        x = motion[0];
        z = motion[2];
        x = x * x + z * z;
        if (x < D_800A0310) {
            stop = 1;
        } else {
            x = func_150484A0(motion[0], motion[2]);
            x = func_15144C8C(x, *(f32 *)(actor + 0x160));
            if (D_800A0314 < x) {
                stop = 1;
            }
        }
    }
    if (stop != 0) {
        *(s16 *)(actor + 0x1C) = 5;
    }
    return 1;
}

/* Emit the special actor texture phase and retain the previous phase for wrapping. */
Gfx *func_150C3160(Gfx *commands, u8 *actor) {
    f32 ratio;
    s32 coordinate, previous;

    if (*(s32 *)(actor + 0x2E8) != 0) {
        ratio = (f32)*(s32 *)(actor + 0x2E4) / (f32)*(s32 *)(actor + 0x2E8);
    } else {
        ratio = 1.0f;
    }
    ratio = 1.0f - ratio;
    coordinate = (s32)(500.0f * ratio + 2.0f);
    previous = (s32)(2U - *(u32 *)(actor + 0x2EC));
    *(s32 *)(actor + 0x2EC) = coordinate / 3;
    while (previous < 0) {
        previous += 64;
    }
    gDPSetTileSize(commands++, 4, coordinate, previous, 0x1FE, 0x3E);
    return commands;
}
/* Original bomb animation, fuse and explosion lifecycle. */
#pragma GLOBAL_ASM("asm/nonmatchings/game_EF410/func_150C3230.s")
/* Update the state-24 actor's movement, facing, animation and loop sound. */
void func_150C3574(u8 *actor) {
    f32 deceleration = 0.25f;
    f32 animationScale = 0.5f;
    f32 speed;
    u16 heading;
    u16 currentHeading;
    s32 volume;

    actor[0x80] = 10;
    if (actor[4] == 0x25) {
        func_1505A250(0.0f, 0.0f, 0.15f,
                     (f32 *)(actor + 0x164), (f32 *)(actor + 0x168));
        deceleration = D_800A0320;
        if (actor[0x87] & 1) {
            *(s16 *)(actor + 0x224) = (s32)*(f32 *)(actor + 0x18);
        }
        *(s16 *)(actor + 0x160) = 0;
    }
    func_1505A3A8(0.0f, actor, 2.0f, deceleration, 0);
    *(f32 *)(actor + 0x24) = 3.0f;
    if (actor[4] == 0x10) {
        animationScale = 0.375f;
    }
    if (actor[4] == 0xAC) {
        animationScale = 1.5f;
    }
    animationScale *= 0.75f;
    func_15056B08(actor);
    if (actor[0x13D] != 0) {
        func_150562FC(actor);
    }
    func_15059140((struct127 *)actor);
    *(f32 *)(actor + 0xBC) =
        (*(f32 *)(actor + 0x14) - *(f32 *)(actor + 0x2C)) * D_800BE9A8;
    *(f32 *)(actor + 0x148) =
        (*(f32 *)(actor + 0x1C) - *(f32 *)(actor + 0x34)) * D_800BE9A8;
    speed = sqrtf(*(f32 *)(actor + 0x148) * *(f32 *)(actor + 0x148) +
                  *(f32 *)(actor + 0xBC) * *(f32 *)(actor + 0xBC));
    if ((speed + 4.0f) + (speed + 4.0f) < *(f32 *)(actor + 0x3C)) {
        *(f32 *)(actor + 0x3C) = speed + speed;
    }
    if (actor[0x87] == 4) {
        D_800D1580 = 0xFF020133;
        D_800D154C = D_800CC2D0;
        func_1506E8D8();
        D_800D154C = (struct127 *)actor;
        *(f32 *)(actor + 0x164) = *(f32 *)(actor + 0xBC);
        *(f32 *)(actor + 0x168) = *(f32 *)(actor + 0x148);
        *(f32 *)(actor + 0x3C) = 0.0f;
    }
    actor[0x87] <<= 1;
    if (0.5f < speed && actor[0x13D] == 0) {
        *(u16 *)(actor + 0x78) = func_1505A630(
            *(f32 *)(actor + 0x14) - *(f32 *)(actor + 0x2C),
            *(f32 *)(actor + 0x34) - *(f32 *)(actor + 0x1C), 0);
    }
    currentHeading = *(u16 *)(actor + 0x78);
    if ((*(u16 *)(actor + 0x7A) - currentHeading - 0x4000) & 0x8000) {
        heading = currentHeading;
    } else {
        heading = currentHeading ^ 0x8000;
    }
    func_150599C8(actor, 2, heading);
    if (30.0f < *(f32 *)(actor + 0x28)) {
        *(f32 *)(actor + 0x44) *= D_800A0324;
    } else {
        *(f32 *)(actor + 0x44) = speed + speed;
    }
    if (actor[0x13D] != 0) {
        *(f32 *)(actor + 0x44) = 0.0f;
    }
    func_15052490((struct127 *)actor, *(u16 *)(actor + 0x78),
                  *(f32 *)(actor + 0x44),
                  (2.0f - *(f32 *)(actor + 0x14C)) * animationScale);
    if (*(f32 *)(actor + 0x44) < D_800A0328) {
        func_100109D0((struct127 *)actor);
    } else if (func_100107F8((struct127 *)actor) == 0) {
        if (actor[4] == 0xAC) {
            D_800D1580 = 0x630;
        } else if (actor[4] == 0x25) {
            D_800D1580 = 0x67A;
        } else {
            D_800D1580 = 0x62A;
        }
        func_1506E5FC();
    } else {
        volume = (s32)(*(f32 *)(actor + 0x44) * D_800A032C);
        if (volume > 28000) {
            volume = 28000;
        }
        if (actor[4] == 0x25) {
            volume >>= 1;
        }
        func_1001091C((struct127 *)actor, volume);
    }
    if (*(f32 *)(actor + 0x44) < D_800A0330) {
        func_100109D0((struct127 *)actor);
    }
}
/* Advance the state-19/20 effect phase, motion and exit transition. */
void func_150C3994(u8 *actor) {
    if (*(s32 *)actor == 20) {
        if (*(s32 *)(actor + 0x2E4) == 0) {
            func_151B9BF0(47, 1,
                (s16)(s32)*(f32 *)(actor + 0x14),
                (s16)(s32)(*(f32 *)(actor + 0x18) + 30.0f),
                (s16)(s32)*(f32 *)(actor + 0x1C),
                2000, 1000, 400, 200, 3072, 3072, 1, 1, 0, 255, 0);
        } else {
            func_15188810(actor, 100, 0);
        }
    }
    if (*(f32 *)(actor + 0x20) < 0.0f &&
        20.0f < *(f32 *)(actor + 0x28) && actor[0x136] == 0 &&
        *(f32 *)(actor + 0x28) < -20.0f * *(f32 *)(actor + 0x20)) {
        func_10010630(0x92, (struct127 *)actor, 32000, 200, 2500);
        actor[0x136] = 1;
    }
    if (actor[0x83] == 0) {
        *(f32 *)(actor + 0x148) = 70.0f;
        if (*(s32 *)(actor + 0x2E4) == 0) {
            func_151B9BF0(47, 1,
                (s16)(s32)*(f32 *)(actor + 0x14),
                (s16)(s32)(*(f32 *)(actor + 0x18) + 30.0f),
                (s16)(s32)*(f32 *)(actor + 0x1C),
                2200, 1280, 800, 700, 3072, 3072, 20, 1, 0, 255, 0);
            func_150C1660(*(f32 *)(actor + 0x14),
                          *(f32 *)(actor + 0x18) + 30.0f,
                          *(f32 *)(actor + 0x1C), 255);
            func_1506AC8C(actor, 6, 0);
        } else {
            func_15188810(actor, 100, 0);
        }
        func_10010344(0x1A9, actor, 32767, 1000, 2000);
        *(f32 *)(actor + 0x114) = 500.0f;
        actor[0xD0] = 1;
        *(u32 *)(actor + 0xF8) |= 0x01008000;
    }
    actor[0x125] = 255;
    actor[0x83]++;
    if (actor[0x83] >= 11) {
        *(u32 *)(actor + 0xF8) &= 0xFFFF7FFF;
    }
    *(f32 *)(actor + 0x40) =
        (*(u16 *)(actor + 0x7A) + 16384) * 0.0054931640625f;
    func_15059140((struct127 *)actor);
    *(f32 *)(actor + 0xB8) += *(f32 *)(actor + 0x148);
    *(f32 *)(actor + 0x148) *= D_800A0334;
    if ((*(f32 *)(actor + 0x28) == 0.0f && actor[0x83] >= 21 &&
         *(s16 *)(actor + 0xCC) == 0) || actor[0x107] != 0 || actor[0x1CA] == 0) {
        func_150C3D5C(actor);
        func_10010630(0x93, (struct127 *)actor, 32000, 200, 2500);
        func_15060F28((struct127 *)actor, 1);
    }
}

s32 func_150C3D48(s32 arg0) {
    return arg0 + 0xEDCBA988;
}

/* Submit the actor's exit effects and preserve the retail cartridge check. */
void func_150C3D5C(u8 *actor) {
    s32 cartridgeWord;
    Header descriptor;
    Header2 position;
    s32 (*readWord)(s32, s32) = func_151EF040;

    func_151B9BF0(47, 1,
        (s16)(s32)*(f32 *)(actor + 0x14),
        (s16)(s32)*(f32 *)(actor + 0x18),
        (s16)(s32)*(f32 *)(actor + 0x1C),
        1400, 1280, 800, 1200, 512, 512, 30, 1, 0, 255, 0);

    cartridgeWord = 0xC23459B8;
    readWord(func_150C3D48(cartridgeWord), (s32)&cartridgeWord);
    if (cartridgeWord != 0x0330C820) {
        /* Retail disables this entrypoint when the cartridge word differs. */
        ((u32 *)&func_10004074)[0] = 0x03E00008;
        ((u32 *)&func_10004074)[1] = 0;
    }
    func_15171200(3, 203, *(f32 *)(actor + 0x14),
        *(f32 *)(actor + 0x18), *(f32 *)(actor + 0x1C),
        10.0f, 1.0f, 2.0f, 60.0f, 3, 60, D_800A0338, 255, 0);
    func_151709B4((s32)*(f32 *)(actor + 0x14),
        (s32)(*(f32 *)(actor + 0x18) + 20.0f),
        (s32)*(f32 *)(actor + 0x1C), 10, 2000.0f, 255, 0);
    func_1516D99C(
        (s16)(s32)*(f32 *)(actor + 0x14),
        (s16)(s32)*(f32 *)(actor + 0x18),
        (s16)(s32)*(f32 *)(actor + 0x1C),
        13, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 255, 0, 0, 0,
        20, 20, 2, 0, 0, 0, 0, 81, 81, 81, 81, 10, 1, 0, 255,
        10, 1400, 400, 1, 1, 0, 1, 0, 0, 0, 0, 0, 255, 0);
    descriptor.unk0 = 3;
    descriptor.unk1 = -1;
    descriptor.unk2 = (u32)func_150ADA20() % 11U + 10;
    descriptor.unk4 = 0;
    position.unk0 = (s32)*(f32 *)(actor + 0x14);
    position.unk4 = (s32)*(f32 *)(actor + 0x18);
    position.unk8 = (s32)*(f32 *)(actor + 0x1C);
    func_151602C0(&descriptor, &position, (u32)func_150ADA20() % 52U + 40,
                  255, 255, 90, 255, 0, 0, 255, 1);
}
