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


#include <string.h>
s32 func_151422DC(s32,s32,s32,s32,s32,s32,s32);
extern u8 D_8009F968[],D_8009F970[],D_8009F998[],D_8009F9A4[];
extern u8 D_8009F9CC[],D_8009F9D8[],D_8009FA00[],D_8009FA0C[];
extern u8 D_8009FA34[],D_8009FA44[],D_8009FA6C[],D_8009FA78[];
extern u8 D_8009FAA0[],D_8009FAB0[],D_8009FAD8[],D_8009FAE4[],D_8009FB0C[],D_8009FB18[];
extern f32 D_8009FB9C,D_8009FBA0,D_8009FBA4,D_8009FBA8,D_8009FBAC,D_8009FBB0;

/* Capture retail tweak defaults, build the effect, and attach its extra float. */
s32 func_150B3188(s32 source,s16 index,f32 x,f32 y,f32 z,
    f32 originX,f32 originY,f32 originZ,u32 heading,s32 start,f32 radius,
    s32 style,f32 extra,s32 context,u8 slot) {
    f32 headingCosine,headingSine,horizontal,yawCosine,yawSine,pitchCosine,pitchSine,speed;
    s16 duration;
    f32 fieldBias,fieldRange,speedBase,speedRange,sizeBase,sizeRange,yawScale,pitchScale;
    AngularExtended150B2EB4 descriptor;
    u8 *created;
    f32 payload;
    headingCosine = func_151423D8((u8)(heading - 64U));
    headingSine = func_151423D8((u8)heading);
    duration = func_151422DC(6,(s32)D_8009F968,1,500,300,(s32)D_8009F970,0x742);
    fieldBias = func_151422DC(7,(s32)D_8009F998,-5000,0,0,(s32)D_8009F9A4,0x750) * D_8009FB9C;
    fieldRange = func_151422DC(8,(s32)D_8009F9CC,-5000,0,0,(s32)D_8009F9D8,0x752) * D_8009FBA0;
    speedBase = func_151422DC(9,(s32)D_8009FA00,0,500,0,(s32)D_8009FA0C,0x75A);
    speedRange = func_151422DC(10,(s32)D_8009FA34,0,500,0,(s32)D_8009FA44,0x75C);
    sizeBase = func_151422DC(11,(s32)D_8009FA6C,0,5000,1000,(s32)D_8009FA78,0x761) * D_8009FBA4;
    sizeRange = func_151422DC(12,(s32)D_8009FAA0,0,5000,0,(s32)D_8009FAB0,0x763) * D_8009FBA8;
    yawScale = func_151422DC(13,(s32)D_8009FAD8,-255,255,0,(s32)D_8009FAE4,0x769);
    pitchScale = func_151422DC(14,(s32)D_8009FB0C,-255,255,0,(s32)D_8009FB18,0x76F);
    descriptor.flags = 0x29E9;
    descriptor.scale[0] = 1.0f;
    descriptor.scale[1] = 1.0f;
    descriptor.scale[2] = 1.0f;
    descriptor.rotation[0] = 0.0f;
    descriptor.rotation[1] = 0.0f;
    descriptor.rotation[2] = 0.0f;
    payload = -18.0f;
    descriptor.position[0] = x;
    descriptor.position[1] = y;
    descriptor.position[2] = z;
    descriptor.field04 = D_8009FBAC;
    speed = func_150ADA68() * speedRange + speedBase;
    index = (u32)start + (s32)(((yawScale * headingSine) * radius) * extra) - 64U;
    yawCosine = func_151423D8((u8)(index - 64));
    yawSine = func_151423D8((u8)index);
    index = (s32)(pitchScale * headingCosine) - 20;
    pitchCosine = func_151423D8((u8)(index - 64));
    pitchSine = func_151423D8((u8)index);
    horizontal = speed * pitchSine;
    descriptor.velocity[0] = horizontal * yawCosine;
    descriptor.velocity[1] = -speed * pitchCosine;
    descriptor.velocity[2] = horizontal * yawSine;
    descriptor.field40 = func_150ADA68() * 4.0f + -2.0f;
    descriptor.field44 = 0.0f;
    descriptor.field48 = func_150ADA68() * 4.0f + -2.0f;
    descriptor.duration = duration + 32;
    descriptor.field4C = func_150ADA68() * fieldRange + fieldBias;
    descriptor.field08 = descriptor.field0C = func_150ADA68() * sizeRange + sizeBase;
    descriptor.field00 = descriptor.field08 * D_8009FBB0;
    descriptor.resource = 28;
    descriptor.field58 = 0;
    descriptor.field5C = 0;
    descriptor.field60 = 255;
    descriptor.field61 = 1;
    descriptor.field62 = 0;
    descriptor.field63 = 5;
    descriptor.field64 = 0;
    descriptor.field65 = 0;
    descriptor.field66 = 0;
    descriptor.field67 = 0;
    descriptor.field68 = 0;
    descriptor.field6A = 2;
    descriptor.field6C = 0;
    descriptor.field70 = 0;
    descriptor.field72 = 32;
    descriptor.field74 = 7;
    created = func_15132A4C(&descriptor,3,255,4,slot,0);
    if (created != 0) {
        memcpy((u8 *)created + 0x170,&payload,4);
    }
    return 1;
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

#include "structs.h"
typedef struct { f32 x,y,z; u8 opaque0C[8]; } Position150B37C8;
typedef struct {
    s32 flags; s16 duration; u8 kind,opaque07;
    s32 field08,field0C;
    u8 field10,field11,field12,field13,field14,field15,opaque16[2];
    u32 resource; u8 opaque1C[12];
} Descriptor150B37C8;
typedef struct { s16 entries[3]; } Choices150B37C8;
typedef struct {
    vertex position; s16 duration,field0E; s32 active;
    u8 opaque14,count,opaque16[6];
} Request150B37C8;
typedef struct {
    f32 field00; vertex velocity; f32 field10;
    u8 opaque14[4],field18,kind,alpha,field1B,opaque1C[4];
} Payload150B37C8;
typedef struct {
    s32 field00,field04,field08,field0C,field10,field14,field18;
    u8 field1C,field1D,opaque1E[2];
} Render150B37C8;
extern Choices150B37C8 D_80088700;
s32 func_150ADA20(void);
struct210 *func_1513C73C(s32,u8,u8,s32,f32,f32,f32,f32,f32,u8,u8,s32,u8,s32);
void *func_15147DA0(void *,void *,s32,s32,s32,s32,s32,s32,s32,s32,s32,void *,s32,u8,s32);

/* Submit the actor's captured position effect and its live secondary payload. */
s32 func_150B37C8(u8 *actor,f32 previousX,f32 previousY,f32 previousZ,
    f32 height,void *parameter) {
    u8 *record=*(u8 **)(actor+0x98);
    Position150B37C8 *positions=*(Position150B37C8 **)(actor+0x94);
    Descriptor150B37C8 descriptor;
    f32 range;
    Choices150B37C8 choices=D_80088700;
    Request150B37C8 request;
    Payload150B37C8 payload;
    Render150B37C8 render;
    s32 byteDraw,parity;
    record[0x20]=4;
    range=func_150ADA68()*50.0f+50.0f;
    descriptor.kind=choices.entries[(u32)func_150ADA20()%3U];
    descriptor.field08=0;
    descriptor.field0C=0;
    descriptor.flags=17;
    descriptor.duration=150;
    descriptor.field10=record[0x1B];
    descriptor.field11=record[0x1A];
    descriptor.field12=0;
    descriptor.field13=0;
    descriptor.field14=0;
    descriptor.field15=255;
    descriptor.resource=0x30002;
    /* Capture one byte draw, then combine the following two low bits. */
    byteDraw=func_150ADA20();
    parity=func_150ADA20();
    parity=(func_150ADA20()&1)+(parity&1);
    func_1513C73C((s32)&descriptor,1,0,(s32)parameter,positions[*(s8 *)(actor+0x2D)].x,height,positions[*(s8 *)(actor+0x2D)].z,range,range,
        byteDraw&255,parity,0,actor[0x0C],actor[1]);
    render.field00=0;
    render.field04=1;
    render.field08=0x160600;
    render.field0C=3;
    render.field10=16;
    render.field14=128;
    render.field18=32;
    render.field1C=0;
    render.field1D=9;
    request.active=1;
    request.field0E=1;
    payload.field18=8;
    payload.kind=record[0x19];
    payload.alpha=record[0x1A];
    payload.field1B=record[0x1B];
    request.position.x=positions[*(s8 *)(actor+0x2D)].x;
    request.position.y=height;
    request.position.z=positions[*(s8 *)(actor+0x2D)].z;
    request.count=actor[0x25];
    request.duration=60;
    payload.field00=*(f32 *)(record+0)*0.75f;
    payload.field10=*(f32 *)(record+0x10);
    payload.velocity.x=*(f32 *)(record+4);
    payload.velocity.y=func_150ADA68()*15.0f+15.0f;
    payload.velocity.z=*(f32 *)(record+0x0C);
    func_15147DA0(&request,&payload,0,1,7,0,0,0,0,0,0,&render,0,actor[0x0C],actor[1]);
    return 1;
}
