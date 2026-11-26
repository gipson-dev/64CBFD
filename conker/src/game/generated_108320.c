#include <ultra64.h>

/* Recovered effect routines and remaining placeholders for asm/108320.s. */

s32 func_150DAE70() {
    return 0;
}

typedef struct {
    f32 velocityX, velocityY, velocityZ;
    f32 scale, scaleRate;
    f32 stretchY, stretchZ;
    f32 stretchVelocityY, stretchVelocityZ;
    f32 damping;
    u8 fadeStep;
    u8 retained29[3];
} BouncingEffectMotion150DB114;
typedef struct {
    u8 retained00[0x2C];
    f32 sizeY, sizeZ;
    f32 x, y, z;
    u8 retained40[0x1C];
    u8 alpha;
    u8 retained5D[0xB3];
    BouncingEffectMotion150DB114 motion;
} BouncingEffectOwner150DB114;
extern f32 D_800BE9A4;

/* Integrate damped motion, bounce the two stretch factors, and fade alpha. */
s32 func_150DB114(BouncingEffectOwner150DB114 *owner) {
    f32 upper = 1.2f;
    BouncingEffectMotion150DB114 *motion = &owner->motion;
    f32 damping = motion->damping;
    f32 lower;
    s16 alpha = owner->alpha;

    motion->velocityX *= damping;
    motion->velocityY *= damping;
    motion->velocityZ *= damping;
    owner->x += motion->velocityX * D_800BE9A4;
    owner->y += motion->velocityY * D_800BE9A4;
    owner->z += motion->velocityZ * D_800BE9A4;
    motion->stretchY += motion->stretchVelocityY * D_800BE9A4;
    if (upper < motion->stretchY) {
        motion->stretchY = upper;
        motion->stretchVelocityY = -motion->stretchVelocityY;
        lower = 0.8f;
    } else {
        lower = 0.8f;
        if (motion->stretchY < lower) {
            motion->stretchY = lower;
            motion->stretchVelocityY = -motion->stretchVelocityY;
        }
    }
    motion->stretchZ += motion->stretchVelocityZ * D_800BE9A4;
    if (upper < motion->stretchZ) {
        motion->stretchZ = upper;
        motion->stretchVelocityZ = -motion->stretchVelocityZ;
    } else if (motion->stretchZ < lower) {
        motion->stretchZ = lower;
        motion->stretchVelocityZ = -motion->stretchVelocityZ;
    }
    motion->scale += motion->scaleRate * D_800BE9A4;
    owner->sizeY = motion->scale * motion->stretchY;
    owner->sizeZ = motion->scale * motion->stretchZ;
    alpha -= motion->fadeStep;
    if (alpha < 0) {
        owner->alpha = 0;
        return 0;
    }
    owner->alpha = alpha;
    return 1;
}


typedef struct {
    u8 retained00[0x2C];
    f32 halfWidth, halfHeight;
    f32 x, y, z;
    f32 axisX, retained44, axisZ;
    u8 retained4C[0x74];
    Vtx vertexTemplate[4];
    u8 *buffers[4];
} AxisQuadOwner150DB2D8;
void func_151D5D60(void *, s16, s32, Vtx **, u8 *);
void *memcpy(void *, const void *, u32);

/* Fill the current quad's four positions, retaining template UV and colour. */
Vtx *func_150DB2D8(AxisQuadOwner150DB2D8 *owner, s16 view) {
    Vtx *cursor, *first;
    f32 horizontal, depth;
    u8 fresh;

    func_151D5D60(owner->buffers, view, 0x40, &cursor, &fresh);
    first = cursor;
    if (cursor != NULL) {
        if (fresh) {
            memcpy(owner->buffers[view], owner->vertexTemplate, 0x40);
            memcpy(owner->buffers[view] + 0x40, owner->vertexTemplate, 0x40);
        }
    } else {
        return NULL;
    }
    horizontal = owner->halfWidth * owner->axisX;
    depth = -owner->halfWidth * owner->axisZ;
    cursor[0].v.ob[0] = (s32)(owner->x + horizontal);
    cursor[0].v.ob[1] = (s32)(owner->y + owner->halfHeight);
    cursor[0].v.ob[2] = (s32)(owner->z + depth);
    cursor[0].v.flag = 0;
    cursor[1].v.ob[0] = (s32)(owner->x + horizontal);
    cursor[1].v.ob[1] = (s32)(owner->y - owner->halfHeight);
    cursor[1].v.ob[2] = (s32)(owner->z + depth);
    cursor[1].v.flag = 0;
    cursor[2].v.ob[0] = (s32)(owner->x - horizontal);
    cursor[2].v.ob[1] = (s32)(owner->y - owner->halfHeight);
    cursor[2].v.ob[2] = (s32)(owner->z - depth);
    cursor[2].v.flag = 0;
    cursor[3].v.ob[0] = (s32)(owner->x - horizontal);
    cursor[3].v.ob[1] = (s32)(owner->y + owner->halfHeight);
    cursor[3].v.ob[2] = (s32)(owner->z - depth);
    cursor[3].v.flag = 0;
    return first;
}


typedef struct EffectRequest150DB518 {
    u8 kind, reserved01;
    u16 mode;
    s16 duration;
    u8 reserved06[2];
    s32 value;
    u32 flags;
    u8 red, green, blue, alpha;
    u8 reserved14[0x2C];
    u32 allocationFlags;
    u8 first, second, reserved46[0x12];
} EffectRequest150DB518;
typedef struct EffectSources150DB518 {
    u8 reserved[0x110];
    void *first, *second, *third, *fifth, *fourth;
} EffectSources150DB518;
void *func_1513D524(void *, u8, u8, u8, u8, u8, s32, u8, s32);
/* Create a parameter-driven effect and retain its five live source pointers. */
void func_150DB518(void *first, void *second, void *third, void *fourth,
                   void *fifth, s16 duration, u8 channel, s32 context) {
    EffectRequest150DB518 request;
    EffectSources150DB518 *effect;

    if (first && second && third && fourth && fifth && duration) {
        /* Reserved descriptor bytes retain their original stack contents. */
        request.kind = 0x17;
        request.flags = 0x243A;
        request.allocationFlags = 0x401;
        request.first = 255;
        request.value = 0;
        request.duration = duration;
        request.second = 255;
        request.red = request.green = request.blue = 200;
        request.alpha = 200;
        request.mode = 0x401;
        effect = func_1513D524(&request, 0, 10, 0, 8, 0, 20, channel, context);
        if (effect) {
            effect->first = first;
            effect->second = second;
            effect->third = third;
            effect->fifth = fifth;
            effect->fourth = fourth;
        }
    }
}

/* Clamp the sampled actor parameter to its unsigned byte range. */
s32 func_150DB630(u8 *actor) {
    f32 value;

    /* Preserve the retail reload of the parameter pointer on the lower path. */
    if (**(f32 * volatile *)(actor + 0x120) > 255.0f) {
        actor[0x5C] = 255;
    } else {
        value = **(f32 **)(actor + 0x120);
        if (value < 0.0f) {
            actor[0x5C] = 0;
        } else {
            actor[0x5C] = (u32)value;
        }
    }
    return 1;
}

s32 func_150DB714() {
    return 0;
}
