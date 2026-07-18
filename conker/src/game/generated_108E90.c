#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/108E90.s. */

s32 func_150DB9E0() {
    return 0;
}

s32 func_150DBC60() {
    return 0;
}

s32 func_150DBD70() {
    return 0;
}

s32 func_150DC558() {
    return 0;
}

s32 func_150DCEA0() {
    return 0;
}

s32 func_150DD640() {
    return 0;
}

s32 func_150DDED0() {
    return 0;
}

void func_150DDF88(u8 *arg0) {
    func_150DBD70(*(u8 *)(arg0 + 0x28), arg0);
}

s32 func_150DDFAC() {
    return 0;
}

s32 func_150DE12C() {
    return 0;
}

s32 func_150DE2A4(u8 *arg0) {
    s16 value = *(s16 *)(arg0 + 0x1C);

    if (value < 0x20) {
        arg0[0x28] = value << 3;
    }
    return 1;
}

s32 func_150DE2C4() {
    return 0;
}
