#include <ultra64.h>

/* Audio script dispatch and query callbacks; retail layout asm/CBAF0.s. */

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

s32 func_1509E6F0(s32 arg0, s32 arg1, s32 *arg2) {
    if (arg1 == 3) {
        return func_151F2CDC() == 1;
    }
    return 0;
}

void func_1000DE1C(s32, s32);

/* Dispatch an audio control command, preserving legacy script packet layouts. */
s32 func_1509E730(s32 handle, s32 command, s32 *packet) {
    s32 enabled;
    switch (command) {
        case 0:
            func_1000D96C(handle & 0xFFF, packet[2], packet[3]);
            return 1;
        case 2:
            func_1000DF68(handle & 0xFFF, packet[2], 0);
            return 1;
        case 5:
            func_1000DF68(handle & 0xFFF, packet[2], 1);
            return 1;
        case 1:
            func_1000DE1C(handle & 0xFFF, packet[2]);
            return 1;
        case 3:
            if (D_800D3840 == 5) {
                return func_1000E46C(handle & 0xFFF, packet[2], packet[3], packet[4]);
            }
            return func_1000E46C(handle & 0xFFF, packet[2], packet[3], 60);
        case 4:
            if (D_800D3840 == 5) {
                return func_1000E654(handle & 0xFFF, packet[2], packet[3], packet[4] & 0xFFF);
            }
            return func_1000E654(handle & 0xFFF, packet[2], packet[3], handle & 0xFFF);
        case 6:
            enabled = 1;
            if (D_800D3840 == 3) enabled = packet[2];
            func_1000E054(handle & 0xFFF, enabled);
            return 1;
    }
    return 0;
}

s32 func_1509E8A0(s32 arg0, s32 arg1, s32 *arg2) {
    switch (arg1) {
        case 7:
            return func_1000E0F8(arg0);
        case 8:
            return func_1000E8F0(arg0);
        default:
            return 0;
    }
}
