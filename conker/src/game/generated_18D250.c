#include <ultra64.h>
void func_15169260(void *, s32, s32, u8);
extern u8 D_800A6670[];
extern s32 D_800BE9E4;
extern s32 (*D_8008B0D0[])();
void func_1516972C(u8 *arg0);

typedef struct { s32 val; } OneWord18D250;

/* Recovered effect setup and remaining placeholders from asm/18D250.s. */

extern void (*D_8008B0E4[])(u8 *, s32, u8);
void *func_15167A68(s32, s32, s32, s32, u8, u8);

s32 func_1515FDA0() {
    return 0;
}

void *func_1515FF74(void *source, s32 offset, u8 selector, s32 category) {
    u8 *record = func_15167A68(0x34, category, offset + 0x18, 1, selector, 1);

    if (record == NULL) {
        return NULL;
    }

    memcpy(record + 0xE, source, 8);
    return record;
}

void func_1515FFEC(u8 *arg0) {
    s32 remove = 0;
    s8 callbackIndex;

    if ((arg0[0xE] & 1) != 0) {
        *(s16 *)(arg0 + 0x12) -= D_800BE9E4;
        if (*(s16 *)(arg0 + 0x12) < 0) {
            remove = 1;
        }
    }
    if (remove == 0) {
        callbackIndex = *(s8 *)(arg0 + 0xF);
        if ((callbackIndex != -1) && (D_8008B0D0[callbackIndex](arg0) == 0)) {
            remove = 1;
        }
    }
    if (remove != 0) {
        func_1516972C(arg0);
    }
}

void func_15160090(u8 *arg0, s32 arg1, u8 arg2) {
    void (*callback)(u8 *, s32, u8) = D_8008B0E4[arg0[0x14]];

    if (callback != NULL) {
        callback(arg0, arg1, arg2);
    }
}

typedef struct {
    f32 positionS, positionT;
    f32 sizeS, sizeT;
    s32 pixelation;
} ColourFrameBufferSettings151600D8;

typedef struct {
    u8 retained00[0xE];
    u8 flags;
    s8 callbackIndex;
    u8 retained10[2];
    s16 remainingTicks;
    u8 retained14[4];
    ColourFrameBufferSettings151600D8 settings;
} ColourFrameBufferOwner151600D8;

s32 func_151422DC(s32, s32, s32, s32, s32, s32, s32);
extern u8 D_800A6540[], D_800A6548[], D_800A657C[], D_800A6584[];
extern u8 D_800A65B8[], D_800A65C0[], D_800A65F4[], D_800A65FC[];
extern u8 D_800A6630[], D_800A663C[];
extern f32 D_800A6674, D_800A6678, D_800A667C, D_800A6680;

/* Read the retail colour-framebuffer position, size and pixelation settings. */
s32 func_151600D8(u8 *owner) {
    s32 index = 0;
    ColourFrameBufferSettings151600D8 *settings = &((ColourFrameBufferOwner151600D8 *)owner)->settings;

    settings->positionS =
        (f32)func_151422DC(index++, (s32)D_800A6540, -2000, 2000, 0,
                         (s32)D_800A6548, 452) * D_800A6674;
    settings->positionT =
        (f32)func_151422DC(index++, (s32)D_800A657C, -2000, 2000, 0,
                         (s32)D_800A6584, 457) * D_800A6678;
    settings->sizeS =
        (f32)func_151422DC(index++, (s32)D_800A65B8, 0, 2000, 500,
                         (s32)D_800A65C0, 462) * D_800A667C;
    settings->sizeT =
        (f32)func_151422DC(index++, (s32)D_800A65F4, 0, 2000, 500,
                         (s32)D_800A65FC, 467) * D_800A6680;
    settings->pixelation =
        func_151422DC(index++, (s32)D_800A6630, 0, 65536, 65536,
                     (s32)D_800A663C, 473);
    return 1;
}


void func_15160274(s32 arg0, u8 arg1) {
    OneWord18D250 tmp;

    tmp = *(OneWord18D250 *) D_800A6670;
    func_15169260(&tmp, 1, arg0, arg1);
}
