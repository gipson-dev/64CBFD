#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/61D10.s. */

extern u8 D_800C3F00;
extern s16 D_800C3EF0;
extern f32 D_80097D60;

s32 func_15034860() {
    return 0;
}

void func_15034EB4(u8 *arg0, s32 arg1, s32 arg2) {
    u8 *records;
    f32 amount;

    if (D_800C3EF0 != 0) {
        amount = (f32) D_800C3EF0 * D_80097D60 * *(f32 *) (arg0 + 0x14C);
        records = *(u8 **) (arg0 + 0x1D4);
        *(f32 *) (records + arg1 * 0x40 + 0x34) -= amount;
        if (arg2 != -1) {
            *(f32 *) (records + arg2 * 0x40 + 0x34) -= amount;
        }
    }
}

void func_15034F20(void) {
    D_800C3F00 = 0;
}

s32 func_15034F30() {
    return 0;
}

u8 *func_150356C8(void) {
    extern u8 D_800C3F08[];
    u8 val = D_800C3F00;

    if (val == 15) {
        return 0;
    }
    val++;
    D_800C3F00 = val;
    return D_800C3F08 + (val - 1) * 12;
}

s32 func_15035714() {
    return 0;
}

s32 func_15035808() {
    return 0;
}

s32 func_15035D6C() {
    return 0;
}

s32 func_15035FE8() {
    return 0;
}

s32 func_15036148() {
    return 0;
}
