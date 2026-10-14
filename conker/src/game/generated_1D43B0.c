#include <ultra64.h>

typedef struct {
    s16 count;
    u8 pad2[2];
    f32 position[3];
    s16 duration;
    u8 pad12[2];
    f32 radius;
    s16 angle0, range0, angle1, range1;
    f32 speed, speedRange;
    f32 unk28, unk2C;
    f32 direction[3];
    f32 scale, scaleRange;
    f32 unk44, unk48, unk4C, unk50;
    u8 unk54, unk55;
    s16 unk56, unk58;
    u8 pad5A[2];
} ActorBurstPacket97AA0;
typedef char ActorBurstPacketSize97AA0[(sizeof(ActorBurstPacket97AA0) == 0x5C) ? 1 : -1];

typedef struct { f32 x, y, z; } BurstVector1D43B0;
typedef struct {
    f32 field00, field04, field08, field0C;
    f32 rotation[3], scale[3];
    BurstVector1D43B0 position, velocity;
    f32 field40, field44, field48, field4C;
    u32 flags;
    s16 duration, id;
    u8 field58, reserved59[3];
    u32 field5C;
    u8 field60, field61, field62, field63;
    u8 field64, field65, field66, field67, field68;
    u8 reserved69, field6A, reserved6B;
    u32 field6C;
    u8 field70, reserved71;
    s16 field72, field74;
    u8 reserved76[2];
} BurstCreationDescriptor1D43B0;
typedef struct {
    f32 field00;
    u8 *animation;
    u8 field08, field09;
    s16 field0A, field0C;
    u8 reserved0E[2];
} BurstExtra1D43B0;
typedef struct {
    f32 *x, *y, *z;
    f32 rate, parameter;
    s16 duration;
    u8 flags, kind;
    u8 reserved18[4];
} BurstAnimationPacket1D43B0;
typedef char BurstDescriptorSize1D43B0[(sizeof(BurstCreationDescriptor1D43B0) == 0x78) ? 1 : -1];
typedef char BurstExtraSize1D43B0[(sizeof(BurstExtra1D43B0) == 16) ? 1 : -1];
typedef char BurstAnimationSize1D43B0[(sizeof(BurstAnimationPacket1D43B0) == 28) ? 1 : -1];
s32 func_150ADA20(void);
f32 func_150ADA68(void);
f32 func_151423D8(u8);
void *func_15132A4C(void *, s32, s32, s32, u8, s32);
void *func_15134908(void *, s32, u8, s32);
void *memcpy(void *, const void *, unsigned int);
extern f32 D_800A8DC0;
extern f32 D_800A8DC4;

void func_1516972C(u32);
void func_1514AB5C(f32, f32, s32, f32, s32, f32, f32, f32, f32, s16, s16, u8);

extern s32 D_800BE9E4;

/* Non-matching placeholders for the text-only asm slice asm/1D43B0.s. */

void func_151A6F00(ActorBurstPacket97AA0 *params, u8 kind, u8 slot, s32 context) {
    u32 angle0, angle1;
    BurstCreationDescriptor1D43B0 descriptor;
    f32 horizontalSpeed;
    BurstExtra1D43B0 payload;
    f32 retainedScale;
    f32 cosine0, sine0, cosine1, sine1;
    f32 radius, horizontal;
    f32 verticalSpeed;
    f32 speed;
    u8 *created;
    BurstExtra1D43B0 *attached;
    BurstAnimationPacket1D43B0 animation;
    u8 *animationResult;
    s16 remaining = params->count;

    descriptor.scale[0] = 1.0f;
    descriptor.scale[1] = 1.0f;
    descriptor.scale[2] = 1.0f;
    descriptor.flags = 0x21E9;
    descriptor.field58 = 0;
    descriptor.duration = params->duration;
    descriptor.id = 0x1B;
    descriptor.rotation[0] = 0.0f;
    descriptor.rotation[1] = 0.0f;
    descriptor.rotation[2] = 0.0f;
    descriptor.field44 = 0.0f;
    descriptor.field04 = D_800A8DC0;
    payload.field00 = -18.0f;
    payload.field08 = params->unk54;
    payload.field09 = params->unk55;
    payload.field0A = params->unk56;
    payload.field0C = params->unk58;
    descriptor.field5C = 0;
    descriptor.field60 = 255;
    descriptor.field61 = 1;
    descriptor.field62 = 5;
    descriptor.field63 = 4;
    descriptor.field64 = 0;
    descriptor.field65 = 0;
    descriptor.field66 = 1;
    descriptor.field67 = 0;
    descriptor.field68 = 0;
    descriptor.field6A = 0;
    descriptor.field6C = 0;
    descriptor.field70 = 0;
    descriptor.field72 = 0x20;
    descriptor.field74 = 7;
    while (remaining--) {
        angle0 = ((u32)func_150ADA20() % (u32)(params->range0 + 1) + params->angle0) & 255;
        angle1 = ((u32)func_150ADA20() % (u32)(params->range1 + 1) + params->angle1) & 255;
        cosine0 = func_151423D8(angle0 - 64);
        sine0 = func_151423D8(angle0);
        cosine1 = func_151423D8(angle1 - 64);
        sine1 = func_151423D8(angle1);
        radius = func_150ADA68() * params->radius;
        horizontal = radius * sine1;
        descriptor.position.x = params->position[0] + horizontal * cosine0;
        descriptor.position.y = params->position[1] - radius * cosine1;
        descriptor.position.z = params->position[2] + horizontal * sine0;
        switch (kind) {
            case 0:
                speed = func_150ADA68() * params->speedRange + params->speed;
                verticalSpeed = func_150ADA68() * params->unk2C + params->unk28;
                descriptor.velocity.x = speed * cosine0;
                descriptor.velocity.y = verticalSpeed;
                descriptor.velocity.z = speed * sine0;
                break;
            case 1:
                radius = func_150ADA68() * params->speedRange + params->speed;
                horizontalSpeed = radius * sine1;
                descriptor.velocity.x = horizontalSpeed * cosine0;
                descriptor.velocity.y = -radius * cosine1;
                descriptor.velocity.z = horizontalSpeed * sine0;
                break;
            case 2:
                descriptor.velocity = *(BurstVector1D43B0 *)params->direction;
                break;
            case 3:
                radius = func_150ADA68() * params->speedRange + params->speed;
                descriptor.velocity.x = params->direction[0] * radius;
                descriptor.velocity.y = params->direction[1] * radius;
                descriptor.velocity.z = params->direction[2] * radius;
                break;
        }
        retainedScale = descriptor.field08 = descriptor.field0C =
            func_150ADA68() * params->scaleRange + params->scale;
        descriptor.field00 = retainedScale * 30.0f;
        descriptor.field4C = func_150ADA68() * params->unk48 + params->unk44;
        descriptor.field40 = func_150ADA68() * params->unk50 + params->unk4C;
        descriptor.field48 = func_150ADA68() * params->unk50 + params->unk4C;
        created = func_15132A4C(&descriptor, 0, 0, sizeof(payload), slot, context);
        if (created != NULL) {
            attached = (BurstExtra1D43B0 *)(created + 0x170);
            memcpy(attached, &payload, sizeof(payload));
            animation.x = (f32 *)(created + 0x38);
            animation.y = (f32 *)(created + 0x3C);
            animation.z = (f32 *)(created + 0x40);
            animation.rate = 15.0f * descriptor.field0C;
            animation.duration = 300;
            animation.flags = 0;
            animation.kind = 1;
            animation.parameter = D_800A8DC4;
            attached->animation = NULL;
            animationResult = func_15134908(&animation, 4, slot, context);
            attached->animation = animationResult;
            if (animationResult != NULL) {
                memcpy(animationResult + 0x40, &retainedScale, sizeof(retainedScale));
            }
        }
    }
}

s32 func_151A73EC(u8 *arg0) {
    u8 *entry = arg0 + 0x170;

    if (*(s16 *)(arg0 + 0x64) < 0x20) {
        if (*(u32 *)(entry + 4) != 0) {
            func_1516972C(*(u32 *)(entry + 4));
            *(u32 *)(entry + 4) = 0;
        }
    }
    return 1;
}

s32 func_151A743C(u8 *actor, f32 arg1, s32 unused, s32 context, f32 arg4) {
    BurstExtra1D43B0 *extra = (BurstExtra1D43B0 *)(actor + 0x170);
    u8 variant;
    u32 count;

    *(f32 *)(actor + 0x3C) = *(f32 *)(actor + 0x10) + arg4;
    if (*(u32 *)(actor + 0x174) != 0) {
        func_1516972C((u32)extra->animation);
        extra->animation = NULL;
    }
    if (extra->field00 < *(f32 *)(actor + 0x48)) {
        *(u32 *)(actor + 0x60) &= ~7;
        *(u32 *)(actor + 0x60) &= ~8;
        *(u32 *)(actor + 0x60) &= ~0x40;
        *(u32 *)(actor + 0x60) &= ~0x20;
        *(f32 *)(actor + 0x44) = 0.0f;
        *(f32 *)(actor + 0x48) = 0.0f;
        *(f32 *)(actor + 0x4C) = 0.0f;
        if (*(s16 *)(actor + 0x64) > 32) {
            *(s16 *)(actor + 0x64) = 32;
        }
        if (extra->field08 != 0) {
            variant = 0;
            if (extra->field09 != 0) {
                variant = 1;
            }
            count = (u32)func_150ADA20() % 3 + 2;
            func_1514AB5C(arg1, arg4, context, *(f32 *)(actor + 0x18) * 35.0f, count,
                *(f32 *)(actor + 0x18), *(f32 *)(actor + 0x18) * 0.5f, *(f32 *)(actor + 0x18), *(f32 *)(actor + 0x18) * 0.5f, extra->field0A, extra->field0C, variant);
        }
    } else {
        *(f32 *)(actor + 0x44) *= *(f32 *)(actor + 0x14);
        *(f32 *)(actor + 0x48) = *(f32 *)(actor + 0x14) * -*(f32 *)(actor + 0x48);
        *(f32 *)(actor + 0x4C) *= *(f32 *)(actor + 0x14);
        *(f32 *)(actor + 0x50) *= *(f32 *)(actor + 0x14);
        *(f32 *)(actor + 0x54) *= *(f32 *)(actor + 0x14);
        *(f32 *)(actor + 0x58) *= *(f32 *)(actor + 0x14);
    }
    return 1;
}

s32 func_151A7610() {
    return 0;
}

s32 func_151A77C0() {
    return 0;
}

void func_151A787C(u8 *arg0) {
    u8 *params = arg0 + 0x50;
    s32 value = *(s16 *)(arg0 + 0x38);
    s32 delta;
    s32 intensity;

    if (value < *(s16 *)(params + 4)) {
        arg0[0x3F] = value * (u32)*(s16 *)(params + 6);
    }

    if (value < *(s16 *)(params + 8)) {
        delta = *(s16 *)(params + 0xA) * (u32)D_800BE9E4;
        *(s16 *)(arg0 + 0x34) += delta;
        *(s16 *)(arg0 + 0x36) += delta;
        value = *(s16 *)(arg0 + 0x38);
    }

    intensity = value * (u32)*(s16 *)(params + 2);
    arg0[0x42] = intensity;
    arg0[0x41] = intensity;
    arg0[0x40] = intensity;
}

void func_151A7908(u8 *arg0) {
    u8 *temp_v0 = arg0 + 0x170;

    if (*(s32 *) (arg0 + 0x174) != 0) {
        func_1516972C(*(u32 *) (temp_v0 + 4));
        *(u32 *) (temp_v0 + 4) = 0;
    }
}
