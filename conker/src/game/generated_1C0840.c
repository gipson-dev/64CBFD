#include <ultra64.h>

/* Recovered sprite construction and lifetime update from asm/1C0840.s. */

typedef struct {
    Vtx vertices[8];
    u8 retained80[6];
    s16 parameter86;
    u8 retained88[4];
    s16 x, y, z, parameter92, parameter94, height;
    u16 flags;
    u8 retained9A[6];
    u8 textureIndex, retainedA1, mode, variant, parameterA4, retainedA5[3];
} SeedSpriteDescriptor;
typedef struct { s16 x, y, z, height; u8 variant; } SeedSpriteInput;
extern f32 D_800A81B0;
void func_1516865C(void *, u8, u8, u8, u8);
void *func_15168800(void *, u8, s32);
s32 func_150ADA20(void);

/* Build the sprite and retain the live O32 actor argument home across helpers. */
void func_15193390(u8 *volatile actor) {
    SeedSpriteDescriptor descriptor;
    SeedSpriteInput *cursor;
    s16 height;
    bzero(&descriptor, sizeof(descriptor));
    cursor = (SeedSpriteInput *)(actor + 0x28);
    height = cursor->height;
    if (D_800A81B0 == (f32)height) {
        descriptor.height = (s32)((f32)cursor->y - 200.0f);
        cursor->variant = 0;
    } else {
        descriptor.height = height;
    }
    descriptor.x = cursor->x;
    descriptor.y = cursor->y;
    descriptor.z = cursor->z;
    descriptor.parameter92 = 0;
    descriptor.parameter94 = 0;
    descriptor.mode = 15;
    descriptor.textureIndex = 0x45;
    descriptor.parameter86 = 10;
    descriptor.variant = cursor->variant;
    descriptor.flags = 0x4880;
    descriptor.parameterA4 = 128;
    func_1516865C(&descriptor, 255, 255, 255, 128);
    cursor = (SeedSpriteInput *)actor;
    func_15168800(&descriptor, ((u8 *)cursor)[0xC], ((u8 *)cursor)[1]);
    *(s16 *)(actor + 0xE) = ((u32)func_150ADA20() & 127) + 100;
}

typedef struct {
    u8 retained00[0x94];
    s16 fallTicks;
    s16 targetExtent;
    s16 phase;
    u8 retained9A[2];
    s16 x, y, z;
    s16 horizontalExtent;
    s16 verticalExtent;
    s16 floorY;
    u8 retainedA8[2];
    s16 growthTicks;
    u8 retainedAC[7];
    s8 variant;
} SeedSpriteRuntime151934B4;
extern s32 D_800BE9E4;
void func_151DBCBC(u8, f32, s16, s32, void *, u8, s32);

/* Grow the seed sprite, then accelerate its fall and expire at the floor. */
void func_151934B4(SeedSpriteRuntime151934B4 *sprite) {
    s32 growth;
    f32 position[3];
    if (sprite->verticalExtent < sprite->targetExtent) {
        growth = sprite->growthTicks;
        sprite->verticalExtent = ((growth >> 2) * 24) / 3;
        sprite->horizontalExtent = ((growth >> 2) * 6) / 3;
        sprite->growthTicks = (u32)growth + (u32)D_800BE9E4;
    } else {
        sprite->fallTicks++;
        if (sprite->fallTicks > 20) sprite->fallTicks = 20;
        sprite->y = (u32)(s32)sprite->y - (u32)((s32)((u32)(s32)sprite->fallTicks * (u32)D_800BE9E4) >> 1);
        if (sprite->y < sprite->floorY) {
            if (sprite->variant == 1) {
                position[0] = sprite->x;
                position[1] = sprite->floorY;
                position[2] = sprite->z;
                func_151DBCBC(5, 30.0f, 255, 0, position,
                    ((u8 *)sprite)[0xC], ((u8 *)sprite)[1]);
            }
            sprite->phase = -1;
        }
    }
}
