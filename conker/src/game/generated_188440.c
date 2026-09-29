#include <ultra64.h>

extern f32 D_800BE9A4;

/* Non-matching placeholders for the text-only asm slice asm/188440.s. */

s32 func_1515AF90() {
    return 0;
}

s32 func_1515B21C() {
    return 0;
}

void func_1515B5F4(arg0)
s16 arg0;
{
    s16 value[1];

    value[0] = arg0;
    func_1515572C(value, 0xB);
}

void func_1515B62C(u8 *arg0, s16 *arg1, u8 arg2) {
    if (arg2 == 0xB) {
        if (*(s16 *) (arg0 + 0x70) == *arg1) {
            func_1516972C(arg0);
        }
    }
}

s32 func_1515B674() {
    return 0;
}

s32 func_1515B994(u8 *arg0) {
    f32 velocity;
    f32 acceleration;
    f32 timestep;
    f32 velocity_sum;

    velocity = *(f32 *) (arg0 + 0x78);
    acceleration = *(f32 *) (arg0 + 0x74);
    timestep = D_800BE9A4;
    *(f32 *) (arg0 + 0x14) += velocity * timestep +
        0.5f * acceleration * timestep;
    *(f32 *) (arg0 + 0x78) = velocity + acceleration * D_800BE9A4;
    velocity_sum = *(f32 *) (arg0 + 0x78) + velocity;
    *(f32 *) (arg0 + 0x1C) += *(f32 *) (arg0 + 0x80) *
        velocity_sum * 0.5f;
    return 1;
}

void func_1515BA10(s32 arg0) {
}

s32 func_1515BA1C(s16 arg0) {
    func_1515AF90(arg0);
}

void func_1515BA48(s32 arg0) {
}

s32 func_1515BA54(s16 arg0) {
    func_1515B674(arg0);
}

s32 func_1515BA80(s16 arg0) {
    func_1515B5F4(arg0);
}

s32 func_1515BAAC(s16 arg0) {
    func_1515B5F4(arg0);
}
