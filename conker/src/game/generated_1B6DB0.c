#include <ultra64.h>

typedef struct {
    u8 retained00[0x08];
    f32 positionX;
    f32 positionY;
    f32 positionZ;
    f32 velocityX;
    f32 velocityY;
    f32 velocityZ;
    u8 retained20[0x30];
} MotionEffectDescriptor15189900;

typedef struct {
    u8 retained00[0x10];
    MotionEffectDescriptor15189900 descriptor;
    s16 age;
    u8 retained62[2];
    f32 elapsed;
    f32 baselineY;
    s32 spatialHandle;
    u8 enabled;
    u8 retained71[7];
} MotionEffect15189900;

void *func_15167A68(s32, s32, s32, s32, u8, u8);
void func_1510F800(s32);
u8 *func_1510FD20(s32, s32);
void *memcpy(void *, const void *, u32);

/* Recovered function and remaining placeholders for asm/1B6DB0.s. */

/* Create and register an effect from a copied motion descriptor. */
void func_15189900(MotionEffectDescriptor15189900 *descriptor, u8 enabled) {
    MotionEffect15189900 *effect;
    s32 enabledValue;

    effect = (MotionEffect15189900 *)func_15167A68(0x1A, 1,
                                                   sizeof(MotionEffect15189900),
                                                   1, 0xFF, 1);
    if (effect != NULL) {
        memcpy(&effect->descriptor, descriptor, sizeof(*descriptor));
        func_1510F800(0);
        effect->spatialHandle = (s32)func_1510FD20(
            (s32)(effect->descriptor.positionX + effect->descriptor.velocityX * 0.5f),
            (s32)(effect->descriptor.positionZ + effect->descriptor.velocityZ * 0.5f));
        if (enabled != 0) {
            enabledValue = 1;
        } else {
            enabledValue = 0;
        }
        effect->enabled = enabledValue;
        effect->age = 0;
        effect->elapsed = 0.0f;
        if (effect->descriptor.velocityY < 0.0f) {
            effect->baselineY = effect->descriptor.positionY + effect->descriptor.velocityY;
        } else {
            effect->baselineY = effect->descriptor.positionY;
        }
    }
}

s32 func_15189A00() {
    return 0;
}

s32 func_15189EBC() {
    return 0;
}

s32 func_15189FD0(s32 arg0, s32 arg1, s32 arg2, s32 arg3) {
    return 1;
}
