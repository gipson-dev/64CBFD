#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/12D630.s. */

extern s32 D_800BE9E4;

s32 func_15100180(u8 *arg0) {
    struct { u8 *ptr; u8 value; } temp;

    temp.ptr = arg0;
    temp.value = *(u8 *)(arg0 + 0x3B);
    func_151494E0(&temp, 0x48);
}

s32 func_151001B4() {
    return 0;
}

s32 func_15100230() {
    return 0;
}

void func_151002BC(u8 *arg0) {
    s16 invalid = -1;
    u8 *state = arg0 + 0x28;
    u8 *entry = *(u8 **) state;

    if (*(s32 *) entry == 0) {
        goto invalid_state;
    }
    if (entry[4] == 0xFF) {
        goto invalid_state;
    }
    if (state[4] == entry[0x3B]) {
        goto valid_state;
    }

invalid_state:
    *(s16 *) (arg0 + 0xE) = invalid;
    return;

valid_state:
    if (*(s32 *) (entry + 0x318) != 0) {
        *(s16 *) (state + 6) -= D_800BE9E4;
    }
}
