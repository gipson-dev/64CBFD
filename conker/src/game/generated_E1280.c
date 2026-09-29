#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/E1280.s. */

void func_1000FC18(u16, s16, s16, s16, u16);
s32 func_151478F4(s32);
s32 func_15147928(s32);

s32 func_150B3DD0() {
    return 0;
}

void func_150B3E74(s32 arg0) {
    func_1000FC18(0x221, (s16) *(f32 *) (arg0 + 0x10), (s16) *(f32 *) (arg0 + 0x14),
                  (s16) *(f32 *) (arg0 + 0x18), 0xFA0);
    func_151478F4(arg0);
}

void func_150B3EE8(s32 arg0) {
    func_1000FC18(0x221, (s16) *(f32 *) (arg0 + 0x10), (s16) *(f32 *) (arg0 + 0x14),
                  (s16) *(f32 *) (arg0 + 0x18), 0xFA0);
    func_15147928(arg0);
}

s32 func_150B3F5C() {
    return 0;
}

s32 func_150B40E8() {
    return 0;
}

s32 func_150B4294() {
    return 0;
}

s32 func_150B4710() {
    return 0;
}

void func_150B5060(u8 *arg0) {
    u8 *temp_v0 = *(u8 **) (arg0 + 0x98);

    arg0[0x30] = 0;
    *(u16 *) (arg0 + 0x1E) &= ~2;
    temp_v0[0x1C] |= 1;
}

s32 func_150B5088() {
    return 0;
}

void func_150B538C(u8 *arg0, u8 arg1, u8 arg2) {
    if (arg2 == 5) {
        func_150B5060(arg0);
    }
}
