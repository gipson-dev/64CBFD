#include <ultra64.h>
extern s32 D_800BE9E4;
extern s32 (*D_8008ACC8[])(u8 *);
void func_1516972C(u8 *);

s32 func_15144E80(s16 *, f32 *, f32 *, f32 *);
f32 func_15144A74(f32 *, f32 *);

typedef struct { s32 a, b; } TwoWord17CAF0;

/* Non-matching placeholders for the text-only asm slice asm/17CAF0.s. */

extern void (*D_8008AD04[])(u8 *, s32, u8);
extern u8 D_800A6038[];
extern u8 D_800A5FE0[][3];
void func_15169260(void *, s32, void *, u8);
s32 func_150ADA20(void);
s32 func_1514FF44(u8 *arg0, s32 arg1, s32 arg2, u8 arg3, s32 arg4);
s32 func_15153CCC(u8 *arg0, s32 arg1, s32 arg2, u8 arg3, s32 arg4);

/* Build triangle vectors and orient the normal toward the source vector. */
void func_1514F640(u8 *source, u8 *output) {
    output[0] = 2;
    *(f32 *)(output + 0x28) = *(f32 *)(source + 0x20);
    if (func_15144E80((s16 *)(source + 0xC), (f32 *)(output + 0x10),
                     (f32 *)(output + 0x1C), (f32 *)(output + 4))) {
        if (func_15144A74((f32 *)(output + 4), (f32 *)source) < 0.0f) {
            *(f32 *)(output + 4) = -*(f32 *)(output + 4);
            *(f32 *)(output + 8) = -*(f32 *)(output + 8);
            *(f32 *)(output + 0xC) = -*(f32 *)(output + 0xC);
        }
    }
}

s32 func_1514F6E8() {
    return 0;
}

s32 func_150ADA20(void);
f32 func_150ADA68(void);
void func_15143874(s16,f32,f32*,f32*);
/* Sample a radial point and transform its three components through the live basis. */
void func_1514F808(f32 *basis, f32 scale, f32 *output) {
    f32 second;
    f32 first;
    f32 sample;
    s32 random;
    random = func_150ADA20();
    sample = func_150ADA68();
    func_15143874((s16)(random & 255), sample * basis[10], &first, &second);
    output[0] = ((basis[4] * first + basis[7] * second) + basis[1]) * scale;
    output[1] = ((basis[5] * first + basis[8] * second) + basis[2]) * scale;
    output[2] = ((basis[6] * first + basis[9] * second) + basis[3]) * scale;
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_17CAF0/func_1514F8F8.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_17CAF0/func_1514FB98.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_17CAF0/func_1514FBFC.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_17CAF0/func_1514FCE8.s")

void func_1514FEFC(s32 arg0, s32 arg1, s32 arg2, u8 arg3, s32 arg4) {
    u8 temp[0x2C];

    func_1514F640((u8 *)arg0, temp);
    func_1514FF44(temp, arg1, arg2, arg3, arg4);
}

s32 func_1514FF44(u8 *arg0, s32 arg1, s32 arg2, u8 arg3, s32 arg4) {
    return 0;
}

s32 func_15150178() {
    return 0;
}

s32 func_15150400() {
    return 0;
}

s32 func_1515080C() {
    return 0;
}

s32 func_15150D1C() {
    return 0;
}

s32 func_15150F90() {
    return 0;
}

s32 func_151511FC() {
    return 0;
}

s32 func_15151670() {
    return 0;
}

s32 func_15151A38() {
    return 0;
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_17CAF0/func_15151D6C.s")

s32 func_15152190() {
    return 0;
}

typedef struct {
    s32 baseCount, countRange;
    f32 position[3];
    s16 field14, field16, field18, field1A;
    f32 parameters[5];
    s16 lifetimeBase, lifetimeRange;
    s32 field34, field38, field3C;
    f32 values[10];
    u8 colors[8];
    u8 field70, field71;
    s16 field72, field74;
    u8 padding76[2];
} ParticleFactoryInput;
typedef struct { u8 r, g, b, a; } ParticleColor;
typedef struct { f32 x, y, z; } ParticlePosition;
typedef struct {
    u8 flags, field1, field2;
    s8 field3, field4;
    u8 padding5;
    s16 lifetime;
    s32 field8, fieldC, field10;
    u32 field14, field18;
    s32 field1C, field20, field24, field28;
    u8 field2C, field2D, padding2E[2];
    ParticleColor colors[2];
    u8 field38, padding39[3];
    s32 field3C;
    u8 field40, field41, padding42[2];
    ParticlePosition position;
    u8 padding50[4];
    s16 field54, field56;
} ParticleSpawnDescriptor;
typedef struct {
    f32 rotation[3];
    f32 fieldC;
    f32 direction[3];
    f32 velocity[3];
    f32 field28, field2C;
    u8 property, padding31[3];
} ParticleSpawnState;
s32 func_150ADA20(void);
f32 func_150ADA68(void);
void func_15143794(s16, s16, f32, f32 *);
s32 func_15157898(s32, void *, s32, f32,
                  s32, s32, u8 *, u8, s32);

/* Spawn copies state plus the descriptor first word from this complete object. */
typedef struct { ParticleSpawnState state; ParticleSpawnDescriptor descriptor; } ParticleSpawnScratch;
/* Emit randomized particles from live input fields using one contiguous spawn scratch object. */
void func_15152520(ParticleFactoryInput *input, u8 mode, s32 extra) {
    ParticleSpawnScratch scratch;
    u32 remaining;
    u32 first;
    u32 second;

    scratch.descriptor.field38 = 0;
    scratch.descriptor.flags = input->field70 | 2;
    scratch.descriptor.field1 = 0;
    scratch.descriptor.field2 = 1;
    scratch.descriptor.field3 = -1;
    scratch.descriptor.field4 = -1;
    scratch.descriptor.field8 = input->field34;
    scratch.descriptor.fieldC = input->field38;
    scratch.descriptor.field24 = 128;
    scratch.descriptor.field28 = 32;
    scratch.descriptor.field10 = 0;
    scratch.descriptor.field14 = 0x220405;
    scratch.descriptor.field18 = 0x40200;
    scratch.descriptor.field2C = 0;
    scratch.descriptor.field2D = 8;
    scratch.descriptor.field1C = 1;
    scratch.descriptor.field20 = 0x38;
    scratch.descriptor.field3C = 0;
    scratch.descriptor.field40 = 0;
    scratch.descriptor.field41 = 2;
    scratch.descriptor.position = *(ParticlePosition *)input->position;
    scratch.state.field2C = input->parameters[2];
    scratch.descriptor.colors[0] = *(ParticleColor *)&input->colors[0];
    scratch.descriptor.colors[1] = *(ParticleColor *)&input->colors[4];
    scratch.descriptor.field54 = input->field72;
    scratch.descriptor.field56 = input->field74;
    scratch.state.property = input->field71;
    remaining = (u32)func_150ADA20();
    remaining = remaining % ((u32)input->countRange + 1U) + (u32)input->baseCount;
    while (remaining != 0) {
        first = (u32)func_150ADA20();
        scratch.descriptor.lifetime = (s16)(first % (u32)(input->lifetimeRange + 1) + input->lifetimeBase);
        scratch.state.rotation[0] = func_150ADA68() * 360.0f;
        scratch.state.rotation[1] = func_150ADA68() * 360.0f;
        scratch.state.rotation[2] = func_150ADA68() * 360.0f;
        scratch.state.fieldC = func_150ADA68() * input->values[3] + input->values[2];
        first = (u32)func_150ADA20();
        second = (u32)func_150ADA20();
        func_15143794((s16)(first % (u32)(input->field16 + 1) + input->field14),
                      (s16)(second % (u32)(input->field1A + 1) + input->field18),
                      func_150ADA68() * input->parameters[1] + input->parameters[0], scratch.state.direction);
        scratch.state.velocity[0] = func_150ADA68() * input->values[7] + input->values[4];
        scratch.state.velocity[1] = func_150ADA68() * input->values[8] + input->values[5];
        scratch.state.velocity[2] = func_150ADA68() * input->values[9] + input->values[6];
        scratch.state.field28 = func_150ADA68() * input->parameters[4] + input->parameters[3];
        func_15157898((s32)&scratch.descriptor, &scratch, input->field3C, func_150ADA68() * input->values[1] + input->values[0], 0, 0, 0, (u8)mode, extra);
        remaining--;
    }
}

typedef struct { f32 x, y, z; } EffectPosition;
typedef struct {
    s32 baseCount, countRange;
    EffectPosition position;
    s16 firstBase, firstRange, secondBase, secondRange;
    f32 radiusBase, radiusRange, field24;
    f32 scaleBase, scaleRange;
    s8 colorSelector;
    u8 padding31;
    s16 lifetimeBase, lifetimeRange;
    u8 padding36[2];
    f32 field38, field3C, field40, field44, field48;
} ColorEffectInput;
typedef struct {
    EffectPosition position;
    f32 direction[3];
    f32 field18, scale;
    u8 colors[4];
    s32 lifetime;
    f32 field28, field2C, field30;
    u8 privateTail34[4];
} ColorEffectPacket;
s32 func_150ADA20(void);
f32 func_150ADA68(void);
void func_15143794(s16, s16, f32, f32 *);
s32 func_150CCEB0(ColorEffectPacket *, u8, u8);
extern void (*D_8008AC60[])(u8 *);
/* Emit randomized color-effect packets from live input fields using the complete private packet extent. */
void func_15152874(ColorEffectInput *input, u8 mode, s32 extra) {
    ColorEffectPacket packet;
    u32 remaining;
    u32 first, second;
    first = (u32)func_150ADA20();
    remaining = first % ((u32)input->countRange + 1U) + (u32)input->baseCount;
    packet.position = input->position;
    packet.field18 = input->field24;
    packet.field30 = input->field48;
    while (remaining != 0) {
        first = (u32)func_150ADA20();
        second = (u32)func_150ADA20();
        func_15143794((s16)(first % (u32)(input->firstRange + 1) + input->firstBase),
                      (s16)(second % (u32)(input->secondRange + 1) + input->secondBase),
                      func_150ADA68() * input->radiusRange + input->radiusBase, packet.direction);
        packet.scale = func_150ADA68() * input->scaleRange + input->scaleBase;
        first = (u32)func_150ADA20();
        packet.lifetime = first % (u32)(input->lifetimeRange + 1) + input->lifetimeBase;
        packet.field28 = func_150ADA68() * input->field40 + input->field38;
        packet.field2C = func_150ADA68() * input->field44 + input->field3C;
        if (input->colorSelector != -1) {
            D_8008AC60[input->colorSelector](packet.colors);
        } else {
            packet.colors[0] = 255;
            packet.colors[1] = 255;
            packet.colors[2] = 255;
            packet.colors[3] = 255;
        }
        func_150CCEB0(&packet, (u8)mode, (u8)extra);
        remaining--;
    }
}

/* Note 532: randomized RGBA color initialization. */
void func_15152ABC(u8 *arg0) {
    u8 index;
    u8 *color;

    index = func_150ADA20() % 5U;
    color = D_800A5FE0[index];
    arg0[3] = (func_150ADA20() % 101U) + 155;
    arg0[0] = color[0];
    arg0[1] = color[1];
    arg0[2] = color[2];
}


typedef struct {
    f32 x, y, z;
} CompositeEffectPosition;

typedef struct {
    s32 baseCount;
    s32 countRange;
    CompositeEffectPosition position;
    f32 field14Base;
    f32 field18Range;
    f32 field1CBase;
    f32 field20Range;
    f32 radiusBase;
    f32 radiusRange;
    s16 firstBase;
    s16 firstRange;
    s16 secondBase;
    s16 secondRange;
    s32 headerByteBase;
    s32 headerByteRange;
    s16 headerShortBase;
    s16 headerShortRange;
    u16 field40;
    u8 fixed42;
    u8 fixed43;
    u8 fixed44;
    u8 byteBase45;
    u8 byteBase46;
    u8 byteBase47;
    u8 byteBase48;
    u8 byteRange49;
    u8 byteRange4A;
    u8 byteRange4B;
    u8 byteRange4C;
    u8 byteBase4D;
    u8 byteBase4E;
    u8 byteBase4F;
    u8 byteBase50;
    u8 byteRange51;
    u8 byteRange52;
    u8 byteRange53;
    u8 byteRange54;
    u8 byteBase55;
    u8 byteRange56;
    u8 fixed57;
    u8 fixed58;
    u8 padding59[3];
    s32 field5C;
    s32 field60;
    s16 field64;
    s16 field66;
    s16 field68;
    u8 field6A;
    u8 padding6B;
    f32 field6C;
    s8 field70;
    s8 field71;
    u8 privateTail72[2];
} CompositeEffectInput;

typedef struct {
    f32 field0;
    f32 direction[3];
    f32 field10;
    u8 fixed14;
    u8 fixed15;
    u8 fixed16;
    s8 random17;
    s8 random18;
    s8 random19;
    s8 random1A;
    s8 random1B;
    s8 random1C;
    s8 random1D;
    s8 random1E;
    s8 random1F;
    u8 fixed20;
    u8 fixed21;
    u8 private22[2];
    s32 field24;
    s32 field28;
    s16 field2C;
    s16 field2E;
    s16 field30;
    u8 field32;
    u8 private33;
    f32 field34;
    s8 field38;
    s8 field39;
    u8 privateTail3A[2];
} CompositeEffectPacket;

typedef struct {
    CompositeEffectPosition position;
    s16 randomC;
    u16 fieldE;
    s32 constant10;
    u8 private14;
    s8 random15;
    u8 privateTail16[2];
} CompositeEffectHeader;

s32 func_150ADA20(void);
f32 func_150ADA68(void);
void func_15143794(s16, s16, f32, f32 *);
s32 func_1515C2F0(CompositeEffectHeader *, s32, CompositeEffectPacket *, s32, u8, s32);

typedef struct {
    CompositeEffectPacket packet;
    CompositeEffectHeader header;
    u8 privateTail54[4];
} CompositeEffectScratch;
/* Emit randomized composite-effect packets from live input fields using the complete private scratch extents. */
void func_15152B38(CompositeEffectInput *input, u8 mode, s32 extra) {
    CompositeEffectScratch scratch;
    u32 remaining;
    u32 first;
    u32 second;

    first = (u32)func_150ADA20();
    remaining = first % ((u32)input->countRange + 1U) + (u32)input->baseCount;
    scratch.header.position = input->position;
    scratch.header.fieldE = input->field40;
    scratch.header.constant10 = 10;
    scratch.packet.fixed14 = input->fixed42;
    scratch.packet.fixed15 = input->fixed43;
    scratch.packet.fixed16 = input->fixed44;
    scratch.packet.fixed20 = input->fixed57;
    scratch.packet.fixed21 = input->fixed58;
    scratch.packet.field24 = input->field5C;
    scratch.packet.field28 = input->field60;
    scratch.packet.field2C = input->field64;
    scratch.packet.field2E = input->field66;
    scratch.packet.field38 = input->field70;
    scratch.packet.field39 = input->field71;
    scratch.packet.field30 = input->field68;
    scratch.packet.field32 = input->field6A;
    scratch.packet.field34 = input->field6C;

    while (remaining != 0) {
        first = (u32)func_150ADA20();
        scratch.header.random15 = (s8)(first % ((u32)input->headerByteRange + 1U) +
                                  (u32)input->headerByteBase);
        first = (u32)func_150ADA20();
        scratch.header.randomC = (s16)(first % ((u32)(input->headerShortRange + 1)) +
                                   input->headerShortBase);
        scratch.packet.field0 = func_150ADA68() * input->field18Range + input->field14Base;
        scratch.packet.field10 = func_150ADA68() * input->field20Range + input->field1CBase;
        first = (u32)func_150ADA20();
        second = (u32)func_150ADA20();
        func_15143794((s16)(first % (u32)(input->firstRange + 1) + input->firstBase),
                      (s16)(second % (u32)(input->secondRange + 1) + input->secondBase),
                      func_150ADA68() * input->radiusRange + input->radiusBase,
                      scratch.packet.direction);
        first = (u32)func_150ADA20();
        scratch.packet.random17 = (s8)(first % ((u32)input->byteRange49 + 1U) + input->byteBase45);
        first = (u32)func_150ADA20();
        scratch.packet.random18 = (s8)(first % ((u32)input->byteRange4A + 1U) + input->byteBase46);
        first = (u32)func_150ADA20();
        scratch.packet.random19 = (s8)(first % ((u32)input->byteRange4B + 1U) + input->byteBase47);
        first = (u32)func_150ADA20();
        scratch.packet.random1A = (s8)(first % ((u32)input->byteRange4C + 1U) + input->byteBase48);
        first = (u32)func_150ADA20();
        scratch.packet.random1B = (s8)(first % ((u32)input->byteRange51 + 1U) + input->byteBase4D);
        first = (u32)func_150ADA20();
        scratch.packet.random1C = (s8)(first % ((u32)input->byteRange52 + 1U) + input->byteBase4E);
        first = (u32)func_150ADA20();
        scratch.packet.random1D = (s8)(first % ((u32)input->byteRange53 + 1U) + input->byteBase4F);
        first = (u32)func_150ADA20();
        scratch.packet.random1E = (s8)(first % ((u32)input->byteRange54 + 1U) + input->byteBase50);
        first = (u32)func_150ADA20();
        scratch.packet.random1F = (s8)(first % ((u32)input->byteRange56 + 1U) + input->byteBase55);
        func_1515C2F0(&scratch.header, 0, &scratch.packet, 0, (u8)mode, extra);
        remaining--;
    }
}


typedef struct {
    f32 x;
    f32 y;
    f32 z;
} OrientedEffectPosition;

typedef struct {
    OrientedEffectPosition position;
    f32 fieldCBase;
    f32 field10Range;
    f32 field14Base;
    f32 field18Range;
    f32 speedBase;
    f32 speedRange;
    s16 countBase;
    s16 countRange;
    s16 firstAngleBase;
    s16 firstAngleRange;
    s16 secondAngleBase;
    s16 secondAngleRange;
    s16 byteBase;
    s16 byteRange;
    s16 shortBase;
    s16 shortRange;
    u8 fixed38;
    u8 fixed39;
    u8 private3A[2];
    s32 argument3C;
    s32 argument40;
    s32 argument44;
    s32 argument48;
    s32 argument4C;
    s32 argument50;
    u8 fixed54;
    u8 fixed55;
    u8 privateTail56[2];
} OrientedEffectInput;

typedef struct {
    s32 field0;
    s32 field4;
    s32 field8;
    s32 fieldC;
    s32 field10;
    s32 field14;
    s32 field18;
    u8 field1C;
    u8 field1D;
    u8 privateTail1E[6];
} OrientedEffectDescriptor;

typedef struct {
    f32 field0;
    f32 direction[3];
    f32 field10;
    u8 private14[4];
    u8 fixed18;
    u8 fixed19;
    u8 fixed1A;
    u8 fixed1B;
    u8 privateTail1C[4];
} OrientedEffectMotion;

typedef struct {
    OrientedEffectPosition position;
    s16 randomC;
    s16 constantE;
    s32 constant10;
    u8 private14;
    s8 random15;
    u8 privateTail16[2];
} OrientedEffectHeader;

typedef struct {
    OrientedEffectDescriptor descriptor;
    OrientedEffectMotion motion;
    OrientedEffectHeader header;
} OrientedEffectScratch;

s32 func_150ADA20(void);
f32 func_150ADA68(void);
f32 func_151423D8(s32 angle);
void func_15147DA0();
/* Emit oriented randomized effect packets from live input fields using complete private scratch extents. */
void func_15152F70(OrientedEffectInput *input, u8 mode) {
    OrientedEffectHeader header;
    OrientedEffectMotion motion;
    OrientedEffectDescriptor descriptor;
    f32 speed;
    f32 secondPrimary;
    f32 secondQuarter;
    f32 firstPrimary;
    f32 firstQuarter;
    f32 product;
    s16 firstAngle;
    s16 secondAngle;
    s32 remaining;

    header.constant10 = 1;
    header.constantE = 1;
    motion.fixed19 = input->fixed38;
    motion.fixed1A = input->fixed54;
    motion.fixed18 = input->fixed39;
    motion.fixed1B = input->fixed55;
    header.position = input->position;
    descriptor.field0 = 0;
    descriptor.field4 = 1;
    descriptor.field8 = 0x160600;
    descriptor.fieldC = 3;
    descriptor.field10 = 0x10;
    descriptor.field14 = 0x80;
    descriptor.field18 = 0x20;
    descriptor.field1C = 0;
    descriptor.field1D = 9;
    remaining = (u32)func_150ADA20() % ((u32)input->countRange + 1U) + input->countBase;
    if (remaining != 0) {
        do {
            firstAngle = (u32)func_150ADA20() % ((u32)input->firstAngleRange + 1U) + input->firstAngleBase;
            secondAngle = (u32)func_150ADA20() % ((u32)input->secondAngleRange + 1U) + input->secondAngleBase;
            secondPrimary = func_151423D8((u8)secondAngle);
            secondQuarter = func_151423D8((u8)(secondAngle - 0x40));
            firstPrimary = func_151423D8((u8)firstAngle);
            firstQuarter = func_151423D8((u8)(firstAngle - 0x40));
            speed = func_150ADA68() * input->speedRange + input->speedBase;
            header.random15 = (u32)func_150ADA20() % ((u32)input->byteRange + 1U) + input->byteBase;
            header.randomC = (u32)func_150ADA20() % ((u32)input->shortRange + 1U) + input->shortBase;
            motion.field0 = func_150ADA68() * input->field10Range + input->fieldCBase;
            product = speed * secondPrimary;
            motion.field10 = func_150ADA68() * input->field18Range + input->field14Base;
            motion.direction[0] = product * firstQuarter;
            motion.direction[1] = -speed * secondQuarter;
            motion.direction[2] = product * firstPrimary;
            func_15147DA0(&header.position, &motion.field0, 0,
                          input->argument3C, input->argument40, input->argument44,
                          input->argument48, input->argument4C, input->argument50,
                          0, 0, &descriptor, 0, mode, 1);
            remaining--;
        } while (remaining != 0);
    }
}


typedef struct {
    f32 x;
    f32 y;
    f32 z;
    s16 countBase;
    s16 countRange;
    s16 firstAngleBase;
    s16 firstAngleRange;
    s16 secondAngleBase;
    s16 secondAngleRange;
    f32 speedBase;
    f32 speedRange;
    s16 magnitudeBase;
    s16 magnitudeRange;
    s16 field22Base;
    s16 field22Range;
    s8 fixed1F;
    u8 fixed34;
    s16 field2ABase;
    s16 field2ARange;
    s16 fixed0E;
    s16 field24Base;
    s16 field24Range;
    s16 field26Base;
    s16 field26Range;
    s32 owner;
    u8 color;
    u8 alpha;
    u8 privateTail3E[2];
} ShortPacketInput;

typedef struct {
    s32 owner;
    u8 private04[8];
    s16 zero0C;
    s16 fixed0E;
    s16 positionX;
    s16 positionY;
    s16 positionZ;
    s16 directionX;
    s16 directionZ;
    u8 private1A[2];
    s8 scaledX;
    s8 scaledY;
    s8 scaledZ;
    s8 fixed1F;
    s16 directionY;
    s16 field22;
    s16 field24;
    s16 field26;
    s16 magnitude;
    s8 field2A;
    u8 private2B;
    u8 color0;
    u8 color1;
    u8 color2;
    u8 alpha;
    s8 zero30;
    s8 zero31;
    s8 zero32;
    u8 private33;
    u16 fixed34;
    u8 privateTail36[2];
} ShortPacket;

s32 func_150ADA20(void);
f32 func_150ADA68(void);
f32 func_151423D8(s32 angle);
void func_15167D84(void *packet, s32 kind, s32 offset, s8 marker, u8 mode, s32 owner);
/* Emit randomized short-form effect packets from a complete live input record. */
void func_15153298(ShortPacketInput *input, u8 mode, s32 owner) {
    ShortPacket packet;
    f32 speed;
    f32 secondPrimary;
    f32 secondQuarter;
    f32 firstPrimary;
    f32 firstQuarter;
    f32 product;
    s16 firstAngle;
    s16 secondAngle;
    s32 remaining;

    packet.positionX = (s16)input->x;
    packet.positionY = (s16)input->y;
    packet.positionZ = (s16)input->z;
    packet.scaledX = (s8)(input->x * 256.0f);
    packet.scaledY = (s8)(input->y * 256.0f);
    packet.scaledZ = (s8)(input->z * 256.0f);
    packet.color0 = input->color;
    packet.color1 = input->color;
    packet.zero30 = 0;
    packet.zero31 = 0;
    packet.zero32 = 0;
    packet.color2 = input->color;
    packet.alpha = input->alpha;
    packet.fixed1F = input->fixed1F;
    packet.zero0C = 0;
    packet.fixed34 = input->fixed34;
    packet.fixed0E = input->fixed0E;
    packet.owner = input->owner;
    remaining = (u32)func_150ADA20() % ((u32)input->countRange + 1U) + input->countBase;
    if (remaining != 0) {
        do {
            firstAngle = (u32)func_150ADA20() % ((u32)input->firstAngleRange + 1U) + input->firstAngleBase;
            secondAngle = (u32)func_150ADA20() % ((u32)input->secondAngleRange + 1U) + input->secondAngleBase;
            secondPrimary = func_151423D8((u8)secondAngle);
            secondQuarter = func_151423D8((u8)(secondAngle - 0x40));
            firstPrimary = func_151423D8((u8)firstAngle);
            firstQuarter = func_151423D8((u8)(firstAngle - 0x40));
            speed = func_150ADA68() * input->speedRange + input->speedBase;
            product = speed * secondPrimary;
            packet.magnitude = (u32)func_150ADA20() % ((u32)input->magnitudeRange + 1U) + input->magnitudeBase;
            packet.directionX = (s16)(product * firstQuarter);
            packet.directionY = (s16)(-speed * secondQuarter);
            packet.directionZ = (s16)(product * firstPrimary);
            packet.field22 = (u32)func_150ADA20() % ((u32)input->field22Range + 1U) + input->field22Base;
            packet.field2A = (u32)func_150ADA20() % ((u32)input->field2ARange + 1U) + input->field2ABase;
            packet.field24 = (u32)func_150ADA20() % ((u32)input->field24Range + 1U) + input->field24Base;
            packet.field26 = (u32)func_150ADA20() % ((u32)input->field26Range + 1U) + input->field26Base;
            func_15167D84(&packet, 0, 0, -1, mode, owner);
            remaining--;
        } while (remaining != 0);
    }
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_17CAF0/func_15153634.s")


typedef struct {
    s16 countBase;
    s16 countRange;
    f32 origin[3];
    s16 firstAngleBase;
    s16 secondAngleBase;
    s16 firstAngleRange;
    s16 secondAngleRange;
    f32 firstValueBase;
    f32 firstValueRange;
    f32 secondValueBase;
    f32 secondValueRange;
    u8 copiedBytes[9];
    u8 private31;
    s16 shortBase;
    s16 shortRange;
    u16 fixed36;
    f32 floatBase;
    f32 floatRange;
    u8 byteBase;
    u8 byteRange;
    s16 fixed42;
    s16 fixed44;
    u8 kind;
    u8 privateTail47;
} WidePacketInput;

typedef struct {
    f32 origin[3];
    f32 directionX;
    f32 directionY;
    f32 directionZ;
    f32 firstValue;
    f32 secondValue;
    u8 copiedBytes[9];
    u8 private29;
    s16 randomShort;
    u16 fixed2C;
    u8 private2E[2];
    f32 randomFloat;
    s8 randomByte;
    u8 private35;
    s16 fixed36;
    s16 fixed38;
    u8 privateTail3A[2];
} WidePacket;

s32 func_150ADA20(void);
f32 func_150ADA68(void);
f32 func_151423D8(s32 angle);
void func_15156190(void *packet, u8 kind, s32 zero, u8 mode, s32 owner);
/* Emit randomized wide effect packets from a complete live input record. */
void func_151539B4(WidePacketInput *input, u8 mode) {
    WidePacket packet;
    WidePacket *packetPtr;
    f32 secondPrimary;
    f32 secondQuarter;
    f32 firstPrimary;
    f32 directionScale;
    s16 firstAngle;
    s16 secondAngle;
    s32 remaining;

    remaining = (u32)func_150ADA20() % ((u32)input->countRange + 1U) + input->countBase;
    packetPtr = &packet;
    *(volatile u8 *)&input->copiedBytes[0];
    *(s32 *)&packetPtr->origin[0] = *(s32 *)&input->origin[0];
    *(s32 *)&packetPtr->origin[1] = *(s32 *)&input->origin[1];
    *(s32 *)&packetPtr->origin[2] = *(s32 *)&input->origin[2];
    packetPtr->copiedBytes[0] = input->copiedBytes[0];
    packetPtr->copiedBytes[1] = input->copiedBytes[1];
    packetPtr->copiedBytes[2] = input->copiedBytes[2];
    packetPtr->copiedBytes[3] = input->copiedBytes[3];
    packetPtr->copiedBytes[4] = input->copiedBytes[4];
    packetPtr->copiedBytes[5] = input->copiedBytes[5];
    packetPtr->copiedBytes[6] = input->copiedBytes[6];
    packetPtr->copiedBytes[7] = input->copiedBytes[7];
    packetPtr->copiedBytes[8] = input->copiedBytes[8];
    packetPtr->fixed2C = input->fixed36;
    packetPtr->fixed36 = input->fixed42;
    packetPtr->fixed38 = input->fixed44;
    if (remaining != 0) {
        do {
            firstAngle = (u32)func_150ADA20() % ((u32)input->firstAngleRange + 1U) + input->firstAngleBase;
            secondAngle = (u32)func_150ADA20() % ((u32)input->secondAngleRange + 1U) + input->secondAngleBase;
            secondPrimary = func_151423D8((u8)secondAngle);
            secondQuarter = func_151423D8((u8)(secondAngle - 0x40));
            firstPrimary = func_151423D8((u8)firstAngle);
            directionScale = 10.0f * secondPrimary;
            packetPtr->directionX = directionScale * func_151423D8((u8)(firstAngle - 0x40));
            packetPtr->directionY = -10.0f * secondQuarter;
            packetPtr->directionZ = directionScale * firstPrimary;
            packetPtr->firstValue = func_150ADA68() * input->firstValueRange + input->firstValueBase;
            packetPtr->secondValue = func_150ADA68() * input->secondValueRange + input->secondValueBase;
            packetPtr->randomShort = (u32)func_150ADA20() % ((u32)input->shortRange + 1U) + input->shortBase;
            packetPtr->randomFloat = func_150ADA68() * input->floatRange + input->floatBase;
            packetPtr->randomByte = (u32)func_150ADA20() % ((u32)input->byteRange + 1U) + input->byteBase;
            func_15156190(packetPtr, input->kind, 0, mode, 0);
            remaining--;
        } while (remaining != 0);
    }
}

void func_15153C84(s32 arg0, s32 arg1, s32 arg2, u8 arg3, s32 arg4) {
    u8 temp[0x2C];

    func_1514F640((u8 *)arg0, temp);
    func_15153CCC(temp, arg1, arg2, arg3, arg4);
}

s32 func_15153CCC(u8 *arg0, s32 arg1, s32 arg2, u8 arg3, s32 arg4) {
    return 0;
}

s32 func_15153F18() {
    return 0;
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_17CAF0/func_151541B8.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_17CAF0/func_1515452C.s")

s32 func_15154684() {
    return 0;
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_17CAF0/func_15154884.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_17CAF0/func_15154A88.s")

/* Advance a live effect, dispatch its update and limit the fading byte. */
void func_15154C90(u8 *owner) {
    s8 expired;
    s32 method;
    s16 opacity;
    expired = 0;
    if (*(u16 *)(owner + 0x24) & 1) {
        *(s16 *)(owner + 0x22) = (u32)*(s16 *)(owner + 0x22) - (u32)D_800BE9E4;
        if (*(s16 *)(owner + 0x22) < 0) expired = 1;
    }
    if ((method = owner[0x68] & 15) && !expired) {
        if (!D_8008ACC8[method](owner)) expired = 1;
    }
    if ((*(u16 *)(owner + 0x24) & 8) &&
        *(s16 *)(owner + 0x22) < *(s16 *)(owner + 0x26)) {
        opacity = *(s16 *)(owner + 0x22) * *(s16 *)(owner + 0x28);
        if (opacity < owner[0x2E]) owner[0x2E] = opacity;
    }
    if (expired) func_1516972C(owner);
}

s32 func_15154D80() {
    return 0;
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_17CAF0/func_1515548C.s")

void func_15155564(u8 *arg0, s32 arg1, u8 arg2) {
    void (*callback)(u8 *, s32, u8) = D_8008AD04[arg0[0x2A]];

    if (callback != NULL) {
        callback(arg0, arg1, arg2);
    }
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_17CAF0/func_151555AC.s")

void func_1515572C(void *arg0, u8 arg1) {
    TwoWord17CAF0 tmp;

    tmp = *(TwoWord17CAF0 *) D_800A6038;
    func_15169260(&tmp, 2, arg0, arg1);
}
