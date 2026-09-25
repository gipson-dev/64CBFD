#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/200930.s. */

s32 func_15131828();
s32 func_15131958();

#pragma GLOBAL_ASM("asm/nonmatchings/generated_200930/func_151D3480.s")

s32 func_151D3D50() {
    return 0;
}


#pragma GLOBAL_ASM("asm/nonmatchings/generated_200930/func_151D3E04.s")


#pragma GLOBAL_ASM("asm/nonmatchings/generated_200930/func_151D3E6C.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_200930/func_151D3F14.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_200930/func_151D3FF4.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_200930/func_151D40D4.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_200930/func_151D42E8.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_200930/func_151D4408.s")

s32 func_151D4668(u8 *arg0) {
    struct { u8 *ptr; u8 value; } temp;

    temp.ptr = arg0;
    temp.value = *(u8 *)(arg0 + 0x3B);
    func_151494E0(&temp, 0x3C);
}


#pragma GLOBAL_ASM("asm/nonmatchings/generated_200930/func_151D469C.s")



#pragma GLOBAL_ASM("asm/nonmatchings/generated_200930/func_151D4794.s")


s32 func_151D4C38() {
    return 0;
}

s32 func_151D4D04(u8 *arg0, s32 arg1) {
    u8 *temp_a2 = arg0 + 0xA8;

    func_15131828(arg0, arg0 + 0xAC, temp_a2, arg0 + 0xAA);
    func_15131958(arg0 + 0x58, *(s32 *) (temp_a2 + 0xC));
    return 1;
}

s32 func_151D4D58() {
    return 0;
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_200930/func_151D4DAC.s")

void func_151D5148(u8 *arg0) {
    u8 *temp_v0 = *(u8 **) (arg0 + 0x31C);
    s16 value = *(s16 *) (temp_v0 + 0x24);

    if (value > 0) {
        *(s16 *) (temp_v0 + 0x24) = value - 1;
        temp_v0 = *(u8 **) (arg0 + 0x31C);
    }
    (*(s16 *) (temp_v0 + 0x1AA))++;
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_200930/func_151D5174.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_200930/func_151D5334.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_200930/func_151D5404.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_200930/func_151D5514.s")

s32 func_151D5648() {
    return 0;
}

s32 func_151D5714() {
    return 0;
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_200930/func_151D57F8.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_200930/func_151D5A18.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_200930/func_151D5B6C.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_200930/func_151D5D60.s")

s32 func_151D5E30() {
    return 0;
}
