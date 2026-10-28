#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/1E6B40.s. */

s32 func_151B9690() {
    return 0;
}

s32 func_151B9964() {
    return 0;
}

typedef struct {
    u8 header[0x10];
    u32 value;
    u8 first;
    u8 second;
    s16 parameters[11];
} Type07ParameterRecord;
void *func_15167A68(s32, s32, s32, s32, u8, u8);

/* Create a type-7 record with two byte fields and eleven signed parameters. */
void func_151B9BF0(s32 first, s32 second, s16 p0, s16 p1,
    s16 p2, s16 p3, s16 p4, s16 p5, s16 p6, s16 p7, s16 p8, s16 p9,
    s16 p10, u32 value, u8 view, s32 context) {
    Type07ParameterRecord *record = func_15167A68(7, context, 0x2C, 0, view, 1);

    if (record != NULL) {
        record->first = first;
        record->second = second;
        record->parameters[0] = p0;
        record->parameters[1] = p1;
        record->parameters[2] = p2;
        record->parameters[3] = p3;
        record->parameters[4] = p4;
        record->parameters[5] = p5;
        record->parameters[6] = p6;
        record->parameters[7] = p7;
        record->parameters[8] = p8;
        record->parameters[9] = p9;
        record->parameters[10] = p10;
        record->value = value;
    }
}

s32 func_151B9CB0() {
    return 0;
}
