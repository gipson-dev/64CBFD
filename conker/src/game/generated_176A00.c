#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/176A00.s. */

extern f32 D_800BE9A4;

s32 func_1514BC08();

s32 func_15149550() {
    return 0;
}

s32 func_15149838() {
    return 0;
}

s32 func_15149A94() {
    return 0;
}

s32 func_15149BF4() {
    return 0;
}

s32 func_15149C58() {
    return 0;
}

s32 func_15149D18() {
    return 0;
}

s32 func_15149EC4() {
    return 0;
}

s32 func_15149FD0() {
    return 0;
}

s32 func_1514A19C() {
    return 0;
}

s32 func_1514A380() {
    return 0;
}

s32 func_1514A498() {
    return 0;
}

s32 func_1514A4EC() {
    return 0;
}

s32 func_1514A594() {
    return 0;
}

s32 func_1514A6A0() {
    return 0;
}

s32 func_1514AB5C() {
    return 0;
}

s32 func_1514AD9C() {
    return 0;
}

s32 func_1514AF74() {
    return 0;
}

s32 func_1514B034() {
    return 0;
}

s32 func_1514B364() {
    return 0;
}

s32 func_1514B844() {
    return 0;
}

s32 func_1514B87C(f32 *arg0) {
    f32 delta = arg0[0x4C / 4] * D_800BE9A4;

    arg0[0x2C / 4] += delta;
    arg0[0x30 / 4] += delta;
    return 1;
}

s32 func_1514B8B0(u8 *arg0) {
    s32 temp_v0 = *(s16 *)(arg0 + 0x1C);

    if (temp_v0 < 0x10) {
        s32 temp_v1 = temp_v0 << 4;
        if (temp_v1 < *(u8 *)(arg0 + 0x5C)) {
            *(u8 *)(arg0 + 0x5C) = temp_v1;
        }
    }
    return 1;
}

s32 func_1514B8E4() {
    return 0;
}

s32 func_1514BC08() {
    return 0;
}

void func_1514BE00(register u8 *arg0) {
    func_1514BC08(arg0, arg0 + 0x110);
}

s32 func_1514BE20() {
    return 0;
}

void func_1514BF50(u8 *arg0) {
    *(f32 *) (arg0 + 0x40) = *(f32 *) (arg0 + 0x34);
    *(f32 *) (arg0 + 0x44) = *(f32 *) (arg0 + 0x38) + 100.0f;
    *(f32 *) (arg0 + 0x48) = *(f32 *) (arg0 + 0x3C);
}

void func_1514BF7C(register u8 *arg0) {
    func_1514BC08(arg0, arg0 + 0x110);
}

s32 func_1514BF9C() {
    return 0;
}

s32 func_1514C258(s32 arg0) {
    func_1514BF9C(arg0);
    func_1514BE20(arg0);
    return 1;
}

s32 func_1514C288(s32 arg0) {
    func_1514BF9C(arg0);
    func_1514BF50(arg0);
    return 1;
}

s32 func_1514C2B8() {
    return 0;
}

s32 func_1514C2F0() {
    return 0;
}

s32 func_1514C470() {
    return 0;
}

s32 func_1514C678() {
    return 0;
}

s32 func_1514C858() {
    return 0;
}
