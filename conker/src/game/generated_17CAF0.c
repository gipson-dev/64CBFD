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

s32 func_15152874() {
    return 0;
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

s32 func_15152B38() {
    return 0;
}

s32 func_15152F70() {
    return 0;
}

s32 func_15153298() {
    return 0;
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_17CAF0/func_15153634.s")

s32 func_151539B4() {
    return 0;
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
