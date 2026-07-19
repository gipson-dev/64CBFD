#include <ultra64.h>
extern s32 D_800BE9E4;
extern u8 D_800DDD8C;
extern u8 D_800DDD8B;
extern u8 D_800DDD8A;
extern u8 D_800DDD89;
extern u8 D_800DDD88;
extern u16 D_800DDE08;
extern s32 D_800DDE28[];
extern s32 D_800DDDB0[];
extern f32 D_800DDDC8[];

/* Non-matching placeholders for the text-only asm slice asm/1AC2F0.s. */

s32 func_1517EE40() {
    return 0;
}

s32 func_1517EF00() {
    return 0;
}

s32 func_1517EFAC(void) {
    if (func_1517EF00() == 0xFF) {
        return 1;
    }
    return 0;
}

s32 func_1517EFDC() {
    return 0;
}

s32 func_1517F08C() {
    return 0;
}

s32 func_1517F3A0() {
    return 0;
}

s32 func_1517F40C(s32 arg0) {
    if (D_800DDDB0[arg0] >= D_800DDE28[arg0]) {
        return 1;
    }
    return 0;
}

void func_1517F448(s32 arg0) {
    s32 *ptr = &D_800DDDB0[arg0];
    s32 value = *ptr;

    if (D_800DDE28[arg0] != value) {
        *ptr = value + D_800BE9E4;
    }
}

s32 func_1517F488() {
    return 0;
}

s32 func_1517F4D8() {
    return 0;
}

s32 func_1517F564() {
    return 0;
}

void func_1517F720(s32 arg0, s32 arg1, s32 arg2, s32 arg3, s32 arg4) {
    D_800DDE08 = arg1;
    D_800DDD88 = arg2;
    D_800DDD89 = 0;
    D_800DDD8A = arg0;
    D_800DDD8B = arg3;
    D_800DDD8C = arg4;
}

s32 func_1517F75C() {
    return 0;
}

s32 func_1517F7B4() {
    return 0;
}

s32 func_1517F814() {
    return 0;
}

s32 func_1517F9F4() {
    return 0;
}

s32 func_1517FB9C() {
    return 0;
}

s32 func_15180580() {
    return 0;
}

s32 func_151814FC() {
    return 0;
}

s32 func_15181CC8(s32 arg0) {
    if (0.0f == D_800DDDC8[arg0]) {
        return 1;
    }
    return 0;
}

s32 func_15181D00() {
    return 0;
}

s32 func_15181D70() {
    return 0;
}

s32 func_15181DC8() {
    return 0;
}

s32 func_15181E18() {
    return 0;
}

s32 func_15181EE0() {
    return 0;
}

s32 func_15182670() {
    return 0;
}

void func_15182748(u8 *arg0) {
    *(u8 *)(arg0 + 0x2B) = *(s16 *)(arg0 + 0xE) * *(s16 *)(arg0 + 0x2E);
}

s32 func_15182768() {
    return 0;
}
