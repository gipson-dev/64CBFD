#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/6E770.s. */

extern u8 D_800848D0[];

s32 func_15041480(u8 arg0);
s32 func_15041508(s32 arg0, u8 *arg1, s32 arg2, s32 arg3);

s32 func_150412C0() {
    return 0;
}

s32 func_150413FC(s32 arg0, u8 *arg1, s32 arg2, u8 *arg3) {
    s32 result;
    s32 value;
    u8 *commands;
    u8 *row;

    result = arg0;
    value = arg2;
    commands = arg3;
    row = arg1;

    while (*commands != 0) {
        result = func_15041508(result, row, value, func_15041480(*commands));
        commands++;
        row += 8;
    }
    return result;
}

s32 func_15041480(u8 arg0) {
    s32 i;

    for (i = 0; i != 0x50; i += 4) {
        if (arg0 == D_800848D0[i]) {
            return i;
        }
        if (arg0 == D_800848D0[i + 1]) {
            return i + 1;
        }
        if (arg0 == D_800848D0[i + 2]) {
            return i + 2;
        }
        if (arg0 == D_800848D0[i + 3]) {
            return i + 3;
        }
    }
    return i;
}

s32 func_15041508(s32 arg0, u8 *arg1, s32 arg2, s32 arg3) {
    return 0;
}

s32 func_150415E0() {
    return 0;
}

s32 func_150417AC() {
    return 0;
}

s32 func_150428D4() {
    return 0;
}

s32 func_15042C40() {
    return 0;
}
