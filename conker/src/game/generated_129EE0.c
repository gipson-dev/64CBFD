#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/129EE0.s. */

s32 func_15103828();
f32 func_15165BB0(u8 *, f32 *, s32, s32, f32);
extern s16 *D_800D9AA0;
extern f32 D_800A1F2C;

typedef struct {
    u8 flags;
    u8 unused1;
    s16 lifetime;
    u8 level;
    u8 players;
    s8 callback;
    u8 unused7;
} TimedViewRequest150FCA30;
/* This callback is passed as an opaque SDK32 code-address word. */
s32 func_1000EC24();
s32 func_150FCBC0();
u16 func_1000FA64(u16, s16, s16, s16, s32, u16, s16, s32, void *, s32, s32, s32);
void func_15164F0C(u8, u8, s32, u8, s32);
u8 *func_151D8868(u8 *, s32, u8, s32);
extern s32 D_80082FA0;

/* Initialize scene views, three sound emitters and the timed view request. */
void func_150FCA30(void) {
    u32 index;
    TimedViewRequest150FCA30 request;

    func_150FCBC0(0);
    func_150FCBC0(1);
    func_150FCBC0(2);
    func_1000FA64(0x2B8, -2038, 1560, -2631, 28000, 9000, 7000,
        (s32)(u32)func_1000EC24, (void *)45, 0, 0, 0);
    func_1000FA64(0x2B7, -319, -273, -3419, 28000, 9000, 7000,
        (s32)(u32)func_1000EC24, NULL, 0, 0, 0);
    func_1000FA64(0x2B6, 1519, 947, -2633, 28000, 9000, 7000,
        (s32)(u32)func_1000EC24, (void *)90, 0, 0, 0);
    index = 0;
    if ((s32)((u32)D_80082FA0 + 1U) > 0) {
        do {
            func_15164F0C(4, (u8)index, 0, 0xFF, 1);
            index++;
        } while ((s32)index <= D_80082FA0);
    }
    request.flags = 1;
    request.lifetime = 100;
    request.players = 15;
    request.level = 8;
    request.callback = -1;
    func_151D8868((u8 *)&request, 0, 0xFF, 0);
}


s32 func_150FCBC0() {
    return 0;
}

f32 func_150FCF1C(u8 *arg0) {
    f32 position[3];

    if (D_800D9AA0 == NULL) {
        return 1.0f;
    }
    position[0] = D_800D9AA0[0];
    position[1] = D_800D9AA0[1];
    position[2] = D_800D9AA0[2];
    return func_15165BB0(arg0, position, 0x44FAE000, 0x460CB400, D_800A1F2C);
}

void func_150FCFB0(s32 arg0) {
    func_15103828();
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_129EE0/func_150FCFD4.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_129EE0/func_150FD514.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_129EE0/func_150FDB0C.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_129EE0/func_150FDBA0.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_129EE0/func_150FDC2C.s")

s32 func_150FDCAC(s32 arg0) {
    func_150FDC2C(arg0);
    func_1513CA6C(arg0);
}

s32 func_150FDCD8(s32 arg0) {
    func_150FDC2C(arg0);
    func_1513CAA0(arg0);
}
