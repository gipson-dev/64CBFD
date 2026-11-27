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
void func_15165F80(s32, s32, s32, s32, s32, s32, s32, u8, s32);
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

/* The descriptor's unspecified words and tail are retained for the factory. */
typedef struct {
    u32 field00, field04;
    s16 field08, field0A;
    u32 field0C, field10;
    u8 field14, field15, field16, field17;
    u8 field18, field19, field1A, field1B;
    u8 field1C, field1D;
    s16 field1E, field20, field22;
    f32 field24, field28, field2C;
    f32 position[3];
    u32 retained3C[3];
    f32 velocity[3];
    f32 field54;
    u32 flags;
    u32 retained5C;
    u8 field60, field61;
    s8 field62, field63;
    u8 retained64[12];
} AngularEmitterDescriptorE8090;
extern f32 D_8009FE74, D_8009FE78;
f32 func_151423D8(u8);
void *func_15130374(void *, u8, s32, u8, s32);
void *memcpy(void *, const void *, size_t);


/* Build an angular emitter from the callback's fifteen o32 argument words. */
/* Unused words keep their original positions in the shared callback interface. */
s32 func_150BAFEC(s32 unused0, s16 unused1, f32 x, f32 y, f32 z,
                  f32 unused5, f32 unused6, f32 unused7, u32 heading,
                  u8 unused9, f32 unused10, s32 unused11, f32 unused12,
                  s32 unused13, u8 context) {
    AngularEmitterDescriptorE8090 descriptor;
    void *result;
    f32 extra;
    s16 pitch;
    f32 headingCosine;
    f32 headingSine;
    f32 pitchCosine;
    f32 pitchSine;
    f32 speed;

    headingCosine = func_151423D8((u8)(heading - 64U));
    headingSine = func_151423D8((u8)heading);
    descriptor.field1D = 41;
    descriptor.field08 = 0xE03;
    descriptor.field00 = 0x200005;
    descriptor.field04 = 0;
    descriptor.field0A = (u32)func_150ADA20() % 36U + 70U;
    descriptor.field0C = 0;
    descriptor.field10 = 0;
    descriptor.field18 = 176;
    descriptor.field19 = 160;
    descriptor.field1A = 42;
    descriptor.field14 = 64;
    descriptor.field15 = 11;
    descriptor.field16 = 106;
    descriptor.field17 = 255;
    descriptor.field1B = (u32)func_150ADA20() % 52U + 90U;
    descriptor.field1C = 255;
    descriptor.field60 = 3;
    descriptor.field61 = 3;
    descriptor.field28 = descriptor.field2C = func_150ADA68() * 165.0f + 800.0f;
    descriptor.position[0] = x;
    descriptor.position[1] = y;
    descriptor.position[2] = z;
    pitch = (u32)func_150ADA20() % 11U - 12U;
    pitchCosine = func_151423D8((u8)(pitch - 64));
    pitchSine = func_151423D8((u8)pitch);
    speed = func_150ADA68() * 11.0f + 15.0f;
    descriptor.flags = 0xE05;
    descriptor.velocity[0] = (speed * pitchSine) * headingCosine;
    descriptor.velocity[1] = -speed * pitchCosine;
    descriptor.velocity[2] = (speed * pitchSine) * headingSine;
    descriptor.field54 = 0.0f;
    if ((u32)func_150ADA20() & 1U) descriptor.flags |= 0x40;
    if ((u32)func_150ADA20() & 1U) descriptor.flags |= 0x80;
    descriptor.field62 = 2;
    descriptor.field63 = -1;
    descriptor.field1E = 22;
    descriptor.field20 = 11;
    descriptor.field22 = 1;
    descriptor.field24 = D_8009FE74;
    extra = D_8009FE78;
    result = func_15130374(&descriptor, 0, 4, context, 1);
    if (result != 0) memcpy((u8 *)result + 0xA8, &extra, 4);
    return 1;
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

/* Retail copies the full descriptor, including its unspecified reserved bytes. */
typedef struct {
    f32 field00, field04, field08, field0C;
    f32 rotation[3], scale[3], position[3], velocity[3];
    f32 field40, field44, field48, field4C;
    u32 flags;
    s16 duration;
    u16 resource;
    u8 field58, retained59[3];
    u32 field5C;
    u8 field60, field61, field62, field63, field64, field65, field66, field67, field68;
    u8 retained69, field6A, retained6B;
    u32 field6C;
    u8 field70, retained71;
    s16 field72, field74;
    u8 retained76[6];
} ExtendedEmitterDescriptorE8090;
extern f32 D_8009FE7C, D_8009FE80, D_8009FE84, D_8009FE88, D_8009FE8C;
void *func_15132A4C(void *, s32, s32, s32, u8, s32);


/* Emit the extended angular effect through the shared fifteen-word callback ABI. */
s32 func_150BB498(s32 unused0, s16 unused1, f32 x, f32 y, f32 z,
                  f32 unused5, f32 unused6, f32 unused7, u32 heading,
                  u8 unused9, f32 unused10, s32 unused11, f32 unused12,
                  s32 unused13, u8 context) {
    s16 pitch;
    f32 headingCosine;
    f32 headingSine;
    f32 pitchCosine;
    f32 pitchSine;
    f32 speed;
    ExtendedEmitterDescriptorE8090 descriptor;

    headingCosine = func_151423D8((u8)(heading - 64U));
    headingSine = func_151423D8((u8)heading);
    descriptor.flags = 0x9E8;
    descriptor.rotation[0] = 0.0f;
    descriptor.rotation[1] = 0.0f;
    descriptor.rotation[2] = 0.0f;
    descriptor.scale[0] = 1.0f;
    descriptor.scale[1] = 1.0f;
    descriptor.scale[2] = 1.0f;
    descriptor.position[0] = x;
    descriptor.position[1] = y;
    descriptor.position[2] = z;
    descriptor.field04 = D_8009FE7C;
    pitch = (u32)func_150ADA20() % 13U - 52U;
    pitchCosine = func_151423D8((u8)(pitch - 64));
    pitchSine = func_151423D8((u8)pitch);
    speed = func_150ADA68() * 9.0f + 3.0f;
    descriptor.velocity[0] = (speed * pitchSine) * headingCosine;
    descriptor.velocity[1] = -speed * pitchCosine;
    descriptor.velocity[2] = (speed * pitchSine) * headingSine;
    descriptor.field40 = func_150ADA68() * 50.0f + -25.0f;
    descriptor.field44 = 0.0f;
    descriptor.field48 = func_150ADA68() * 50.0f + -25.0f;
    descriptor.duration = (u32)func_150ADA20() % 68U + 38U;
    descriptor.field4C = func_150ADA68() * D_8009FE80 + D_8009FE84;
    descriptor.field00 = 1.0f;
    descriptor.field08 = descriptor.field0C = func_150ADA68() * D_8009FE88 + D_8009FE8C;
    descriptor.resource = 31;
    descriptor.field58 = 0;
    descriptor.field5C = 0;
    descriptor.field60 = 255;
    descriptor.field61 = 1;
    descriptor.field62 = 0;
    descriptor.field63 = 0;
    descriptor.field64 = 0;
    descriptor.field65 = 0;
    descriptor.field66 = 0;
    descriptor.field67 = 0;
    descriptor.field68 = 0;
    descriptor.field6A = 0;
    descriptor.field6C = 0;
    descriptor.field70 = 0;
    descriptor.field72 = 1;
    descriptor.field74 = 255;
    func_15132A4C(&descriptor, 3, 255, 0, context, 0);
    return 1;
}
