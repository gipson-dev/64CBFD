#include <ultra64.h>
extern void (*D_8008FB98[])();

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

s32 func_151B7678() {
    return 0;
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
    void (*temp_v1)() = D_8008FB98[*(*(u8 **) (arg0 + 0x98) + 8)];

    if (temp_v1 != 0) {
        temp_v1();
    }
}

s32 func_151B8318() {
    return 0;
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
