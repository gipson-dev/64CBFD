#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/F3270.s. */

s32 func_150C6460();
s32 func_150C5F94();

void func_150C5DC0(u8 *arg0) {
    if (*(u32 *) (arg0 + 0x58) != 0) {
        u8 *temp_v0 = *(u8 **) (arg0 + 0x58) + 0xB0;

        *(temp_v0 + 4) = 1;
    } else {
        *(u32 *) (arg0 + 0x58) = func_150C6460(arg0);
    }
}

typedef struct {
    u32 opaque0;
    u8 notification;
    u8 opaque5[3];
    f32 base;
    f32 amplitude;
    f32 target;
    s16 remaining;
    s16 minimum;
    s16 range;
    u16 opaque1A;
    f32 gain;
} EmbeddedIntegerOscillator;
extern s32 D_800BE9E4;
s32 func_150ADA20(void);
f32 func_150ADA68(void);
/* Capture and clear notification, renew expired timing, then blend the signed rate. */
s32 func_150C5E0C(u8 *input) {
    EmbeddedIntegerOscillator *oscillator;
    s8 notified;
    oscillator = (EmbeddedIntegerOscillator *)(input + 0xB0);
    notified = 1;
    if (oscillator->notification == 0) notified = 0;
    oscillator->notification = 0;
    oscillator->remaining -= (u32)D_800BE9E4;
    if (oscillator->remaining < 0) {
        u32 randomValue;
        randomValue = (u32)func_150ADA20();
        oscillator->remaining = randomValue % (oscillator->range + 1) + oscillator->minimum;
        oscillator->target = func_150ADA68();
        oscillator->target = oscillator->target * oscillator->amplitude + oscillator->base;
    }
    *(s32 *)(input + 0x24) = (u32)(s32)((oscillator->target - (f32)*(s32 *)(input + 0x24)) * oscillator->gain) + (u32)*(s32 *)(input + 0x24);
    return notified;
}

// Retail retains the otherwise dead temp_v0 + 0x58 update before the call.
#pragma GLOBAL_ASM("asm/nonmatchings/generated_F3270/func_150C5EFC.s")

void func_150C5F40(u8 *arg0) {
    u8 *owner = *(u8 **)(arg0 + 0x18);

    if (*(u32 *)(arg0 + 0x5C) != 0) {
        u8 *record = *(u8 **)(arg0 + 0x5C) + 0x58;

        *(record + 4) = 1;
    } else {
        *(u32 *)(arg0 + 0x5C) = func_150C5F94(owner, arg0);
    }
}

typedef struct { u8 *context; u8 active; u8 pad[3]; f32 height; } HeightPayload;
typedef struct {
    u32 zero0, zero4;
    u8 color; u8 pad09[3];
    u8 *owner;
    u8 flag; u8 pad11[3];
    f32 x, y, z, size, rate;
    s16 duration;
    u8 kind, variant, mode, extra;
    u8 pad2e[2];
} HeightDescriptor;
extern f32 D_800A0410, D_800A0414, D_800A0418;
s32 func_15045800(f32 *, u16, f32, void *);
void *func_1513418C(void *, s32, u8, s32);
void *memcpy(void *, const void *, u32); /* Attach the ground-height payload to a new owner effect. */
s32 func_150C5F94(u8 *owner, u8 *context) {
    HeightDescriptor desc;
    struct { f32 point[3]; u32 gap; HeightPayload payload; } local;
    u8 *effect;
    local.payload.context = context;
    local.payload.active = 1;
    local.point[0] = *(f32 *)(owner + 0x14);
    local.point[1] = *(f32 *)(owner + 0x18) + D_800A0410;
    local.point[2] = *(f32 *)(owner + 0x1C);
    if (func_15045800(local.point, 0, *(f32 *)(owner + 0x18) - 100.0f, context + 0x34)) {
        local.payload.height = *(f32 *)(context + 0x34);
    } else {
        local.payload.height = *(f32 *)(owner + 0x18) + D_800A0414;
    }
    desc.zero0 = 0;
    desc.zero4 = 0;
    desc.color = owner[0x3B];
    desc.owner = owner;
    desc.flag = 0;
    desc.x = 0.0f;
    desc.y = 0.0f;
    desc.z = 0.0f;
    desc.size = 25.0f;
    desc.rate = D_800A0418;
    desc.duration = 300;
    desc.kind = 10;
    desc.variant = 4;
    desc.mode = 1;
    desc.extra = 2;
    effect = func_1513418C(&desc, 12, 255, 0);
    if (effect != 0) memcpy(effect + 0x58, &local.payload, 12);
    return (s32)effect;
}

typedef struct {
    f32 scale;
    u8 first0, first1, first2, first3;
    f32 firstX, firstY, firstRange, firstRate;
    u8 second0, second1, second2, second3;
    f32 secondX, secondY, ownerHeight;
} PairedRandomPayload;
typedef struct {
    u32 flags, unused04;
    u16 kind, randomSize;
    u32 unused0c, unused10;
    u8 channel[8];
    u8 alpha, color;
    s16 duration, count, zero22;
    f32 zero24, scale0, scale1;
    f32 x, y, z, zero3c, zero40, zero44;
    f32 dx, zero4c, dz, angle;
    u32 options, untouched5c;
    u8 variant0, variant1, variant2;
    s8 variant3;
    u8 untouched64[12];
} PairedRandomDescriptor;
extern f32 D_800A041C, D_800A0420, D_800A0424, D_800A0428;
extern f32 D_800A042C, D_800A0430, D_800A0434, D_800A0438;
void *func_151303BC(void *, u8, s32); /* Build a randomized owner effect and its copied payload. */
void func_150C60D8(f32 x, f32 y, f32 z, f32 dx, s32 ignored, f32 dz, u8 *owner) {
    struct { PairedRandomPayload payload; u32 gap; PairedRandomDescriptor descriptor; } local;
    local.descriptor.kind = 0xC01;
    local.descriptor.color = 0x2F;
    local.descriptor.flags = 0x200005;
    local.descriptor.unused04 = 0;
    local.descriptor.channel[6] = 0;
    local.descriptor.channel[5] = 0;
    local.descriptor.channel[4] = 0;
    local.descriptor.channel[3] = 0;
    local.descriptor.channel[2] = 0;
    local.descriptor.channel[1] = 0;
    local.descriptor.channel[0] = 0;
    local.descriptor.unused10 = 0;
    local.descriptor.unused0c = 0;
    local.descriptor.alpha = 255;
    local.descriptor.zero22 = 0;
    local.descriptor.zero24 = 0.0f;
    local.descriptor.options = 0x3207;
    local.descriptor.variant0 = 5;
    local.descriptor.variant1 = 5;
    local.descriptor.variant2 = 4;
    local.descriptor.variant3 = -1;
    local.descriptor.x = x;
    local.descriptor.y = y;
    local.descriptor.zero3c = 0.0f;
    local.descriptor.zero40 = 0.0f;
    local.descriptor.zero44 = 0.0f;
    local.descriptor.duration = 30;
    local.descriptor.count = 8;
    local.descriptor.z = z;
    local.payload.ownerHeight = *(f32 *)(owner + 0x60);
    local.payload.firstRange = 4.0f;
    local.payload.firstRate = 0.25f;
    local.descriptor.dx = -dx * D_800A041C;
    local.descriptor.dz = -dz * D_800A041C;
    local.payload.first0 = 0;
    local.payload.first1 = 0;
    local.payload.second0 = 0;
    local.payload.second1 = 0;
    local.descriptor.zero4c = 0.0f;
    if (func_150ADA20() & 1) local.descriptor.options |= 0x40;
    if (func_150ADA20() & 1) local.descriptor.options |= 0x80;
    local.descriptor.randomSize = ((u32)func_150ADA20() % 51U) + 106;
    local.descriptor.channel[7] = ((u32)func_150ADA20() % 101U) + 100;
    local.payload.scale = func_150ADA68() * 62.0f + 41.0f;
    local.descriptor.scale0 = local.payload.scale;
    local.descriptor.scale1 = local.payload.scale;
    local.payload.first2 = (u32)func_150ADA20() % 5U + 4;
    local.payload.first3 = (u32)func_150ADA20() % 5U + 4;
    local.payload.firstX = (func_150ADA68() * 0.25f + D_800A0420) * local.payload.scale;
    local.payload.firstY = (func_150ADA68() * 0.25f + D_800A0424) * local.payload.scale;
    local.payload.second2 = (u32)func_150ADA20() % 5U + 4;
    local.payload.second3 = (u32)func_150ADA20() % 5U + 4;
    local.payload.secondX = (func_150ADA68() * D_800A0428 + D_800A042C) * local.payload.scale;
    local.payload.secondY = (func_150ADA68() * D_800A0430 + D_800A0434) * local.payload.scale;
    local.descriptor.angle = (func_150ADA68() * 60.0f + 21.0f) * D_800A0438;
    owner = func_151303BC(&local.descriptor, 2, 40);
    if (owner != 0) memcpy(owner + 0xA8, &local.payload, 40);
}

s32 func_150C63EC(u8 *arg0) {
    s32 result = 1;

    if (*(u8 *)(arg0 + 0x5C) == 0) {
        result = 0;
    }
    *(u8 *)(arg0 + 0x5C) = 0;
    return result;
}

s32 func_150C6410(u8 *arg0) {
    u8 *temp_v0 = *(u8 **)(arg0 + 0x58) + 0x58;

    *(s32 *)(temp_v0 + 0x4) = 0;
    func_151346EC(arg0);
}

s32 func_150C6438(u8 *arg0) {
    u8 *temp_v0 = *(u8 **)(arg0 + 0x58) + 0x58;

    *(s32 *)(temp_v0 + 0x4) = 0;
    func_1513470C(arg0);
}

typedef struct {
    u8 *owner;
    u8 enabled, pad05[3];
    f32 base, range, zero;
    s16 zero14, count0, count1;
    u8 pad1a[2];
    f32 rate;
} GroundEffectPayload;
typedef struct {
    u32 flags;
    s16 duration;
    u8 kind, pad07;
    u32 zero08;
    s32 angle;
    u8 opacity, alpha, red, green, blue, alpha2, zero16, mode;
    u32 flags18;
    u8 untouched1c[12];
} GroundEffectDescriptor;
typedef struct { f32 coords[3]; } GroundVectorWords;
extern GroundVectorWords D_800887D0;
extern f32 D_800A043C,D_800A0440;
extern u8 D_800AB414[];
void func_15143134(f32 *, f32 *, u8 *);
s32 func_15045800(f32 *, u16, f32, void *);
s32 func_151D8E20(void); /* Create a ground-linked effect and its owner payload. */
u8 *func_1513C73C(s32,u8,u8,s32,f32,f32,f32,f32,f32,u8,u8,s32,u8,s32);
s32 func_150C6460(u8 *context) {
    struct {
        f32 scale;
        GroundEffectPayload payload;
        GroundEffectDescriptor descriptor;
        f32 query[3];
        GroundVectorWords preset;
        u32 gap74;
        f32 position[3];
        u8 *result;
    } local;
    u8 index;
    u8 *actor;
    u32 second;
    u32 first;
    local.result = 0;
    actor = *(u8 **)(context + 0x18);
    if (*(u8 **)(actor + 0x1D4) != 0) {
        local.preset = D_800887D0;
        func_15143134(local.preset.coords, local.position, *(u8 **)(actor + 0x1D4));
    } else {
        local.position[0] = *(f32 *)(actor + 0x14);
        local.position[1] = *(f32 *)(actor + 0x18);
        local.position[2] = *(f32 *)(actor + 0x1C);
    }
    local.query[0] = local.position[0];
    local.query[1] = local.position[1] + 200.0f;
    local.query[2] = local.position[2];
    if (func_15045800(local.query, 0, local.position[1] - 200.0f, context + 0x34)) {
        index = func_151D8E20();
        local.query[1] = *(f32 *)(context + 0x34);
        local.scale = func_150ADA68() * 50.0f + 100.0f;
        local.payload.owner = context;
        local.payload.enabled = 1;
        local.payload.base = D_800A043C;
        local.payload.range = 32768.0f;
        local.payload.zero = 0.0f;
        local.payload.zero14 = 0;
        local.payload.count0 = 10;
        local.payload.count1 = 10;
        local.payload.rate = D_800A0440;
        local.descriptor.flags = 0x20300;
        local.descriptor.duration = 300;
        local.descriptor.kind = 0x38;
        local.descriptor.zero08 = 0;
        local.descriptor.angle = (s32)(32768.0f * 0.5f + D_800A043C);
        local.descriptor.opacity = 150;
        local.descriptor.alpha = 255;
        actor = D_800AB414 + index * 3;
        local.descriptor.red = actor[0];
        local.descriptor.green = actor[1];
        local.descriptor.blue = actor[2];
        local.descriptor.alpha2 = 255;
        local.descriptor.zero16 = 0;
        local.descriptor.mode = 6;
        local.descriptor.flags18 = 0x440001;
        first = (u32)func_150ADA20();
        second = (u32)func_150ADA20();
        local.result = func_1513C73C((s32)&local.descriptor, 8, 2, (s32)(context + 0x38),
            local.query[0], local.query[1], local.query[2], local.scale, local.scale,
            first & 255, (((u32)func_150ADA20() & 1) << 1) + (second & 1),
            32, context[0x0C], context[1]);
        if (local.result != 0) memcpy(local.result + 0xB0, &local.payload, 32);
    }
    return (s32)local.result;
}
