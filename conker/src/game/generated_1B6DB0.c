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

typedef struct {
    f32 x, y, z;
    u8 retained0C[8];
} BelowHeightPosition;
extern f64 D_800A73A8;
extern f32 D_800A73B0;
f32 func_150ADA68(void);
u8 func_151D8E20(void);
void func_151DBCBC(u8, f32, s16, s32, void *, u8, s32);

/* Emit an occasional below-height effect, then reset the captured payload. */
s32 func_15189EBC(u8 *actor) {
    BelowHeightPosition *positions = *(BelowHeightPosition **)(actor + 0x94);
    u8 *payload = *(u8 **)(actor + 0x98);
    f32 point[3];
    s32 choice;
    if (positions[(s8)actor[0x2D]].y < *(f32 *)(payload + 0x48)) {
        if ((f64)func_150ADA68() < D_800A73A8) {
            point[0] = positions[(s8)actor[0x2D]].x;
            point[1] = *(f32 *)(payload + 0x48);
            point[2] = positions[(s8)actor[0x2D]].z;
            choice = func_151D8E20();
            func_151DBCBC((u8)choice, *(f32 *)payload * 6.0f,
                         payload[0x1B], 0, point, actor[0xC], actor[1]);
        }
        payload[0x20] = 4;
        *(f32 *)(payload + 0x48) = D_800A73B0;
    }
    return 1;
}

s32 func_15189FD0(s32 arg0, s32 arg1, s32 arg2, s32 arg3) {
    return 1;
}
