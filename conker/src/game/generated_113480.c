#include <ultra64.h>
#include "structs.h"

/* Non-matching placeholders for the text-only asm slice asm/113480.s. */

s32 func_150E5FD0() {
    return 0;
}

extern f32 D_800BE9A4;
extern s32 (*D_80088A10[])(u8 *);
f32 func_15144A74(f32 *, f32 *);
/* Advance motion and dispatch the configured crossing effect when its sign changes. */
s32 func_150E6230(u8 *actor) {
    u8 *state = actor + 0x110;
    f32 delta[3];
    f32 speed, vx, vy, vz, sign;
    s8 result = 1;
    if (state[0] & 1) {
        delta[0] = *(f32 *)(state + 4) - *(f32 *)(actor + 0x34);
        delta[1] = *(f32 *)(state + 8) - *(f32 *)(actor + 0x38);
        delta[2] = *(f32 *)(state + 12) - *(f32 *)(actor + 0x3C);
        sign = func_15144A74(delta, (f32 *)(state + 4)) < 0.0f ? -1.0f : 1.0f;
        if (sign != *(f32 *)(state + 0x28)) {
            s8 selector = *(s8 *)(state + 0x2C);
            result = 0;
            if (selector != -1) {
                result = (s8)D_80088A10[selector](actor);
            }
        }
    }
    speed = *(f32 *)(actor + 0x50);
    vx = *(f32 *)(actor + 0x40) * speed;
    vy = *(f32 *)(actor + 0x44) * speed;
    vz = *(f32 *)(actor + 0x48) * speed;
    *(f32 *)(actor + 0x34) += vx * D_800BE9A4;
    *(f32 *)(actor + 0x38) += vy * D_800BE9A4;
    *(f32 *)(actor + 0x3C) += vz * D_800BE9A4;
    return result;
}

s32 func_150E63A0() {
    return 0;
}

s32 func_150E679C(u8 *arg0) {
    s32 temp_v0 = *(s16 *)(arg0 + 0x1C);

    if (temp_v0 < 8) {
        s32 temp_v1 = temp_v0 << 5;
        if (temp_v1 < *(u8 *)(arg0 + 0x5C)) {
            *(u8 *)(arg0 + 0x5C) = temp_v1;
        }
    }
    return 1;
}

typedef struct {
    s32 flags;
    s16 lifetime;
    u8 kind;
    u8 pad7;
    s32 value8;
    s32 valueC;
    u8 value10, value11, value12, value13, value14, value15;
    u8 pad16[2];
    s32 resource;
    u8 pad1C[12];
} ActorEffectDescriptor;
s32 func_150ADA20(void);
struct210 *func_1513C73C(s32, u8, u8, s32, f32, f32, f32, f32, f32, u8, u8, s32, u8, s32);

/* Submit an effect descriptor using the actor's live position and tags. */
s32 func_150E67D0(u8 *actor) {
    f32 *position;
    f32 range;
    ActorEffectDescriptor descriptor;

    descriptor.kind = 0x3A;
    descriptor.flags = 1;
    descriptor.lifetime = 100;
    descriptor.value8 = 0;
    descriptor.valueC = 0;
    descriptor.value10 = 255;
    descriptor.value11 = 255;
    descriptor.value12 = 0;
    descriptor.value13 = 0;
    descriptor.value14 = 0;
    descriptor.value15 = 255;
    descriptor.resource = 0x130001;
    range = 50.0f;
    position = (f32 *)(actor + 0x110);
    func_1513C73C((s32)&descriptor, 0, 0, (s32)(position + 5),
                 position[1], position[2], position[3], range, range,
                 func_150ADA20() & 255, 0, 0, actor[0xC], actor[1]);
    return 0;
}
