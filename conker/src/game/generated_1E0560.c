#include <ultra64.h>

extern f32 D_800AA390;
void *func_15167A68(s32, s32, s32, s32, u8, u8);
void *memcpy(void *, const void *, u32);

/* Non-matching placeholders for the text-only asm slice asm/1E0560.s. */

extern void (*D_8008FB68[])(u8 *, s32, u8);
extern void (*D_8008FB70[])(u8 *);

s32 func_151D5E30();

u8 *func_151B30B0(void *request, f32 parameter, s32 extraBytes, u8 slot, s32 context) {
    u8 *created;
    f32 distance;
    f32 scaled;

    created = func_15167A68(0x33, context, extraBytes + 0x150, 1, slot, 1);
    if (created == NULL) {
        return NULL;
    }
    memcpy(created + 0x10, request, 56);
    distance = *(f32 *)(created + 0x38);
    created[0x10] |= 0xE;
    scaled = distance * distance / D_800AA390;
    *(f32 *)(created + 0x138) = scaled + scaled;
    *(s32 *)(created + 0x13C) = (s32)(distance * parameter * 4096.0f);
    bzero(created + 0x140, 16);
    return created;
}

s32 func_151B3184() {
    return 0;
}

s32 func_151B32C8() {
    return 0;
}

void func_151B3A34(u8 *arg0, s32 arg1, u8 arg2) {
    void (*callback)(u8 *, s32, u8) = D_8008FB68[arg0[0x44]];

    if (callback != NULL) {
        callback(arg0, arg1, arg2);
    }
}

s32 func_151B3A7C() {
    return 0;
}

s32 func_151B3CF0() {
    return 0;
}

s32 func_151B3F28() {
    return 0;
}

s32 func_151B3FDC() {
    return 0;
}

s32 func_151B42A4() {
    return 0;
}

s32 func_151B47D8() {
    return 0;
}

s32 func_151B48DC() {
    return 0;
}

s32 func_151B498C(u8 *arg0, s32 *arg1, s32 *arg2, s32 *arg3, s32 *arg4,
                  s32 *arg5, s32 *arg6, s32 *arg7, s32 *arg8, s32 *arg9,
                  s32 *arg10, s32 *arg11, u8 *arg12, u8 *arg13) {
    *arg1 = 0x220005;
    *arg2 = 0x40600;
    *arg3 = 0xFF;
    *arg4 = 0xFF;
    *arg5 = 0xFF;
    *arg6 = 0xFF;
    *arg7 = 0xFF;
    *arg8 = 0xFF;
    *arg9 = 0xFF;
    *arg10 = 0xFF;
    *arg11 = 0;
    *arg12 = 5;
    *arg13 = 0x2B;
    return 1;
}

s32 func_151B4A14() {
    return 0;
}

s32 func_151B4B78() {
    return 0;
}

void func_151B4C1C(u8 *arg0) {
    void (*callback)(u8 *);

    func_151D5E30(arg0 + 0x140);
    callback = D_8008FB70[arg0[0x44]];
    if (callback != NULL) {
        callback(arg0);
    }
}

void func_151B4C6C(u8 *arg0) {
    func_151B4C1C(arg0);
    func_15169824(arg0);
}

void func_151B4C98(u8 *arg0) {
    func_151B4C1C(arg0);
    func_15169824(arg0);
}
