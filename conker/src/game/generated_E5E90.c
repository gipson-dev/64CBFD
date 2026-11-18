#include <ultra64.h>
extern f32 D_8009FDD4, D_8009FDD8, D_8009FDDC, D_800BE9A4;

void func_15142600(Mtx *output, f32 row0, f32 row1, f32 cx, f32 cy, f32 cz,
    f32 sx, f32 sy, f32 sz, f32 ex, f32 ey, f32 ez);

/* Non-matching placeholders for the text-only asm slice asm/E5E90.s. */

typedef struct { f32 x, y, z; } TerminalPointE5E90;
typedef struct {
    u8 category, field01;
    s16 field02, duration;
    u8 reserved06[2];
    u32 field08, field0C;
    u8 color[4];
    f32 field14, field18;
    TerminalPointE5E90 position;
    f32 field28, field2C, field30, field34, field38, field3C;
    u32 flags;
    u8 field44, field45, field46, field47, reserved48[8];
    u32 field50;
    s16 field54, field56;
} TerminalBurstE5E90;
typedef struct { f32 value; u8 retained04[4]; } TerminalExtraE5E90;
typedef struct {
    TerminalPointE5E90 position;
    f32 field0C, field10, field14, field18, field1C, field20;
    s16 field24, field26, field28, field2A, field2C, field2E;
    s16 field30, field32, field34, field36;
    u8 field38, field39, field3A, reserved3B;
    u32 field3C, field40, field44, field48, field4C, field50;
    u8 field54, field55, field56, reserved57;
    u32 field58, field5C, field60, field64, field68;
    u32 field6C, field70, field74, field78;
    u8 field7C, field7D, reserved7E[2];
    s16 field80, field82;
    u32 field84;
} TerminalSprayE5E90;
extern f32 D_8009FDB0, D_8009FDB4, D_8009FDB8;
extern u8 D_800A4AA0[];
extern s32 D_80088734[], D_8008873C;
u32 func_150ADA20(void);
f32 func_150ADA68(void);
void *func_1513D594(void *, void *, u8, u8, u8, u8, s16, f32, f32,
    s32, void *, s32, s32, u8, s32, u8, s32);
void func_15151A38(void *, u8, s32);
/* These call sites supply full argument words; the audio callee narrows them. */
u16 func_10010F88(s32, s32, s32, s32, s32, s32, s32, s32, s32, s32);
void *memcpy(void *, const void *, size_t);
void func_150A8050(f32 (*)[4], f32, f32, f32);
void func_150A7960(f32 (*)[4], f32, f32, f32, f32 *, f32 *, f32 *);


/* Advance the actor's amplitude-gated motion or submit its terminal effects. */
s32 func_150B89E0(u8 *actor, f32 x, f32 unusedY, f32 z, f32 y, void *context) {
    TerminalBurstE5E90 burst;
    TerminalExtraE5E90 extra;
    TerminalSprayE5E90 spray;
    f32 matrix[4][4];
    u32 firstRandom, secondRandom, thirdRandom;
    void *allocated;

    *(f32 *)(actor + 0x3C) = *(f32 *)(actor + 0x10) + y;
    if (*(f32 *)(actor + 0x140) > 15.0f) {
        if (*(f32 *)(actor + 0x140) > 30.0f) {
            burst.field54 = 25;
            burst.field56 = 10;
            burst.category = 4;
            burst.field01 = 0;
            burst.field02 = 0x3B02;
            burst.duration = (u32)func_150ADA20() % 31U + 40;
            burst.field08 = 0;
            burst.field0C = 0;
            burst.color[0] = 255;
            burst.color[1] = 255;
            burst.color[2] = 255;
            burst.color[3] = 255;
            burst.field14 = burst.field18 = (func_150ADA68() * 25.0f + 25.0f) * D_8009FDB0;
            burst.position.x = x;
            burst.position.y = y;
            burst.position.z = z;
            burst.field28 = 0.0f;
            burst.field2C = 0.0f;
            burst.field30 = 0.0f;
            burst.field34 = 0.0f;
            burst.field38 = 0.0f;
            burst.field3C = 0.0f;
            burst.flags = 0xC5C0001;
            burst.field44 = 255;
            burst.field45 = 255;
            burst.field46 = 0;
            burst.field47 = 7;
            extra.value = (func_150ADA68() * 80.0f + 50.0f) * D_8009FDB4;
            burst.field50 = *(u32 *)(actor + 0x128);
            firstRandom = func_150ADA20();
            secondRandom = func_150ADA20();
            thirdRandom = func_150ADA20();
            allocated = func_1513D594(&burst, D_800A4AA0, 24, 0, 0,
                (secondRandom & 1) + ((firstRandom & 1) << 1), thirdRandom & 255,
                500.0f, 500.0f, 0, context, *(u32 *)(actor + 0x14C),
                *(u32 *)(actor + 0x168), 0, 8, actor[0xC], actor[1]);
            if (allocated != NULL) memcpy((u8 *)allocated + 0x128, &extra, 8);
            spray.position.x = x;
            spray.position.y = y;
            spray.position.z = z;
            spray.field0C = 3.0f;
            spray.field10 = 3.0f;
            spray.field14 = D_8009FDB8;
            spray.field18 = 0;
            spray.field1C = 10.0f;
            spray.field20 = 10.0f;
            spray.field24 = 6;
            spray.field26 = 6;
            spray.field28 = 0;
            spray.field2A = 255;
            spray.field2C = -63;
            spray.field2E = 29;
            spray.field30 = 3;
            spray.field32 = 3;
            spray.field34 = 50;
            spray.field36 = 20;
            spray.field38 = 1;
            spray.field39 = 33;
            spray.field3A = 72;
            spray.field3C = 1;
            spray.field40 = 0;
            spray.field44 = 0;
            spray.field48 = 0;
            spray.field4C = 0;
            spray.field50 = 0;
            spray.field54 = 0;
            spray.field55 = 155;
            spray.field56 = 100;
            spray.field58 = *(u32 *)(actor + 0x14C);
            spray.field5C = *(u32 *)(actor + 0x168);
            spray.field60 = 0;
            spray.field64 = 0x220005;
            spray.field68 = 0x1D0600;
            spray.field6C = 1;
            spray.field70 = 0x3B;
            spray.field74 = 0x80;
            spray.field78 = 0x20;
            spray.field7C = 0;
            spray.field7D = 7;
            spray.field80 = 10;
            spray.field82 = 25;
            spray.field84 = *(u32 *)(actor + 0x128);
            func_15151A38(&spray, actor[0xC], actor[1]);
            thirdRandom = func_150ADA20();
            func_10010F88(D_80088734[thirdRandom & 1], 32000, 0, 0, 0,
                (s32)*(f32 *)(actor + 0x38), (s32)(y + 25.0f),
                (s32)*(f32 *)(actor + 0x40), 1000, 4000);
            return 0;
        }
        *(f32 *)(actor + 0x44) *= *(f32 *)(actor + 0x14);
        *(f32 *)(actor + 0x48) = -*(f32 *)(actor + 0x48) * *(f32 *)(actor + 0x14);
        *(f32 *)(actor + 0x4C) *= *(f32 *)(actor + 0x14);
        *(f32 *)(actor + 0x50) *= *(f32 *)(actor + 0x14);
        *(f32 *)(actor + 0x54) *= *(f32 *)(actor + 0x14);
        *(f32 *)(actor + 0x58) *= *(f32 *)(actor + 0x14);
        func_10010F88(D_8008873C, 32000, 0, 0, 0,
            (s32)*(f32 *)(actor + 0x38), (s32)*(f32 *)(actor + 0x3C),
            (s32)*(f32 *)(actor + 0x40), 1000, 4000);
    } else {
        actor[0x72] = 1;
        actor[0x78] = 1;
        *(u32 *)(actor + 0x60) &= 0xFFFFFF00U;
        func_150A8050(matrix, *(f32 *)(actor + 0x20),
            *(f32 *)(actor + 0x24), *(f32 *)(actor + 0x28));
        func_150A7960(matrix, 0.0f, 0.0f, 200.0f,
            (f32 *)(actor + 0x20), (f32 *)(actor + 0x24), (f32 *)(actor + 0x28));
        *(f32 *)(actor + 0x20) += *(f32 *)(actor + 0x38);
        *(f32 *)(actor + 0x24) += *(f32 *)(actor + 0x3C);
        *(f32 *)(actor + 0x28) += *(f32 *)(actor + 0x40);
    }
    return 1;
}

/* Collision metadata is copied as nine halfwords; its field meanings are unknown. */
typedef struct { s16 field[9]; } ImpactContextE5E90;
typedef struct {
    TerminalPointE5E90 position, velocity;
    ImpactContextE5E90 context;
    u8 reserved2A[2];
    f32 field2C, field30, field34, field38, field3C, field40, field44;
    s16 field48, field4A, field4C, field4E, field50, field52;
    u8 field54, field55, field56, reserved57;
    u32 field58, field5C, field60, field64, field68, field6C;
    u8 field70, field71, field72, reserved73;
    u32 field74, field78, field7C, field80, field84;
    u32 field88, field8C, field90, field94;
    u8 field98, field99, reserved9A[2];
    s16 field9C, field9E;
    u32 fieldA0;
} ImpactSprayE5E90;
extern f32 D_8009FDBC, D_8009FDC0, D_8009FDC4, D_8009FDC8, D_8009FDCC, D_8009FDD0;
f32 fabsf(f32);
#pragma intrinsic (fabsf)
s32 func_150A3058(s32, s16, s16, s16);
s32 func_150AC9C0(f32, f32, f32, f32, f32, f32, s32, void *,
    f32 *, f32 *, f32 *, f32 *, s32 *, s32, f32);
u8 func_15145C90(s32);
void func_15151670(void *, u8, s32);


/* Resolve an impact: damp light motion, or query and submit terminal effects. */
s32 func_150B8F44(u8 *actor, u8 *surface, f32 oldX, f32 oldY, f32 oldZ) {
    f32 dz, dy, dx;
    TerminalPointE5E90 position;
    ImpactContextE5E90 context;
    s32 hit;
    TerminalBurstE5E90 burst;
    TerminalExtraE5E90 extra;
    ImpactSprayE5E90 spray;
    u32 firstRandom, secondRandom, thirdRandom;
    void *allocated;
    f32 vertical = *(f32 *)(actor + 0x48);

    if (*(f32 *)(actor + 0x140) - fabsf(vertical) > 6.0f) {
        if (!func_150A3058(1, (s16)(s32)*(f32 *)(surface + 0x14),
                (s16)(s32)*(f32 *)(surface + 0x18), (s16)(s32)*(f32 *)(surface + 0x1C))) {
            dx = *(f32 *)(actor + 0x38) - oldX;
            dy = *(f32 *)(actor + 0x3C) - oldY;
            dz = *(f32 *)(actor + 0x40) - oldZ;
            if (func_150AC9C0(oldX, oldY, oldZ, dx, dy, dz, 0, &context,
                    &position.x, &position.y, &position.z, NULL, &hit, 0, 0.0f)) {
                if (func_15145C90(hit)) {
                    burst.field54 = 25;
                    burst.field56 = 10;
                    burst.category = 4;
                    burst.field01 = 0;
                    burst.field02 = 0x3B02;
                    burst.duration = func_150ADA20() % 31U + 40;
                    burst.field08 = 0;
                    burst.field0C = 0;
                    burst.color[0] = 255;
                    burst.color[1] = 255;
                    burst.color[2] = 255;
                    burst.color[3] = 255;
                    burst.field14 = burst.field18 = (func_150ADA68() * 25.0f + 25.0f) * D_8009FDBC;
                    burst.position = position;
                    burst.flags = 0xC5C0001;
                    burst.field44 = 255;
                    burst.field45 = 255;
                    burst.field46 = 0;
                    burst.field47 = 7;
                    burst.field28 = 0;
                    burst.field2C = 0;
                    burst.field30 = 0;
                    burst.field34 = 0;
                    burst.field38 = 0;
                    burst.field3C = 0;
                    extra.value = (func_150ADA68() * 80.0f + 50.0f) * D_8009FDC0;
                    burst.field50 = *(u32 *)(actor + 0x128);
                    firstRandom = func_150ADA20();
                    secondRandom = func_150ADA20();
                    thirdRandom = func_150ADA20();
                    allocated = func_1513D594(&burst, D_800A4AA0, 24, 0, 0,
                        (secondRandom & 1) + ((firstRandom & 1) << 1), thirdRandom & 255,
                        500.0f, 500.0f, 0, &context, *(u32 *)(actor + 0x14C),
                        *(u32 *)(actor + 0x168), 0, 8, actor[0xC], actor[1]);
                    if (allocated != NULL) memcpy((u8 *)allocated + 0x128, &extra, 8);
                }
                spray.velocity.x = -dx;
                spray.velocity.y = -dy;
                spray.velocity.z = -dz;
                spray.context = context;
                spray.field2C = 502.0f;
                spray.position = position;
                spray.field48 = 6;
                spray.field4A = 6;
                spray.field30 = 3.0f;
                spray.field34 = 3.0f;
                spray.field4C = 3;
                spray.field4E = 3;
                spray.field50 = 50;
                spray.field52 = 20;
                spray.field54 = 1;
                spray.field55 = 33;
                spray.field56 = 72;
                spray.field58 = 1;
                spray.field5C = 0;
                spray.field60 = 0;
                spray.field64 = 0;
                spray.field68 = 0;
                spray.field6C = 0;
                spray.field70 = 0;
                spray.field71 = 155;
                spray.field72 = 100;
                spray.field38 = D_8009FDC4;
                spray.field3C = D_8009FDC8;
                spray.field40 = D_8009FDCC;
                spray.field44 = D_8009FDD0;
                spray.field74 = *(u32 *)(actor + 0x14C);
                spray.field78 = *(u32 *)(actor + 0x168);
                spray.field7C = 0;
                spray.field80 = 0x220005;
                spray.field84 = 0x1D0600;
                spray.field88 = 1;
                spray.field8C = 0x3B;
                spray.field90 = 0x80;
                spray.field94 = 0x20;
                spray.field98 = 0;
                spray.field99 = 7;
                spray.field9C = 10;
                spray.field9E = 25;
                spray.fieldA0 = *(u32 *)(actor + 0x128);
                func_15151670(&spray, actor[0xC], actor[1]);
            }
        }
        thirdRandom = func_150ADA20();
        func_10010F88(D_80088734[thirdRandom & 1], 32000, 0, 0, 0,
            (s32)*(f32 *)(actor + 0x38), (s32)*(f32 *)(actor + 0x3C),
            (s32)*(f32 *)(actor + 0x40), 1000, 4000);
        return 0;
    }
    *(f32 *)(actor + 0x44) = 0;
    *(f32 *)(actor + 0x4C) = 0;
    if (vertical > 0.0f) *(f32 *)(actor + 0x48) = vertical * *(f32 *)(actor + 0x14);
    *(f32 *)(actor + 0x38) = *(f32 *)(surface + 0x14);
    *(f32 *)(actor + 0x3C) = *(f32 *)(surface + 0x18);
    *(f32 *)(actor + 0x40) = *(f32 *)(surface + 0x1C);
    *(f32 *)(actor + 0x50) *= *(f32 *)(actor + 0x14);
    *(f32 *)(actor + 0x54) *= *(f32 *)(actor + 0x14);
    *(f32 *)(actor + 0x58) *= *(f32 *)(actor + 0x14);
    func_10010F88(D_8008873C, 64000, 0, 0, 0,
        (s32)*(f32 *)(surface + 0x14), (s32)*(f32 *)(surface + 0x18),
        (s32)*(f32 *)(surface + 0x1C), 1000, 4000);
    return 1;
}


/* Apply the actor's counter-gated motion updates. */
s32 func_150B9560(u8 *actor) {
    f32 *step = (f32 *)(actor + 0x110);
    f32 factor;

    if (*(s16 *)(actor + 0x1C) < 80) {
        *step += D_8009FDD4 * D_800BE9A4;
        *(f32 *)(actor + 0x38) -= *step;
    }
    if (*(s16 *)(actor + 0x1C) >= 115) {
        factor = D_8009FDD8;
        *(f32 *)(actor + 0x2C) *= factor;
        *(f32 *)(actor + 0x30) *= factor;
    } else if (*(s16 *)(actor + 0x1C) < 65) {
        *(f32 *)(actor + 0x30) += D_8009FDDC;
    }
    return 1;
}

s32 func_150B95FC(u8 *arg0) {
    s16 value = *(s16 *)(arg0 + 0x1C);

    if (value < 0x20) {
        arg0[0x5C] = value << 3;
    }
    return 1;
}

s32 func_150B961C(u8 *arg0) {
    s16 value = *(s16 *)(arg0 + 0x1C);

    if (value < 0x40) {
        arg0[0x28] = value << 2;
    }
    return 1;
}

extern u8 *D_80088720, *D_80088730;
extern TerminalPointE5E90 D_80088724;
extern s32 D_80088740;
extern f32 D_8009FDE0, D_8009FDE4, D_8009FDE8, D_8009FDEC, D_8009FDF0;
extern f32 D_8009FDF4, D_8009FDF8, D_8009FDFC, D_8009FE00;
u8 *func_15083E90(s32);
f32 func_151423D8(u8);
s32 func_15046C80(void *, s32, f32, void *);


/* Steer toward cached targets, bounce on a close fast target, or submit terminal effects. */
s32 func_150B963C(u8 *actor) {
    f32 distance;
    f32 targetZ;
    f32 sine, cosine;
    TerminalPointE5E90 position;
    TerminalBurstE5E90 burst;
    TerminalExtraE5E90 extra;
    TerminalSprayE5E90 spray;
    u32 firstRandom, secondRandom, thirdRandom;
    u8 *target = D_80088730;
    void *allocated;
    f32 dx, dy, dz;

    if (target == NULL || *(u32 *)target == 0 || target[0x3B] != 1) {
        D_80088730 = func_15083E90(1);
    }
    target = D_80088730;
    if (target != NULL) {
        targetZ = *(f32 *)(target + 0x1C);
        dx = *(f32 *)(actor + 0x38) - *(f32 *)(target + 0x14);
        dy = *(f32 *)(actor + 0x3C) - *(f32 *)(target + 0x18);
        dz = *(f32 *)(actor + 0x40) - targetZ;
        distance = (dx * dx + dy * dy) + dz * dz;
        if (distance < *(f32 *)(actor + 0x10) * *(f32 *)(actor + 0x10) + D_8009FDE0) {
            if (*(f32 *)(target + 0x3C) > 15.0f) {
                if (func_150ADA20() & 1) {
                    sine = func_151423D8((u16)*(u16 *)(D_80088730 + 0x76) >> 8);
                    cosine = func_151423D8(((u16)*(u16 *)(D_80088730 + 0x76) >> 8) + 0x40);
                    actor[0x71] = 1;
                    *(u32 *)(actor + 0x60) |= 0x7D;
                    actor[0x73] = 1;
                    actor[0x75] = 1;
                    actor[0x78] = 0;
                    *(f32 *)(actor + 0x44) = (*(f32 *)(D_80088730 + 0x3C) * sine) * D_8009FDE4;
                    *(f32 *)(actor + 0x48) = func_150ADA68() * 15.0f + 10.0f;
                    *(f32 *)(actor + 0x4C) = (*(f32 *)(D_80088730 + 0x3C) * cosine) * D_8009FDE8;
                    *(s16 *)(actor + 0x64) = 300;
                    *(u32 *)(actor + 0x60) |= 0x80;
                    *(f32 *)(actor + 0x20) = 0;
                    *(f32 *)(actor + 0x24) = 0;
                    *(f32 *)(actor + 0x28) = 0;
                    return 1;
                }
            }
            position.x = *(f32 *)(actor + 0x38);
            position.y = *(f32 *)(actor + 0x3C) + 100.0f;
            position.z = *(f32 *)(actor + 0x40);
            if (func_15046C80(&position, 0, *(f32 *)(actor + 0x3C) - 2000.0f, actor + 0x110)) {
                position.y = *(f32 *)(actor + 0x110);
                burst.field54 = 25;
                burst.field56 = 10;
                burst.category = 4;
                burst.field01 = 0;
                burst.field02 = 0x3B02;
                burst.duration = func_150ADA20() % 31U + 40;
                burst.field08 = 0;
                burst.field0C = 0;
                burst.color[0] = 255;
                burst.color[1] = 255;
                burst.color[2] = 255;
                burst.color[3] = 255;
                burst.field14 = burst.field18 = (func_150ADA68() * 25.0f + 25.0f) * D_8009FDEC;
                burst.position = position;
                burst.flags = 0xC5C0001;
                burst.field44 = 255;
                burst.field45 = 255;
                burst.field46 = 0;
                burst.field47 = 7;
                burst.field28 = 0;
                burst.field2C = 0;
                burst.field30 = 0;
                burst.field34 = 0;
                burst.field38 = 0;
                burst.field3C = 0;
                extra.value = (func_150ADA68() * 80.0f + 50.0f) * D_8009FDF0;
                burst.field50 = *(u32 *)(actor + 0x128);
                firstRandom = func_150ADA20();
                secondRandom = func_150ADA20();
                thirdRandom = func_150ADA20();
                allocated = func_1513D594(&burst, D_800A4AA0, 24, 0, 0,
                    (secondRandom & 1) + ((firstRandom & 1) << 1), thirdRandom & 255,
                    500.0f, 500.0f, 0, actor + 0x114, *(u32 *)(actor + 0x14C),
                    *(u32 *)(actor + 0x168), 0, 8, actor[0xC], actor[1]);
                if (allocated != NULL) memcpy((u8 *)allocated + 0x128, &extra, 8);
            }
            spray.position = *(TerminalPointE5E90 *)(actor + 0x38);
            spray.field24 = 6;
            spray.field26 = 6;
            spray.field28 = 0;
            spray.field2A = 255;
            spray.field2C = -64;
            spray.field2E = 30;
            spray.field30 = 3;
            spray.field32 = 3;
            spray.field34 = 30;
            spray.field36 = 20;
            spray.field38 = 1;
            spray.field39 = 33;
            spray.field3A = 72;
            spray.field3C = 1;
            spray.field40 = 0;
            spray.field44 = 0;
            spray.field48 = 0;
            spray.field4C = 0;
            spray.field50 = 0;
            spray.field54 = 0;
            spray.field55 = 154;
            spray.field56 = 101;
            spray.field0C = 3.0f;
            spray.field10 = D_8009FDF4;
            spray.field14 = D_8009FDF8;
            spray.field18 = D_8009FDFC;
            spray.field1C = 5.0f;
            spray.field20 = 7.0f;
            spray.field58 = *(u32 *)(actor + 0x14C);
            spray.field5C = *(u32 *)(actor + 0x168);
            spray.field60 = 0;
            spray.field64 = 0x220005;
            spray.field68 = 0x1D0600;
            spray.field6C = 1;
            spray.field70 = 0x3B;
            spray.field74 = 0x80;
            spray.field78 = 0x20;
            spray.field7C = 0;
            spray.field7D = 7;
            spray.field80 = 10;
            spray.field82 = 25;
            spray.field84 = *(u32 *)(actor + 0x128);
            func_15151A38(&spray, actor[0xC], actor[1]);
            func_10010F88(D_80088740, 25000, 0, 0, 0,
                (s32)*(f32 *)(actor + 0x38), (s32)*(f32 *)(actor + 0x3C),
                (s32)*(f32 *)(actor + 0x40), 1000, 4000);
            return 0;
        }
    }
    target = D_80088720;
    if (target == NULL || *(u32 *)target == 0 || target[0x3B] != 1) {
        D_80088720 = func_15083E90(1);
    }
    target = D_80088720;
    if (target != NULL) {
        D_80088724.x = *(f32 *)(target + 0x14);
        D_80088724.y = *(f32 *)(target + 0x18) + 50.0f;
        D_80088724.z = *(f32 *)(target + 0x1C);
    }
    {
    f32 steeringFactor = D_8009FE00;
    dx = *(f32 *)(actor + 0x20);
    dy = *(f32 *)(actor + 0x24);
    dz = *(f32 *)(actor + 0x28);
    *(f32 *)(actor + 0x20) = dx + steeringFactor * (D_80088724.x - dx);
    *(f32 *)(actor + 0x24) = dy + steeringFactor * (D_80088724.y - dy);
    *(f32 *)(actor + 0x28) = dz + steeringFactor * (D_80088724.z - dz);
    return 1;
    }
}


s32 func_150B9D14(Mtx *output, u8 *source) {
    func_15142600(output,
                  *(f32 *)(source + 0x18),
                  *(f32 *)(source + 0x1C),
                  *(f32 *)(source + 0x2C),
                  *(f32 *)(source + 0x30),
                  *(f32 *)(source + 0x34),
                  *(f32 *)(source + 0x38),
                  *(f32 *)(source + 0x3C),
                  *(f32 *)(source + 0x40),
                  *(f32 *)(source + 0x20),
                  *(f32 *)(source + 0x24),
                  *(f32 *)(source + 0x28));
    return 1;
}

typedef struct EffectDescriptor150B9D8C {
    u32 flags;
    s16 count;
    u8 category;
    u8 pad07;
    s32 zero;
    s32 phase;
    u8 color[6];
    u8 pad16[2];
    u32 mode;
    u8 pad1C[12];
} EffectDescriptor150B9D8C;

typedef struct EffectWork150B9D8C {
    u32 first;
    u32 second;
    u8 pad08[4];
    EffectDescriptor150B9D8C descriptor;
} EffectWork150B9D8C;

u32 func_150ADA20(void);
void *func_1513C4EC(s32, s32, u8, u8, f32, f32, f32, f32, f32,
                    u8, u8, s32, s32, s32, u8, s32);

/* Submit a randomized descriptor when the actor's selector is unset. */
void func_150B9D8C(u8 *actor) {
    u32 third;
    EffectWork150B9D8C work;

    if (*(s16 *)(actor + 0x98) == -1) {
        work.descriptor.category = 4;
        work.descriptor.zero = 0;
        work.descriptor.phase = 0;
        work.descriptor.flags = 0x11;
        work.descriptor.count = 100;
        work.descriptor.color[0] = 255;
        work.descriptor.color[1] = *(u32 *)(actor + 0x90);
        work.descriptor.color[2] = 0;
        work.descriptor.color[3] = 0;
        work.descriptor.color[4] = 0;
        work.descriptor.color[5] = 255;
        work.descriptor.mode = 0x30001;
        work.first = func_150ADA20();
        work.second = func_150ADA20();
        third = func_150ADA20();
        func_1513C4EC((s32)&work.descriptor, 0, 2, 0,
                      (f32)*(s16 *)(actor + 0x9C),
                      (f32)(*(s16 *)(actor + 0xA6) + 2),
                      (f32)*(s16 *)(actor + 0xA0), (f32)*(s16 *)(actor + 0xA2), (f32)*(s16 *)(actor + 0xA2),
                      work.first & 255U, ((third & 1U) << 1) + (work.second & 1U),
                      3, 255, 0, actor[0x0C], actor[1]);
    }
}
