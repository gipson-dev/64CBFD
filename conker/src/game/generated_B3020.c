#include <ultra64.h>
extern u8 *D_8008FDD4;
extern s8 D_8008FD90;
extern u8 *D_800872A0;

/* Non-matching placeholders for the text-only asm slice asm/B3020.s. */

extern s32 D_800D23B0;
extern u8 D_800CC40F[];

s32 func_15085B70() {
    return 0;
}

s32 func_15085BE8() {
    return 0;
}

s32 func_15085DA8() {
    return 0;
}

s32 func_15085DF8() {
    return 0;
}

s32 func_15086098() {
    return 0;
}

s32 func_15086364() {
    return 0;
}

s32 func_15086BD0() {
    return 0;
}

s32 func_15086C70() {
    return 0;
}

s32 func_15086CBC() {
    return 0;
}

s32 func_15086D48() {
    return 0;
}

s32 func_15086D94() {
    return 0;
}

s32 func_150870D0() {
    return 0;
}

s32 func_15087350() {
    return 0;
}

s32 func_15087CC0() {
    return 0;
}

s32 func_15087DCC() {
    return 0;
}

s32 func_15087E54() {
    return 0;
}

s32 func_15087EF0() {
    return 0;
}

void func_15087FC4(s32 arg0, s32 arg1) {
    u8 *temp_v0 = D_800872A0;

    if (temp_v0 != 0) {
        *(u8 *) (arg0 * 0x84 + (s32) temp_v0 + 0x31) = arg1;
    }
}

void func_15087FEC(s32 arg0, s32 arg1) {
    u8 *temp_v0 = D_800872A0;

    if (temp_v0 != 0) {
        *(f32 *) (arg0 * 0x84 + (s32) temp_v0 + 4) = arg1 * 0.00390625f;
    }
}

s32 func_1508802C() {
    return 0;
}

s32 func_150880F8() {
    return 0;
}

s32 func_150881CC() {
    return 0;
}

s32 func_15088218() {
    return 0;
}

s32 func_15088270() {
    return 0;
}

s32 func_150882B0(s32 arg0) {
    s32 idx = arg0;
    u8 *temp_v1 = D_800872A0;
    u8 *ptr;

    if (temp_v1 == 0) {
        return 0;
    }
    ptr = (u8 *) (idx * 0x84 + (s32) temp_v1);
    return *(s8 *) (ptr + 0x27);
}

s32 func_150882E4() {
    return 0;
}

s32 func_150883B0() {
    return 0;
}

s32 func_1508855C() {
    return 0;
}

s32 func_150885EC() {
    return 0;
}

s32 func_1508868C() {
    return 0;
}

s32 func_15088780() {
    return 0;
}

s32 func_150887F8(void) {
    u8 *temp_v1 = D_800872A0;

    if (temp_v1 == 0) {
        return 0;
    }
    return temp_v1[0x46] == 0xFF;
}

s32 func_15088824() {
    return 0;
}

s32 func_150888A8() {
    return 0;
}

s32 func_15088A08() {
    return 0;
}

s32 func_15088D58() {
    return 0;
}

s32 func_15088F30() {
    return 0;
}

s32 func_1508907C() {
    return 0;
}

s32 func_150891E8() {
    return 0;
}

s32 func_150896EC() {
    return 0;
}

void func_15089BB0() {
    D_800D23B0 = 0;
}

s32 func_15089BC0() {
    return 0;
}

s32 func_15089F9C() {
    return 0;
}

s32 func_1508A1BC() {
    return 0;
}

s32 func_1508A6FC() {
    return 0;
}

s32 func_1508B194(s32 arg0) {
    if (arg0 < D_8008FD90) {
        return *(s16 *) (D_8008FDD4 + arg0 * 12 + 0x70);
    }
    return 0;
}

void func_1508B1D4(s32 arg0) {
    if (arg0 < D_8008FD90) {
        *(u16 *) (D_8008FDD4 + arg0 * 12 + 0x70) = 0;
    }
}

s32 func_1508B20C() {
    return 0;
}

s32 func_1508B2A8() {
    return 0;
}

s32 func_1508B3F8() {
    return 0;
}

s32 func_1508B9BC() {
    return 0;
}

s32 func_1508BC20() {
    return 0;
}

s32 func_1508BF14() {
    return 0;
}

s32 func_1508C194(s32 arg0) {
    return 0;
}

s32 func_1508C1A4() {
    return 0;
}

s32 func_1508C5B8() {
    return 0;
}

s32 func_1508C9CC() {
    return 0;
}

s32 func_1508CA88() {
    return 0;
}

s32 func_1508CAD8() {
    return 0;
}

s32 func_1508D850() {
    return 0;
}

s32 func_1508DA1C() {
    return 0;
}

s32 func_1508DAEC() {
    return 0;
}

s32 func_1508DC24() {
    return 0;
}

void func_1508E6C8() {
}

s32 func_1508E6D0() {
    return 0;
}

s32 func_1508E780() {
    return 0;
}

s32 func_1508E89C() {
    return 0;
}

s32 func_1508EB90() {
    return 0;
}

void func_1508EBF8(s32 arg0, s32 arg1) {
    s32 temp_v0 = D_800CC40F[arg0 * 0x32C];

    func_1509BFB0(1, temp_v0 | 0x2000, 0x14, arg1);
}

void func_1508EC5C(s32 arg0, s32 arg1) {
    s32 temp_v0 = D_800CC40F[arg0 * 0x32C];

    func_1509BFB0(1, temp_v0 | 0x2000, 0x61, arg1);
}

s32 func_1508ECC0() {
    return 0;
}

s32 func_1508EDBC() {
    return 0;
}

s32 func_1508EE0C() {
    return 0;
}
