#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/1F3780.s. */

s32 func_151C69CC();

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1F3780/func_151C62D0.s")

void func_151C6974(s32 arg0, u8 arg1, s32 arg2) {
    func_151C69CC(arg0, arg2, 0, arg2);
}

void func_151C69A0(s32 arg0, u8 arg1, s32 arg2) {
    func_151C69CC(arg0, arg2, 1, arg2);
}


#pragma GLOBAL_ASM("asm/nonmatchings/generated_1F3780/func_151C69CC.s")


s32 func_151C6A28() {
    return 0;
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1F3780/func_151C6D70.s")

s32 func_151C6EA0() {
    return 0;
}

typedef struct {
    u8 pad00[0x4C];
    f32 scale;
    u8 pad50[0x34];
    u16 kind;
} Effect151C7038;
typedef struct {
    u8 pad00[0x60];
    u32 flags;
    u8 pad64[0x0C];
    u8 intensity;
    u8 pad71[0x0B];
    Effect151C7038 *effect;
} Owner151C7038;
s32 func_15142A5C(s32 *effect);

/* Update effect status and scaled intensity for effect type 0xE9. */
s32 func_151C7038(Owner151C7038 *owner) {
    Effect151C7038 *effect = owner->effect;
    f32 intensity;

    if (effect->kind != 0xE9) {
        return 0;
    }
    if (func_15142A5C((s32 *)effect) != 0) {
        owner->flags |= 0x20000;
    } else {
        owner->flags &= ~0x20000;
    }
    intensity = effect->scale * 35.0f;
    if (intensity > 255.0f) {
        intensity = 255.0f;
    } else if (intensity < 0.0f) {
        intensity = 0.0f;
    }
    owner->intensity = (u32)intensity;
    return 1;
}
