#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/204660.s. */

s32 func_151D77C8();

s32 func_151D71B0() {
    return 0;
}

s32 func_151D7264() {
    return 0;
}

s32 func_151D73A8() {
    return 0;
}

void func_151D7404() {
    func_151D77C8();
}

s32 func_151D7424(s32 arg0) {
    func_151D7404(arg0);
    func_1514933C(arg0);
}

s32 func_151D7450(s32 arg0) {
    func_151D7404(arg0);
    func_15149368(arg0);
}

s32 func_151D747C(u8 *arg0) {
    struct { u8 *ptr; u8 value; } temp;

    temp.ptr = arg0;
    temp.value = *(u8 *)(arg0 + 0x3B);
    func_151494E0(&temp, 0x3D);
}

s32 func_151D74B0() {
    return 0;
}

s32 func_151D7538() {
    return 0;
}

s32 func_151D75C4() {
    return 0;
}

s32 func_151D7724() {
    return 0;
}

s32 func_151D7770(u8 *arg0) {
    u8 *temp_v0 = arg0 + 0x28;

    if (*(u16 *) (*(u8 **) (arg0 + 0x40) + 0x84) == 0) {
        temp_v0[5] &= 0xFE;
    }
    return 1;
}

s32 func_151D779C(u8 *arg0) {
    u8 *temp_v0 = arg0 + 0x28;

    if ((*(u8 **) (arg0 + 0x40))[0xAD] != 0) {
        temp_v0[5] &= 0xFE;
    }
    return 1;
}

s32 func_151D77C8() {
    return 0;
}

s32 func_151D7830() {
    return 0;
}

s32 func_151D792C() {
    return 0;
}

s32 func_151D7A38() {
    return 0;
}

s32 func_151D7CD0() {
    return 0;
}

s32 func_151D80C4() {
    return 0;
}

s32 func_151D8718() {
    return 0;
}

void func_151D8764(u8 *arg0) {
    u8 *temp_v0 = *(u8 **)(arg0 + 0x98);
    u8 *temp_v1 = *(u8 **)temp_v0;

    if (temp_v1 != NULL) {
        *(s32 *)(temp_v1 + 0x28) = 0;
    }
}

s32 func_151D8780(s32 arg0) {
    func_151D8764(arg0);
    func_151478F4(arg0);
}

s32 func_151D87AC(s32 arg0) {
    func_151D8764(arg0);
    func_15147928(arg0);
}
