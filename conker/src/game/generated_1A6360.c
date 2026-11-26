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

s32 func_15179600() {
    return 0;
}

s32 func_151797B0() {
    return 0;
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
