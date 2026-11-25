#include <ultra64.h>

/* Recovered effect routines and remaining non-matching code for asm/EEB10.s. */

void func_1514C2F0(f32, f32, f32, f32, u8, s8, s16, u8, s32, f32, s32, u8);

void func_150C1660(f32 arg0, f32 arg1, f32 arg2, u8 arg3) {
    func_1514C2F0(arg0, arg1, arg2, 80.0f, 0, 3, 0x19, 2, 0, 0.0f, 0, arg3);
}

#include "structs.h"

typedef struct {
    vertex position;
    s16 lifetime,field0E;
    s32 active;
    u8 reserved14,count,reserved16[6];
} RadialRequest150C16C0;
typedef struct {
    f32 field00;
    vertex velocity;
    f32 field10;
    u8 reserved14[4],field18,kind,alpha,field1B,reserved1C[4];
} RadialPayload150C16C0;
typedef struct {
    s32 field00,field04,field08,field0C,field10,field14,field18;
    u8 field1C,field1D,reserved1E[2];
} RadialRender150C16C0;
f32 func_150ADA68(void);
s32 func_150ADA20(void);
f32 func_151423D8(u8);
void *func_15147DA0(void *,void *,s32,s32,s32,s32,s32,s32,s32,s32,s32,void *,s32,u8,s32);
extern f32 D_800A01F0,D_800A01F4,D_800A01F8,D_800A01FC,D_800A0200;

/* Emit one randomized radial effect using the captured heading. */
s32 func_150C16C0(s32 source,s16 index,f32 x,f32 y,f32 z,
    f32 originX,f32 originY,f32 originZ,s32 angle,s32 start,f32 radius,
    s32 style,f32 extra,s32 context,u8 slot) {
    f32 scale;
    RadialRequest150C16C0 request;
    RadialPayload150C16C0 payload;
    RadialRender150C16C0 render;
    s16 pitch;
    f32 pitchValue,pitchQuarter,headingValue,headingQuarter,speed;
    s32 remaining = 1;
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
    payload.kind = 10;
    payload.alpha = 255;
    payload.field18 = 40;
    payload.field1B = 255;
    request.position.x = x;
    request.position.y = y;
    scale = D_800A01F0;
    request.position.z = z;
    do {
        pitch = (u32)func_150ADA20() % 13U - 63;
        pitchValue = func_151423D8((u8)pitch);
        pitchQuarter = func_151423D8((u8)((u32)pitch - 64U));
        headingValue = func_151423D8((u8)angle);
        headingQuarter = func_151423D8((u8)((u32)angle - 64U));
        speed = func_150ADA68() * scale + 25.5f;
        request.count = (u32)func_150ADA20() % 9U + 5;
        request.lifetime = ((u32)func_150ADA20() & 63U) + 90;
        payload.field00 = func_150ADA68() * D_800A01F4 + D_800A01F8;
        payload.field10 = func_150ADA68() * D_800A01FC + D_800A0200;
        payload.velocity.x = (speed * pitchValue) * headingQuarter;
        payload.velocity.y = -speed * pitchQuarter;
        payload.velocity.z = (speed * pitchValue) * headingValue;
        func_15147DA0(&request,&payload,0,1,5,0,0,0,0,0,0,&render,0,slot,0);
        remaining--;
    } while (remaining != 0);
    return 1;
}


s32 func_150C1978(u8 *arg0) {
    u8 *temp_v0 = *(u8 **) (arg0 + 0x98);
    s32 temp_v1 = *(s16 *) (arg0 + 0x1C) << 3;

    if (temp_v1 >= 0x100) {
        temp_v1 = 0xFF;
    }
    *(temp_v0 + 0x1B) = temp_v1;
    if ((temp_v1 & 0xFF) < 0) {
        return 0;
    }
    return 1;
}
