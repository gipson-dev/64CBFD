#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/CBAF0.s. */

extern s32 D_800D3840;
void func_1001263C(s32, s32, s32);
void func_151F2D6C(s32, s32);
void func_151F2BA8(void);

/* Dispatch sequence start, level, and stop requests from the script packet. */
s32 func_1509E640(s32 sequence, s32 command, s32 *packet) {
    s32 level;

    switch (command) {
        case 0:
            level = 0x7FFF;
            if (D_800D3840 >= 3) {
                level = packet[2];
            }
            func_1001263C(sequence, level, 0x40);
            return 1;
        case 1:
            if (D_800D3840 == 4) {
                func_151F2D6C(packet[2], packet[3]);
            } else {
                func_151F2D6C(packet[2], 0);
            }
            return 1;
        case 2:
            func_151F2BA8();
            return 1;
    }
    return 0;
}

s32 func_1509E6F0(u8 *arg0, s32 arg1, s32 arg2) {
    if (arg1 == 3) {
        return func_151F2CDC() == 1;
    }
    return 0;
}

s32 func_1509E730() {
    return 0;
}

s32 func_1509E8A0(s32 arg0, s32 arg1, s32 arg2) {
    switch (arg1) {
        case 7:
            return func_1000E0F8(arg0);
        case 8:
            return func_1000E8F0(arg0);
        default:
            return 0;
    }
}
