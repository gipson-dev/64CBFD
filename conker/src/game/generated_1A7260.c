#include <ultra64.h>

s32 func_150ADA20(void);
void *func_15167A68(s32, s32, s32, s32, u8, u8);
void func_1510E82C(s32, s32, f32 *, s32, s32, s32, f32, f32, f32, f32, u16, s32);
extern f32 D_800A7224, D_800A7228;


typedef struct {
    u8 retained00[0x90];
    s16 x, y, z;
    s16 angleX, angleY, angleZ;
    s8 spinX, spinY, spinZ;
    u8 variant;
    s16 speedX, speedY, speedZ;
    u16 timer;
    f32 scale;
    u8 retainedAC[4];
    s16 floorY;
    u8 retainedB2;
    u8 opacity;
    u8 retainedB4[4];
} SettleFade1517A84C;
extern s32 D_800BE9E4;
void func_1516972C(void *);

extern s16 D_800DD450;
extern s32 D_800DD1B0;
extern u8 D_80090614[];

s32 func_15094F70(s32, u8 *, s32, u8 *, s32, s32, s32, s32, s32);

/* Non-matching placeholders for the text-only asm slice asm/1A7260.s. */

s32 func_15179DB0() {
    return 0;
}

s32 func_15179FE0() {
    return 0;
}

s32 func_1517A1EC() {
    return 0;
}

s32 func_1517A394(register s32 arg0) {
    return arg0;
}

s32 func_1517A3A0() {
    return 0;
}

/* Allocate and initialize one settling burst piece, including its random spin. */
void func_1517A644(f32 size, u8 kind, s16 x, s16 y, s32 z) {
    SettleFade1517A84C *record;
    s32 range;
    f32 height;
    s32 halfSize;

    range = size;
    if (range != 0) {
        record = func_15167A68(9, 0, 0xB8, 1, 255, 1);
        if (record != NULL) {
            func_1510E82C(0, 0, &height, 0, 0, 0, (f32)x, (f32)y,
                          (f32)(s16)z, (f32)y, 0, 0);
            record->y = record->floorY = (s16)(s32)(height + 3.0f);
            record->x = x;
            record->z = (s16)z;
            record->angleX = 90;
            record->angleY = (u32)func_150ADA20() % 360;
            record->angleZ = 0;
            record->speedX = 0;
            record->speedZ = 0;
            record->variant = kind;
            record->scale = (s32)((u32)func_150ADA20() % 80 + 100) * D_800A7224;
            record->speedY = (s16)(s32)(size * D_800A7228);
            record->spinX = (u32)func_150ADA20() % range - (halfSize = size * 0.5f);
            record->spinY = (u32)func_150ADA20() % range - halfSize;
            record->spinZ = (u32)func_150ADA20() % range - halfSize;
            record->timer = 0;
            record->opacity = 255;
        }
    }
}

/* Move and rotate the record until it lands, then fade and retire it. */
void func_1517A84C(SettleFade1517A84C *record) {
    s32 remaining = record->timer;

    if (remaining == 0) {
        record->x += record->speedX;
        record->y += record->speedY;
        record->z += record->speedZ;
        if (record->speedY > 0) {
            record->speedY--;
            if (record->speedY <= 0) {
                record->speedY = -3;
            }
        }
        remaining = record->y - record->floorY;
        if (remaining <= 0) {
            record->angleX = 90;
            record->angleZ = 0;
            record->timer = 60;
            record->y = record->floorY;
        } else {
            record->angleX += record->spinX;
            record->angleY += record->spinY;
            record->angleZ += record->spinZ;
        }
    } else {
        remaining = (s32)((u32)remaining - (u32)D_800BE9E4);
        if (remaining > 0) {
            record->timer = remaining;
            record->opacity = (s32)((u32)remaining << 8) / 60;
        } else {
            func_1516972C(record);
        }
    }
}

u8 *func_1517A958(u8 *arg0, s32 arg1, s32 arg2, s32 arg3) {
    D_800DD450 = -1;
    if ((arg1 == 0xC) || (arg1 == 0x59)) {
        arg0 = (u8 *) func_1517A394((s32) arg0);
    }
    return arg0;
}

s32 func_1517A9A8(s32 arg0, volatile s32 arg1) {
    u8 output[0x14];

    if (arg1 != D_800DD1B0) {
        arg0 = func_15094F70(arg0, D_80090614, arg1 << 8, output,
                            0, 0, 0, 2, 3);
        D_800DD1B0 = arg1;
    }
    return arg0;
}

/* Emit a randomized burst around the supplied position when its size permits. */
void func_1517AA20(f32 size, s32 x, s32 yArgument, s32 z, s32 count) {
    s32 dx;
    s32 dz;
    s32 i;
    s32 range;
    f32 pieceSize;
    s32 kind;
    s16 y;

    if (size < 12.0f) {
        return;
    }
    range = size * 8.0f;
    size *= 0.5f;
    y = yArgument;
    for (i = 0; i < count; i++) {
        dx = func_150ADA20() & 63;
        dz = func_150ADA20() & 63;
        dx -= 32;
        dz -= 32;
        pieceSize = (f32)(((u32)func_150ADA20() % range) >> 4) + size;
        kind = func_150ADA20();
        func_1517A644(pieceSize, kind & 1, (s16)((u32)x + (u32)dx), y,
                     (s32)((u32)z + (u32)dz));
    }
}

void func_1517AB7C(arg0, arg1, arg2)
s32 arg0;
s16 arg1;
s16 arg2;
{
    func_1510B7B4(arg0, arg2);
}
