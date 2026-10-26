#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/CBDB0.s. */

s32 func_1509E900() {
    return 0;
}

s32 func_1509ED74() {
    return 0;
}

s32 func_1509EFF0() {
    return 0;
}

// Matched with the explicit unsigned halfword narrowing used by retail.
s32 func_1509F248(s32 arg0, u8 *arg1) {
    if (arg0 != 0) {
        func_100111C8((u16) ((*(s32 *) (arg1 + 0x0) & 0xFFFF0000) >> 16));
    }
    return 1;
}

void func_1509F660(s32, s32);
/* Full-width call slots are narrowed inside this provider. */
s32 func_1509F77C(u32, s32, s32, s32, s32);

/* Decode the packed identifiers for the three recognized record commands. */
s32 func_1509F284(s32 unused, s32 command, u32 *record) {
    switch (command) {
        case 1:
            func_1509F660(record[2] & 0xFFF, 0);
            return 1;
        case 0:
            func_1509F660(record[2] & 0xFFF, 1);
            return 1;
        case 2:
            func_1509F77C((record[0] & 0xFFFF0000U) >> 16, record[2] & 0xFFF, record[3], record[4], record[5]);
            return 1;
    }
    return 0;
}

s32 func_1509F33C(s32 arg0, s32 arg1, s32 arg2) {
    return 0;
}

s32 func_1509F354() {
    return 0;
}

s32 func_1509F47C(s32 arg0, s32 arg1, s32 arg2, s32 arg3, s16 arg4, s32 arg5) {
    s32 temp_v0 = func_151149AC((u8) arg3);
    return func_15114D24(temp_v0, func_1000F568(arg0, (u8) (arg1 - arg0 + 1)), arg2, arg4, arg5, 0);
}

s32 func_1509F4E8() {
    return 0;
}

void func_1509F5A8(s32 arg0, s32 arg1, u16 arg2) {
    func_10010F30(func_1000F568(arg0, (u8) (arg1 - arg0 + 1)), arg2, 0x40, 0, 0);
}

void func_1509F5F4(u16 arg0, s32 arg1, s32 arg2, s16 arg3, s32 arg4, s32 arg5) {
    void *object = (void *) func_1505EEF4(arg2);

    if (object != 0) {
        if ((arg5 != 0) || (func_10010894(object) == 0)) {
            func_10010344(arg0, object, arg1, arg3, arg4);
        }
    }
}

void func_1509F660(s32 arg0, s32 arg1) {
    void *temp_v0 = (void *)func_1505EEF4(arg0);

    if (temp_v0 != 0) {
        if (arg1 != 0) {
            func_10010A3C(temp_v0);
        } else {
            func_100109D0(temp_v0);
        }
    }
}

// Matched with guarded incoming-argument spill/reload scheduling.
void func_1509F6B0(s32 arg0, u16 arg1, s16 arg2, u8 arg3) {
    func_10010F30(arg0, arg1, arg3, arg2, 0);
}

s32 func_1509F6E8(s32 arg0, s32 arg1, u16 arg2, s32 arg3, s32 arg4) {
    u8 *object = (u8 *)func_1505EEF4(arg1);
    s32 x, y, z;

    if (object == 0) {
        return 0;
    }
    x = (s32)*(f32 *)(object + 0x14);
    y = (s32)*(f32 *)(object + 0x18);
    z = (s32)*(f32 *)(object + 0x1C);
    return func_10010F88(arg0, arg2, 0, 0, 0, x, y, z, arg3, arg4);
}

// Matches retail directly from the explicit coordinate temporaries.
/* Preserve full incoming words; narrow identifiers at the downstream call. */
s32 func_1509F77C(u32 arg0, s32 arg1, s32 arg2, s32 arg3, s32 arg4) {
    u8 *object = (u8 *)func_1505EEF4(arg1);
    s32 x = (s32)*(f32 *)(object + 0x14);
    s32 y = (s32)*(f32 *)(object + 0x18);
    s32 z = (s32)*(f32 *)(object + 0x1C);

    return func_1000F91C(
        (u16) arg0,
        0x7FFF,
        (s16) arg2,
        0,
        0,
        x,
        y,
        z,
        arg3,
        arg4);
}

s32 func_1509F800(s32 arg0, s32 arg1, s32 arg2) {
    return 0;
}

s32 func_1509F818(u8 arg0, u8 arg1, u8 arg2) {
    func_150AD770();
    return 0;
}
