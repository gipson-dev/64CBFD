#include <ultra64.h>
extern s32 D_800BE9E8;
extern u8 D_800D98A0[];
void *func_151A4FD0(s32, u32, s32, s32, s32, s32, u8, u32);

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

/* Replace the color record and reset the ten pointer slots. */
void func_150B6C90(void) {
    void **current;

    if (D_800D9894 != NULL) {
        func_1516972C(D_800D9894);
    }
    D_800D9894 = func_151A4FD0(0, 0, 255, 0, 0, D_800BE9E8, 0, 0);
    D_800D9890 = 3;
    ((void **)D_800D9898)[0] = NULL;
    ((void **)D_800D9898)[1] = NULL;
    current = (void **)D_800D98A0;
    do {
        current[1] = NULL;
        current[2] = NULL;
        current[3] = NULL;
        current[0] = NULL;
        current += 4;
    } while (current != (void **)D_800D98C0);
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

extern u8 D_800918DC[];
void *func_15169968(void *);

typedef struct {
    u8 *asset;
    u8 reserved04[0x10];
    s16 field14;
    s16 field16;
    s16 field18;
    u8 reserved1A[2];
    f32 field1C;
    f32 field20;
    s16 field24;
    s16 field26;
    s16 field28;
    s16 field2A;
    s16 field2C;
    s16 field2E;
    u8 field30;
    u8 field31;
    u8 field32;
    u8 field33;
    u8 field34;
    u8 field35;
    u8 field36;
    u8 field37;
    u8 field38;
    u8 field39;
    u8 reserved3A[2];
} MenuRecordDescriptorE4070;

/* Replace the menu record from its fixed descriptor, then select state 3. */
void func_150B7484(void) {
    MenuRecordDescriptorE4070 descriptor;

    descriptor.field31 = 1;
    descriptor.field2C = 88;
    descriptor.field1C = 60.0f;
    descriptor.field20 = 60.0f;
    descriptor.field14 = 0;
    descriptor.field16 = 0;
    descriptor.field18 = 0;
    descriptor.field2E = 88;
    descriptor.field30 = 6;
    descriptor.asset = D_800918DC;
    descriptor.field32 = 255;
    descriptor.field33 = 0;
    descriptor.field34 = 0;
    descriptor.field35 = 255;
    descriptor.field24 = 0;
    descriptor.field26 = 0;
    descriptor.field39 = 0;
    descriptor.field36 = 7;
    descriptor.field37 = 21;
    descriptor.field38 = 1;
    descriptor.field28 = 81;
    descriptor.field2A = 81;
    if (*(void **)D_800D9898 != NULL) {
        func_1516972C(*(void **)D_800D9898);
    }
    *(void **)D_800D9898 = func_15169968(&descriptor);
    D_800D9890 = 3;
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
