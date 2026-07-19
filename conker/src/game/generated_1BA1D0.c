#include <ultra64.h>
f32 func_150ADA68();
extern void (*D_8008D680[])();
typedef struct { s32 a, b, c; } ThreeWord1BA1D0;
void func_15169260(s32, s32, s32, u8);
extern u8 D_800A74D4[];
typedef struct { s32 val; } OneWord1BA1D0;

/* Non-matching placeholders for the text-only asm slice asm/1BA1D0.s. */

s32 func_1518F8E0();

s32 func_15191400();

s32 func_1518CD20() {
    return 0;
}

s32 func_1518D1C0() {
    return 0;
}

s32 func_1518D6E0() {
    return 0;
}

s32 func_1518E298() {
    return 0;
}

s32 func_1518E308() {
    return 0;
}

void func_1518E37C(u8 *arg0, u8 arg1) {
    if (arg1 != *(arg0 + 0x22)) {
        func_1518E308(arg0);
        *(arg0 + 0x22) = arg1;
    }
}

s32 func_1518E3C4() {
    return 0;
}

void func_1518E4A0(u8 *arg0) {
    func_1518E308(arg0);
    func_1514EDF0(arg0, *(s32 *) (arg0 + 0x18));
}

s32 func_1518E4CC(s32 arg0) {
    func_1518E4A0(arg0);
    func_15169804(arg0);
}

s32 func_1518E4F8(s32 arg0) {
    func_1518E4A0(arg0);
    func_15169824(arg0);
}

s32 func_1518E524() {
    return 0;
}

s32 func_1518E5D8() {
    return 0;
}

s32 func_1518E66C() {
    return 0;
}

s32 func_1518E6D4() {
    return 0;
}

s32 func_1518E73C() {
    return 0;
}

s32 func_1518EB10() {
    return 0;
}

s32 func_1518EF54() {
    return 0;
}

s32 func_1518F058() {
    return 0;
}

s32 func_1518F108() {
    return 0;
}

s32 func_1518F15C(u8 *arg0) {
    s32 temp_v0 = *(s16 *) (arg0 + 0x1C);

    *(f32 *) (arg0 + 0x30) = *(f32 *) (arg0 + 0x30) - *(f32 *) (arg0 + 0x30) * *(f32 *) (arg0 + 0x154);
    if (temp_v0 < *(s16 *) (arg0 + 0x158)) {
        *(arg0 + 0x5C) = (u32) *(s16 *) (arg0 + 0x15A) * temp_v0;
    }
    return 1;
}

s32 func_1518F1A0() {
    return 0;
}

s32 func_1518F384() {
    return 0;
}

void func_1518F45C(s32 arg0, u8 arg1) {
    s32 tmp[1];

    tmp[0] = *(s32 *) D_800A74D4;
    func_15169260(tmp, 1, arg0, arg1);
}

s32 func_1518F49C() {
    return 0;
}

s32 func_1518F51C() {
    return 0;
}

s32 func_1518F5D0() {
    return 0;
}

s32 func_1518F7C4() {
    return 0;
}

void func_1518F858(u8 *arg0) {
    if (*(s8 *) (arg0 + 0x89) != -1) {
        D_8008D680[*(s8 *) (arg0 + 0x89)]();
    }
}

void func_1518F89C(u8 *arg0) {
    u8 *temp_v0;
    f32 r = func_150ADA68();

    temp_v0 = arg0 + 0x30;
    *(f32 *) temp_v0 = r * *(f32 *) (temp_v0 + 0x10) + *(f32 *) (temp_v0 + 0xC);
    func_1518F8E0(arg0);
}

s32 func_1518F8E0() {
    return 0;
}

s32 func_1518FC04(u8 *arg0, ThreeWord1BA1D0 *arg1) {
    u8 *temp = *(u8 **) (arg0 + 0x2C);

    *(ThreeWord1BA1D0 *) (temp + 0x34) = *arg1;
    func_1514BE20(temp);
    return 1;
}

s32 func_1518FC44(u8 *arg0, ThreeWord1BA1D0 *arg1) {
    u8 *temp = *(u8 **) (arg0 + 0x2C);

    *(ThreeWord1BA1D0 *) (temp + 0x34) = *arg1;
    func_1514BF50(temp);
    return 1;
}

s32 func_1518FC84() {
    return 0;
}

s32 func_1518FDC4() {
    return 0;
}

s32 func_1519003C() {
    return 0;
}

s32 func_1519021C() {
    return 0;
}

void func_151903D0(u8 *arg0) {
    func_15163DEC(arg0, arg0 + 0x20);
    func_15163F50(arg0, arg0 + 0x18);
}

s32 func_15190400() {
    return 0;
}

void func_15190454(u8 *arg0) {
    u8 *temp_v0;

    temp_v0 = *(u8 **)(arg0 + 0x40);
    *(s32 *)(temp_v0 + 0x84) = 0;
}

s32 func_15190464(s32 arg0) {
    func_15190454(arg0);
    func_151617C4(arg0);
}

s32 func_15190490(s32 arg0) {
    func_15190454(arg0);
    func_151617E4(arg0);
}

s32 func_151904BC() {
    return 0;
}

void func_15190518(u8 *arg0) {
    struct {
        u8 *target;
        u8 code;
    } rec;

    rec.target = arg0;
    rec.code = *(arg0 + 0x3B);
    func_1516944C(0x3E, &rec, 0x2A);
}

s32 func_15190550() {
    return 0;
}

s32 func_151905BC() {
    return 0;
}

void func_151906C4(u8 *arg0) {
    u8 *target = *(u8 **)(*(u8 **)(arg0 + 0x10) + 0x31C);

    if (target != NULL) {
        target[0x1AC] = 0;
    }
}

void func_151906E0(u8 *arg0, s32 *arg1, u8 arg2) {
    u8 *temp_v0 = arg0 + 0x90;

    if (arg2 == 0x2D) {
        s32 temp_v1 = arg1[0];
        s32 temp_a2 = *(s32 *) (temp_v0 + 8);

        if (temp_v1 == temp_a2) {
            *(s32 *) (temp_v0 + 8) = arg1[1];
            return;
        }
        if (temp_a2 == arg1[1]) {
            *(s32 *) (temp_v0 + 8) = temp_v1;
        }
    }
}

void func_1519072C(u8 *arg0) {
    struct {
        u8 *target;
        u8 code;
    } rec;

    rec.target = arg0;
    rec.code = *(arg0 + 0x3B);
    func_151D343C(&rec, 0x2A);
    func_1518F45C(&rec, 0x49);
}

s32 func_15190770() {
    return 0;
}

s32 func_15190840(s32 arg0) {
    func_15191400(arg0);
    func_15169804(arg0);
}

s32 func_1519086C(s32 arg0) {
    func_15191400(arg0);
    func_15169824(arg0);
}

s32 func_15190898() {
    return 0;
}

s32 func_15190F9C() {
    return 0;
}

s32 func_1519108C() {
    return 0;
}

s32 func_15191400() {
    return 0;
}

s32 func_15191520() {
    return 0;
}

s32 func_1519187C(u8 *arg0) {
    s32 temp_v0 = *(s16 *) (arg0 + 0x1C);

    if (temp_v0 < *(s16 *) (arg0 + 0x124)) {
        s32 temp_v1 = (u32) *(s16 *) (arg0 + 0x126) * temp_v0;

        if (temp_v1 < *(arg0 + 0x5C)) {
            *(arg0 + 0x5C) = temp_v1;
        }
    }
    return 1;
}

s32 func_151918BC() {
    return 0;
}

s32 func_15191980() {
    return 0;
}

s32 func_15191A84() {
    return 0;
}

s32 func_15191B8C() {
    return 0;
}
