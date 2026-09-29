#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/770F0.s. */

void func_15049C40(f32 *arg0, f32 *arg1) {
    f32 dot = arg0[0] * arg1[0] + arg0[1] * arg1[1] +
              arg0[2] * arg1[2] + arg0[3] * arg1[3];

    if (dot < 0.0f) {
        arg1[0] = -arg1[0];
        arg1[1] = -arg1[1];
        arg1[2] = -arg1[2];
        arg1[3] = -arg1[3];
    }
}

s32 func_15049CB8() {
    return 0;
}

s32 func_15049EDC() {
    return 0;
}

s32 func_1504A140() {
    return 0;
}
