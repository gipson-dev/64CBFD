#include <ultra64.h>
void func_15169260(s32, s32, s32, u8);
extern u8 D_80088C58[];
typedef struct { s32 a, b; } TwoWord135D00;
extern s32 D_800BE9E4;

/* Non-matching placeholders for the text-only asm slice asm/135D00.s. */

s32 func_15108850() {
    return 0;
}

s32 func_15108AB4() {
    return 0;
}

void func_15108B80(u8 *arg0) {
    s32 end = 0x3E7;
    u8 *temp_v0 = arg0 + *(s32 *) (arg0 + 0x50) + 0xF8;

    if (end != *(s32 *) (temp_v0 + 0x14)) {
        s32 t = *(s32 *) (temp_v0 + 0x1C) - D_800BE9E4;

        *(s32 *) (temp_v0 + 0x1C) = t;
        if (t < 0) {
            *(s32 *) (temp_v0 + 0x14) = end;
        }
    }
}

s32 func_15108BC0() {
    return 0;
}

s32 func_15108C38() {
    return 0;
}

s32 func_15108D24() {
    return 0;
}

s32 func_15108E10() {
    return 0;
}

s32 func_15108FFC() {
    return 0;
}

s32 func_15109064() {
    return 0;
}

void func_151090DC(void) {
    s32 tmp[2];

    tmp[0] = *(s32 *) D_80088C58;
    tmp[1] = *(s32 *) (D_80088C58 + 4);
    func_15169260(tmp, 2, 0, 0x1E);
}

s32 func_15109120() {
    return 0;
}
