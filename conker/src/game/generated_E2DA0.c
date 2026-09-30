#include <ultra64.h>
extern u8 D_8009FC30[];
extern u8 D_800C35EA;
extern u8 D_800CC34A[];

s32 func_150ADA20(void);
void func_15182670(u8 arg0, u8 arg1, u8 arg2, u8 arg3, s16 arg4, u8 arg5,
                   u8 arg6, s32 arg7);

/* Non-matching placeholders for the text-only asm slice asm/E2DA0.s. */

u8 *func_150B58F0(u8 *arg0, s32 arg1) {
    if (D_800C35EA == 1) {
        return arg0;
    }

    *(u16 *) arg0 = 0x1A;
    *(u16 *) (arg0 + 2) = *(u16 *) (D_800CC34A + arg1 * 0x32C);
    return arg0 + 4;
}

s32 func_150B5950() {
    return 0;
}

s32 func_150B5A3C() {
    return 0;
}

s32 func_150B5C38() {
    return 0;
}

s32 func_150B5E34() {
    return 0;
}

s32 func_150B6000() {
    return 0;
}

void func_150B60E0(u8 *arg0, s32 arg1) {
    func_15143134(&D_8009FC30, arg1, *(s32 *) (arg0 + 0x1D4) + 0x140);
}

s32 func_150B6110() {
    return 0;
}

void func_150B6450(u8 *arg0, u8 arg1, u8 arg2) {
    if (arg2 == 0x4A) {
        func_1516972C(arg0);
    }
}

s32 func_150B648C() {
    return 0;
}

s32 func_150B66DC(u8 *arg0) {
    u8 *source;
    s32 result;
    s32 selector;

    source = *(u8 **)(arg0 + 0x18);
    selector = source[0x68];
    result = 1;
    selector -= 15;

    switch (selector) {
        case 0:
            *(*(u8 **)(arg0 + 0x14) + 9) = 1;
            break;
        case 1:
            *(*(u8 **)(arg0 + 0x14) + 9) = 0;
            *(*(u8 **)(arg0 + 0x14) + 0x2F) = 20;
            break;
        case 2:
        default:
            *(*(u8 **)(arg0 + 0x14) + 9) = 0;
            *(*(u8 **)(arg0 + 0x14) + 0x2F) = 40;
            break;
    }
    return result;
}

void func_150B6754(u8 arg0, s32 arg1) {
    func_15182670(0xCC, 0xCC, 0xFF, (func_150ADA20() % 56U) + 200,
                  (func_150ADA20() % 11U) + 15, 0, arg0, arg1);
}
