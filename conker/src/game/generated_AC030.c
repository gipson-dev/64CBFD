#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/AC030.s. */

s32 func_1507EB80() {
    return 0;
}

s32 func_1507EBB8() {
    return 0;
}

s32 func_1507EC38() {
    return 0;
}

s32 func_1507EE58() {
    return 0;
}

s32 func_1507EEB8() {
    return 0;
}

s32 func_1507EEF4() {
    return 0;
}

void func_1507EFA0(s32 arg0, u8 *arg1) {
    s32 i = 4;
    u8 *ptr = arg1 + 4;

    for (; i >= 0; i--) {
        if (arg0 == *ptr) {
            *ptr = 0;
            return;
        }
        ptr--;
    }
}

s32 func_1507EFD0() {
    return 0;
}

s32 func_1507F454() {
    return 0;
}

s32 func_1507F4C0() {
    return 0;
}

s32 func_1507F54C() {
    return 0;
}

s32 func_1507F640() {
    return 0;
}

s32 func_1507FC2C() {
    return 0;
}

s32 func_1507FEA0() {
    return 0;
}

void func_1507FF94(u8 *arg0) {
    struct {
        u8 *ptr;
        u8 value;
    } temp;
    void *record = &temp;

    temp.ptr = arg0;
    temp.value = arg0[0x3B];
    func_15191B8C(record, 0xD);
    func_151494E0(record, 0xD);
}

s32 func_1507FFD8() {
    return 0;
}
