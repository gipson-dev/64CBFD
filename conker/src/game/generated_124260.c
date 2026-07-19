#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/124260.s. */

s32 func_150F6DB0(u8 *arg0) {
    struct { u8 *ptr; u8 value; } temp;

    temp.ptr = arg0;
    temp.value = *(u8 *)(arg0 + 0x3B);
    func_151494E0(&temp, 0x3E);
}

s32 func_150F6DE4() {
    return 0;
}

s32 func_150F706C() {
    return 0;
}

s32 func_150F7310() {
    return 0;
}

s32 func_150F739C() {
    return 0;
}

s32 func_150F740C(s32 arg0) {
    func_150F739C(arg0);
    func_1514933C(arg0);
}

s32 func_150F7438(s32 arg0) {
    func_150F739C(arg0);
    func_15149368(arg0);
}
