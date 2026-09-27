#include <ultra64.h>
extern void (*D_8008FB98[])(u8 *, s32, u8);

/* Non-matching placeholders for the text-only asm slice asm/1E37D0.s. */

s32 func_151B6320() {
    return 0;
}

s32 func_151B6420() {
    return 0;
}

s32 func_151B65D4() {
    return 0;
}

s32 func_151B6928() {
    return 0;
}

s32 func_151B70B4() {
    return 0;
}

s32 func_151B7144() {
    return 0;
}

s32 func_151B7328() {
    return 0;
}

s32 func_151B7678(u8 *arg0, f32 *arg1) {
    u8 *container = *(u8 **)(arg0 + 0x98);
    u8 *entry = *(u8 **)(container + 4);
    u8 *record = *(u8 **)entry;

    if (*(s32 *)record == 0 || entry[4] != record[0x3B]) {
        return 0;
    }
    arg1[0] = *(f32 *)(record + 0x14);
    arg1[1] = *(f32 *)(record + 0x18);
    arg1[2] = *(f32 *)(record + 0x1C);
    return 1;
}

s32 func_151B76CC() {
    return 0;
}

s32 func_151B77F4() {
    return 0;
}

s32 func_151B7998() {
    return 0;
}

s32 func_151B7C38() {
    return 0;
}

void func_151B82CC(u8 *arg0, s32 arg1, u8 arg2) {
    u8 *temp_v0 = *(u8 **) (arg0 + 0x98);
    void (*temp_v1)(u8 *, s32, u8) =
        D_8008FB98[*(temp_v0 + 8)];

    if (temp_v1 != 0) {
        temp_v1(arg0, arg1, arg2);
    }
}

void func_151B8318(u8 *arg0, u8 *arg1, u8 arg2) {
    u8 *container = *(u8 **)(arg0 + 0x98);
    u8 *entry = *(u8 **)(container + 4);

    if (arg2 == 0) {
        s32 value = *(s32 *)arg1;

        if (value == *(s32 *)entry || entry[4] == arg1[4]) {
            func_1516972C(arg0);
        }
    }
}

void func_151B8370(arg0, arg1)
u8 *arg0;
s32 arg1;
{
    u8 *temp_v0 = *(u8 **) (arg0 + 0x98);

    arg1 = *(s32 *) temp_v0;
    if (arg1 != 0) {
        func_1516972C(arg1);
    }
}

s32 func_151B83A0(s32 arg0) {
    func_151B8370(arg0);
    func_151478F4(arg0);
}

s32 func_151B83CC(s32 arg0) {
    func_151B8370(arg0);
    func_15147928(arg0);
}
