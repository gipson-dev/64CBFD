#include <ultra64.h>

typedef struct {
    s32 first;
    s32 second;
    s32 third;
    s32 fourth;
} FourWord1CC440;

/* Non-matching placeholders for the text-only asm slice asm/1CC440.s. */

s32 func_1519EF90() {
    return 0;
}

s32 func_1519F108() {
    return 0;
}

s32 func_1519F168() {
    return 0;
}

s32 func_1519F1C8() {
    return 0;
}

void func_1519F3B8(u8 *arg0) {
    FourWord1CC440 *temp_v1;
    s32 r = func_1519F1C8(arg0, 6);

    temp_v1 = (FourWord1CC440 *) (arg0 + 0x58);
    temp_v1->first = r;
    temp_v1->second = 0;
    r = func_1519F1C8(arg0, 7);
    temp_v1->third = r;
    temp_v1->fourth = 0;
}

s32 func_1519F400() {
    return 0;
}

s32 func_1519F48C() {
    return 0;
}

s32 func_1519F4F0() {
    return 0;
}

s32 func_1519F7F0() {
    return 0;
}

s32 func_1519FE6C() {
    return 0;
}

s32 func_151A084C() {
    return 0;
}

void func_151A0928(u8 *arg0) {
    u8 *temp_v0 = *(u8 **) (arg0 + 0x28) + 0x58;

    if (arg0[0x2C] == 6) {
        *(s32 *) (temp_v0 + 4) = 0;
    } else {
        *(s32 *) (temp_v0 + 0xC) = 0;
    }
}

s32 func_151A0950() {
    return 0;
}

s32 func_151A09B4() {
    return 0;
}

s32 func_151A0A10() {
    return 0;
}

s32 func_151A0AF8() {
    return 0;
}

s32 func_151A0C0C() {
    return 0;
}

s32 func_151A0E40() {
    return 0;
}

s32 func_151A0F28() {
    return 0;
}

s32 func_151A1010() {
    return 0;
}

void func_151A11CC(f32 arg0, f32 arg1, s32 arg2, s32 arg3) {
}

s32 func_151A11E4() {
    return 0;
}

s32 func_151A175C() {
    return 0;
}

s32 func_151A18DC() {
    return 0;
}

s32 func_151A1998() {
    return 0;
}

s32 func_151A1E34() {
    return 0;
}

s32 func_151A1EE8() {
    return 0;
}

s32 func_151A1FB4() {
    return 0;
}

s32 func_151A24A8() {
    return 0;
}

s32 func_151A25E0() {
    return 0;
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1CC440/func_151A26EC.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1CC440/func_151A2960.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1CC440/func_151A2A14.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1CC440/func_151A2AD4.s")

void func_151A2B84(f32 *arg0, s32 arg1, s32 arg2, s32 arg3, f32 arg4, f32 *arg5) {
    f32 t = 1.0f - arg4;

    arg5[0] = arg0[0] * t;
    arg5[1] = arg0[1] * t;
    arg5[2] = arg0[2] * t;
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1CC440/func_151A2BD0.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1CC440/func_151A2C24.s")

s32 func_151A2F0C() {
    return 0;
}

s32 func_151A3150() {
    return 0;
}
