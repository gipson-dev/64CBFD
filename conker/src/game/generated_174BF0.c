#include <ultra64.h>
extern void (*D_8008A340[])();
extern void (*D_8008A2F0[])();
extern void (*D_8008A390[])();

/* Non-matching placeholders for the text-only asm slice asm/174BF0.s. */

s32 func_151D5E30();
s32 func_1514795C();
void func_15169260(s32, s32, s32, u8);
extern u8 D_800A5760[];

s32 func_15147740() {
    return 0;
}

void func_151478D0(u8 *arg0) {
    func_151D5E30(arg0 + 0x84, arg0);
}

s32 func_151478F4(s32 arg0) {
    func_151478D0(arg0);
    func_1514795C(arg0);
    func_15169804(arg0);
}

s32 func_15147928(s32 arg0) {
    func_151478D0(arg0);
    func_1514795C(arg0);
    func_15169824(arg0);
}

s32 func_1514795C() {
    return 0;
}

void func_151479E0(u8 *arg0) {
    s32 idx = *(s32 *) (arg0 + 0x20);

    if (idx < 0) {
        idx = 0;
    } else if (idx >= 0x14) {
        idx = 0;
    }
    D_8008A2F0[idx]();
}

void func_15147A30(u8 *arg0) {
    s32 idx = *(s32 *) (arg0 + 0x20);

    if (idx < 0) {
        idx = 0;
    } else if (idx >= 0x14) {
        idx = 0;
    }
    D_8008A340[idx]();
}

s32 func_15147A80() {
    return 0;
}

s32 func_15147C4C() {
    return 0;
}

void func_15147D1C(u8 *arg0, s32 arg1, u8 arg2) {
    void (*temp_v0)() = D_8008A390[*(s32 *) (arg0 + 0x20)];

    if (temp_v0 != 0) {
        temp_v0();
    }
}

void func_15147D64(s32 arg0, u8 arg1) {
    func_15169260((s32) D_800A5760, 2, arg0, arg1);
}
