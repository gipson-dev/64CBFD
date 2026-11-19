#include <ultra64.h>

typedef struct {
    u8 pad0[0x1C];
    s16 timer;
    u8 pad1E[0xA];
    u8 value;
    u8 pad29[0x87];
    s16 limit;
    s16 scale;
} GeneratedE8090Record;

/* Recovered C for the text-only slice asm/E8090.s. */

typedef struct { u8 reserved[0x380]; f32 field380; u8 tail[0x61C]; } EffectAngleRecordE8090;
typedef struct { f32 height; u8 retained04[0x20]; } EffectSurfaceE8090;
typedef struct {
    u32 flags;
    s16 duration;
    u8 kind, reserved07;
    u32 zero08;
    s32 angle;
    u8 opacity, alpha, red, green, blue, alpha2, zero16, mode;
    u32 flags18, zero1C;
    u8 opacity20, reserved21[7];
} SurfaceEffectDescriptorE8090;
extern EffectAngleRecordE8090 *D_800DBFF0;
extern s32 D_80082FA4;
extern f32 D_8009FE70;
extern u8 *D_80088750;
s32 func_150ADA20(void);
f32 func_150ADA68(void);
void func_15142314(void *, s32, f32 *);
u8 func_15143E94(s32, s32);
s32 func_15165F80(s32, s32, s32, s32, s32, s32, s32, u8, s32);
void func_1514C678(f32, f32, f32, f32, s16, s16, s16, u8, s32, f32, void *, u8);
void func_1504715C(EffectSurfaceE8090 *, void *);
s32 func_15046C80(f32 *, u16, f32, EffectSurfaceE8090 *);
void *func_1513C73C(void *, u8, u8, void *, f32, f32, f32, f32, f32, u8, u8, s32, u8, s32);
s32 func_1518ABD0(u8 *, void *, u8);
void func_1516972C(void *);


/* Emit the selected attachment's paired angular effects and surface-linked child. */
/* The direct callers select attachment 0 or 1; other low-byte values have no index. */
void func_150BABE0(u8 *actor, u8 selector, u8 context) {
    f32 position[3];
    s32 attachment;
    s32 angle;
    EffectSurfaceE8090 surface;
    f32 probe[3];
    SurfaceEffectDescriptorE8090 descriptor;
    void *effect;
    f32 size;
    u32 third;
    f32 sample;
    u32 second;
    u32 first;

    angle = (s32)(D_800DBFF0[(u32)D_80082FA4].field380 * D_8009FE70);
    if (actor == 0 || *(s32 *)actor == 0 || *(s32 *)actor == 8) return;
    if (*(s32 *)(actor + 0x1D4) == 0) return;
    switch ((u8)selector) {
        case 0: attachment = 17; break;
        case 1: attachment = 26; break;
    }
    func_15142314((void *)*(s32 *)(actor + 0x1D4), attachment, position);
    position[1] = *(f32 *)(actor + 0x180);
    func_15143E94(5, 0x4022);
    func_15165F80(-1, (s32)position[0], (s32)(position[1] + 6.0f),
                  (s32)position[2], 25, 18, 0, (u8)context, 1);
    sample = func_150ADA68();
    func_1514C678(position[0], position[1], position[2], sample * 50.0f + 40.0f,
                 (s16)((u32)angle + 60U), (s16)((u32)angle - 60U), (u32)func_150ADA20() % 11U + 30U, 5, 0, 0.0f, 0, (u8)context);
    func_1504715C(&surface, actor);
    probe[0] = position[0];
    probe[1] = position[1] + 100.0f;
    probe[2] = position[2];
    if (func_15046C80(probe, 0, position[1] - 100.0f, &surface)) {
        size = func_150ADA68() * 200.0f + 200.0f;
        descriptor.kind = 42;
        descriptor.reserved07 = 0;
        descriptor.flags = 0x7340;
        descriptor.duration = 300;
        descriptor.zero08 = 0;
        descriptor.angle = (u32)func_150ADA20() % 2001U + 2000U;
        descriptor.opacity = 255;
        descriptor.alpha = 255;
        descriptor.red = 0;
        descriptor.green = 0;
        descriptor.blue = 0;
        descriptor.alpha2 = 255;
        descriptor.zero16 = 0;
        descriptor.mode = 13;
        descriptor.opacity20 = 255;
        descriptor.zero1C = 0;
        descriptor.flags18 = 0x170002;
        first = (u32)func_150ADA20();
        second = (u32)func_150ADA20();
        third = (u32)func_150ADA20();
        effect = func_1513C73C(&descriptor, 0, 0, (u8 *)&surface + 4,
                    position[0], surface.height, position[2], size, size,
                    first & 0xFFU, (third & 1U) + ((second & 1U) << 1), 4, (u8)context, 0);
        if (effect != 0 && func_1518ABD0(D_80088750, effect, 1) == 0) {
            func_1516972C(effect);
        }
    }
    sample = func_150ADA68();
    func_1514C678(position[0], position[1], position[2], sample * 40.0f + 60.0f,
                 (s16)((u32)angle + 60U), (s16)((u32)angle - 60U), (u32)func_150ADA20() % 7U + 6U, 6, 0, 0.0f, 0, (u8)context);
}

s32 func_150BAFEC() {
    return 0;
}

extern s32 D_800BE9E4;
typedef struct { u8 pad00[0x58]; f32 x, pad5C, z; u8 pad64[0x44]; f32 damping; } DampingState150BB260;
/* Apply one damping step for each elapsed tick. */
s32 func_150BB260(DampingState150BB260 *state, s32 unused) {
    u32 ticks;
    f32 *factor = &state->damping;
    for (ticks = (u32)D_800BE9E4; ticks != 0; ticks--) {
        state->x *= *factor;
        state->z *= *factor;
    }
    return 1;
}

void func_150BB408(u8 *arg0) {
    *(u32 *) (arg0 + 0x18) |= 1;
    *(s16 *) (arg0 + 0x1C) = 0x32;
    *(s16 *) (arg0 + 0xB0) = *(s16 *) (arg0 + 0x1C);
    *(s16 *) (arg0 + 0xB2) = 5;
    func_1513F6C0(arg0, 6, *(arg0 + 0x81));
}

s32 func_150BB450(u8 *arg0) {
    GeneratedE8090Record *self = (void *) arg0;
    s32 temp_v0 = self->timer;

    if (temp_v0 < self->limit) {
        s32 temp_v1 = (s16) (temp_v0 * (u32) self->scale);

        if (temp_v1 < self->value) {
            self->value = temp_v1;
        }
    }
    return 1;
}

s32 func_150BB498() {
    return 0;
}
