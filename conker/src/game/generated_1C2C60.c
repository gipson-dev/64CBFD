#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/1C2C60.s. */

s32 func_1519CDB0(s32 arg0, f32 arg1, s32 arg2);

s32 func_15199980();
void func_100111C8(u16 arg0);
void func_1519C258();

extern f32 D_800A8AA4;
extern f32 D_800A8AAC;

s32 func_151957B0() {
    return 0;
}

s32 func_1519582C() {
    return 0;
}

s32 func_15195868() {
    return 0;
}

s32 func_15195984() {
    return 0;
}

s32 func_15195A84(s16 arg0, s32 arg1, s32 arg2, s32 arg3) {
    return arg0;
}

s32 func_15195AA8() {
    return 0;
}

s32 func_15195D00() {
    return 0;
}

s32 func_15195DD4() {
    return 0;
}

s32 func_15195FB0() {
    return 0;
}

s32 func_15195FF0() {
    return 0;
}

void func_15196318(u8 *arg0, s32 arg1, s32 arg2) {
    if (arg0 != NULL) {
        arg0[0x12] = arg1;
        arg0[0x13] = arg2;
    }
}

s32 func_15196330() {
    return 0;
}

s32 func_151963B4() {
    return 0;
}

s32 func_15196438() {
    return 0;
}

s32 func_15196748() {
    return 0;
}

s32 func_15196B4C() {
    return 0;
}

s32 func_15197148() {
    return 0;
}

f32 func_151979F8(s32 arg0) {
    return D_800A8AA4;
}

s32 func_15197A0C() {
    return 0;
}

f32 func_15197A68(s32 arg0) {
    return D_800A8AAC;
}

void func_15197A7C(u8 *arg0) {
    struct {
        u8 *ptr;
        u8 value;
    } temp;

    if (arg0 != NULL) {
        temp.ptr = arg0;
        temp.value = arg0[0x3B];
        func_15147D64(&temp, 8);
    }
}

s32 func_15197AB4() {
    return 0;
}

s32 func_15197BBC() {
    return 0;
}

s32 func_15197C10() {
    return 0;
}

s32 func_15198054() {
    return 0;
}

s32 func_15198110() {
    return 0;
}

s32 func_15198570() {
    return 0;
}

s32 func_151987CC() {
    return 0;
}

s32 func_1519897C() {
    return 0;
}

s32 func_15198C60(void) {
    func_10010F30(0x1AA, 0x7FFF, 0x40, 0, 0);
}

s32 func_15198C90() {
    return 0;
}

s32 func_15198D40() {
    return 0;
}

void func_15198D7C(s32 arg0) {
}

s32 func_15198D88() {
    return 0;
}

s32 func_151990AC() {
    return 0;
}

void func_151993B4(u8 *arg0) {
    u8 *temp_v0 = *(u8 **) (arg0 + 0x98);

    *(u16 *) (arg0 + 0x1E) &= 0xFFFD;
    *(arg0 + 0x30) = 0;
    *(temp_v0 + 6) |= 1;
    *(temp_v0 + 6) |= 4;
}

s32 func_151993E4() {
    return 0;
}

s32 func_1519944C() {
    return 0;
}

s32 func_151994B8() {
    return 0;
}

void func_15199834(u8 *arg0) {
    struct {
        u8 *ptr;
        u8 value;
    } temp;

    if (arg0 != NULL) {
        temp.ptr = arg0;
        temp.value = arg0[0x3B];
        func_15147D64(&temp, 0x26);
    }
}

s32 func_1519986C() {
    return 0;
}

s32 func_15199928(s32 arg0) {
    func_15199980(arg0);
    func_151478F4(arg0);
}

s32 func_15199954(s32 arg0) {
    func_15199980(arg0);
    func_15147928(arg0);
}

s32 func_15199980() {
    return 0;
}

s32 func_15199A10() {
    return 0;
}

s32 func_15199C34() {
    return 0;
}

s32 func_1519A9A4() {
    return 0;
}

s32 func_1519B4B8() {
    return 0;
}

s32 func_1519BE1C() {
    return 0;
}

s32 func_1519BEB8() {
    return 0;
}

s32 func_1519BF20() {
    return 0;
}

s32 func_1519BF8C(void) {
    func_10010F30(0x1AA, 0x7FFF, 0x40, 0, 0);
}

s32 func_1519BFBC() {
    return 0;
}

void func_1519C06C(arg0, arg1)
u8 *arg0;
s32 arg1;
{
    u8 *temp_v0 = *(u8 **) (arg0 + 0x98);

    arg1 = *(u16 *) (temp_v0 + 0x130);
    if (arg1 != 0) {
        func_100111C8(arg1);
    }
}

s32 func_1519C09C() {
    return 0;
}

s32 func_1519C200(s32 arg0) {
    func_1519C258(arg0);
    func_151617C4(arg0);
}

s32 func_1519C22C(s32 arg0) {
    func_1519C258(arg0);
    func_151617E4(arg0);
}

void func_1519C258(u8 *arg0) {
    u8 *temp_v0;

    temp_v0 = *(u8 **)(*(u8 **)(arg0 + 0x38) + 0x98);
    *(s32 *)(temp_v0 + 0x148) = 0;
}

s32 func_1519C26C() {
    return 0;
}

s32 func_1519C4E4() {
    return 0;
}

s32 func_1519C56C() {
    return 0;
}

s32 func_1519C910() {
    return 0;
}

s32 func_1519C948(s32 arg0) {
    func_1519CDB0(arg0, 0.25f, 0x1C);
    return 0;
}

s32 func_1519C970(s32 arg0) {
    func_1519CDB0(arg0, 0.5f, 0x1D);
    return 0;
}

s32 func_1519C998(s32 arg0) {
    func_1519CDB0(arg0, 0.2f, 0x1D);
    return 0;
}

s32 func_1519C9C4() {
    return 0;
}

s32 func_1519CD64() {
    return 0;
}

s32 func_1519CDB0(s32 arg0, f32 arg1, s32 arg2) {
    return 0;
}
