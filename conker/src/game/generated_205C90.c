#include <ultra64.h>
extern u8 D_800E0A00;

/* Non-matching placeholders for the text-only asm slice asm/205C90.s. */

s32 func_151D8C00();
void func_15169260(s32, s32, s32, u8);
extern u8 D_800AB300[];

s32 func_151D87E0() {
    return 0;
}

s32 func_151D8868() {
    return 0;
}

s32 func_151D8A24() {
    return 0;
}

s32 func_151D8B24() {
    return 0;
}

s32 func_151D8B88(s32 arg0) {
    func_151D8B24(arg0);
    func_15169804(arg0);
}

s32 func_151D8BB4(s32 arg0) {
    func_151D8B24(arg0);
    func_15169824(arg0);
}

void func_151D8BE0(u8 *arg0) {
    func_151D8C00(arg0, arg0 + 0x18);
}

s32 func_151D8C00() {
    return 0;
}

s32 func_151D8D5C() {
    return 0;
}

void func_151D8DB4(s32 arg0, u8 arg1) {
    func_15169260((s32) D_800AB300, 1, arg0, arg1);
}

void func_151D8DE8(void) {
    D_800E0A00 = 1;
    func_151D8DB4(0, 0x58);
}
