#include <ultra64.h>

extern s32 D_800BE9E4;

/* Non-matching placeholders for the text-only asm slice asm/EC420.s. */

void func_150BEF70(s32 arg0) {
}

s32 func_150BEF7C() {
    return 0;
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
