#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/13BB20.s. */

extern u8 *D_800DBE48;

s32 func_1510E670() {
    return 0;
}

s32 func_1510E7A4() {
    return 0;
}

s32 func_1510E82C() {
    return 0;
}

s32 func_1510E8BC() {
    return 0;
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_13BB20/func_1510E950.s")

s32 func_1510F648() {
    return 0;
}

s32 func_1510F720() {
    return 0;
}

void func_1510F800() {
    func_150A49F4();
}

s32 func_1510F820() {
    return 0;
}

s32 func_1510F8CC() {
    return 0;
}

s32 func_1510F8D8() {
    return 0;
}

s32 func_1510FC34() {
    return 0;
}

s32 func_1510FD20() {
    return 0;
}

s32 func_1510FE30(u8 *arg0) {
    u8 *current = D_800DBE48;
    s32 index = 0;
    s16 offset;

    while (current != NULL) {
        if (current == arg0) {
            return index;
        }

        offset = *(s16 *)(current + 0xC);
        if (offset != 0) {
            current += offset;
        } else {
            offset = *(s16 *)(current + 4);
            current += offset;
            if (offset != 0) {
                index++;
            } else {
                current = NULL;
            }
        }
    }

    return 0;
}
