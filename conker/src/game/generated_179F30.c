#include <ultra64.h>
s32 func_151ACA60(u8 *, f32, s32);
extern u8 *D_800D2E4C;
void func_15083568(u8 *, s32, f32, s32);
extern s32 D_800BE9F0;

/* Non-matching placeholders for the text-only asm slice asm/179F30.s. */

void func_1500EE18();

s32 func_1514F194();
void func_1514DCAC();
s32 func_1516972C();
s32 func_1515F10C();
s32 func_1514E920();
s32 func_1514E89C();
s32 func_1514EC1C(s32 arg0, s32 arg1, s32 arg2);
extern u8 D_800A5920[];
extern u8 D_800A5988[];

s32 func_1514CA80() {
    return 0;
}

s32 func_1514D15C() {
    return 0;
}

s32 func_1514D310() {
    return 0;
}

s32 func_1514D3B0() {
    return 0;
}

s32 func_1514D4B8() {
    return 0;
}

s32 func_1514D564() {
    return 0;
}

s32 func_1514D64C() {
    return 0;
}

void func_1514D96C(s32 arg0) {
}

s32 func_1514D978() {
    return 0;
}

void func_1514D9F4(u8 *arg0) {
    u8 *temp;

    func_1514D978(arg0);
    temp = (u8 *) func_151ACA60(arg0, 20.0f, 0);
    func_1514EC1C(temp, arg0, 0x14);
}

s32 func_1514DA38() {
    return 0;
}

s32 func_1514DAA4() {
    return 0;
}

void func_1514DB18(u8 *arg0) {
    u8 *temp_v0 = (u8 *) func_15158BD0(arg0, 1, 0);

    if (temp_v0 != 0) {
        func_1514EC1C(temp_v0, arg0, 0x13);
    }
}

void func_1514DB58(s32 arg0) {
}

void func_1514DB64(void) {
    if (D_800BE9F0 == 0x14) {
        func_151B2060();
    }
}

void func_1514DB98() {
    func_1514F194();
}

s32 func_1514DBB8() {
    return 0;
}

void func_1514DC38(s32 arg0) {
    func_1500EE18(arg0, 0xFF, 1);
}

s32 func_1514DC5C(s32 arg0) {
    func_151D0F60(arg0, 0, 0xFF, 1);
}

void func_1514DC84(u8 *arg0) {
    *(u32 *)(arg0 + 0x94) |= 2;
}

void func_1514DC98(u8 *arg0) {
    *(u32 *)(arg0 + 0x94) |= 0x710;
}

void func_1514DCAC(arg0)
u8 *arg0;
{
    *(s32 *) (arg0 + 0x9C) = 0x6000;
    func_15083568(arg0, 0x23, 1.0f, 0);
    func_15083568(arg0, 0x44, 1.0f, 0);
}

void func_1514DCF4(u8 *arg0) {
    u8 *temp_v0 = *(u8 **) (arg0 + 0x31C);

    if (temp_v0 != 0) {
        *(temp_v0 + 0x94) = 1;
    }
    func_15083568(arg0, 0x17, 1.0f, 0);
}

void func_1514DD2C() {
    func_1514DCAC();
}

void func_1514DD4C() {
    func_1514DCAC();
}

void func_1514DD6C() {
    func_1514DCAC();
}

void func_1514DD8C() {
    func_1514DCAC();
}

void func_1514DDAC() {
    func_1514DCAC();
}

void func_1514DDCC() {
    func_1514DCAC();
}

void func_1514DDEC() {
    func_1514DCAC();
}

void func_1514DE0C() {
    func_1514DCAC();
}

void func_1514DE2C(s32 arg0) {
}

void func_1514DE38(s32 arg0) {
}

void func_1514DE44(s32 arg0) {
}

void func_1514DE50(void) {
    if (*(D_800D2E4C + 0x11) & 8) {
        func_1514DCAC();
    }
}

void func_1514DE88(s32 arg0) {
}

s32 func_1514DE94() {
    return 0;
}

void func_1514DFD0(u8 *arg0) {
    s32 ret = func_15083FB0(9);

    *(arg0 + 0x65) = ret + 1;
    *(arg0 + 0x101) |= 0x34;
}

s32 func_1514E00C() {
    return 0;
}

s32 func_1514E194() {
    return 0;
}

s32 func_1514E31C() {
    return 0;
}

s32 func_1514E508() {
    return 0;
}

s32 func_1514E5B8() {
    return 0;
}

s32 func_1514E668() {
    return 0;
}

s32 func_1514E718() {
    return 0;
}

void func_1514E7C8(s32 arg0) {
    s32 temp_v0 = func_1518D1C0(arg0, 7, 0, 1, 0xFF, 1, D_800A5920);

    func_1514EC1C(temp_v0, arg0, 0xF);
}

void func_1514E824(s32 arg0) {
}

void func_1514E830() {
    func_1516972C();
}

s32 func_1514E850(s32 arg0) {
    func_1518E308(arg0);
    func_1516972C(arg0);
}

void func_1514E87C() {
    func_1515F10C();
}

s32 func_1514E89C() {
    return 0;
}

s32 func_1514E920() {
    return 0;
}

void func_1514E9DC() {
    func_1514E920();
}

void func_1514E9FC() {
    func_1514E89C();
}

s32 func_1514EA1C() {
    return 0;
}

void func_1514EB6C() {
    func_1514E89C();
}

s32 func_1514EB8C(s32 arg0, s32 arg1, s32 arg2) {
    return 1;
}

s32 func_1514EBA4() {
    return 0;
}

s32 func_1514EC1C(s32 arg0, s32 arg1, s32 arg2) {
    return 0;
}

s32 func_1514ECE0() {
    return 0;
}

s32 func_1514ED3C() {
    return 0;
}

s32 func_1514ED8C() {
    return 0;
}

s32 func_1514EDF0() {
    return 0;
}

s32 func_1514EE70() {
    return 0;
}

s32 func_1514EECC() {
    return 0;
}

void func_1514F110() {
    func_1514F194();
}

s32 func_1514F130() {
    return 0;
}

s32 func_1514F194() {
    return 0;
}

s32 func_1514F308() {
    return 0;
}

s32 func_1514F3CC() {
    return 0;
}

void func_1514F44C(s32 arg0) {
    s32 temp_v0 = func_1518D1C0(arg0, 5, 0, 1, 0xFF, 1, D_800A5988);

    func_1514EC1C(temp_v0, arg0, 0xD);
}

s32 func_1514F4A8(s32 arg0) {
    func_151D74B0(arg0, 1, -1, 0xFF, 1);
}

s32 func_1514F4D8(s32 arg0) {
    func_151D74B0(arg0, 2, 1, 0xFF, 1);
}

void func_1514F508(s32 arg0) {
    func_151D74B0(arg0, 3, 0, 0xFF, 1);
}

s32 func_1514F538(s32 arg0) {
    func_151D74B0(arg0, 4, -1, 0xFF, 1);
}

s32 func_1514F568(s32 arg0) {
    func_150C4120(arg0, -1, 0xFF, 1);
}

void func_1514F590(u8 *arg0) {
    func_1501175C(arg0, 0xFF, 1);
    func_15011A78(arg0, 0xFF, 1);
}

s32 func_1514F5CC() {
    return 0;
}
