#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/183640.s. */

s32 func_151D5E30();
s32 func_15157DEC();
extern u8 D_800A6060[];

s32 func_15156190() {
    return 0;
}

s32 func_15156388(s32 arg0, u8 arg1, s32 arg2) {
    func_15156190(arg0, arg1, arg2, 0xFF, 0);
}

s32 func_151563B8() {
    return 0;
}

s32 func_151564F8() {
    return 0;
}

s32 func_151568F8() {
    return 0;
}

s32 func_15156B54() {
    return 0;
}

s32 func_15156D24() {
    return 0;
}

void func_15156F94(u8 *arg0) {
    func_151D5E30(arg0 + 0x88, arg0);
}

s32 func_15156FB8(s32 arg0) {
    func_15156F94(arg0);
    func_15169804(arg0);
}

s32 func_15156FE4(s32 arg0) {
    func_15156F94(arg0);
    func_15169824(arg0);
}

s32 func_15157010() {
    return 0;
}

s32 func_151571C4() {
    return 0;
}

void func_15157248(u8 *arg0) {
    func_151571C4(arg0);
    func_1518CA04(*(s32 *) (arg0 + 0x18));
    func_1503F7B8(*(s32 *) (arg0 + 0x68));
    func_15169804(arg0);
}

void func_1515728C(u8 *arg0) {
    func_151571C4(arg0);
    func_1518CA04(*(s32 *) (arg0 + 0x18));
    func_1503F7B8(*(s32 *) (arg0 + 0x68));
    func_15169824(arg0);
}

s32 func_151572D0() {
    return 0;
}

s32 func_15157420() {
    return 0;
}

s32 func_15157860() {
    return 0;
}

s32 func_15157898() {
    return 0;
}

s32 func_15157918() {
    return 0;
}

s32 func_15157AA8() {
    return 0;
}

void func_15157D88(u8 *arg0, s32 arg1, u8 arg2) {
    func_15169850(arg1, arg2, (s32) (arg0 + 0x4C), (s32) (arg0 + 0x50), (s32) arg0);
}

s32 func_15157DC8(u8 *arg0) {
    func_15157DEC(arg0, arg0 + 0x120);
    return 1;
}

s32 func_15157DEC() {
    return 0;
}

s32 func_15157F80() {
    return 0;
}

s32 func_15157FE8() {
    return 0;
}

s32 func_15158078(s32 arg0, u8 arg1) {
    func_15169260(D_800A6060, 3, arg0, arg1);
}
