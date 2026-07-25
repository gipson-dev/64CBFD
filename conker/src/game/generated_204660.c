#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/204660.s. */

s32 func_151D77C8();
void *memcpy(void *dst, const void *src, unsigned int len);

extern void (*D_8008FCA4[])(u8 *, s32, u8);
extern f32 D_800AB2EC;
extern f32 D_800AB2F0;

s32 func_151D71B0() {
    return 0;
}

s32 func_151D7264() {
    return 0;
}

void func_151D73A8(u8 *arg0, s32 arg1, u8 arg2) {
    if (D_8008FCA4[arg0[0x2C]] != 0) {
        D_8008FCA4[arg0[0x2C]](arg0, arg1, arg2);
    }
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

void func_151D74B0(u8 *arg0, u8 arg1, s8 arg2, u8 arg3, s32 arg4) {
    struct { u8 *word0; u8 byte0; u8 byte1; s8 byte2; } rec;
    s32 temp_v0;

    rec.byte0 = arg0[0x3B];
    rec.byte1 = arg1;
    rec.byte2 = arg2;
    rec.word0 = arg0;
    temp_v0 = func_151D71B0(0x12C, 0, 0, 0x41400000, 8, arg3, arg4);
    if (temp_v0 != 0) {
        memcpy((u8 *)(temp_v0 + 0x40), &rec, 8);
    }
}

void func_151D7538(s32 arg0, s32 *arg1, u8 arg2) {
    if (arg2 == 0x3D) {
        if (*(s32 *)(arg0 + 0x40) == *arg1 || *(u8 *)(arg0 + 0x44) == *((u8 *)arg1 + 4)) {
            func_1516972C(arg0);
        }
    } else {
        func_15149514(arg1, arg2, arg0 + 0x40, arg0 + 0x44, arg0);
    }
}

s32 func_151D75C4() {
    return 0;
}

s32 func_151D7724(u8 *arg0) {
    u8 *temp_v0 = *(u8 **)(arg0 + 0x40);
    u8 *temp_v1 = arg0 + 0x28;

    if ((*(s32 *)(temp_v0 + 0x94) & 2) != 0 || *(u16 *)(temp_v0 + 0x84) == 4 ||
        *(u16 *)(temp_v0 + 0x84) == 0xA || *(u16 *)(temp_v0 + 0x84) == 0xC) {
        temp_v1[5] &= 0xFFFE;
    }
    return 1;
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

s32 func_151D77C8(u8 *arg0) {
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

void func_151D8718(u8 *arg0, f32 *arg1, f32 arg2) {
    f32 temp = *arg1;

    *arg1 = temp + D_800AB2EC * arg2;
    *(f32 *)(arg0 + 4) = *(f32 *)(arg0 + 4) + (temp * arg2 + D_800AB2F0 * arg2 * arg2);
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
