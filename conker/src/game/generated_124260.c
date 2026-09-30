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

void func_150F7310(u8 *arg0, u8 *volatile arg1, volatile u8 arg2) {
    u8 *target = arg0 + 0x28;

    if (arg2 == 0x3E) {
        u8 *word_owner = arg1;
        u8 *byte_owner = arg1;

        if ((*(s32 *)target == *(s32 *)word_owner) ||
            (target[4] == byte_owner[4])) {
            func_1516972C(arg0);
        }
    } else {
        func_15149514((s32)arg1, arg2, (s32)target,
                      (s32)(target + 4), (s32)arg0);
    }
}

void func_150F739C(u8 *arg0) {
    u8 *sub = arg0 + 0x28;
    u8 i;

    for (i = 0; i < 2; i++) {
        void *entry = *(void **) (sub + 8 + i * 4);

        if (entry != NULL) {
            func_1516972C(entry);
        }
    }
    func_1514EDF0(arg0, *(s32 *) sub);
}

void func_150F740C(u8 *arg0) {
    func_150F739C(arg0);
    func_1514933C(arg0);
}

void func_150F7438(u8 *arg0) {
    func_150F739C(arg0);
    func_15149368(arg0);
}
