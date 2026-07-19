#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/105FC0.s. */

s32 func_15131828();
s32 func_15131958();

void func_150D8B10(f32 *arg0, f32 *arg1) {
    arg1[0] = arg0[5];
    arg1[1] = arg0[6] + 20.0f;
    arg1[2] = arg0[7];
}

s32 func_150D8B3C() {
    return 0;
}

s32 func_150D8B88() {
    return 0;
}

s32 func_150D8D84() {
    return 0;
}

s32 func_150D8E1C() {
    return 0;
}

s32 func_150D8E4C() {
    return 0;
}

s32 func_150D8FAC() {
    return 0;
}

s32 func_150D942C() {
    return 0;
}

s32 func_150D9C7C() {
    return 0;
}

void func_150DA484(u8 *arg0) {
    u8 *temp_v0 = *(u8 **) (arg0 + 0x98);
    u16 value = *(u16 *) (temp_v0 + 0x30);

    if (value != 0) {
        func_140111C8(value);
    }
}

s32 func_150DA4B4(s32 arg0) {
    func_150DA484(arg0);
    func_151478F4(arg0);
}

s32 func_150DA4E0(s32 arg0) {
    func_150DA484(arg0);
    func_15147928(arg0);
}

s32 func_150DA50C() {
    return 0;
}

s32 func_150DA5EC() {
    return 0;
}

s32 func_150DA628(u8 *arg0, s32 arg1) {
    u8 *temp_a2 = arg0 + 0xA8;

    func_15131828(arg0, arg0 + 0xAC, temp_a2, arg0 + 0xAA);
    func_15131958(arg0 + 0x58, *(s32 *) (temp_a2 + 0xC));
    return 1;
}

s32 func_150DA67C() {
    return 0;
}
