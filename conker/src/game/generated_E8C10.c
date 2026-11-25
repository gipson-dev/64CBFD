#include <ultra64.h>

/* Recovered C and remaining placeholders for asm/E8C10.s. */

/* The factory consumes all 124 bytes, including the untouched reserved bytes. */
typedef struct {
    f32 field00, field04, field08, field0C;
    f32 rotation[3], scale[3], position[3], velocity[3];
    f32 field40, field44, field48, field4C;
    u32 flags;
    s16 duration;
    u16 resource;
    u8 field58, retained59[3];
    u32 field5C;
    u8 field60, field61, field62, field63, field64, field65, field66, field67, field68;
    u8 retained69, field6A, retained6B;
    void *owner;
    u8 field70, retained71;
    s16 field72, field74;
    u8 retained76[6];
} ActorEmitterDescriptorE8C10;
s32 func_150ADA20(void);
f32 func_150ADA68(void);
f32 func_151423D8(u8);
void *func_15132A4C(void *, s32, s32, s32, u8, s32);
extern f32 D_8009FE94, D_8009FE98, D_8009FE9C, D_8009FEA0, D_8009FEA4;


/* Emit an attached particle using cached actor dimensions and heading. */
/* The known caller ignores the result; retail falls through after the factory. */
s32 func_150BB760(u8 *actor) {
    ActorEmitterDescriptorE8C10 descriptor;
    f32 width;
    f32 height;
    f32 headingSine;
    f32 sample;
    f32 driftX;
    f32 driftZ;
    u8 angle;
    f32 radialSine;
    f32 radialCosine;
    f32 radius;
    f32 offsetX;
    f32 offsetZ;
    u8 spreadAngle;
    f32 spreadSine;
    f32 spreadCosine;
    f32 speed;
    f32 velocityX;
    f32 velocityZ;
    f32 firstSize;

    /* This type read deliberately precedes the retail null check. */
    if (actor[4] != 32) return 1;
    if (actor != 0 && *(s32 *)actor != 0 && *(s32 *)(actor + 0x1D4) != 0) {
        width = *(s16 *)(actor + 0xE4);
        height = *(s16 *)(actor + 0xE6);
        headingSine = func_151423D8((u8)(*(u16 *)(actor + 0x76) >> 8));
        sample = func_151423D8((u8)((*(u16 *)(actor + 0x76) >> 8) + 64));
        driftX = (*(f32 *)(actor + 0x3C) * headingSine) * 0.5f;
        driftZ = (*(f32 *)(actor + 0x3C) * sample) * 0.5f;
        descriptor.resource = 1;
        descriptor.flags = 0x29E9;
        descriptor.field58 = 0;
        descriptor.field5C = 0;
        descriptor.field60 = 255;
        descriptor.field61 = 1;
        descriptor.field62 = 0;
        descriptor.field63 = 2;
        descriptor.field64 = 0;
        descriptor.field65 = 0;
        descriptor.field66 = 0;
        descriptor.field67 = 0;
        descriptor.field68 = 0;
        descriptor.field6A = 1;
        descriptor.owner = actor;
        descriptor.scale[0] = 1.0f;
        descriptor.scale[1] = 1.0f;
        descriptor.scale[2] = 1.0f;
        descriptor.field48 = 0.0f;
        descriptor.field4C = -1.0f;
        descriptor.field70 = actor[0x3B];
        descriptor.field72 = 32;
        descriptor.field74 = 7;
        angle = func_150ADA20();
        radialSine = func_151423D8(angle);
        radialCosine = func_151423D8((u8)(angle - 64));
        radius = func_150ADA68() * width;
        offsetX = radialSine * radius;
        offsetZ = -radialCosine * radius;
        angle = func_150ADA20();
        spreadAngle = (*(u16 *)(actor + 0x76) >> 8) - (angle & 63U) - 32U;
        spreadSine = func_151423D8(spreadAngle);
        spreadCosine = func_151423D8((u8)(spreadAngle - 64));
        speed = func_150ADA68() * 5.0f + 3.0f;
        velocityX = spreadCosine * speed;
        velocityZ = spreadSine * speed;
        firstSize = func_150ADA68() * D_8009FE94 + D_8009FE98;
        /* The earlier heading sample is dead; reuse its scalar for the second size. */
        sample = func_150ADA68() * D_8009FE9C + D_8009FEA0;
        descriptor.field08 = firstSize;
        descriptor.field0C = sample;
        descriptor.field00 = (firstSize + sample) * 0.5f;
        descriptor.rotation[0] = func_150ADA68() * 360.0f;
        descriptor.rotation[1] = func_150ADA68() * 360.0f;
        descriptor.rotation[2] = func_150ADA68() * 360.0f;
        descriptor.position[0] = *(f32 *)(actor + 0x14) + offsetX;
        radius = func_150ADA68();
        descriptor.position[1] = (radius * height + *(f32 *)(actor + 0x18)) + 4.0f;
        descriptor.position[2] = *(f32 *)(actor + 0x1C) + offsetZ;
        descriptor.velocity[0] = velocityX + driftX;
        descriptor.velocity[1] = func_150ADA68() * 5.0f + 3.0f;
        descriptor.velocity[2] = velocityZ + driftZ;
        descriptor.field40 = 25.0f - func_150ADA68() * 50.0f;
        descriptor.field44 = 25.0f - func_150ADA68() * 50.0f;
        descriptor.duration = ((u32)func_150ADA20() & 31U) + 60U;
        descriptor.field04 = func_150ADA68() * D_8009FEA4 + 0.25f;
        func_15132A4C(&descriptor, 3, 255, 0, 255, 0);
    }
}

s32 func_150BBB5C() {
    return 0;
}

s32 func_150BC488() {
    return 0;
}

s32 func_150BCBBC() {
    return 0;
}

typedef struct {
    u8 reserved[0x10];
    f32 extent;
    f32 damping;
    u8 reserved18[0x24];
    f32 height;
    f32 reserved40;
    f32 velocity[3];
    f32 rotationVelocity[3];
    f32 reserved5C;
    u32 flags;
} ReboundRecordE8C10;
extern f32 D_8009FEF8;

/* Set the ground height, then stop or reflect and damp the record's motion. */
s32 func_150BCFB8(ReboundRecordE8C10 *record, f32 x, f32 y, f32 z,
                 f32 groundHeight, f32 *normal) {
    record->height = record->extent * D_8009FEF8 + groundHeight;
    if (record->velocity[1] > -2.0f) {
        record->velocity[0] = 0.0f;
        record->flags &= 0xFFFFFF90U;
        record->velocity[1] = 0.0f;
        record->velocity[2] = 0.0f;
    } else {
        f32 damping = record->damping;
        record->velocity[0] *= damping;
        record->velocity[1] = -record->velocity[1] * damping;
        record->velocity[2] *= damping;
        record->rotationVelocity[0] *= damping;
        record->rotationVelocity[1] *= damping;
        record->rotationVelocity[2] *= damping;
    }
    return 1;
}

s32 func_150BD070() {
    return 0;
}

s32 func_150BD740() {
    return 0;
}

#include "structs.h"

typedef struct {
    vertex position;
    s16 lifetime,field0E;
    s32 active;
    u8 reserved14,count,reserved16[6];
} RadialRequest150BD954;
typedef struct {
    f32 field00;
    vertex velocity;
    f32 field10,field14;
    u8 field18,kind,alpha,field1B;
    u8 reserved1C[4];
} RadialPayload150BD954;
typedef struct {
    s32 field00,field04,field08,field0C,field10,field14,field18;
    u8 field1C,field1D,reserved1E[2];
} RadialRender150BD954;
f32 func_150ADA68(void);
void *func_15147DA0(void *,void *,s32,s32,s32,s32,s32,s32,s32,s32,s32,void *,s32,u8,s32);
extern f32 D_8009FFD0,D_8009FFD4,D_8009FFD8,D_8009FFDC;
extern f32 D_8009FFE0,D_8009FFE4;

/* Emit a randomized effect along the supplied direction vector. */
s32 func_150BD954(s32 source,s16 index,f32 x,f32 y,f32 z,
    f32 originX,f32 originY,f32 originZ,s16 angle,u8 start,f32 radius,
    s32 style,f32 extra,vertex *direction,u8 slot) {
    f32 sample;
    RadialRequest150BD954 request;
    RadialPayload150BD954 payload;
    f32 speed;
    RadialRender150BD954 render;
    render.field00 = 0;
    render.field04 = 1;
    render.field08 = 0x160600;
    render.field0C = 3;
    render.field10 = 16;
    render.field14 = 128;
    render.field18 = 32;
    render.field1C = 0;
    render.field1D = 9;
    request.active = 1;
    request.field0E = 1;
    request.position.x = x;
    request.position.y = y;
    payload.field14 = y;
    payload.kind = 9;
    payload.alpha = 255;
    payload.field18 = 8;
    request.position.z = z;
    sample = func_150ADA68();
    speed = (sample * 127.0f + 85.0f) * D_8009FFD0;
    payload.velocity.x = direction->x * speed;
    payload.velocity.y = direction->y * speed;
    payload.velocity.z = direction->z * speed;
    payload.field1B = (u32)func_150ADA20() % 86U + 180;
    request.count = ((u32)func_150ADA20() & 3U) + 3;
    request.lifetime = (u32)func_150ADA20() % 31U + 39;
    payload.field00 = (func_150ADA68() * D_8009FFD4 + D_8009FFD8) * D_8009FFDC;
    payload.field10 = (func_150ADA68() * 356.0f + D_8009FFE0) * D_8009FFE4;
    func_15147DA0(&request,&payload,0,1,11,0,0,0,0,0,0,&render,0,slot,1);
    return 1;
}


// Matched with guarded scalar-temporary register normalization.
s32 func_150BDB3C(u8 *arg0) {
    u8 *temp_v0 = *(u8 **) (arg0 + 0x98);
    s32 temp_v1 = *(s16 *) (arg0 + 0x1C);
    {
        s32 shifted = temp_v1 << 3;

        if (shifted < *(temp_v0 + 0x1B)) {
            *(temp_v0 + 0x1B) = shifted;
        }
    }
    return 1;
}
