#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/1D6E80.s. */

s32 func_1519F400();

s32 func_151A99D0() {
    return 0;
}

s32 func_151A9AA4() {
    return 0;
}

s32 func_151A9BA0() {
    return 0;
}

s32 func_151A9CA0() {
    return 0;
}

s32 func_151A9DC0() {
    return 0;
}

s32 func_151A9EC0() {
    return 0;
}

s32 func_151A9FC8() {
    return 0;
}

s32 func_151AA09C() {
    return 0;
}

void func_151AA170(s32 arg0) {
}

s32 func_151AA17C() {
    return 0;
}

void func_151AA1D0(void) {
    func_1519F400();
}

void func_151AA1F0(void) {
    func_1519F400();
}

s32 func_151AA210() {
    return 0;
}

s32 func_151AA264() {
    return 0;
}

s32 func_151AA30C() {
    return 0;
}

s32 func_151AA48C() {
    return 0;
}

s32 func_151AA5A4() {
    return 0;
}

s32 func_151AA6D8() {
    return 0;
}

s32 func_151AAA4C() {
    return 0;
}

s32 func_151AAABC() {
    return 0;
}

s32 func_151AAB50(u8 *arg0) {
    u8 *temp_v0 = *(u8 **)(arg0 + 0x80) + 0x58;

    *(s32 *)(temp_v0 + 0x14) = 0;
    func_151352EC(arg0);
}

s32 func_151AAB78(u8 *arg0) {
    u8 *temp_v0 = *(u8 **)(arg0 + 0x80) + 0x58;

    *(s32 *)(temp_v0 + 0x14) = 0;
    func_1513530C(arg0);
}

s32 func_151AABA0(u8 *arg0) {
    s32 result = 1;

    if (*(u8 *)(arg0 + 0x84) == 0) {
        result = 0;
    }
    *(u8 *)(arg0 + 0x84) = 0;
    return result;
}

s32 func_151AABC4() {
    return 0;
}

s32 func_151AADBC(u8 *arg0) {
    u8 *temp_v0 = *(u8 **) (arg0 + 0x98);
    s32 temp_v1 = *(s16 *) (arg0 + 0x1C) << 4;

    if (temp_v1 >= 0x100) {
        temp_v1 = 0xFF;
    }
    if (temp_v1 < *(temp_v0 + 0x1B)) {
        *(temp_v0 + 0x1B) = temp_v1;
    }
    return 1;
}

s32 func_151AADF8() {
    return 0;
}

s32 func_151AB090() {
    return 0;
}

s32 func_151AB180(u8 *arg0) {
    u8 *temp_v0 = *(u8 **) (arg0 + 0xB0);

    *(s32 *) (temp_v0 + 0x70) = 0;
    *(u32 *) (arg0 + 0xB0) = 0;
    *(u32 *) (arg0 + 0x18) |= 2;
    temp_v0 += 0x58;
    func_1513F6C0(arg0, 0, 0);
    return 0;
}

s32 func_151AB1C4() {
    return 0;
}

s32 func_151AB2C4() {
    return 0;
}

s32 func_151AB3A4() {
    return 0;
}

s32 func_151AB6B8() {
    return 0;
}

s32 func_151AB788() {
    return 0;
}

s32 func_151AB7D8() {
    return 0;
}

void func_151AB828(u8 *arg0) {
    func_15141DA4(*(s32 *) (arg0 + 0x18), 0, 4);
}

s32 func_151AB854() {
    return 0;
}

void func_151AB920(s32 arg0, s32 arg1) {
}

s32 func_151AB930() {
    return 0;
}

s32 func_151AB9C8() {
    return 0;
}

s32 func_151ABD54() {
    return 0;
}

void func_151ABE00(u8 *arg0) {
    struct {
        u8 *target;
        u8 code;
    } rec;

    rec.target = arg0;
    rec.code = *(arg0 + 0x3B);
    func_1516944C(0x20, &rec, 0xC);
}
