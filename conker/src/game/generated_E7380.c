#include <ultra64.h>
extern f32 D_800BE9A4;
extern f32 D_8009FE2C;


/* Partially recovered text-only slice asm/E7380.s. */

typedef struct { f32 x, y, z; } SurfacePointE7380;
/* The query supplies nine halfwords; their individual meanings are unrecovered. */
typedef struct { s16 field[9]; } SurfaceContextE7380;
typedef struct {
    u32 flags;
    u16 duration;
    u8 category, field07;
    u32 field08, field0C;
    u8 color[4], field14, field15, field16, field17;
    u32 field18;
    u8 reserved1C[6];
    s16 field22, field24;
    u8 reserved26[2];
} SurfaceBurstE7380;
typedef struct {
    s16 field00, field02;
    SurfacePointE7380 position, direction;
    SurfaceContextE7380 context;
    u8 reserved2E[2];
    f32 field30;
    u8 category, field35;
    u16 field36;
    s16 field38, field3A;
    f32 field3C, field40;
    u32 flags;
    u8 field48, field49, reserved4A[2];
    f32 field4C, field50, field54, field58;
    u8 field5C, field5D, reserved5E[2];
    u32 field60, field64;
    s16 field68, field6A;
    f32 field6C, field70;
} SurfaceSprayE7380;
extern u8 D_80084060;
extern f32 D_8009FE10, D_8009FE14, D_8009FE18, D_8009FE1C;
extern f32 D_8009FE20, D_8009FE24, D_8009FE28;
void func_151E7EF8(void);
void func_151E7F60(void);
s32 func_150A3058(s32, s16, s16, s16);
s32 func_150AC9C0(f32, f32, f32, f32, f32, f32, s32, void *,
    f32 *, f32 *, f32 *, f32 *, s32 *, s32, f32);
u8 func_15145C90(s32);
u32 func_150ADA20(void);
f32 func_150ADA68(void);
void *func_1513C650(void *, u8, u8, void *, f32, f32, f32, f32, f32,
    u8, u8, s32, s32, s32, u8, s32);
void func_151511FC(void *, u8, s32);


/* Check the position gates, query the surface, and submit impact descriptors. */
void func_150B9ED0(u8 *point, f32 oldX, f32 oldZ, u8 mode, s32 tag) {
    f32 dx, dy, dz;
    SurfacePointE7380 position;
    SurfaceContextE7380 context;
    s32 hit;
    SurfaceBurstE7380 burst;
    SurfaceSprayE7380 spray;
    f32 firstScale, secondScale;
    u32 firstRandom, secondRandom, thirdRandom;
    u32 *limit;
    u32 *cursor;
    u32 checksum;
    if (point == NULL) return;
    limit = (u32 *)func_151E7F60;
    cursor = (u32 *)func_151E7EF8;
    checksum = 0;
    while (cursor < limit) {
        checksum += ~*cursor++;
    }
    if (checksum != 0x3843095EU) D_80084060 = 255;

    if (func_150A3058(2, (s16)(s32)*(f32 *)(point + 0x14),
            (s16)(s32)*(f32 *)(point + 0x18), (s16)(s32)*(f32 *)(point + 0x1C))) return;
    if (func_150A3058(1, (s16)(s32)*(f32 *)(point + 0x14),
            (s16)(s32)*(f32 *)(point + 0x18), (s16)(s32)*(f32 *)(point + 0x1C))) return;

    dy = 0.0f;
    dx = -(*(f32 *)(point + 0x14) - oldX);
    dz = -(*(f32 *)(point + 0x1C) - oldZ);
    if (!func_150AC9C0(*(f32 *)(point + 0x14), *(f32 *)(point + 0x18) + 80.0f,
            *(f32 *)(point + 0x1C), dx, dy, dz, 0, &context,
            &position.x, &position.y, &position.z, NULL, &hit, 0, 0.0f)) return;

    if (func_15145C90(hit)) {
        burst.category = 6;
        burst.field07 = 0;
        burst.flags = 0x9F01;
        burst.duration = func_150ADA20() % 51U + 100;
        burst.field08 = 0;
        burst.field0C = 0;
        burst.color[0] = func_150ADA20() % 101U + 155;
        burst.color[1] = 255;
        burst.color[2] = 255;
        burst.color[3] = 255;
        burst.field14 = 255;
        burst.field15 = 255;
        burst.field18 = 0x3B0002;
        burst.field16 = 0;
        burst.field17 = 7;
        burst.field22 = 25;
        burst.field24 = 10;
        firstScale = func_150ADA68();
        secondScale = func_150ADA68();
        firstRandom = func_150ADA20();
        secondRandom = func_150ADA20();
        thirdRandom = func_150ADA20();
        func_1513C650(&burst, 0, 0, &context, position.x, position.y, position.z,
            firstScale * 20.0f + 40.0f, secondScale * 20.0f + 40.0f,
            firstRandom & 255, (thirdRandom & 1) + ((secondRandom & 1) << 1),
            3, 255, 0, mode, tag);
    }

    spray.field00 = 15;
    spray.field02 = 10;
    spray.position = position;
    spray.direction.x = -dx;
    spray.direction.y = -dy;
    spray.direction.z = -dz;
    spray.context = context;
    spray.field30 = D_8009FE10;
    spray.category = 7;
    spray.field35 = 0;
    spray.field36 = 0x3B01;
    spray.field38 = 26;
    spray.field3A = 20;
    spray.field3C = 7.0f;
    spray.field40 = 10.0f;
    spray.flags = 0x5C0001;
    spray.field48 = 100;
    spray.field49 = 155;
    spray.field4C = D_8009FE14;
    spray.field50 = D_8009FE18;
    spray.field54 = D_8009FE1C;
    spray.field58 = D_8009FE20;
    spray.field5C = 0;
    spray.field5D = 7;
    spray.field60 = 3;
    spray.field64 = 255;
    spray.field68 = 10;
    spray.field6A = 25;
    spray.field6C = D_8009FE24;
    spray.field70 = D_8009FE28;
    func_151511FC(&spray, mode, tag);
}


s32 func_150BA35C(u8 *arg0) {
    s16 value = *(s16 *)(arg0 + 0x1C);

    if (value < 0x40) {
        arg0[0x28] = value << 2;
    }
    return 1;
}

/* Apply vertical acceleration and advance five float fields by the live timestep. */
s32 func_150BA37C(u8 *actor) {
    *(f32 *)(actor + 0x114) += D_8009FE2C * D_800BE9A4;
    *(f32 *)(actor + 0x34) += *(f32 *)(actor + 0x110) * D_800BE9A4;
    *(f32 *)(actor + 0x38) += *(f32 *)(actor + 0x114) * D_800BE9A4;
    *(f32 *)(actor + 0x3C) += *(f32 *)(actor + 0x118) * D_800BE9A4;
    *(f32 *)(actor + 0x40) += *(f32 *)(actor + 0x11C) * D_800BE9A4;
    *(f32 *)(actor + 0x44) += *(f32 *)(actor + 0x120) * D_800BE9A4;
    return 1;
}

s32 func_150BA424(u8 *arg0) {
    f32 delta;
    s32 actor_intensity;
    s32 distance_intensity;
    s32 result;

    delta = *(f32 *)(arg0 + 0x38) - *(f32 *)(arg0 + 0x124);
    if (delta < 0.0f) {
        return 0;
    }

    actor_intensity = *(s16 *)(arg0 + 0x1C) << 4;
    if (actor_intensity >= 0x100) {
        actor_intensity = 0xFF;
    }

    distance_intensity = (s32)delta << 2;
    if (distance_intensity >= 0x100) {
        distance_intensity = 0xFF;
    }

    if (distance_intensity < actor_intensity) {
        arg0[0x5C] = distance_intensity;
    } else {
        arg0[0x5C] = actor_intensity;
    }

    result = 1;
    if (arg0[0x5C] < 0) {
        return 0;
    }
    return result;
}
