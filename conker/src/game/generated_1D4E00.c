#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/1D4E00.s. */

s32 func_151A931C();

s32 func_151D5E30();
void func_151432BC(void *, f32 *, f32 *, f32 *, f32 *);

extern void (*D_8008F964[])(u8 *, s32, u8);

s32 func_151A7950() {
    return 0;
}

s32 func_151A7A90() {
    return 0;
}

s32 func_151A7D6C() {
    return 0;
}

s32 func_151A8340() {
    return 0;
}

void func_151A8560(u8 *arg0) {
    func_151D5E30(arg0 + 0x6C, arg0);
}

s32 func_151A8584() {
    return 0;
}

s32 func_151A85D4() {
    return 0;
}

s32 func_151A8624() {
    return 0;
}

s32 func_151A87F8() {
    return 0;
}

void func_151A8A20(u8 *arg0, s32 arg1, u8 arg2) {
    s32 index = arg0[0x5C];
    void (*callback)(u8 *, s32, u8);

    if (index >= 3) {
        index = 0;
    }
    callback = D_8008F964[index];
    if (callback != NULL) {
        callback(arg0, arg1, arg2);
    }
}

s32 func_151A8A78() {
    return 0;
}

s32 func_151A8B20() {
    return 0;
}

s32 func_151A8CEC() {
    return 0;
}

void func_151A8F1C(u8 *arg0, f32 *arg1, f32 *arg2, f32 *arg3) {
    func_151432BC(*(void **) (arg0 + 0x2C), arg1, arg1 + 2, arg2, arg3);
    arg1[1] = arg2[0];
}

s32 func_151A8F6C() {
    return 0;
}

void func_151A9024(u8 *arg0, s32 arg1, u8 arg2) {
    if (*(arg0 + 0x4C) == 1) {
        func_151A931C(arg0, arg1, arg2);
    }
}

s32 func_151A9060() {
    return 0;
}

s32 func_151A90C0() {
    return 0;
}

s32 func_151A91AC() {
    return 0;
}

s32 func_151A931C() {
    return 0;
}

s32 func_151A9390() {
    return 0;
}

s32 func_151A9634() {
    return 0;
}

s32 func_151A9834() {
    return 0;
}
