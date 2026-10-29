#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/E7970.s. */

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

s32 func_150BA55C() {
    return 0;
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

s32 func_150BAA14() {
    return 0;
}
