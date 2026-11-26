#include <ultra64.h>

/* Recovered routines and remaining placeholders for asm/1A6360.s. */

extern u8 *D_800DBFF0;
extern s16 D_800DD436;
extern u8 **D_800DD440;

extern u8 D_800DD432, D_800DD433, D_800DD434;
extern s8 D_800DD446;
extern s16 D_800DD444;
extern u16 D_800DD430;
void func_1516972C(void *);
void func_10004074(void *);
void func_100111C8(u16);

/* Reset the display state and its default timers. */
void func_15178EB0(void) {
    D_800DD434 = 0;
    D_800DD446 = 0;
    D_800DD444 = 600;
    D_800DD432 = 240;
    D_800DD433 = 20;
    D_800DD436 = 0;
    D_800DD440 = 0;
}

/* Transition the display state, disposing all slots on state 2. */
void func_15178EFC(s32 state) {
    s32 i;
    if (state == 2) {
        D_800DD434 = 0;
        D_800DD446 = 0;
        if (D_800DD440 != NULL) {
            for (i = 0; i < 300; i++) {
                if (D_800DD440[i] != NULL) {
                    func_1516972C(D_800DD440[i]);
                    D_800DD440[i] = NULL;
                }
            }
            func_10004074(D_800DD440);
            D_800DD440 = NULL;
        }
        func_100111C8(D_800DD430);
        D_800DD444 = 0;
        D_800DD436 = 0;
    } else if (state == 3) {
        if (D_800DD446 == 0) {
            D_800DD444 = 600;
        } else if (D_800DD446 == 3) {
            D_800DD446 = 1;
        }
        D_800DD434 = state;
    } else {
        D_800DD434 = state;
    }
}

s32 func_15179008() {
    return 0;
}

#include "structs.h"
#include <math.h>

extern u8 *D_800DBFF0;
f32 func_150AD78C(f32);
f32 func_150AD780(f32);
extern s16 D_800DD438[3];

/* Build the offset point from truncated camera coordinates and two live angles. */
void func_151794C8(void) {
    s32 x;
    s32 y;
    s32 z;
    f32 zero;
    f32 vertical;
    f32 horizontal;
    f32 sine;
    f32 angle;

    zero = 0.0f;
    x = (s32)((struct108 *)D_800DBFF0)->unk2F8;
    y = (s32)((struct108 *)D_800DBFF0)->unk2FC;
    z = (s32)((struct108 *)D_800DBFF0)->unk300;
    angle = ((struct108 *)D_800DBFF0)->unk398;
    sine = func_150AD78C(angle);
    horizontal = func_150AD780(angle);
    vertical = 500.0f * sine;
    horizontal = -500.0f * horizontal;
    angle = ((struct108 *)D_800DBFF0)->unk3A0;
    sine = func_150AD78C(angle);
    angle = func_150AD780(angle);
    x = (s32)((f32)x + (zero + horizontal * sine));
    z = (s32)((f32)z + (horizontal * angle - zero));
    y = (s32)((f32)y + vertical);
    D_800DD438[0] = x;
    D_800DD438[2] = z;
    D_800DD438[1] = y;
}

typedef struct {
    Vtx vertices[8];
    u32 value80;
    s16 slotIndex;
    u16 retained86;
    s16 cleared88;
    u16 value8A;
    s16 x, y, z;
    s16 lifetime, remaining, initialHeight;
    u16 flags, retained9A;
    s16 cleared9C, cleared9E;
    u8 textureIndex, mode;
    s8 tag;
    u8 retainedA3;
    u32 retainedA4;
} DisplaySprite15179600;
s32 func_150ADA20(void);
void func_1516865C(void *, u8, u8, u8, u8);
void *func_15168800(void *, u8, s32);

/* Create a display sprite near the camera and retain its allocated slot. */
void func_15179600(s32 randomizeHeight, u32 value) {
    s32 x, y, z;
    s32 originX, originY, originZ;
    s32 randomValue;
    u32 variation;
    void *object;
    DisplaySprite15179600 sprite;
    sprite.textureIndex = 17;
    sprite.value8A = 51;
    sprite.tag = 1;
    sprite.flags = 0;
    func_1516865C(&sprite, 255, 255, 255, 80);
    originX = (s32)((struct108 *)D_800DBFF0)->unk2F8;
    originY = (s32)((struct108 *)D_800DBFF0)->unk2FC;
    originZ = (s32)((struct108 *)D_800DBFF0)->unk300;
    randomValue = func_150ADA20();
    x = randomValue % 500 + originX;
    randomValue = func_150ADA20();
    z = randomValue % 500 + originZ;
    if (randomizeHeight == 0) {
        y = originY + 500;
    } else {
        randomValue = func_150ADA20();
        y = randomValue % 500 + originY;
    }
    variation = (u32)func_150ADA20() % 10;
    sprite.cleared9C = 0;
    sprite.cleared9E = 0;
    sprite.lifetime = 4;
    sprite.remaining = variation + 35;
    sprite.flags = 0x8C00;
    sprite.mode = variation + 10;
    sprite.y = y;
    sprite.x = x;
    sprite.z = z;
    sprite.value80 = value;
    sprite.slotIndex = D_800DD436;
    object = func_15168800(&sprite, 255, 0);
    if (object != NULL) {
        D_800DD440[D_800DD436] = object;
        D_800DD436++;
    }
}


extern u32 D_800BE9E4;
extern f32 D_800A7204;
f32 func_15048A40(u8);
f32 func_150489B0(u8);

typedef struct {
    u8 unidentified00[0x98];
    s16 phase;
    s16 speed;
    u8 unidentified9C[0xC];
    u16 flags;
    u8 unidentifiedAA[6];
    u8 textureIndex;
    u8 unidentifiedB1;
    s8 callbackIndex;
    u8 unidentifiedB3[5];
} SpriteFrameState;
/* Update opacity, heading and planar motion, then wrap or release a display sprite. */
void func_151797B0(SpriteFrameState *record) {
    f32 dz, dx, wave, distance, speed;
    s32 opacity, angle, wrapped;
    u32 randomValue;
    s32 heading;
    s32 originX, originY, originZ;
    dz = (f32)*(s16 *)((u8 *)record + 0xA0) - ((struct108 *)D_800DBFF0)->unk300;
    dx = (f32)*(s16 *)((u8 *)record + 0x9C) - ((struct108 *)D_800DBFF0)->unk2F8;
    distance = sqrtf(dz * dz + dx * dx);
    opacity = (s32)(80.0f - 80.0f * distance / 1000.0f);
    if (opacity < 0) opacity = 0;
    angle = *(u16 *)((u8 *)record + 0xAE);
    ((u8 *)record)[0xB4] = opacity;
    randomValue = func_150ADA20();
    angle += (((u32)D_800DD433 << 4) * ((randomValue & 255) + 128)) >> 9;
    angle = (s32)((f32)angle * D_800A7204);
    if (angle > 12800) angle = 12800;
    *(u16 *)((u8 *)record + 0xAE) = angle;
    speed = (f32)(s32)((u32)((u8 *)record)[0xB1] * D_800BE9E4);
    heading = (*(u16 *)((u8 *)record + 0xAE) >> 8) & 255;
    wave = func_15048A40(heading);
    *(s16 *)((u8 *)record + 0x9C) = (s32)((f32)*(s16 *)((u8 *)record + 0x9C) + speed * wave);
    heading = (*(u16 *)((u8 *)record + 0xAE) >> 8) & 255;
    wave = func_150489B0(heading);
    *(s16 *)((u8 *)record + 0x9E) = (s32)((f32)*(s16 *)((u8 *)record + 0x9E) - speed * wave);
    originX = D_800DD438[0];
    originY = D_800DD438[1];
    originZ = D_800DD438[2];
    wrapped = 0;
    if (*(s16 *)((u8 *)record + 0x9C) < originX - 500) {
        *(s16 *)((u8 *)record + 0x9C) = originX - (originX - *(s16 *)((u8 *)record + 0x9C) - 1000);
        wrapped = 1;
    } else if (originX + 500 < *(s16 *)((u8 *)record + 0x9C)) {
        *(s16 *)((u8 *)record + 0x9C) = originX + *(s16 *)((u8 *)record + 0x9C) - originX - 1000;
        wrapped = 1;
    }
    if (*(s16 *)((u8 *)record + 0x9E) < originY - 500) {
        *(s16 *)((u8 *)record + 0x9E) = originY - (originY - *(s16 *)((u8 *)record + 0x9E) - 1000);
        wrapped = 1;
    } else if (originY + 500 < *(s16 *)((u8 *)record + 0x9E)) {
        *(s16 *)((u8 *)record + 0x9E) = originY + *(s16 *)((u8 *)record + 0x9E) - originY - 1000;
        wrapped = 1;
    }
    if (*(s16 *)((u8 *)record + 0xA0) < originZ - 500) {
        *(s16 *)((u8 *)record + 0xA0) = originZ - (originZ - *(s16 *)((u8 *)record + 0xA0) - 1000);
        wrapped = 1;
    } else if (originZ + 500 < *(s16 *)((u8 *)record + 0xA0)) {
        *(s16 *)((u8 *)record + 0xA0) = originZ + *(s16 *)((u8 *)record + 0xA0) - originZ - 1000;
        wrapped = 1;
    }

    if ((*(u32 *)((u8 *)record + 0x90) & 2) && wrapped) {
        D_800DD436--;
        D_800DD440[*(s16 *)((u8 *)record + 0x94)] = NULL;
        func_1516972C(record);
    } else if (*(u32 *)((u8 *)record + 0x90) & 1) {
        if (wrapped) *(u32 *)((u8 *)record + 0x90) ^= 1;
        else ((u8 *)record)[0xB4] = 0;
    }
}


void func_15179AB8(void) {
    s32 i;
    u8 *object;
    u32 flags;

    for (i = D_800DD436 - 1; i >= 0; i--) {
        object = D_800DD440[i];
        if (object != NULL) {
            flags = *(u32 *) (object + 0x90);
            if (!(flags & 2)) {
                *(u32 *) (object + 0x90) = flags | 2;
                return;
            }
        }
    }
}

typedef struct {
    Vtx vertices[8];
    u32 value80;
    u32 retained84;
    s16 cleared88;
    u16 value8A;
    s16 x, y, z;
    s16 lifetime, remaining;
    s16 initialHeight;
    u16 flags;
    u16 retained9A;
    s16 cleared9C, cleared9E;
    u8 textureIndex, mode;
    s8 tag;
    u8 retainedA3;
    u32 retainedA4;
} SelectedVertexSprite;
extern s16 D_800DD438[];
extern f32 D_800A7208;
s32 func_150ADA20(void);
s32 func_1510F8D8(s32, s32, s32, s32);
void func_1516865C(void *, u8, u8, u8, u8);
void *func_15168800(void *, u8, s32);

/* Scatter bounded random sprite requests around the captured display origin. */
void func_15179B14(s32 count) {
    f32 noGround;
    s32 x, z, height;
    s32 i;
    s32 originX = D_800DD438[0];
    s32 originZ = D_800DD438[2];
    SelectedVertexSprite sprite;
    i = 0;
    if (count > 0) {
        noGround = D_800A7208;
        do {
            x = func_150ADA20() % 500 + originX;
            z = func_150ADA20() % 500 + originZ;
            height = func_1510F8D8(x, 10000, z, 0);
            if ((f32)height != noGround) {
                sprite.value80 = 0;
                sprite.value8A = 128;
                sprite.x = x;
                sprite.y = height;
                sprite.z = z;
                sprite.remaining = 25;
                sprite.lifetime = 25;
                sprite.initialHeight = 0;
                sprite.tag = 14;
                sprite.textureIndex = 18;
                sprite.flags = 0x9804;
                sprite.mode = 0;
                func_1516865C(&sprite, 255, 255, 255, 255);
                func_15168800(&sprite, 255, 0);
            }
            i++;
        } while (i != count);
    }
}



/* Derive the record opacity byte from planar viewer distance. */
void func_15179CB0(u8 *record) {
    f32 dx;
    f32 dz;
    f32 distance;
    u8 *viewer;

    viewer = D_800DBFF0;
    dx = (f32)*(s16 *)(record + 0xA0) - *(f32 *)(viewer + 0x300);
    dz = (f32)*(s16 *)(record + 0x9C) - *(f32 *)(viewer + 0x2F8);
    distance = sqrtf(dx * dx + dz * dz);
    record[0xB4] = (u32)(255.0f - distance * 160.0f / 1000.0f);
}
