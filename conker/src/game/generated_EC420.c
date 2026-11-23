#include <ultra64.h>

extern s32 D_800BE9E4;

/* Non-matching placeholders for the text-only asm slice asm/EC420.s. */

void func_150BEF70(s32 arg0) {
}

void func_1516D99C(
    s16 arg0, s16 arg1, s16 arg2, u8 arg3, u8 arg4, u8 arg5,
    u8 arg6, u8 arg7, u8 arg8, u8 arg9, u8 arg10, u8 arg11,
    u8 arg12, u8 arg13, u8 arg14, u8 arg15, u8 arg16, u8 arg17,
    u8 arg18, u8 arg19, u8 arg20, u8 arg21, u8 arg22, u8 arg23,
    u8 arg24, u8 arg25, u8 arg26, s16 arg27, s16 arg28, s16 arg29,
    s16 arg30, u16 arg31, u8 arg32, u8 arg33, u8 arg34, u8 arg35,
    s16 arg36, u16 arg37, u16 arg38, u8 arg39, u8 arg40, u8 arg41,
    u8 arg42, u8 arg43, s32 arg44, u8 arg45, u8 arg46, s32 arg47,
    s32 arg48);

/* Submit the same factory request at two opposite signed positions. */
void func_150BEF7C(s32 parameter) {
    s32 position;
    s32 count;

    position = 380;
    count = 0;
    do {
        func_1516D99C(0x1FDB, 0x25, (s16)position, 0xD, 0, 0x50, 0x8F,
            0, 0, 0, 0, 0, 8, 200,
            10, 0, 0, 0, 0, 0, 40,
            40, 4, 0, 0, 0, 0, 0x555,
            0x555, 0x555, 0x555, parameter, 50, 0, 255,
            20, 4000, 2000, 1, 6, 0, 1,
            0, 0, 0, 0, 3, 255, 0);
        count++;
        position = -position;
    } while (count != 2);
}

/* Advance effect intensity and two signed accumulators; return 1 when finished. */
s32 func_150BF0F4(u8 *record) {
    s32 value = record[0x1F];
    s32 target = record[0x26];
    s32 phase;
    if (record[0x24] != 0) {
        if (value != target) {
            value = (s32)((u32)value + (u32)D_800BE9E4 * record[0x27]);
            if (value > target) value = target;
            record[0x1F] = value;
        }
    } else if (value != 0) {
        value = (s32)((u32)value - (u32)D_800BE9E4 * record[0x2F]);
        if (value < 0) value = 0;
        record[0x1F] = value;
    }
    if (record[0x24] == 0 && value == 0) return 1;
    *(s16 *)(record + 0x14) = (s32)((u32)*(s16 *)(record + 0x14) + (u32)(s32)*(s8 *)(record + 0x2D) * (u32)D_800BE9E4);
    *(s16 *)(record + 0x16) = (s32)((u32)*(s16 *)(record + 0x16) + (u32)(s32)*(s8 *)(record + 0x2E) * (u32)D_800BE9E4);
    if (*(s16 *)(record + 0x14) <= 0) {
        *(s16 *)(record + 0x16) = 0;
        *(s16 *)(record + 0x14) = *(s16 *)(record + 0x16);
        return 1;
    }
    phase = (s32)((u32)record[0x2C] + (u32)D_800BE9E4);
    if (phase >= 128) phase = 127;
    record[0x2C] = phase;
    return 0;
}

s32 func_150BF21C() {
    return 0;
}

s32 func_150BF760() {
    return 0;
}

s32 func_150BFA7C() {
    return 0;
}

s32 func_150BFFE0() {
    return 0;
}

s32 func_150C01DC() {
    return 0;
}

s32 func_150C04C0() {
    return 0;
}

s32 func_150C0648() {
    return 0;
}
