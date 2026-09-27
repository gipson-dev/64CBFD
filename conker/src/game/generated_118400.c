#include <ultra64.h>

extern s32 D_800BE9F0;
s32 func_151420F8(s32);

/* Non-matching placeholders for the text-only asm slice asm/118400.s. */

s32 func_150EAF50() {
    return 0;
}

s32 func_150EB030(s32 arg0, s32 arg1) {
    switch (arg0) {
        case 1:
            switch (D_800BE9F0) {
                case 4:
                    if (func_151420F8(arg1) != 0) {
                        return 6;
                    }
                    return 3;
                default:
                    return -1;
            }
        default:
            return -1;
    }
}

s32 func_150EB090() {
    return 0;
}
