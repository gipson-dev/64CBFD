#include <ultra64.h>

typedef struct {
    u8 retained00[0x90];
    s16 x, y, z;
    s16 angleX, angleY, angleZ;
    s8 spinX, spinY, spinZ;
    u8 retained9F;
    s16 speedX, speedY, speedZ;
    u16 timer;
    u8 retainedA8[8];
    s16 floorY;
    u8 retainedB2;
    u8 opacity;
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

s32 func_1517A644() {
    return 0;
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

s32 func_1517AA20() {
    return 0;
}

void func_1517AB7C(arg0, arg1, arg2)
s32 arg0;
s16 arg1;
s16 arg2;
{
    func_1510B7B4(arg0, arg2);
}
