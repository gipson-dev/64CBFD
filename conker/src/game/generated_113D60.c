#include <ultra64.h>
extern s32 D_800D9A20[];
extern f32 D_800A1378;
extern f32 D_800BE9A4;
extern f32 *D_80088A44[6];
f32 func_150ADA68(void);
f32 func_151423D8(u8 angle);
s32 func_1514ECE0(void *node, s16 key, void **result);
s32 func_150E8930();
void *func_15149130(s16 arg0, s8 arg1, s8 arg2, s8 arg3, u8 arg4,
                    u8 arg5, s32 arg6, u8 arg7, s32 arg8);

/* Non-matching placeholders for the text-only asm slice asm/113D60.s. */

s32 func_150E68B0() {
    return 0;
}

s32 func_150E6B84() {
    return 0;
}

s32 func_150E6E34() {
    return 0;
}

void func_150E6ED8(u8 *arg0) {
    func_1514470C(D_800D9A20[func_150ADA20() & 1], arg0);
}

void func_150E6F18(f32 *output) {
    f32 *range = D_80088A44[(u32)func_150ADA20() % 6];
    f32 fraction = func_150ADA68();

    output[0] = range[0] + (range[3] - range[0]) * fraction;
    output[1] = range[1] + (range[4] - range[1]) * fraction;
    output[2] = range[2] + (range[5] - range[2]) * fraction;
}

void func_150E6FAC(f32 *output, u8 *actor) {
    void *node;
    f32 radius;
    s16 angle;
    f32 xOffset;
    f32 zOffset;
    u8 *record;

    if (func_1514ECE0(*(void **)(actor + 0x2F4), 0x16, &node)) {
        radius = func_150ADA68() * 100.0f + 80.0f;
        angle = func_150ADA20() & 0xFF;
        xOffset = func_151423D8((u8)(angle - 0x40));
        zOffset = func_151423D8((u8)angle);
        record = *(u8 **)((u8 *)node + 0x10);
        output[0] = (*(f32 *)(actor + 0x14) + *(f32 *)(record + 0x38) * -80.0f) + xOffset * radius;
        output[1] = (*(f32 *)(actor + 0x18) + *(f32 *)(record + 0x3C) * -80.0f) + 100.0f;
        output[2] = (*(f32 *)(actor + 0x1C) + *(f32 *)(record + 0x40) * -80.0f) + zOffset * radius;
    } else {
        output[0] = *(f32 *)(actor + 0x14);
        output[1] = *(f32 *)(actor + 0x18);
        output[2] = *(f32 *)(actor + 0x1C);
    }
}

void func_150E70CC(f32 *arg0, u8 *arg1) {
    arg0[0] = *(f32 *)(arg1 + 0x14);
    arg0[1] = *(f32 *)(arg1 + 0x18);
    arg0[2] = *(f32 *)(arg1 + 0x1C);
}

s32 func_150E70EC() {
    return 0;
}

s32 func_150E71E4() {
    return 0;
}

s32 func_150E7290() {
    return 0;
}

s32 func_150E75A0() {
    return 0;
}

s32 func_150E76D0() {
    return 0;
}

s32 func_150E7994() {
    return 0;
}

s32 func_150E7C9C() {
    return 0;
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_113D60/func_150E7FEC.s")

s32 func_150E81A8() {
    return 0;
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_113D60/func_150E83AC.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_113D60/func_150E8470.s")

s32 func_150E8824(u8 *arg0, u8 arg1) {
    func_15131828(arg0, arg0 + 0xAC, arg0 + 0xA8, arg0 + 0xAA);
    return 1;
}

void func_150E8854(void) {
    f32 payload;
    void *result;

    payload = 10.0f;
    result = func_15149130(0x12C, -1, 0x35, -1, 0, 0, 4, 0xFF, 1);
    if (result != 0) {
        memcpy((u8 *) result + 0x28, &payload, 4);
    }
}

void func_150E88C0(u8 *arg0) {
    f32 *timer = (f32 *) (arg0 + 0x28);

    *timer -= D_800BE9A4;
    if (*timer < 0.0f) {
        *timer = func_150ADA68() * D_800A1378 + 201.0f;
        func_150E8930(arg0);
    }
}

s32 func_150E8930() {
    return 0;
}

s32 func_150E8A80() {
    return 0;
}

s32 func_150E8B1C() {
    return 0;
}

s32 func_150E8D5C() {
    return 0;
}

s32 func_150E90DC() {
    return 0;
}

s32 func_150E9178() {
    return 0;
}

s32 func_150E93DC() {
    return 0;
}

s32 func_150E971C() {
    return 0;
}
