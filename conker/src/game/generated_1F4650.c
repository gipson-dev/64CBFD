#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/1F4650.s. */

s32 func_151C71A0() {
    return 0;
}

s32 func_151C756C() {
    return 0;
}

s32 func_151C7E98() {
    return 0;
}

s32 func_151C82D0() {
    return 0;
}

void func_151C8674(s32 arg0, s32 arg1) {
    struct {
        s32 a;
        s32 b;
    } rec;

    if (arg0 != 0) {
        rec.a = arg0;
        rec.b = arg1;
        func_151403A8(&rec, 0x20);
    }
}

s32 func_151C86AC() {
    return 0;
}

s32 func_151C87AC(u8 *arg0, u8 arg1, u8 arg2, u8 arg3, s32 arg4, s32 arg5, u16 *arg6) {
    u8 *temp_v0 = *(u8 **) (arg0 + 0x18);

    if (!(*(temp_v0 + 0x86) & 2)) {
        *arg6 = 0;
    }
    return 0;
}

s32 func_151C87E0() {
    return 0;
}

s32 func_151C899C() {
    return 0;
}

s32 func_151C8FCC() {
    return 0;
}

s32 func_151C9198() {
    return 0;
}

s32 func_151C94D4() {
    return 0;
}

s32 func_151C95D8() {
    return 0;
}

s32 func_151C96DC(u8 *arg0, u8 arg1) {
    u8 *ptr = *(u8 **) (arg0 + 0x170) + 0x110;

    if (*(ptr + 0x86) & 2) {
        return 1;
    }
    return 0;
}

void func_151C970C(s32 arg0, s32 arg1) {
    struct {
        s32 value;
        u8 code;
    } rec;

    rec.value = arg1;
    rec.code = arg0;
    func_151403A8(&rec, 0x3A);
}

s32 func_151C9740() {
    return 0;
}

s32 func_151C9AC0() {
    return 0;
}

s32 func_151C9B30(u8 *arg0) {
    u8 *temp_v0 = *(u8 **) (arg0 + 0x18);

    if (*(temp_v0 + 0x6F) == 0) {
        *(u8 *) (*(u8 **) (arg0 + 0x14) + 9) = 0;
    } else {
        *(u8 *) (*(u8 **) (arg0 + 0x14) + 9) = 1;
    }
    return 1;
}

s32 func_151C9B64(u8 *arg0, u8 *arg1) {
    if (*(*(u8 **) (arg0 + 0x188) + 0x6F) == 0) {
        *(u32 *) (arg0 + 0x58) &= ~2;
        *arg1 = 0;
    } else {
        *arg1 = 1;
    }
    return 1;
}

s32 func_151C9BA0() {
    return 0;
}

s32 func_151C9DE8() {
    return 0;
}

s32 func_151C9ED4() {
    return 0;
}

s32 func_151C9F38() {
    return 0;
}

s32 func_151CA6A0() {
    return 0;
}

s32 func_151CAACC() {
    return 0;
}

s32 func_151CAB78() {
    return 0;
}

s32 func_151CAD28() {
    return 0;
}

s32 func_151CB110() {
    return 0;
}

s32 func_151CB49C() {
    return 0;
}

s32 func_151CB510() {
    return 0;
}

s32 func_151CB5FC() {
    return 0;
}

s32 func_151CB918() {
    return 0;
}

s32 func_151CB970() {
    return 0;
}

s32 func_151CBB6C() {
    return 0;
}

s32 func_151CBBE0() {
    return 0;
}

s32 func_151CBC60() {
    return 0;
}

s32 func_151CC1D4() {
    return 0;
}

void func_151CC290(void *arg0) {
    void *value = arg0;

    func_1515572C(&value, 0x46);
}

s32 func_151CC2BC() {
    return 0;
}

s32 func_151CC524() {
    return 0;
}

s32 func_151CC77C() {
    return 0;
}

s32 func_151CC840() {
    return 0;
}

s32 func_151CCD1C() {
    return 0;
}

s32 func_151CCE94() {
    return 0;
}

s32 func_151CCF08() {
    return 0;
}

s32 func_151CD224() {
    return 0;
}
