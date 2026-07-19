#include <ultra64.h>
extern void (*D_80086014[])();
extern f32 D_800C35A0;
extern s16 D_800C3598[];
extern u16 *D_800C35D8[];
extern u8 D_800C363A[];

/* Non-matching placeholders for the text-only asm slice asm/49D30.s. */

extern u8 D_800C3CA0[];

extern u8 D_800C3510[];
extern u8 D_800C354A[];

s32 func_1501C880() {
    return 0;
}

s32 func_1501CC3C() {
    return 0;
}

s32 func_1501CDC0() {
    return 0;
}

s32 func_1501CE54() {
    return 0;
}

s32 func_1501CFF8(s32 arg0) {
    s32 count = D_800C363A[arg0];
    s32 sum = 0;
    s32 i = 0;

    if (count > 0) {
        u16 *ptr = D_800C35D8[arg0];

        do {
            sum += *ptr;
            i += 1;
            ptr += 1;
        } while (i < count);
    }
    return sum;
}

s32 func_1501D044() {
    return 0;
}

s32 func_1501D1D4() {
    return 0;
}

s32 func_1501D258() {
    return 0;
}

s32 func_1501D2C4() {
    return 0;
}

s32 func_1501D348() {
    return 0;
}

s32 func_1501DAAC() {
    return 0;
}

s32 func_1501DE18() {
    return 0;
}

s32 func_1501DF04() {
    return 0;
}

s32 func_1501E05C() {
    return 0;
}

s32 func_1501E1B4() {
    return 0;
}

s32 func_1501E2F8() {
    return 0;
}

s32 func_1501E400() {
    return 0;
}

s32 func_1501E540() {
    return 0;
}

s32 func_1501E73C() {
    return 0;
}

s32 func_1501E81C() {
    return 0;
}

s32 func_1501EA18() {
    return 0;
}

s32 func_1501EC38() {
    return 0;
}

s32 func_1501F72C() {
    return 0;
}

s32 func_1501FC8C() {
    return 0;
}

s32 func_1501FE68() {
    return 0;
}

s32 func_1501FFE8() {
    return 0;
}

s32 func_15020388() {
    return 0;
}

s32 func_15020878() {
    return 0;
}

s32 func_15020EC4() {
    return 0;
}

s32 func_1502178C() {
    return 0;
}

s32 func_15021DB8() {
    return 0;
}

s32 func_15022024() {
    return 0;
}

s32 func_15022190() {
    return 0;
}

void func_150221E8(s16 arg0, s16 arg1, s16 arg2, f32 arg3) {
    D_800C35A0 = arg3;
    D_800C3598[0] = arg0;
    D_800C3598[1] = arg1;
    D_800C3598[2] = arg2;
}

void func_15022234(s32 arg0) {
    D_800C3510[arg0] = 0;
}

void func_15022248(s32 arg0) {
    D_800C354A[arg0] = 0;
}

s32 func_1502225C() {
    return 0;
}

s32 func_150222E0() {
    return 0;
}

s32 func_15022398() {
    return 0;
}

s32 func_15022528() {
    return 0;
}

s32 func_15022640() {
    return 0;
}

s32 func_150226BC() {
    return 0;
}

s32 func_15022754() {
    return 0;
}

s32 func_150227BC() {
    return 0;
}

s32 func_15022848() {
    return 0;
}

s32 func_150228E4() {
    return 0;
}

void func_15022998(s32 *arg0) {
    s32 temp_v0 = *arg0;

    if ((temp_v0 == 0x1B) || (temp_v0 == 4)) {
        void (*temp_v1)() = D_80086014[temp_v0];

        if (temp_v1 != 0) {
            temp_v1();
        }
    }
}

s32 func_150229E4() {
    return 0;
}

s32 func_15022B08() {
    return 0;
}

s32 func_15022BA4() {
    return 0;
}

s32 func_15023264() {
    return 0;
}

void func_150233BC(void) {
    bzero(D_800C3CA0, 0xA8);
}

s32 func_150233E4() {
    return 0;
}

s32 func_15023440() {
    return 0;
}

s32 func_150234A4() {
    return 0;
}

s32 func_150235DC() {
    return 0;
}

s32 func_1502378C() {
    return 0;
}
