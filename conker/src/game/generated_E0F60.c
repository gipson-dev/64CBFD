#include <ultra64.h>

/* Recovered effect routines from the original assembly slice. */

typedef struct { f32 x, y, z; u8 pad[2]; s16 angle; } EffectPosition150B3AB0;
typedef struct { u8 kind, pad01; s16 size; u8 mode, enabled; s8 value; u8 pad07; } EffectPacket150B3AB0;
extern s32 D_800BE9E8;
extern u8 *D_800DBFF0;
extern f32 D_8009FBC0[];
void func_1512D748(void *, s32, s32);
void func_15143134(f32 *, f32 *, u8 *);
s32 func_150ADA20(void);
void func_1514C858(f32, f32, f32, f32, s32, s32, s32, s32, s32, s32, f32, s32, s32);
u8 *func_151D8868(u8 *, s32, u8, s32);
void func_151D3FF4(f32 *, u8, s32);
/* Dispatch actor-linked effects; retain the retail slot-byte reloads. */
void func_150B3AB0(u8 *actor, volatile u8 slot) {
    EffectPosition150B3AB0 position;
    EffectPacket150B3AB0 packet;
    if (actor != NULL && *(u8 **)(actor + 0x1D4) != NULL) {
        func_1512D748(D_800DBFF0 + D_800BE9E8 * 0x9A0, 6, 1);
        position.angle = (*(u16 *)(actor + 0x7A) >> 8) + 0x40;
        func_15143134(D_8009FBC0, (f32 *)&position, *(u8 **)(actor + 0x1D4) + 0x640);
        func_1514C858(position.x, position.y, position.z, 10.0f, position.angle, 0, 255, (u32)func_150ADA20() % 31 + 40, 8, 0, 0.0f, 0, slot);
        packet.kind = 1;
        packet.size = (func_150ADA20() & 15) + 12;
        packet.mode = (func_150ADA20() & 3) + 5;
        packet.value = -1;
        packet.enabled = 1;
        func_151D8868((u8 *)&packet, 0, slot, 0);
        func_151D3FF4((f32 *)&position, slot, 0);
    }
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
} RadialEffect150B3C0C;
f32 func_151423D8(u8);
f32 func_150ADA68(void);
void func_151429E0(u8,u8 *,u8 *,u8 *);
void *func_15156190(void *,u8,s32,u8,s32);
void func_15156388(void *,u8,s32);
extern f32 D_8009FBCC,D_8009FBD0,D_8009FBD4,D_8009FBD8;
extern f32 D_8009FBDC,D_8009FBE0;

/* Build a radial color effect and submit its shared descriptor twice. */
s32 func_150B3C0C(s32 source,s16 index,f32 x,f32 y,f32 z,
    f32 originX,f32 originY,f32 originZ,s32 angle,s32 start,f32 radius,
    s32 style,f32 extra,s32 context,u8 slot) {
    f32 startQuarter,startValue,angleQuarter,speed;
    RadialEffect150B3C0C packet;
    startQuarter = func_151423D8((u8)((u32)start - 64U));
    startValue = func_151423D8((u8)start);
    angleQuarter = func_151423D8((u8)((u32)angle - 64U));
    speed = func_151423D8((u8)angle);
    speed = 10.0f * speed;
    packet.position.x = x;
    packet.position.y = y;
    packet.position.z = z;
    packet.velocity.x = speed * startQuarter;
    packet.velocity.y = -10.0f * angleQuarter;
    packet.velocity.z = speed * startValue;
    packet.field18 = func_150ADA68() * D_8009FBCC + D_8009FBD0;
    packet.field1C = func_150ADA68() * D_8009FBD4 + D_8009FBD8;
    func_151429E0(8,&packet.color0[0],&packet.color0[1],&packet.color0[2]);
    func_151429E0(8,&packet.color1[0],&packet.color1[1],&packet.color1[2]);
    packet.color0[3] = 255;
    packet.color1[3] = 255;
    packet.kind = 9;
    packet.lifetime = (func_150ADA20() & 15) + 15;
    packet.field30 = func_150ADA68() * D_8009FBDC + D_8009FBE0;
    packet.flags = 0x1601;
    packet.alpha = 255;
    packet.field36 = 10;
    packet.field38 = 25;
    func_15156190(&packet,1,0,slot,1);
    func_15156388(&packet,1,0);
    return 1;
}
