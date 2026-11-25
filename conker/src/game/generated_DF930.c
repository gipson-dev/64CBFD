#include <ultra64.h>

/* Recovered effect routines from the original assembly slice. */

s32 func_150B2480(s32 arg0, s32 arg1) {
    return 0xA;
}

s32 func_150ADA20(void);
void func_1514C678(f32, f32, f32, f32, s16, s16, s16, u8, s32, f32, void *, u8);
void func_151D5404(f32 *, f32, f32, f32, s32, s32, s32, s32);
void func_151D3FF4(f32 *, u8, s32);

/* Capture the actor position before dispatching the three effects. */
/* Retain both unused words required by the callback table interface. */
void func_150B2494(u8 *actor, s32 unused1, s32 unused2) {
    f32 position[3];

    position[0] = *(f32 *)(actor + 0x14);
    position[1] = *(f32 *)(actor + 0x180);
    position[2] = *(f32 *)(actor + 0x1C);
    func_1514C678(position[0], position[1], position[2], 135.0f,
                 0, 255, (u32)func_150ADA20() % 15 + 27, 7, 0, 0.0f, 0, 255);
    func_151D5404(position, 1502.0f, 3000.0f, 0.00033333333f, 12, 15, 255, 0);
    func_151D3FF4(position, 255, 0);
}

#include "structs.h"

typedef struct {
    vertex position,velocity;
    f32 field18,field1C;
    u8 color0[4],color1[4],kind,reserved29;
    s16 lifetime;
    u16 flags,reserved2E;
    f32 field30;
    u8 alpha,reserved35;
    s16 field36,field38;
    u8 reserved3A[2];
} RadialEffect150B2570;
f32 func_151423D8(u8);
f32 func_150ADA68(void);
void func_151429E0(u8,u8 *,u8 *,u8 *);
void *func_15156190(void *,u8,s32,u8,s32);
extern f32 D_8009F900,D_8009F904,D_8009F908,D_8009F90C;
extern f32 D_8009F910,D_8009F914;

/* Emit a radial color effect with a randomized negative pitch. */
s32 func_150B2570(s32 source,s16 index,f32 x,f32 y,f32 z,
    f32 originX,f32 originY,f32 originZ,s32 angle,s32 start,f32 radius,
    s32 style,f32 extra,s32 context,u8 slot) {
    RadialEffect150B2570 packet;
    s16 pitch;
    f32 startQuarter,startValue,angleQuarter,speed;
    startQuarter = func_151423D8((u8)((u32)angle - 64U));
    startValue = func_151423D8((u8)angle);
    pitch = (u32)func_150ADA20() % 21U - 30;
    angleQuarter = func_151423D8((u8)((u32)pitch - 64U));
    speed = func_151423D8((u8)pitch);
    speed = 10.0f * speed;
    packet.position.x = x;
    packet.position.y = y;
    packet.position.z = z;
    packet.velocity.x = speed * startQuarter;
    packet.velocity.y = -10.0f * angleQuarter;
    packet.velocity.z = speed * startValue;
    packet.field18 = func_150ADA68() * D_8009F900 + D_8009F904;
    packet.field1C = func_150ADA68() * D_8009F908 + D_8009F90C;
    func_151429E0(8,&packet.color0[0],&packet.color0[1],&packet.color0[2]);
    func_151429E0(8,&packet.color1[0],&packet.color1[1],&packet.color1[2]);
    packet.color0[3] = 255;
    packet.color1[3] = 255;
    packet.kind = 9;
    packet.lifetime = (u32)func_150ADA20() % 7U + 18;
    packet.field30 = func_150ADA68() * D_8009F910 + D_8009F914;
    packet.flags = 0x1601;
    packet.alpha = 255;
    packet.field36 = 8;
    packet.field38 = 31;
    func_15156190(&packet,1,0,slot,1);
    return 1;
}
