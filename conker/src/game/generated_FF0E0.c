#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/FF0E0.s. */

s32 func_150D1C30() {
    return 0;
}

s32 func_150D1F6C() {
    return 0;
}

void func_150D2054(void *arg0) {
    s32 base = (s32) arg0 + 0x28;
    s32 i = 0;

    do {
        void *entry = ((void **) base)[i + 9];

        if (entry != 0) {
            func_1516972C(entry);
        }
    } while ((i = (u8) (i + 1)) < 6);
}

s32 func_150D20B0(s32 arg0) {
    func_150D2054((void *) arg0);
    func_15149368(arg0);
}

s32 func_150D20DC(s32 arg0) {
    func_150D2054((void *) arg0);
    func_1514933C(arg0);
}
