#include <ultra64.h>

/* Recovered C for the text-only slice asm/E7970.s. */

typedef struct {
    void *source;
    u8 sourceByte;
    u8 reserved[3];
    f32 value;
} EffectPayload;
s32 func_150ADA20(void);
void *func_15149130(s16, s8, s8, s8, u8, u8, s32, u8, s32);
void *memcpy(void *, const void *, u32);

/* Capture the source payload and attach it to a randomized effect. */
void func_150BA4C0(void *source, u8 variant, s32 parameter) {
    EffectPayload payload;
    u8 *effect;
    payload.source = source;
    payload.sourceByte = ((u8 *)source)[0x3B];
    payload.value = 0.0f;
    effect = func_15149130((s16)((u32)func_150ADA20() % 9 + 15), -1, 0x52, -1,
                          1, 0x3F, 0xC, variant, parameter);
    if (effect != 0) {
        memcpy(effect + 0x28, &payload, 12);
    }
}

typedef struct { f32 x, y, z; } AttachedEmitterPointE7970;
extern f32 D_800BE9A4;
extern f32 D_8009FE30, D_8009FE34, D_8009FE38, D_8009FE3C;
extern f32 D_8009FE40, D_8009FE44, D_8009FE48, D_8009FE4C;
extern f32 D_8009FE50, D_8009FE54, D_8009FE58;
f32 func_150ADA68(void);
void func_1515C244(void *, AttachedEmitterPointE7970 *, f32 *, f32 *);
void func_15143794(s16, s16, f32, AttachedEmitterPointE7970 *);
void *func_1518A3C0(AttachedEmitterPointE7970 *, AttachedEmitterPointE7970 *, f32,
    AttachedEmitterPointE7970 *, AttachedEmitterPointE7970 *, f32, f32, u8, s16,
    u8, s32, u8, s32);


/* Emit attached effects while the live fractional accumulator is strictly above one. */
void func_150BA55C(u8 *effect) {
    EffectPayload *payload = (EffectPayload *)(effect + 0x28);
    u8 *source = payload->source;
    AttachedEmitterPointE7970 origin;
    f32 radius, unusedHeight;
    AttachedEmitterPointE7970 acceleration;
    f32 sizeFactor;
    AttachedEmitterPointE7970 position;
    AttachedEmitterPointE7970 rotation;
    AttachedEmitterPointE7970 velocity;
    f32 accelerationBase, accelerationRange;
    f32 sample, spread, sizeSample, speedSample;
    u32 firstRandom, secondRandom, durationRandom;
    s32 heading;

    if (*(u32 *)source == 0 || payload->sourceByte != source[0x3B]) {
        *(s16 *)(effect + 0xE) = -1;
        return;
    }
    if (*(u32 *)(source + 0x1D4) == 0) return;

    sample = func_150ADA68();
    payload->value += (D_8009FE30 + sample * D_8009FE34) * D_800BE9A4;
    if (1.0f < payload->value) {
        sizeFactor = (*(f32 *)(source + 0x14C) + *(f32 *)(source + 0x150)) * 0.5f;
        heading = (*(u16 *)(source + 0x76) >> 8) - 0x40;
        func_1515C244(source, &origin, &radius, &unusedHeight);
        accelerationBase = D_8009FE38;
        accelerationRange = D_8009FE3C;
        acceleration.y = 0.0f;
        do {
            firstRandom = (u32)func_150ADA20();
            secondRandom = (u32)func_150ADA20();
            func_15143794((s16)(firstRandom % 127U + heading - 63),
                (s16)(secondRandom % 31U - 50), radius, &position);
            position.y *= *(f32 *)(source + 0xF0);
            position.x += origin.x;
            position.y += origin.y;
            position.z += origin.z;
            rotation.x = func_150ADA68() * 360.0f;
            rotation.y = func_150ADA68() * 360.0f;
            rotation.z = func_150ADA68() * 360.0f;
            sample = func_150ADA68();
            spread = sample * D_8009FE40 + D_8009FE44;
            velocity.x = (position.x - origin.x) * spread;
            velocity.y = (position.y - origin.y) * spread;
            velocity.z = (position.z - origin.z) * spread;
            acceleration.x = func_150ADA68() * accelerationRange + accelerationBase;
            acceleration.z = func_150ADA68() * accelerationRange + accelerationBase;
            sizeSample = func_150ADA68();
            speedSample = func_150ADA68();
            durationRandom = (u32)func_150ADA20();
            func_1518A3C0(&position, &rotation,
                (sizeSample * D_8009FE48 + D_8009FE4C) * sizeFactor, &velocity,
                &acceleration, speedSample * D_8009FE50 + D_8009FE54,
                D_8009FE58, 7, durationRandom % 41U + 60, 0, 0,
                effect[0xC], effect[1]);
            payload->value -= 1.0f;
        } while (1.0f < payload->value);
    }
}


void func_150BA8F0(u8 *arg0, s32 arg1, u8 arg2) {
    func_15149514(arg1, arg2, (s32) (arg0 + 0x28), (s32) (arg0 + 0x2C), (s32) arg0);
}

typedef struct HeightResult71820 HeightResult71820;
typedef struct HeightActor71820 HeightActor71820;
extern f32 D_8009FE60;
void func_1504715C(HeightResult71820 *, HeightActor71820 *);
s32 func_15046C80(f32 *, u16, f32, HeightResult71820 *);
/* Copy the actor position and optionally query the vertical interval around it. */
s32 func_150BA930(f32 *position, u8 *actor, HeightResult71820 *result, u8 unused) {
    f32 start[3];

    position[0] = *(f32 *)(actor + 0x14);
    if (D_8009FE60 < *(f32 *)(actor + 0x180)) {
        position[1] = *(f32 *)(actor + 0x180);
    } else {
        position[1] = *(f32 *)(actor + 0x18);
    }
    position[2] = *(f32 *)(actor + 0x1C);
    if (result == 0) {
        return 1;
    }
    start[0] = position[0];
    start[1] = position[1] + 100.0f;
    start[2] = position[2];
    func_1504715C(result, (HeightActor71820 *)actor);
    return func_15046C80(start, 0, position[1] - 100.0f, result);
}

s32 func_150BAA00(s32 arg0, s32 arg1) {
    return 9;
}

/* Opaque 36-byte height-query output; its fields are not interpreted here. */
struct HeightResult71820 { u32 words[9]; };
typedef struct { u8 reserved[0x380]; f32 field380; u8 tail[0x61C]; } EffectAngleRecordE7970;
extern EffectAngleRecordE7970 *D_800DBFF0;
extern s32 D_80082FA4;
extern f32 D_8009FE64;
void func_151D5404(f32 *, f32, f32, f32, s32, s32, s32, s32);
u8 func_15143E94(s32, s32);
s32 func_15165F80(s32, s32, s32, s32, s32, s32, s32, u8, s32);
void func_1514C678(f32, f32, f32, f32, s16, s16, s16, u8, s32, f32, void *, u8);


/* Query an actor position, then submit the gated coordinate and angular effects. */
/* Preserve the selector byte and the callback interface's unused third word. */
void func_150BAA14(u8 *actor, s32 selector, s32 unused) {
    f32 position[3];
    HeightResult71820 surface;
    s32 angle;
    u8 hit;
    u32 random;
    f32 sample;

    if (*(u32 *)(actor + 0x1D4) == 0) return;
    hit = func_150BA930(position, actor, &surface, (u8)selector);
    func_151D5404(position, 1307.0f, 2000.0f, 0.0005f, 12, 15, 255, 0);
    func_15143E94(5, 0x4022);
    if (hit != 0) {
        angle = (s32)(D_800DBFF0[(u32)D_80082FA4].field380 * D_8009FE64);
        func_15165F80(-1, (s32)position[0], (s32)(position[1] + 6.0f),
                      (s32)position[2], 25, 18, 0, 255, 1);
        sample = func_150ADA68();
        random = (u32)func_150ADA20();
        func_1514C678(position[0], position[1], position[2], sample * 50.0f + 40.0f,
                     (s16)((u32)angle + 60U), (s16)((u32)angle - 60U),
                     random % 11U + 30U, 5, 0, 0.0f, 0, 255);
    }
}
