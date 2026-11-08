#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/CD860.s. */

typedef struct { u8 bytes[0x34]; } DispatchRecord150A03B0;
extern DispatchRecord150A03B0 *D_800D3098;
void func_150A2864(u32, s32);
void func_150A2940(u32, s32, s32);
void func_150A3444(s32, s16, s16, s16);
void func_150A3398(s32, u16, s32, s32, s32, s32);
void func_151C970C(s32, s32);
/* Dispatch the record's command while preserving each command's field widths. */
s32 func_150A03B0(u32 identity, u32 command, u32 *record) {
    switch (command) {
        case 0:
            func_150A2864(identity, 0);
            return 1;
        case 1:
            func_150A2864(identity, 1);
            return 1;
        case 2:
            func_150A2940(identity, record[2], record[3]);
            return 1;
        case 3:
            func_150A3444(identity, (s16)record[2], (s16)record[3], (s16)record[4]);
            break;
        case 4:
            func_150A3398(identity, (u16)record[2], record[3], record[4], record[5], record[6]);
            break;
        case 5:
            func_151C970C(record[2] == 999 ? 2 : (record[2] != 0 ? 0 : 1),
                          (s32)&D_800D3098[identity]);
            break;
    }
    return 0;
}

s32 func_150A04D8() {
    return 0;
}
