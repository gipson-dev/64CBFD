#include <ultra64.h>

extern f32 D_800AA3D0;
extern u8 D_800A3FE6[];
s32 func_15134070(u8 *);
void func_1516962C(s32, void *, u8);
void *func_1513418C(void *, s32, u8, s32);
void *memcpy(void *, const void *, u32);
typedef struct {
    u32 zero0, zero4;
    u8 ownerIdentity, reserved09[3];
    u8 *owner;
    u8 attachment, reserved11[3];
    f32 vector[3];
    f32 value20, value24;
    s16 duration;
    u8 flags, kind;
    s8 callback;
    u8 mode;
} OwnerEffectDescriptor1E2180;

extern f32 D_800AA3D4,D_800AA3D8,D_800AA3DC;
s32 func_150ADA20(void);
f32 func_150ADA68(void);
void *func_151D9014(f32 *,f32 *,u8,f32,s16,u8,f32,u8,f32,f32,u8,s32,u8,u8,u8,s32);

/* Non-matching placeholders for the text-only asm slice asm/1E2180.s. */

/* Submit an owner-linked effect and copy its descriptor-specific payload. */
void *func_151B4CD0(u8 *owner, u8 selector, s32 category) {
    u8 *created;
    OwnerEffectDescriptor1E2180 descriptor;
    u8 payload[1];
    s32 type;

    if (owner == NULL) {
        return NULL;
    }
    type = func_15134070(owner);
    if (type == 99) {
        return NULL;
    }
    if (D_800A3FE6[type * 0x10] == 2) {
        return NULL;
    }
    func_1516962C(40, owner, 22);
    descriptor.zero0 = 0;
    descriptor.zero4 = 0;
    descriptor.ownerIdentity = owner[0x3B];
    descriptor.owner = owner;
    descriptor.attachment = 2;
    descriptor.vector[0] = 0.0f;
    descriptor.vector[1] = -27.0f;
    descriptor.vector[2] = 16.0f;
    descriptor.value20 = 15.0f;
    descriptor.value24 = D_800AA3D0;
    descriptor.flags = 6;
    descriptor.duration = (u32)func_150ADA20() % 21U + 40;
    descriptor.kind = 8;
    descriptor.callback = -1;
    descriptor.mode = 7;
    if (D_800A3FE6[type * 0x10] == 1) {
        payload[0] = 1;
    } else {
        payload[0] = 0;
    }
    created = func_1513418C(&descriptor, 1, selector, category);
    if (created != NULL) {
        memcpy(created + 0x58, payload, 1);
    }
    return created;
}

void func_151B4EA4(f32 *, f32, f32, f32, u8, u8);

void func_151B4E4C(f32 arg0, f32 arg1, f32 arg2, f32 arg3, f32 arg4,
                   f32 arg5, u8 *arg6) {
    f32 position[3];

    position[0] = arg0;
    position[1] = arg1;
    position[2] = arg2;
    func_151B4EA4(position, arg3, arg4, arg5, arg6[0x58], arg6[0xC]);
}

/* Spawn an effect from a reversed direction and five ordered random draws. */
void func_151B4EA4(f32 *position, f32 x, f32 y, f32 z, u8 selector, u8 mode) {
    f32 size;
    f32 velocity[3];
    f32 scale = D_800AA3D4;
    f32 second;
    u32 alpha, duration;
    f32 first;
    u32 variant;
    velocity[0] = -x * scale;
    velocity[1] = -y * scale;
    velocity[2] = -z * scale;
    first = func_150ADA68();
    duration = (u32)func_150ADA20();
    alpha = (u32)func_150ADA20();
    second = func_150ADA68();
    variant = (u32)func_150ADA20();
    size = D_800AA3D8;
    func_151D9014(position, velocity, selector, first * D_800AA3DC + -1.0f,
                        duration % 31 + 20, alpha % 101 + 155,
                        second * 152.0f + 109.0f, variant & 1,
                        size, size, 0, 0, 1, 0, mode, 1);
}


/* Note 454: original carried actor attachment/effect. */
#pragma GLOBAL_ASM("asm/nonmatchings/generated_1E2180/func_151B4FE0.s")

void *func_151B50F4(f32 *, f32, f32, f32, u8);

void func_151B50A4(f32 arg0, f32 arg1, f32 arg2, f32 arg3, f32 arg4,
                   f32 arg5, u8 *arg6) {
    f32 position[3];

    position[0] = arg0;
    position[1] = arg1;
    position[2] = arg2;
    func_151B50F4(position, arg3, arg4, arg5, arg6[0xC]);
}

extern f32 D_800AA3E8, D_800AA3EC, D_800AA3F0, D_800AA3F4;
/* Spawn an effect using a reversed velocity and five ordered random samples. */
void *func_151B50F4(f32 *position, f32 x, f32 y, f32 z, u8 selector) {
    f32 size;
    f32 velocity[3];
    f32 scale = D_800AA3E8;
    f32 second;
    u32 alpha, duration;
    f32 first;
    u8 variant;
    velocity[0] = -x * scale;
    velocity[1] = -y * scale;
    velocity[2] = -z * scale;
    if (func_150ADA20() & 1) {
        variant = 1;
    } else {
        variant = 0;
    }
    first = func_150ADA68();
    duration = (u32)func_150ADA20();
    alpha = (u32)func_150ADA20();
    second = func_150ADA68();
    size = D_800AA3EC;
    return func_151D9014(position, velocity, 0,
        first * D_800AA3F0 + D_800AA3F4,
        (duration & 15U) + 10, alpha % 45U + 137,
        second * 202.0f + 142.0f, variant,
        size, size, 0, 0, 1, 0, selector, 1);
}
