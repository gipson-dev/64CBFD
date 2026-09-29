#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/EEE70.s. */

s32 func_150C19C0(void *arg0, u8 *arg1, u8 arg2) {
    s32 command;

    switch (arg2) {
        case 1:
            command = 0x18;
            break;
        case 2:
            command = 0x15;
            break;
    }
    func_15142314(*(s32 *) (arg1 + 0x1D4), command, arg0);
    return 1;
}

s32 func_150C1A2C(s32 arg0, s32 arg1) {
    return 7;
}

s32 func_150C1A40() {
    return 0;
}

s32 func_150C1E34() {
    return 0;
}
