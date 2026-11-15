#include <ultra64.h>

typedef struct { f32 x, y, z; } BindingVector150C4120;
typedef struct { s32 values[4]; } BindingPalette150C4120;
typedef struct {
    u8 *actor;
    u8 identity;
    u8 pad05[3];
    f32 zero08;
    u8 *effect;
    f32 zero10;
    s16 selector;
    s8 state;
    u8 pad17;
    s32 zero18;
} BindingPayload150C4120;
typedef struct {
    u8 first, second, width, height;
    f32 scale, horizontal, vertical;
} BindingRandom150C4120;
typedef struct {
    u32 flags00, zero04;
    s16 code08, lifetime;
    u32 zero0C, zero10;
    u8 rgba14[4], rgba18[4];
    u8 value1C, paletteIndex;
    s16 value1E, value20, value22;
    f32 scale, extentX, extentY;
    BindingVector150C4120 first, second, third;
    f32 zero54;
    u32 flags58, zero5C;
    u8 value60, value61, value62;
    s8 value63, value64, value65;
    u8 value66, pad67;
    s16 zero68;
    u8 pad6A[2];
    f32 coefficient;
} BindingDefinition150C4120;
extern BindingPalette150C4120 D_800A0340;
extern BindingVector150C4120 D_800A5480;
extern f32 D_800A03AC, D_800A03B0, D_800A03B4;
u8 *func_15149130(s16, s8, s8, s8, u8, u8, s32, u8, s32);
u8 *func_15130280(BindingDefinition150C4120 *, u8, void *, s32, u8, s32);
s32 func_150ADA20(void);
f32 func_150ADA68(void);
void *memcpy(void *, const void *, u32);


/* Non-matching placeholders for the text-only asm slice asm/F15D0.s. */

/* Bind the actor record to its randomized effect; either allocation may fail. */
void func_150C4120(u8 *actor, s16 requestedLifetime, u8 priority, s32 context) {
    BindingPayload150C4120 binding;
    s32 lifetime;
    s32 active;
    BindingDefinition150C4120 definition;
    BindingRandom150C4120 random;
    BindingPalette150C4120 palette;
    BindingPayload150C4120 *destination;
    u32 firstFlag;

    binding.actor = actor;
    binding.identity = actor[0x3B];
    binding.zero08 = 0.0f;
    binding.effect = 0;
    binding.zero10 = 0.0f;
    binding.selector = -1;
    binding.state = 0;
    binding.zero18 = 0;
    if (actor[4] == 0x34) {
        binding.selector = 0x54;
        binding.state = 1;
    }
    lifetime = requestedLifetime == -1 ? 300 : requestedLifetime;
    active = requestedLifetime == -1 ? 0 : 1;
    destination = (BindingPayload150C4120 *)func_15149130(lifetime, -1, 0x53, -1, active, 0x40,
                          sizeof(binding), priority, context);
    if (destination != 0) {
        destination = (BindingPayload150C4120 *)((u8 *)destination + 0x28);
        memcpy(destination, &binding, sizeof(binding));
        palette = D_800A0340;
        random.first = func_150ADA20();
        random.second = func_150ADA20();
        definition.extentY = 700.0f;
        definition.extentX = 700.0f;
        random.scale = 700.0f;
        random.width = (u32)func_150ADA20() % 6U + 5;
        random.height = (u32)func_150ADA20() % 6U + 5;
        random.horizontal = (func_150ADA68() * 0.25f + D_800A03AC) * random.scale;
        random.vertical = (func_150ADA68() * 0.25f + D_800A03B0) * random.scale;
        definition.paletteIndex = palette.values[(u32)func_150ADA20() & 3];
        definition.code08 = 0x2203;
        definition.flags00 = 0x200005;
        definition.zero04 = 0;
        definition.zero0C = 0;
        definition.zero10 = 0;
        definition.rgba14[0] = 0;
        definition.rgba14[1] = 0;
        definition.rgba14[2] = 0;
        definition.rgba14[3] = 255;
        definition.rgba18[0] = 0;
        definition.rgba18[1] = 0;
        definition.rgba18[2] = 0;
        definition.rgba18[3] = 255;
        definition.value1C = 255;
        definition.first = D_800A5480;
        definition.second = D_800A5480;
        definition.third = D_800A5480;
        definition.value22 = 1;
        definition.zero54 = 0.0f;
        definition.scale = 1.0f;
        firstFlag = ((u32)func_150ADA20() & 1) ? 0x40 : 0;
        definition.flags58 = (((u32)func_150ADA20() & 1) ? 0x80 : 0) | firstFlag | 0xC000;
        definition.lifetime = 300;
        definition.value1E = 1;
        definition.value20 = 255;
        definition.value60 = 6;
        definition.value61 = 8;
        definition.value64 = -1;
        definition.value62 = 0x26;
        definition.value63 = -1;
        definition.value65 = 0;
        definition.zero5C = 0;
        definition.value66 = 255;
        definition.zero68 = 0;
        definition.coefficient = D_800A03B4;
        if ((destination->effect = func_15130280(&definition, 1, 0, sizeof(random), priority, context)) != 0) {
            memcpy(destination->effect + 0xA8, &random, sizeof(random));
        }
    }
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_F15D0/func_150C44A4.s")

s32 func_150C4AD8(u8 *arg0) {
    u8 *temp_a1 = arg0;

    if (*(s32 volatile *)(temp_a1 + 0x34) != 0) {
        func_1516972C(*(s32 volatile *)(temp_a1 + 0x34));
    }
}

s32 func_150C4B08(s32 arg0) {
    func_150C4AD8(arg0);
    func_1514933C(arg0);
}

s32 func_150C4B34(s32 arg0) {
    func_150C4AD8(arg0);
    func_15149368(arg0);
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_F15D0/func_150C4B60.s")
