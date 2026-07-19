#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/17CAF0.s. */

extern void (*D_8008AD04[])(u8 *, s32, u8);
s32 func_1514FF44(u8 *arg0, s32 arg1, s32 arg2, u8 arg3, s32 arg4);
s32 func_15153CCC(u8 *arg0, s32 arg1, s32 arg2, u8 arg3, s32 arg4);

s32 func_1514F640() {
    return 0;
}

s32 func_1514F6E8() {
    return 0;
}

s32 func_1514F808() {
    return 0;
}

s32 func_1514F8F8() {
    return 0;
}

s32 func_1514FB98() {
    return 0;
}

s32 func_1514FBFC() {
    return 0;
}

s32 func_1514FCE8() {
    return 0;
}

void func_1514FEFC(s32 arg0, s32 arg1, s32 arg2, u8 arg3, s32 arg4) {
    u8 temp[0x2C];

    func_1514F640(arg0, temp);
    func_1514FF44(temp, arg1, arg2, arg3, arg4);
}

s32 func_1514FF44(u8 *arg0, s32 arg1, s32 arg2, u8 arg3, s32 arg4) {
    return 0;
}

s32 func_15150178() {
    return 0;
}

s32 func_15150400() {
    return 0;
}

s32 func_1515080C() {
    return 0;
}

s32 func_15150D1C() {
    return 0;
}

s32 func_15150F90() {
    return 0;
}

s32 func_151511FC() {
    return 0;
}

s32 func_15151670() {
    return 0;
}

s32 func_15151A38() {
    return 0;
}

s32 func_15151D6C() {
    return 0;
}

s32 func_15152190() {
    return 0;
}

s32 func_15152520() {
    return 0;
}

s32 func_15152874() {
    return 0;
}

s32 func_15152ABC() {
    return 0;
}

s32 func_15152B38() {
    return 0;
}

s32 func_15152F70() {
    return 0;
}

s32 func_15153298() {
    return 0;
}

s32 func_15153634() {
    return 0;
}

s32 func_151539B4() {
    return 0;
}

void func_15153C84(s32 arg0, s32 arg1, s32 arg2, u8 arg3, s32 arg4) {
    u8 temp[0x2C];

    func_1514F640(arg0, temp);
    func_15153CCC(temp, arg1, arg2, arg3, arg4);
}

s32 func_15153CCC(u8 *arg0, s32 arg1, s32 arg2, u8 arg3, s32 arg4) {
    return 0;
}

s32 func_15153F18() {
    return 0;
}

s32 func_151541B8() {
    return 0;
}

s32 func_1515452C() {
    return 0;
}

s32 func_15154684() {
    return 0;
}

s32 func_15154884() {
    return 0;
}

s32 func_15154A88() {
    return 0;
}

s32 func_15154C90() {
    return 0;
}

s32 func_15154D80() {
    return 0;
}

s32 func_1515548C() {
    return 0;
}

void func_15155564(u8 *arg0, s32 arg1, u8 arg2) {
    void (*callback)(u8 *, s32, u8) = D_8008AD04[arg0[0x2A]];

    if (callback != NULL) {
        callback(arg0, arg1, arg2);
    }
}

s32 func_151555AC() {
    return 0;
}

s32 func_1515572C() {
    return 0;
}
