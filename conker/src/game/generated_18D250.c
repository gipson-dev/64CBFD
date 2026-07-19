#include <ultra64.h>
void func_15169260(s32, s32, s32, u8);
extern u8 D_800A6670[];

/* Non-matching placeholders for the text-only asm slice asm/18D250.s. */

extern void (*D_8008B0E4[])(u8 *, s32, u8);

s32 func_1515FDA0() {
    return 0;
}

s32 func_1515FF74() {
    return 0;
}

s32 func_1515FFEC() {
    return 0;
}

void func_15160090(u8 *arg0, s32 arg1, u8 arg2) {
    void (*callback)(u8 *, s32, u8) = D_8008B0E4[arg0[0x14]];

    if (callback != NULL) {
        callback(arg0, arg1, arg2);
    }
}

s32 func_151600D8() {
    return 0;
}

void func_15160274(s32 arg0, u8 arg1) {
    s32 tmp[1];

    tmp[0] = *(s32 *) D_800A6670;
    func_15169260(tmp, 1, arg0, arg1);
}
