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

s32 func_150C60D8() {
    return 0;
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

s32 func_150C6460() {
    return 0;
}
