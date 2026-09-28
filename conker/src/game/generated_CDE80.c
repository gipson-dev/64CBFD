#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/CDE80.s. */

typedef struct {
    s16 field0;
    s16 field2;
    s16 field4;
    u8 pad6[0x11];
    u8 field17;
    s32 field18;
    s32 field1C;
    s32 field20;
    u8 pad24[0x10];
} GeneratedCDE80Record;

extern GeneratedCDE80Record *D_800D3098;

s32 func_150A09D0() {
    return 0;
}

s32 func_150A0D14() {
    return 0;
}

s32 func_150A0D8C() {
    return 0;
}

s32 func_150A1040(register s32 arg0) {
    return arg0 + 0x400;
}

s32 func_150A104C() {
    return 0;
}

s32 func_150A11C4() {
    return 0;
}

s32 func_150A1DA0() {
    return 0;
}

s32 func_150A23E4() {
    return 0;
}

s32 func_150A24C0() {
    return 0;
}

s32 func_150A25D4() {
    return 0;
}

s32 func_150A278C() {
    return 0;
}

s32 func_150A2864() {
    return 0;
}

s32 func_150A2940() {
    return 0;
}

s32 func_150A29C8() {
    return 0;
}

s32 func_150A2AEC() {
    return 0;
}

/* Original active-actor volume occupancy; OGL Note 640. */
#pragma GLOBAL_ASM("asm/nonmatchings/generated_CDE80/func_150A2CA4.s")

/* Original view-volume query; OGL Note 545. */
#pragma GLOBAL_ASM("asm/nonmatchings/generated_CDE80/func_150A2D84.s")

s32 func_150A2E4C() {
    return 0;
}

s32 func_150A2EE4() {
    return 0;
}

s32 func_150A2FA4() {
    return 0;
}

s32 func_150A3058() {
    return 0;
}

s32 func_150A3194() {
    return 0;
}

s32 func_150A32B4() {
    return 0;
}

void func_150A3330(s32 arg0, s32 *arg1, s32 *arg2, s32 *arg3, s32 *arg4) {
    *arg1 = D_800D3098[arg0].field17;
    *arg2 = D_800D3098[arg0].field18;
    *arg3 = D_800D3098[arg0].field1C;
    *arg4 = D_800D3098[arg0].field20;
}

s32 func_150A3398() {
    return 0;
}

void func_150A3444(s32 index, s16 arg1, s16 arg2, s16 arg3) {
    D_800D3098[index].field0 = arg1;
    D_800D3098[index].field2 = arg2;
    D_800D3098[index].field4 = arg3;
}

s32 func_150A3504();

s32 func_150A34B0(u8 *arg0) {
    if (arg0[0x14] == 1) {
        return 0;
    }
    if ((arg0[0x15] & 3) == 0) {
        return func_150A3504(arg0);
    }
    return 0;
}

s32 func_150A3504() {
    return 0;
}
