#include <ultra64.h>

typedef struct RingColors19E040 {
    u8 values[3];
} RingColors19E040;
extern RingColors19E040 D_8008CC20;
f32 func_15048A40(u8 angle);
f32 func_150489B0(u8 angle);
s32 func_150ADA20(void);
void func_1516D4E8(
    s16 arg0, s16 arg1, s16 arg2, u8 arg3, u8 arg4, u8 arg5,
    u8 arg6, u8 arg7, u8 arg8, u8 arg9, u8 arg10, u8 arg11,
    u8 arg12, u8 arg13, u8 arg14, u8 arg15, u8 arg16, u8 arg17,
    u8 arg18, u8 arg19, u8 arg20, u8 arg21, u8 arg22, s16 arg23,
    s16 arg24, u8 arg25, s16 arg26, s32 arg27, s32 arg28, u8 arg29,
    s32 arg30);

typedef struct DebrisKinds19E040 {
    u8 values[6];
} DebrisKinds19E040;

typedef struct DebrisPacket19E040 {
    f32 position[3];
    f32 rotation[3];
    f32 velocity[3];
    f32 spin[3];
    f32 scale[3];
    s32 lifetime;
    s32 asset;
    u8 reserved44[4];
    f32 coefficient[3];
    u8 mode, alpha, zero56, zero57, zero58, duration, kind, variant;
    u8 control5C, control5D;
    u8 reserved5E[2];
} DebrisPacket19E040;

extern DebrisKinds19E040 D_800A6F80;
extern f32 D_800A6E90[18];
extern f32 D_800A6F88, D_800A6F8C, D_800A6F90, D_800A6F94;
s32 func_1518C900(s32 kind);
f32 fabsf(f32 value);
#pragma intrinsic (fabsf)
void func_15168BE4(void *packet, u8 flags, s32 context);
void func_151718F0(f32 x, f32 y, f32 z, f32 radius, s32 lifetime,
                  f32 speed, s32 kind, s32 count, u8 flags, s32 context);

typedef struct TableDebris19E040 {
    u16 kind;
    u16 reserved02;
    f32 offset[3];
    f32 rotation[3];
} TableDebris19E040;

extern TableDebris19E040 D_800A6ED8[6];
extern f32 D_800A6F98, D_800A6F9C, D_800A6FA0;
f32 func_150ADA68(void);

extern f32 D_800A6FC0, D_800A6FC4;
void func_151717FC(u8 *actor, f32 halfWidth, f32 halfDepth, f32 offsetX,
                  f32 offsetY, f32 offsetZ, s32 kind, s32 preset,
                  s32 xCount, s32 zCount, f32 scale, u8 flags, s32 context);

void func_150AEEB0(u8 *actor, u8 flags);
void func_150BD740(u8 *actor, u8 flags, s32 mode);
void func_150CDBB0(u8 *actor, u8 flags, s32 mode);
s32 func_10010154(u16 sound, void *actor, u16 volume, s16 minimum, u16 maximum);

extern s32 D_800BE9F0;

void func_151700D8(f32 *, f32, f32, s32, f32, s32, s32, s32, u8, s32);

/* C reconstructions for the text-only asm slice asm/19E040.s. */

/* Emit six debris pieces, then a ring, and mark the actor's byte flag.
 * Reserved packet bytes intentionally retain stack residue. Guards normalize
 * independent schedules, FP registers and the unescaped kind staging home. */
void func_15170B90(u8 *actor, s32 baseKind, s32 variant, s32 options,
                  u8 flags, s32 context) {
    f32 originX;
    DebrisPacket19E040 packet;
    f32 originY;
    f32 originZ;
    f32 coefficient;
    f32 *vector;
    f32 component;
    s32 index;
    s32 kind;
    s32 asset;

    originX = (f32)*(s16 *)(actor + 0x10);
    originY = (f32)*(s16 *)(actor + 0x12);
    originZ = (f32)*(s16 *)(actor + 0x14);
    coefficient = D_800A6F94;
    packet.rotation[0] = 0.0f;
    packet.rotation[1] = 0.0f;
    packet.rotation[2] = 0.0f;
    packet.scale[0] = 1.0f;
    packet.scale[1] = 1.0f;
    packet.scale[2] = 1.0f;
    packet.lifetime = 60;
    packet.coefficient[0] = D_800A6F88;
    packet.coefficient[1] = D_800A6F8C;
    packet.coefficient[2] = D_800A6F90;
    packet.mode = 2;
    packet.alpha = 255;
    packet.zero56 = 0;
    packet.zero57 = 0;
    packet.zero58 = 0;
    packet.duration = 60;
    packet.variant = variant;
    packet.control5C = 0;
    packet.control5D = 0;
    index = 0;
    vector = D_800A6E90;
    do {
        if (options & 2) {
            DebrisKinds19E040 kinds;
            kinds = D_800A6F80;
            kind = kinds.values[index];
        } else {
            kind = options & 1 ? (s32)((u32)baseKind + (u32)index) : baseKind;
        }
        asset = func_1518C900(kind);
        component = vector[0];
        packet.position[0] = component + originX;
        packet.velocity[0] = component * coefficient;
        component = vector[1];
        packet.position[1] = component + originY;
        packet.velocity[1] = fabsf(component) * coefficient + 7.0f;
        component = vector[2];
        packet.position[2] = component + originZ;
        packet.velocity[2] = component * coefficient;
        packet.kind = kind;
        packet.velocity[0] += (f32)(func_150ADA20() >> 16) * 0.00006103515625f;
        packet.velocity[1] += (f32)(func_150ADA20() >> 16) * 0.00006103515625f;
        packet.velocity[2] += (f32)(func_150ADA20() >> 16) * 0.00006103515625f;
        packet.spin[0] = (f32)(func_150ADA20() >> 16) * 0.0000762939453125f;
        packet.spin[1] = (f32)(func_150ADA20() >> 16) * 0.0000762939453125f;
        packet.spin[2] = (f32)(func_150ADA20() >> 16) * 0.0000762939453125f;
        packet.asset = asset;
        func_15168BE4(&packet, flags, context);
        index += 1;
        vector += 3;
    } while (index != 6);
    func_151718F0(originX, originY - 80.0f, originZ, 70.0f,
                  500, 0.00457763671875f, 0, 10, flags, context);
    actor[0x6E] = 1;
}

void func_15170EC4(u8 *arg0, u8 arg1, s32 arg2) {
    switch (D_800BE9F0) {
        case 2:
            func_15170B90(arg0, 1, 1, 1, arg1, arg2);
            break;
        case 0x10:
            func_15170B90(arg0, 0xA9, 8, 0, arg1, arg2);
            break;
    }
}

/* Emit six live-table debris packets; keep reserved bytes untouched. */
void func_15170F4C(u8 *actor, u8 flags, s32 context) {
    s32 index;
    DebrisPacket19E040 packet;
    s32 count;
    f32 originX;
    f32 originY;
    f32 originZ;
    TableDebris19E040 *entry;
    s32 asset;

    packet.control5C = 2;
    packet.control5D = 1;
    packet.variant = 6;
    packet.duration = 0;
    count = 6;
    entry = D_800A6ED8;
    originX = (f32)*(s16 *)(actor + 0x10);
    originY = (f32)*(s16 *)(actor + 0x12);
    originZ = (f32)*(s16 *)(actor + 0x14);
    packet.rotation[0] = 0.0f;
    packet.rotation[1] = 0.0f;
    packet.rotation[2] = 0.0f;
    packet.scale[0] = 2.0f;
    packet.scale[1] = 2.0f;
    packet.scale[2] = 2.0f;
    packet.lifetime = 60;
    packet.mode = 2;
    packet.alpha = 255;
    packet.zero56 = 0;
    packet.zero57 = 0;
    packet.zero58 = 0;
    packet.coefficient[0] = D_800A6F98;
    packet.coefficient[1] = D_800A6F9C;
    packet.coefficient[2] = D_800A6FA0;
    index = 0;
    do {
        asset = func_1518C900(entry->kind);
        packet.kind = entry->kind;
        packet.position[0] = entry->offset[0] + originX;
        packet.position[1] = entry->offset[1] + originY;
        packet.position[2] = entry->offset[2] + originZ;
        packet.velocity[0] = entry->offset[0] * 0.09f;
        packet.velocity[1] = fabsf(entry->offset[1]) * 0.23f;
        packet.velocity[2] = entry->offset[2] * 0.09f;
        packet.rotation[0] = entry->rotation[0];
        packet.rotation[1] = entry->rotation[1];
        packet.rotation[2] = entry->rotation[2];
        packet.spin[0] = packet.rotation[0] * 0.1f;
        packet.spin[1] = func_150ADA68() * 4.0f - 2.0f;
        packet.spin[2] = func_150ADA68() * 10.0f - 5.0f;
        packet.asset = asset;
        func_15168BE4(&packet, flags, context);
        index += 1;
        entry += 1;
    } while (index < count);
    actor[0x6E] = 1;
}

void func_151711C4(u8 *arg0) {
    if (*(arg0 + 4) == 0x33) {
        func_150C3D5C(arg0);
    }
    func_15060F28(arg0, 1);
}

/* Emit randomized debris; kind stays word-wide for lookup, byte-wide in packets.
 * Fixed fields are initialized once; reserved packet bytes remain untouched. */
void func_15171200(s32 count, s32 kind, f32 x, f32 y, f32 z,
                  f32 verticalBase, f32 minimumScale, f32 maximumScale,
                  f32 spread, s32 variant, s32 lifetime, f32 coefficient,
                  u8 flags, s32 context) {
    s32 index;
    DebrisPacket19E040 packet;
    f32 scaleRange;
    f32 thirdScale;
    u32 draw0;
    u32 draw1;
    u32 draw2;
    u32 verticalDraw;
    f32 verticalSpread;

    scaleRange = maximumScale - minimumScale;
    packet.rotation[0] = 0.0f;
    packet.rotation[1] = 0.0f;
    packet.rotation[2] = 0.0f;
    packet.coefficient[0] = coefficient * -0.75f;
    packet.coefficient[2] = -0.2f;
    packet.coefficient[1] = coefficient;
    packet.lifetime = lifetime;
    packet.mode = 2;
    packet.alpha = 255;
    packet.zero56 = 0;
    packet.zero57 = 0;
    packet.zero58 = 0;
    packet.variant = variant;
    packet.kind = kind;
    packet.control5C = 1;
    packet.control5D = 1;
    spread = spread * 0.0000152587890625f;
    verticalSpread = verticalBase * 0.000006103515625f;
    verticalBase *= 0.8f;
    index = 0;
    if (count > 0) {
        do {
            packet.position[0] = (f32)(func_150ADA20() >> 16) * spread + x;
            packet.position[1] = (f32)(func_150ADA20() >> 16) * spread + y;
            packet.position[2] = (f32)(func_150ADA20() >> 16) * spread + z;
            packet.asset = func_1518C900(kind);
            packet.velocity[0] = (f32)(func_150ADA20() >> 16) * 0.0002288818359375f;
            verticalDraw = (u32)func_150ADA20() & 65535;
            packet.velocity[1] = (f32)verticalDraw * verticalSpread + verticalBase;
            packet.velocity[2] = (f32)(func_150ADA20() >> 16) * 0.0002288818359375f;
            packet.spin[0] = (f32)(func_150ADA20() >> 16) * 0.000152587890625f;
            packet.spin[1] = (f32)(func_150ADA20() >> 16) * 0.000152587890625f;
            packet.spin[2] = (f32)(func_150ADA20() >> 16) * 0.000152587890625f;
            draw0 = (u32)func_150ADA20() & 65535;
            packet.scale[0] = ((f32)(draw0) * 0.0000152587890625f) * scaleRange + minimumScale;
            draw1 = (u32)func_150ADA20() & 65535;
            packet.scale[1] = ((f32)(draw1) * 0.0000152587890625f) * scaleRange + minimumScale;
            draw2 = (u32)func_150ADA20() & 65535;
            thirdScale = ((f32)(draw2) * 0.0000152587890625f) * scaleRange + minimumScale;
            packet.duration = (u32)(((packet.scale[1] + packet.scale[0]) + thirdScale) * 6.666667f + 20.0f);
            packet.scale[2] = thirdScale;
            func_15168BE4(&packet, flags, context);
            index += 1;
        } while (index != count);
    }
}

/* Select the rectangle debris preset from the actor's byte-sized type. */
void func_15171600(u8 *actor, u8 flags, s32 context) {
    switch (actor[0x72]) {
        case 0xEB:
            func_151717FC(actor, 400.0f, 500.0f, 0.0f, D_800A6FC0, 0.0f,
                          2, 5, 20, 20, 1.0f, flags, context);
            break;
        case 0xF6:
            func_151717FC(actor, 200.0f, 400.0f, -1800.0f, -1000.0f, -1200.0f,
                          2, 5, 4, 10, 1.0f, flags, context);
            break;
        case 0xF8:
            func_151717FC(actor, 100.0f, 160.0f, -2500.0f, D_800A6FC4, 0.0f,
                          2, 5, 4, 4, 0.5f, flags, context);
            break;
        case 0xF9:
            func_151717FC(actor, 200.0f, 100.0f, 100.0f, -300.0f, 0.0f,
                          1, 5, 4, 4, 1.0f, flags, context);
            break;
    }
}

/* Build a rectangle around signed actor coordinates and emit its perimeter.
 * Guards normalize the compiler's private homes and FP/register schedule. */
void func_151717FC(u8 *actor, f32 halfWidth, f32 halfDepth, f32 offsetX,
                  f32 offsetY, f32 offsetZ, s32 kind, s32 preset,
                  s32 xCount, s32 zCount, f32 scale, u8 flags, s32 context) {
    f32 quad[12];
    f32 frontZ;
    f32 centerY;
    f32 centerX;
    f32 centerZ;
    f32 backZ;
    f32 rightX;
    f32 leftX;

    centerX = (f32)*(s16 *)(actor + 0x10) + offsetX;
    centerY = (f32)*(s16 *)(actor + 0x12) + offsetY;
    centerZ = (f32)*(s16 *)(actor + 0x14) + offsetZ;
    quad[1] = centerY;
    quad[4] = centerY;
    rightX = halfWidth + centerX;
    quad[7] = centerY;
    quad[0] = rightX;
    quad[9] = rightX;
    leftX = centerX - halfWidth;
    backZ = centerZ - halfDepth;
    frontZ = halfDepth + centerZ;
    quad[3] = leftX;
    quad[6] = leftX;
    quad[2] = frontZ;
    quad[5] = frontZ;
    quad[10] = centerY;
    quad[8] = (&backZ)[0];
    quad[11] = (&backZ)[0];
    func_151700D8(quad, centerX, centerZ, preset, scale, kind,
                  xCount, zCount, flags, context);
}

/* Emit randomized radial particles using the staged palette-zero color.
 * Nonzero palette selectors would read beyond the original three-byte object.
 * Guards normalize only eight closed initialization temporary-register words. */
void func_151718F0(f32 x, f32 y, f32 z, f32 radius, s32 lifetime,
                  f32 spread, s32 palette, s32 count, u8 flags, s32 context) {
    u8 *color;
    f32 sine;
    f32 cosine;
    f32 positionZ;
    f32 delay;
    f32 baseLifetime;
    s32 phase;
    s32 index;
    s32 angle;
    s32 zHigh;
    s32 zLow;
    s32 extent;
    s32 fixedX;
    s32 fixedZ;
    s32 tail;
    s32 step;
    s16 height;
    u32 draw;
    RingColors19E040 colors;

    colors = D_8008CC20;
    if (count != 0) {
        phase = 0;
        index = 0;
        if (count > 0) {
            step = 0xFFFF / count;
            height = (s16)(s32)y;
            baseLifetime = (f32)lifetime;
            color = colors.values + palette * 3;
            do {
                angle = (phase >> 8) & 255;
                sine = func_15048A40(angle);
                cosine = func_150489B0(angle);
                positionZ = radius * cosine + z;
                fixedZ = (s32)(200.0f * cosine);
                zHigh = (fixedZ >> 8) & 255;
                zLow = fixedZ & 255;
                draw = (u32)func_150ADA20() & 0xFFFFU;
                delay = (f32)draw * 0.0000152587890625f + 100.0f;
                extent = (s32)((f32)((u32)func_150ADA20() & 0xFFFFU) * spread + baseLifetime);
                tail = func_150ADA20();
                fixedX = (s32)(200.0f * sine);
                func_1516D4E8((s16)(s32)(radius * sine + x), height, (s16)(s32)positionZ,
                    0xD, 0, color[0], color[1], color[2], 0, 0, 0, 0, 2,
                    (fixedX >> 8) & 255, fixedX & 255, zHigh, zLow, 0, 0, 5, 0, 0, 0,
                    (s16)extent, (s16)extent, (tail & 15) + 10, (s32)delay,
                    0, 0, flags, context);
                index += 1;
                phase += step;
            } while (index != count);
        }
    }
}

/* Dispatch actor-specific effects; play the paired sound after the first effect. */
void func_15171BF4(u8 *actor, u8 flags) {
    switch (actor[4]) {
        case 0x13:
        case 0x23:
            func_150AEEB0(actor, flags);
            func_10010154(0x69, actor, 0x7D00, 200, 2000);
            break;
        case 0x1E:
            func_150BD740(actor, flags, 1);
            break;
        case 0x54:
            func_150CDBB0(actor, flags, 1);
            break;
    }
}
