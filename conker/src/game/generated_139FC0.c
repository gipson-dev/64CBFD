#include <ultra64.h>
extern s8 D_800BC448[];

/* Non-matching placeholders for the text-only asm slice asm/139FC0.s. */

s32 func_1510CB10() {
    return 0;
}

s32 func_1510CDB8() {
    return 0;
}

s32 func_1510CE60() {
    return 0;
}

s32 func_1510D0EC() {
    return 0;
}

s32 func_1510D374() {
    return 0;
}

s32 func_1510D404() {
    return 0;
}

void func_1510D608(s32 arg0, s32 arg1) {
    s8 *temp_v0 = D_800BC448 + arg0;
    s8 temp_v1 = *temp_v0;

    if (temp_v1 != 0) {
        *temp_v0 = (temp_v1 & 0x40) | arg1;
    }
}

s32 func_1510D630() {
    return 0;
}

s32 func_1510D694() {
    return 0;
}

s32 func_1510D720() {
    return 0;
}

s32 func_1510D7AC() {
    return 0;
}

extern u8 D_800D9ED0;

void func_1510D864(void) {
    D_800D9ED0 = 0;
}

s32 func_1510D874() {
    return 0;
}

s32 func_1510D8C0() {
    return 0;
}
