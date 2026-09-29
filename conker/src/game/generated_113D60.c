#include <ultra64.h>
extern s32 D_800D9A20[];
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

s32 func_150E6F18() {
    return 0;
}

s32 func_150E6FAC() {
    return 0;
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

s32 func_150E88C0() {
    return 0;
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
