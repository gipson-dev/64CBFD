#include <ultra64.h>
extern void (*D_8008B0C0[])();
extern s32 D_800DCD7C;
extern u8 D_800DCD20[];
extern u8 D_800DCD27;
extern void (*D_8008B090[])();
extern u8 *D_800DCD78;

/* Non-matching placeholders for the text-only asm slice asm/18A8F0.s. */

s32 func_1515D5F8();

u8 *func_1515D440(void) {
    u8 *temp_v0 = (u8 *) allocate_memory(0x10, 1, 2, 0);

    bzero(temp_v0, 0x10);
    return temp_v0;
}

s32 func_1515D480() {
    return 0;
}

void func_1515D4D4(s32 arg0, s32 arg1, s32 arg2, u8 arg3) {
    if (arg3 >= D_800DCD27) {
        D_800DCD20[0] = arg0;
        D_800DCD20[1] = arg1;
        D_800DCD20[2] = arg2;
        D_800DCD7C = 1;
        D_800DCD27 = arg3;
    }
}

s32 func_1515D520() {
    return 0;
}

void func_1515D5AC(s32 arg0, s32 arg1, s32 arg2, s32 arg3, s32 arg4, s32 arg5, s32 arg6, s32 arg7, s32 arg8, u8 arg9) {
    func_1515D5F8(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9);
}

s32 func_1515D5F8() {
    return 0;
}

void func_1515D69C(void) {
    u8 *ptr = D_800DCD78;

    if (ptr != 0) {
        do {
            ptr[0xC] = 0;
            ptr[0x30] = 0;
            ptr = *(u8 **) ptr;
        } while (ptr != 0);
    }
}

void func_1515D6C8() {
}

s32 func_1515D6D0() {
    return 0;
}

s32 func_1515D914() {
    return 0;
}

s32 func_1515E278() {
    return 0;
}

s32 func_1515E43C() {
    return 0;
}

s32 func_1515E544() {
    return 0;
}

s32 func_1515E888() {
    return 0;
}

s32 func_1515EB84() {
    return 0;
}

s32 func_1515EC78() {
    return 0;
}

s32 func_1515EF74() {
    return 0;
}

f32 func_1515F008(u8 *arg0, s32 arg1) {
    s32 temp_v0;
    u8 *temp_v1 = arg0 + arg1 * 2;

    temp_v0 = *(s16 *) temp_v1;
    temp_v0 = *(u16 *) (temp_v1 + 0x20) | (temp_v0 << 16);
    return temp_v0 * 1.52587890625e-05f;
}

s32 func_1515F040() {
    return 0;
}

s32 func_1515F0AC() {
    return 0;
}

s32 func_1515F10C() {
    return 0;
}

void func_1515F170(s32 arg0, u8 arg1) {
    u8 *ptr = D_800DCD78;

    if (ptr != 0) {
        do {
            if (arg0 == *(ptr + 0xB)) {
                *(ptr + 9) = arg1;
            }
            ptr = *(u8 **) ptr;
        } while (ptr != 0);
    }
}

s32 func_1515F1B0() {
    return 0;
}

void func_1515F25C(u8 **arg0, u8 *arg1) {
    *(u8 **)(arg1 + 0xC) = *arg0;
    *arg0 = arg1;
}

s32 func_1515F270() {
    return 0;
}

void func_1515F2B8(u8 *arg0, s32 arg1) {
    func_1505D024(arg0, 0x6001D, *(u16 *) (arg0 + 0x7A), -1);
}

void func_1515F2E8(u8 *arg0, u8 *arg1) {
    if (*(arg0 + 0x3B) == 1) {
        s32 idx = *(s32 *) (arg1 + 0x1C);

        if (idx >= 0) {
            if (idx < 3) {
                D_8008B0C0[idx]();
            }
        }
    }
}

s32 func_1515F338() {
    return 0;
}

s32 func_1515F5C4() {
    return 0;
}

s32 func_1515F850() {
    return 0;
}

void func_1515FB70(u8 *arg0, u8 *arg1) {
    if (*(arg0 + 0x3B) == 1) {
        if (*(volatile s32 *) (arg1 + 0x1C) >= 0) {
        }
    }
}

void func_1515FB94(u8 *arg0, s32 arg1) {
    func_1505D024(arg0, 0x6002D, *(u16 *) (arg0 + 0x7A), -1);
}

s32 func_1515FBC4() {
    return 0;
}

void func_1515FC34(s32 arg0, u8 arg1) {
    func_1505D024(arg0, 0x33, 0xC000, -1);
}

s32 func_1515FC60() {
    return 0;
}
