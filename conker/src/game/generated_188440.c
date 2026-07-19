#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/188440.s. */

s32 func_1515AF90() {
    return 0;
}

s32 func_1515B21C() {
    return 0;
}

void func_1515B5F4(arg0)
s16 arg0;
{
    s16 value[1];

    value[0] = arg0;
    func_1515572C(value, 0xB);
}

void func_1515B62C(u8 *arg0, s16 *arg1, u8 arg2) {
    if (arg2 == 0xB) {
        if (*(s16 *) (arg0 + 0x70) == *arg1) {
            func_1516972C(arg0);
        }
    }
}

s32 func_1515B674() {
    return 0;
}

s32 func_1515B994() {
    return 0;
}

void func_1515BA10(s32 arg0) {
}

s32 func_1515BA1C(s16 arg0) {
    func_1515AF90(arg0);
}

void func_1515BA48(s32 arg0) {
}

s32 func_1515BA54(s16 arg0) {
    func_1515B674(arg0);
}

s32 func_1515BA80(s16 arg0) {
    func_1515B5F4(arg0);
}

s32 func_1515BAAC(s16 arg0) {
    func_1515B5F4(arg0);
}
