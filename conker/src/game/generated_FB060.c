#include <ultra64.h>

typedef struct GroundResult150CDBB0 {
    f32 height;
    s16 vertices[9];
    s16 pad16;
    u32 metadata;
    u8 flags;
    u8 state;
    u16 pad1E;
    s32 value;
} GroundResult150CDBB0;

extern f32 D_800A07B0;
void func_1504715C(GroundResult150CDBB0 *, void *);
s32 func_15046C80(f32 *, u16, f32, GroundResult150CDBB0 *);
u32 func_150ADA20(void);
void func_1514C678(f32, f32, f32, f32, s16, s16, s16, u8, s32, f32, void *, u8);

/* Query the ground height and submit two randomized effects on success. */
void func_150CDBB0(u8 *actor, u8 flags, s32 unused) {
    f32 point[3];
    GroundResult150CDBB0 result;
    u32 random;

    if (actor != NULL) {
        func_1504715C(&result, actor);
        point[0] = *(f32 *)(actor + 0x14);
        point[1] = *(f32 *)(actor + 0x18) + 1000.0f;
        point[2] = *(f32 *)(actor + 0x1C);
        if (func_15046C80(point, 0, *(f32 *)(actor + 0x18) - D_800A07B0, &result)) {
            point[1] = result.height;
            random = func_150ADA20();
            func_1514C678(point[0], point[1], point[2], 251.0f, 0, 255,
                          (random & 15U) + 35, 0x17, 0, 0.0f, NULL, flags);
            random = func_150ADA20();
            func_1514C678(point[0], point[1], point[2], 290.0f, 0, 255,
                          (random % 21U) + 30, 0x18, 0, 0.0f, NULL, flags);
        }
    }
}

/* Recovered radial effect constructors from the original assembly slice. */
#include "structs.h"

typedef struct {
    u32 field00,field04; u16 field08; s16 lifetime;
    u32 field0C,field10;
    u8 field14,field15,field16,field17;
    u8 field18,field19,field1A,field1B;
    u8 field1C,kind; s16 field1E,field20,field22;
    f32 field24,sizeStart,sizeEnd;
    vertex position;
    f32 field3C,field40,field44;
    vertex direction;
    f32 field54; u32 flags;
    u8 reserved5C[4]; u8 field60,field61; s8 field62,field63;
    u8 reserved64[12];
} RadialParticle150CDCF4;
u32 func_150ADA20(void);
f32 func_150ADA68(void);
void func_15143794(s16,s16,f32,vertex *);
void *func_15130374(void *,u8,s32,u8,s32);
void *memcpy(void *,const void *,unsigned int);

extern f32 D_800A07B4,D_800A07B8,D_800A07BC,D_800A07C0;

/* Emit a kind-0x29 radial particle and retain its damping payload on success. */
s32 func_150CDCF4(s32 source,s16 index,f32 x,f32 y,f32 z,
    f32 originX,f32 originY,f32 originZ,s16 angle,u8 start,f32 radius,
    s32 style,f32 extra,s32 context,u8 slot) {
    RadialParticle150CDCF4 packet;
    s16 pitch;
    f32 damping;
    f32 sample;
    s32 pitchDraw;
    void *result;
    packet.kind = 0x29;
    packet.field08 = 0xE03;
    packet.field00 = 0x200005;
    packet.field04 = 0;
    packet.lifetime = (u32)func_150ADA20() % 41U + 50;
    packet.field0C = 0;
    packet.field10 = 0;
    packet.field18 = 0xB0;
    packet.field19 = 0xA0;
    packet.field1A = 0x2A;
    packet.field14 = 0x40;
    packet.field15 = 0x0B;
    packet.field16 = 0x6A;
    packet.field17 = 255;
    packet.field1B = (u32)func_150ADA20() % 101U + 100;
    packet.field1C = 255;
    packet.field60 = 3;
    packet.field61 = 3;
    sample = func_150ADA68();
    packet.sizeStart = packet.sizeEnd = sample * D_800A07B4 + 404.0f;
    packet.position.x = x;
    packet.position.y = y;
    packet.position.z = z;
    pitchDraw = func_150ADA20();
    sample = func_150ADA68();
    pitch = (u32)pitchDraw % 20U - 19;
    func_15143794(angle,pitch,
        (sample * 150.0f + 150.0f) * D_800A07B8,&packet.direction);
    packet.field54 = 0.0f;
    packet.flags = 0xE05;
    if (func_150ADA20() & 1) packet.flags |= 0x40;
    if (func_150ADA20() & 1) packet.flags |= 0x80;
    packet.field62 = 10;
    packet.field63 = -1;
    packet.field1E = 30;
    packet.field20 = 8;
    packet.field22 = 70;
    packet.field24 = D_800A07BC;
    damping = D_800A07C0;
    result = func_15130374(&packet,1,4,slot,1);
    if (result != 0) memcpy((u8 *)result + 0xA8,&damping,4);
    return 1;
}



#include "structs.h"

typedef struct {
    f32 field00,field04,sizeStart,sizeEnd;
    vertex rotation,scale,position,direction;
    f32 field40,field44,field48,field4C;
    u32 field50; s16 lifetime,field56;
    u8 field58,reserved59[3]; u32 field5C;
    u8 field60,field61,field62,field63,field64,field65,field66,field67,field68;
    u8 reserved69,field6A,reserved6B; u32 field6C;
    u8 field70,reserved71; s16 field72,field74; u8 reserved76[6];
} RadialSprite150CDF10;
u32 func_150ADA20(void);
f32 func_150ADA68(void);
void func_15143794(s16,s16,f32,vertex *);
void *func_15132A4C(void *,s32,s32,s32,u8,s32);

extern f32 D_800A07C4,D_800A07C8,D_800A07CC,D_800A07D0;
extern f32 D_800A07D8,D_800A07DC,D_800A07D4,D_800A07E0;

/* Emit a rotating radial sprite with randomized velocity and lifetime. */
s32 func_150CDF10(s32 source,s16 index,f32 x,f32 y,f32 z,
    f32 originX,f32 originY,f32 originZ,s16 angle,u8 start,f32 radius,
    s32 style,f32 extra,s32 context,u8 slot) {
    RadialSprite150CDF10 packet;
    s16 pitch;
    f32 sample;
    s32 pitchDraw;
    packet.position.x = x;
    packet.position.y = y;
    packet.position.z = z;
    packet.scale.z = packet.scale.y = packet.scale.x = 1.0f;
    packet.field50 = 0x29E8;
    packet.rotation.z = packet.rotation.y = packet.rotation.x = 0.0f;
    packet.field44 = 0.0f;
    packet.field00 = 1.0f;
    packet.field56 = 32;
    packet.field04 = D_800A07C4;
    pitchDraw = func_150ADA20();
    sample = func_150ADA68();
    pitch = (u32)pitchDraw % 41U - 61;
    func_15143794(angle,pitch,(sample * 101.0f + 150.0f) * D_800A07C8,&packet.direction);
    packet.field40 = (func_150ADA68() * 260.0f + -130.0f) * D_800A07CC;
    packet.field48 = (func_150ADA68() * 260.0f + -130.0f) * D_800A07D0;
    packet.lifetime = (u32)func_150ADA20() % 21U + 50;
    packet.field4C = (func_150ADA68() * D_800A07D4 + D_800A07D8) * D_800A07DC;
    sample = (func_150ADA68() * 302.0f + 52.0f) * D_800A07E0;
    packet.sizeEnd = packet.sizeStart = sample;
    packet.field58 = 0;
    packet.field5C = 0;
    packet.field60 = (u32)func_150ADA20() % 76U + 180;
    packet.field61 = 8;
    packet.field62 = 0;
    packet.field63 = 0;
    packet.field64 = 0;
    packet.field65 = 0;
    packet.field66 = 0;
    packet.field67 = 0;
    packet.field68 = 0;
    packet.field6A = 2;
    packet.field6C = 0;
    packet.field70 = 0;
    packet.field72 = 32;
    packet.field74 = 7;
    func_15132A4C(&packet,3,255,0,slot,0);
    return 1;
}

