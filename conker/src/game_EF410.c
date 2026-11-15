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
void func_15150178(EffectBandDescriptor150C2700 *,
                   EffectBandPayload150C2700 *, s32, u8, s32);

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

/* Generated placeholder declarations. */
s32 func_150C1F60();
s32 func_150C2290();
s32 func_150C2558();
s32 func_150C2700(
        void *unusedOwner, s32 unusedEvent, f32 x, f32 y, f32 z,
        s32 unused5, s32 unused6, s32 unused7, s32 unused8, s32 unused9,
        s32 unused10, s32 unused11, s32 unused12, s32 unused13, u8 channel);
void func_150C2804(f32 *x, f32 *y, f32 *z, s16 delta, u8 channel, s32 context);
s32 func_150C308C(u8 *);
Gfx *func_150C3160(Gfx *, u8 *);
void func_150C3230();
s32 func_150C3D5C();
/* End generated placeholder declarations. */

/* Non-matching C placeholders for asm/nonmatchings/game_EF410/func_150C1F60.s. */
s32 func_150C1F60() {
    return 0;
}
/* Non-matching C placeholders for asm/nonmatchings/game_EF410/func_150C2290.s. */
s32 func_150C2290() {
    return 0;
}
// TODO: figure out this struct!
// void func_150C2290(s32 arg0) {
//     s16 sp9A;
//     s16 sp98;
//     s8 sp95;
//     s8 sp94;
//     ?32 sp90;
//     ?32 sp8C;
//     ?32 sp88;
//     ?32 sp84;
//     ?32 sp80;
//     ?32 sp7C;
//     ?32 sp78;
//     ?32 sp74;
//     ?32 sp70;
//     s8 sp6E;
//     s8 sp6D;
//     s8 sp6C;
//     ?32 sp68;
//     ?32 sp64;
//     ?32 sp60;
//     ?32 sp5C;
//     ?32 sp58;
//     ?32 sp54;
//     s8 sp52;
//     s8 sp51;
//     s8 sp50;
//     s16 sp4E;
//     s16 sp4C;
//     s16 sp4A;
//     s16 sp48;
//     s16 sp46;
//     s16 sp44;
//     s16 sp42;
//     s16 sp40;
//     s16 sp3E;
//     s16 sp3C;
//     f32 sp38;
//     f32 sp34;
//     f32 sp30;
//     f32 sp2C;
//     f32 sp28;
//     f32 sp24;
//     f32 sp20;
//     f32 sp1C;
//     f32 sp18;
//
//     sp18 = *(void *)0x800A0258;
//     sp1C = 40.0f;
//     sp3E = 3;
//     sp40 = -0x29;
//     sp44 = -0x16;
//     sp42 = 0x15;
//     sp46 = 0x16;
//     sp48 = 7;
//     sp4E = 0x15;
//     sp50 = 0xB;
//     sp20 = *(void *)0x800A025C;
//     sp3C = 2;
//     sp4C = 0x30;
//     sp52 = 0x28;
//     sp54 = 1;
//     sp58 = 4;
//     sp6C = 0xFF;
//     sp6D = 0xFF;
//     sp70 = 3;
//     sp4A = 0;
//     sp51 = 1;
//     sp5C = 0;
//     sp60 = 0;
//     sp64 = 0;
//     sp68 = 0;
//     sp6E = 0;
//     sp74 = 0xFF;
//     sp78 = 0;
//     sp7C = 0x220005;
//     sp80 = 0x1D0600;
//     sp84 = (?32) (u8)1;
//     sp88 = 0x3B;
//     sp8C = 0x80;
//     sp90 = 0x20;
//     sp94 = 0;
//     sp95 = 7;
//     sp98 = 0xC;
//     sp9A = 0x15;
//     sp34 = 100.0f;
//     sp38 = 57.5f;
//     sp24 = *(void *)0x800A0260;
//     sp28 = 39.0f;
//     sp2C = *(void *)0x800A0264;
//     sp30 = 1.0f;
//     func_15151A38(&sp18, arg0 & 0xFF, 1);
// }

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
/* Non-matching C placeholders for asm/nonmatchings/game_EF410/func_150C2558.s. */
s32 func_150C2558() {
    return 0;
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

/* Non-matching C placeholders for asm/nonmatchings/game_EF410/func_150C3D5C.s. */
s32 func_150C3D5C() {
    return 0;
}
