#include <ultra64.h>
extern u8 D_800D98A4[];
extern u8 D_800D9898[];
extern u8 D_800D98C0[];
extern void *D_800D9894;
extern s32 D_800BE9E4;
extern void func_1516972C(void *arg0);

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
    u8 *p;
    u8 *ptr = D_800D9898;

    do {
        p = *(u8 **) (ptr + 0x14);
        ptr += 4;
        if (p != 0) {
            *(s32 *) (p + 0x20) = 1;
        }
    } while (ptr != D_800D98A4);
    D_800D9890 = 3;
}

void func_150B6D78(void) {
    void **current;
    void **end;

    if (D_800D9894 != NULL) {
        func_1516972C(D_800D9894);
        D_800D9894 = NULL;
    }

    current = (void **)D_800D9898;
    end = (void **)D_800D98C0;
    do {
        if (*current != NULL) {
            func_1516972C(*current);
            *current = NULL;
        }
        current++;
    } while (current != end);

    D_800D9890 = 3;
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

void func_150B71A8(u8 *arg0) {
    if (*(s16 *) (arg0 + 0x38) != 0x1000) {
        *(s16 *) (arg0 + 0x38) += D_800BE9E4 << 8;
        if (*(s16 *) (arg0 + 0x38) > 0x1000) {
            *(s16 *) (arg0 + 0x38) = 0x1000;
        }
    } else if (*(s16 *) (arg0 + 0x3A) != 0x1000) {
        *(s16 *) (arg0 + 0x3A) += D_800BE9E4 << 8;
        if (*(s16 *) (arg0 + 0x3A) > 0x1000) {
            *(s16 *) (arg0 + 0x3A) = 0x1000;
        }
    }
}

s32 func_150B7220() {
    return 0;
}

void func_150B73F0(u8 *arg0) {
    s32 scale;
    s32 x;
    s32 y;

    scale = (*(s16 *)(arg0 + 0x24) << 16) / *(s32 *)(arg0 + 0x1C);
    x = (((*(s16 *)(arg0 + 0x20) - *(s16 *)(arg0 + 0x18)) * scale) >> 16) +
        *(s16 *)(arg0 + 0x18);
    y = (((*(s16 *)(arg0 + 0x22) - *(s16 *)(arg0 + 0x1A)) * scale) >> 16) +
        *(s16 *)(arg0 + 0x1A);
    *(f32 *)(arg0 + 0x2C) = (f32)x;
    *(f32 *)(arg0 + 0x30) = (f32)y;
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
