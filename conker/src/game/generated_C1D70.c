#include <ultra64.h>
s32 func_15095A90(s32, s32, f32, f32, f32, s32, s32, s32, s32);
extern s32 D_800D2CA0;
extern u8 D_800873D0[];

typedef struct {
    u32 unk0;
    u8 unk4;
    u8 pad5;
    u16 unk6;
    u16 unk8;
    u8 unkA;
    u8 unkB;
} structC1D70Source;

typedef struct {
    u32 unk0;
    u16 unk4;
    u16 unk6;
    u8 unk8;
    u8 unk9;
    u8 unkA;
    u8 padB;
} structC1D70Descriptor;

extern structC1D70Descriptor D_800D2C90;

void func_15095060(structC1D70Source *, s32, u8 *);
s32 func_150950D4(s32, structC1D70Descriptor *, s32, s32, s32, s32, s32, s32, s32, s32);

/* Non-matching placeholders for the text-only asm slice asm/C1D70.s. */

s32 func_15095D34();

s32 func_150948C0() {
    return 0;
}

s32 func_1509499C() {
    return 0;
}

s32 func_15094AB8() {
    return 0;
}

s32 func_15094EA0() {
    return 0;
}

u32 *func_15094F40(u32 *arg0) {
    u32 *temp_v1 = arg0;

    arg0 += 2;
    temp_v1[0] = 0xDE000000;
    temp_v1[1] = (u32) D_800873D0;
    D_800D2CA0 = 0;
    return arg0;
}

s32 func_15094F70(s32 arg0, structC1D70Source *arg1, s32 arg2, u8 *arg3,
                  s32 arg4, s32 arg5, s32 arg6, s32 arg7, s32 arg8) {
    func_15095060(arg1, arg2, arg3);
    return func_150950D4(arg0, &D_800D2C90, arg4, arg5, 0, arg6, arg7,
                         0x100, 0x100, arg8);
}

s32 func_15094FE8() {
    return 0;
}

void func_15095060(structC1D70Source *arg0, s32 arg1, u8 *arg2) {
    structC1D70Descriptor *descriptor;
    u32 value;

    descriptor = &D_800D2C90;
    if (arg2 != NULL) {
        *(structC1D70Descriptor **) (arg2 + 0x10) = descriptor;
    }

    value = arg0->unk0;
    if (value < 0x10000000) {
        descriptor->unk0 = value;
    } else {
        descriptor->unk0 = ((u32 *) value)[arg1 >> 8];
    }

    descriptor->unk4 = arg0->unk6;
    descriptor->unk6 = arg0->unk8;
    descriptor->unk8 = arg0->unkA;
    descriptor->unk9 = arg0->unkB;
    descriptor->unkA = arg0->unk4;
}

s32 func_150950D4(s32 arg0, structC1D70Descriptor *arg1, s32 arg2, s32 arg3,
                  s32 arg4, s32 arg5, s32 arg6, s32 arg7, s32 arg8, s32 arg9) {
    return 0;
}

s32 func_1509563C() {
    return 0;
}

s32 func_15095760() {
    return 0;
}

s32 func_150958B0() {
    return 0;
}

void func_15095A48(s32 arg0, s32 arg1, f32 arg2, f32 arg3) {
    func_15095A90(arg0, arg1, arg2, arg3, 4096.0f, 0, 0, 0, 0);
}

s32 func_15095A90(s32 arg0, s32 arg1, f32 arg2, f32 arg3, f32 arg4, s32 arg5, s32 arg6, s32 arg7, s32 arg8) {
    return 0;
}

s32 func_15095B08() {
    return 0;
}

s32 func_15095D0C(s32 arg0, s32 arg1) {
    func_15095D34(arg0, arg1, 0, 0, 0);
}

s32 func_15095D34() {
    return 0;
}

s32 func_1509629C() {
    return 0;
}

u8 *func_15096934(u8 *arg0) {
    extern u32 D_80087408;
    extern u8 D_800D2DAB;
    u8 *ptr = arg0;

    *(u32 *) (ptr + 0) = 0xde000000;
    *(u32 *) (ptr + 4) = (u32) &D_80087408;
    arg0 = arg0 + 8;
    D_800D2DAB = 0;
    return arg0;
}
