#include <ultra64.h>
extern u8 D_800D98A4[];
extern u8 D_800D9898[];
extern s32 D_800BE9E4;

/* Non-matching placeholders for the text-only asm slice asm/E4070.s. */

extern u8 D_800D9890;
s32 func_150B76BC();

s32 func_150B6BC0() {
    return 0;
}

s32 func_150B6C90() {
    return 0;
}

void func_150B6D34(void) {
    u8 *ptr = D_800D9898;
    u8 *end = D_800D98A4;
    s32 val = 1;

    do {
        u8 *p = *(u8 **) (ptr + 0x14);

        ptr += 4;
        if (p != 0) {
            *(s32 *) (p + 0x20) = val;
        }
    } while (ptr != end);
    D_800D9890 = 3;
}

s32 func_150B6D78() {
    return 0;
}

void func_150B6DFC(u8 *arg0) {
    *(s16 *) (arg0 + 0x34) = *(s16 *) (arg0 + 0x34) + D_800BE9E4 * 48;
    if (*(s16 *) (arg0 + 0x34) >= 0x801) {
        *(s16 *) (arg0 + 0x34) = -0xC00;
    }
}

s32 func_150B6E3C() {
    return 0;
}

s32 func_150B709C() {
    return 0;
}

s32 func_150B71A8() {
    return 0;
}

s32 func_150B7220() {
    return 0;
}

s32 func_150B73F0() {
    return 0;
}

s32 func_150B7484() {
    return 0;
}

s32 func_150B7560() {
    return 0;
}

s32 func_150B765C(void) {
    func_150B76BC(0x3C, 1);
    D_800D9890 = 3;
}

s32 func_150B768C(void) {
    func_150B76BC(0xE6, 2);
    D_800D9890 = 3;
}

s32 func_150B76BC() {
    return 0;
}

s32 func_150B77A8() {
    return 0;
}

s32 func_150B791C() {
    return 0;
}

s32 func_150B7B40() {
    return 0;
}

s32 func_150B82D0() {
    return 0;
}

s32 func_150B85C0() {
    return 0;
}

s32 func_150B879C() {
    return 0;
}
