#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/D3040.s. */

s32 func_150A5B90() {
    return 0;
}

s32 func_150A5C88() {
    return 0;
}

s32 func_150A5E44() {
    return 0;
}

s32 func_150A5FA4() {
    return 0;
}

s32 func_150A60C4() {
    return 0;
}

s32 func_150A613C() {
    return 0;
}

s32 func_150A6210() {
    return 0;
}

// Shared assembly epilogue entered by func_150A6210 with a non-linking jump.
#pragma GLOBAL_ASM("asm/nonmatchings/generated_D3040/func_150A6354.s")

s32 func_150A6360() {
    return 0;
}

/* Shared return for the entity scans, including the empty-list path. */
#pragma GLOBAL_ASM("asm/nonmatchings/generated_D3040/func_150A64B8.s")

s32 func_150A64C8() {
    return 0;
}

s32 func_150A6568(s32 x, s32 z, s32 *secondaryCount, s32 selector,
                  s32 xEnd, s32 zEnd, s32 yMin, s32 yMax);

s32 func_150A6500(s32 arg0, s32 arg1, s32 *arg2, s32 arg3) {
    return func_150A6568(arg0, arg1, arg2, arg3, arg0, arg1, -10000, 20000);
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_D3040/func_150A6538.s")

/* Original register-save scan and its shared loop/cleanup entry. */
#pragma GLOBAL_ASM("asm/nonmatchings/generated_D3040/func_150A6568.s")
#pragma GLOBAL_ASM("asm/nonmatchings/generated_D3040/func_150A66FC.s")

s32 func_150A6760() {
    return 0;
}

s32 func_150A67D0() {
    return 0;
}
