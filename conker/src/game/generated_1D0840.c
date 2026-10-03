#include <ultra64.h>
void func_15169260(void *, s32, s32, u8);
void func_15143134(void *, void *, s32);
extern u8 D_800A8D70[];
extern s32 D_800BE9E4;
typedef struct { s32 val; } OneWord1D0840;
extern void (*D_8008F900[])();

/* Non-matching placeholders for the text-only asm slice asm/1D0840.s. */

extern void (*D_8008F904[])(u8 *, s32, u8);

s32 func_151A3390() {
    return 0;
}

s32 func_151A3504() {
    return 0;
}

s32 func_151A361C() {
    return 0;
}

s32 func_151A37C0() {
    return 0;
}

s32 func_151A3BE4() {
    return 0;
}

s32 func_151A4590() {
    return 0;
}

s32 func_151A4638() {
    return 0;
}

s32 func_151A483C() {
    return 0;
}

typedef struct {
    u8 pad0[0x1A];
    s16 counter;
    u8 pad1[0xF];
    u8 firstOutput;
    u8 secondOutput;
    u8 pad2[0xB];
    f32 firstValue;
    f32 secondValue;
    u8 pad3[0x68];
    s16 parameters[6];
} UpdateRecord1D0840;

s32 func_151A4900(UpdateRecord1D0840 *arg0, s32 arg1) {
    s16 *parameters = arg0->parameters;
    s32 counter = arg0->counter;
    f32 increment;

    if (counter < parameters[2]) {
        arg0->firstOutput = counter * parameters[3];
    }
    if (counter < parameters[4]) {
        increment = (s32)((u32)parameters[5] * (u32)D_800BE9E4);
        arg0->firstValue += increment;
        arg0->secondValue += increment;
        counter = arg0->counter;
    }
    arg0->secondOutput = counter * parameters[1];
    return 1;
}

s32 func_151A499C() {
    return 0;
}

s32 func_151A4A38() {
    return 0;
}

s32 func_151A4CE0() {
    return 0;
}

s32 func_151A4D88() {
    return 0;
}

s32 func_151A4E34(u8 *arg0, void *arg1) {
    u8 *actor = *(u8 **)arg0;
    s32 target = *(s32 *)(actor + 0x1D4);

    if (target == 0) {
        return 0;
    }
    if ((actor[0x74] & 0xF) == 0xF) {
        return 0;
    }
    func_15143134(arg0 + 8, arg1, target + (arg0[5] << 6));
    return 1;
}

void func_151A4E9C(u8 *arg0) {
    u8 *temp_v0 = *(u8 **) (arg0 + 0x98);

    *(u16 *) (arg0 + 0x1E) &= 0xFFFD;
    *(arg0 + 0x30) = 0;
    *(temp_v0 + 0x30) |= 1;
    *(temp_v0 + 0x30) |= 4;
}

s32 func_151A4ECC() {
    return 0;
}

void func_151A4F7C(u8 *arg0, u8 *arg1, u8 arg2) {
    u8 *temp_v0 = arg0 + 0x28;

    if (arg2 == 0) {
        if ((*(s32 *)temp_v0 == *(s32 *)arg1) || (temp_v0[4] == arg1[4])) {
            func_1516972C(arg0);
        }
    }
}

s32 func_151A4FD0() {
    return 0;
}

s32 func_151A5070() {
    return 0;
}

void func_151A5130(arg0, arg1, arg2)
s32 arg0;
u8 *arg1;
s16 arg2;
{
    D_8008F900[*(arg1 + 0x14)](arg0, arg1, arg2);
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1D0840/func_151A5170.s")

void func_151A55D4(u8 *arg0, s32 arg1, u8 arg2) {
    void (*callback)(u8 *, s32, u8) = D_8008F904[arg0[0x19]];

    if (callback != NULL) {
        callback(arg0, arg1, arg2);
    }
}

void func_151A561C(s32 arg0, u8 arg1) {
    OneWord1D0840 tmp;

    tmp = *(OneWord1D0840 *) D_800A8D70;
    func_15169260(&tmp, 1, arg0, arg1);
}
