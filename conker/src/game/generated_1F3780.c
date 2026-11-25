#include <ultra64.h>

/* Recovered effects and remaining assembly from asm/1F3780.s. */

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

#include "libc/string.h"

/* Only the observed source prefix is described here. */
typedef struct {
    u8 retained00[0x3B];
    u8 identity;
} OwnerEffectSource151C6EA0;
typedef struct { f32 x, y, z; } OwnerEffectVector151C6EA0;
typedef struct {
    f32 scale[2];
    f32 extent[2];
    OwnerEffectVector151C6EA0 direction;
    f32 unitScale[3];
    OwnerEffectVector151C6EA0 position;
    OwnerEffectVector151C6EA0 velocity;
    OwnerEffectVector151C6EA0 reference;
    f32 zero4C;
    u32 flags;
    s16 lifetime;
    u16 resourceId;
    u8 zero58, padding59[3];
    u32 zero5C;
    u8 value60, value61, zero62, zero63, zero64, zero65, zero66, zero67, value68;
    s8 sentinel69;
    u8 value6A, padding6B;
    OwnerEffectSource151C6EA0 *owner;
    u8 sourceIdentity, padding71;
    u16 value72, value74;
    u8 padding76[2];
    u32 zero78;
} OwnerEffectDescriptor151C6EA0;
/* Natural alignment keeps the payload byte separate from its descriptor. */
typedef struct {
    u8 initialPayload;
    OwnerEffectDescriptor151C6EA0 descriptor;
} OwnerEffectWorkspace151C6EA0;

typedef struct ExtendedState15F680 ExtendedState15F680;
extern OwnerEffectVector151C6EA0 D_800A5480;
void *func_1513264C(u8 *, s32, s32, ExtendedState15F680 *, s32, u8, s32);

/* Submit the owner-linked descriptor and clear its single payload byte.
 * Preserve the unwritten descriptor padding and the separate byte's lifetime. */
void func_151C6EA0(OwnerEffectSource151C6EA0 *source, u8 slot, s32 context) {
    OwnerEffectWorkspace151C6EA0 workspace;
    u8 *result;

    workspace.initialPayload = 0;
    workspace.descriptor.scale[0] = 1.0f;
    workspace.descriptor.scale[1] = 1.0f;
    workspace.descriptor.extent[1] = 1.0f;
    workspace.descriptor.extent[0] = 1.0f;
    workspace.descriptor.direction = D_800A5480;
    workspace.descriptor.unitScale[0] = 1.0f;
    workspace.descriptor.unitScale[1] = 1.0f;
    workspace.descriptor.unitScale[2] = 1.0f;
    workspace.descriptor.position = D_800A5480;
    workspace.descriptor.velocity = D_800A5480;
    workspace.descriptor.reference = D_800A5480;
    workspace.descriptor.zero4C = 0.0f;
    workspace.descriptor.flags = 0x11900;
    workspace.descriptor.lifetime = 300;
    workspace.descriptor.resourceId = 15;
    workspace.descriptor.zero58 = 0;
    workspace.descriptor.zero5C = 0;
    workspace.descriptor.value60 = 100;
    workspace.descriptor.value61 = 23;
    workspace.descriptor.zero62 = 0;
    workspace.descriptor.zero63 = 0;
    workspace.descriptor.zero64 = 0;
    workspace.descriptor.zero65 = 0;
    workspace.descriptor.zero66 = 0;
    workspace.descriptor.zero67 = 0;
    workspace.descriptor.value68 = 5;
    workspace.descriptor.sentinel69 = -1;
    workspace.descriptor.value6A = 1;
    workspace.descriptor.owner = source;
    workspace.descriptor.sourceIdentity = source->identity;
    workspace.descriptor.value72 = 1;
    workspace.descriptor.value74 = 255;
    workspace.descriptor.zero78 = 0;
    result = func_1513264C((u8 *)&workspace.descriptor, 3, 255, NULL, 1, slot, context);
    if (result != NULL) {
        memcpy(result + 0x170, &workspace.initialPayload, 1);
    }
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
