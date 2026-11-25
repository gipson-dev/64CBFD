#include <ultra64.h>

/* Recovered effects and remaining non-matching code for asm/DFBF0.s. */

s32 func_150B2740() {
    return 0;
}

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
    u32 field6C;
    u8 field70, retained71;
    s16 field72, field74;
    u8 retained76[6];
} AngularExtended150B2EB4;

f32 func_151423D8(u8);
f32 func_150ADA68(void);
void *func_15132A4C(void *,s32,s32,s32,u8,s32);
extern f32 D_8009FB8C,D_8009FB90,D_8009FB94,D_8009FB98;

/* Build one extended emitter from the registry heading and radial parameters. */
s32 func_150B2EB4(s32 source,s16 index,f32 x,f32 y,f32 z,
    f32 originX,f32 originY,f32 originZ,u32 heading,s32 start,f32 radius,
    s32 style,f32 extra,s32 context,u8 slot) {
    f32 headingCosine,headingSine,horizontal,yawCosine,yawSine,pitchCosine,pitchSine,speed;
    AngularExtended150B2EB4 descriptor;
    headingCosine = func_151423D8((u8)(heading - 64U));
    headingSine = func_151423D8((u8)heading);
    descriptor.flags = 0x9E8;
    descriptor.rotation[0] = 0.0f;
    descriptor.rotation[1] = 0.0f;
    descriptor.rotation[2] = 0.0f;
    descriptor.scale[0] = 1.0f;
    descriptor.scale[1] = 1.0f;
    descriptor.scale[2] = 1.0f;
    descriptor.position[0] = x;
    descriptor.position[1] = y;
    descriptor.position[2] = z;
    descriptor.field04 = D_8009FB8C;
    speed = func_150ADA68() * 31.0f + 18.0f;
    index = (u32)start + (s32)(((60.0f * headingSine) * radius) * extra) - 64U;
    yawCosine = func_151423D8((u8)(index - 64));
    yawSine = func_151423D8((u8)index);
    index = (s32)(48.0f * headingCosine) - 20;
    pitchCosine = func_151423D8((u8)(index - 64));
    pitchSine = func_151423D8((u8)index);
    horizontal = speed * pitchSine;
    descriptor.velocity[0] = horizontal * yawCosine;
    descriptor.velocity[1] = -speed * pitchCosine;
    descriptor.velocity[2] = horizontal * yawSine;
    descriptor.field40 = func_150ADA68() * 80.0f + -40.0f;
    descriptor.field44 = 0.0f;
    descriptor.field48 = func_150ADA68() * 80.0f + -40.0f;
    descriptor.duration = 100;
    descriptor.field4C = func_150ADA68() * D_8009FB90 + D_8009FB94;
    descriptor.field00 = 1.0f;
    descriptor.field08 = descriptor.field0C = func_150ADA68() * 72.5f + D_8009FB98;
    descriptor.resource = 28;
    descriptor.field58 = 0;
    descriptor.field5C = 0;
    descriptor.field60 = 255;
    descriptor.field61 = 1;
    descriptor.field62 = 0;
    descriptor.field63 = 0;
    descriptor.field64 = 0;
    descriptor.field65 = 0;
    descriptor.field66 = 0;
    descriptor.field67 = 0;
    descriptor.field68 = 0;
    descriptor.field6A = 2;
    descriptor.field6C = 0;
    descriptor.field70 = 0;
    descriptor.field72 = 1;
    descriptor.field74 = 255;
    func_15132A4C(&descriptor,3,255,0,slot,0);
    return 1;
}


s32 func_150B3188() {
    return 0;
}

/* Reset motion above the threshold; otherwise scale its six components. */
s32 func_150B36AC(u8 *record, s32 unused1, s32 unused2, s32 unused3, f32 offset, void *unused6) {
    f32 vertical = *(f32 *)(record + 0x48);
    f32 scale;
    (void)unused1;
    (void)unused2;
    (void)unused3;
    (void)unused6;

    *(f32 *)(record + 0x3C) = *(f32 *)(record + 0x10) + offset;
    if (*(f32 *)(record + 0x170) < vertical) {
        *(u32 *)(record + 0x60) = *(u32 *)(record + 0x60) & ~7u;
        *(u32 *)(record + 0x60) = *(u32 *)(record + 0x60) & ~8u;
        *(u32 *)(record + 0x60) = *(u32 *)(record + 0x60) & ~0x40u;
        *(u32 *)(record + 0x60) = *(u32 *)(record + 0x60) & ~0x20u;
        *(f32 *)(record + 0x44) = 0.0f;
        *(f32 *)(record + 0x48) = 0.0f;
        *(f32 *)(record + 0x4C) = 0.0f;
        if (*(s16 *)(record + 0x64) >= 33) {
            *(s16 *)(record + 0x64) = 32;
        }
    } else {
        scale = *(f32 *)(record + 0x14);
        *(f32 *)(record + 0x44) *= scale;
        *(f32 *)(record + 0x48) = -vertical * scale;
        *(f32 *)(record + 0x4C) *= scale;
        *(f32 *)(record + 0x50) *= scale;
        *(f32 *)(record + 0x54) *= scale;
        *(f32 *)(record + 0x58) *= scale;
    }
    return 1;
}

s32 func_150B378C(u8 *arg0) {
    u8 *temp_v0 = *(u8 **) (arg0 + 0x98);
    s32 temp_v1 = *(s16 *) (arg0 + 0x1C) << 4;

    if (temp_v1 >= 0x100) {
        temp_v1 = 0xFF;
    }
    if (temp_v1 < *(temp_v0 + 0x1B)) {
        *(temp_v0 + 0x1B) = temp_v1;
    }
    return 1;
}

s32 func_150B37C8() {
    return 0;
}
