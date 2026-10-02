#include <ultra64.h>
extern u8 D_800CC406[];
extern s32 D_800C3E80[];
extern u8 D_800BE9C0;
extern s32 D_800C3E88;
extern s32 D_800C3E8C;
extern u16 D_800C3E7A;
extern u8 D_800C3E90;
extern u16 D_800C4ED0[];
extern u8 D_800CC33A[];
extern u8 D_80038080;
extern s32 D_800BE9F0;
extern u8 D_800D2040[];

/* Non-matching placeholders for the text-only asm slice asm/58F80.s. */

s32 func_1502BAD0() {
    return 0;
}

s32 func_1502BD84() {
    return 0;
}

s32 func_1502BEE4() {
    return 0;
}

s32 func_1502C1A4() {
    return 0;
}

void func_1502C380(void) {
    D_800C3E88 = D_800C3E80[D_800BE9C0];
    D_800C3E8C = D_800C3E88;
    D_800C3E7A = 0;
}

s32 func_1502C3BC(s32 arg0) {
    s32 temp_v1 = *(D_800CC406 + arg0 * 0x32C);

    if (temp_v1 >= 0x46) {
        temp_v1 = 0xB;
    }
    return temp_v1;
}

s32 func_1502C408() {
    return 0;
}

s32 func_1502C608() {
    return 0;
}

s32 func_1502C6E8() {
    return 0;
}

s32 func_1502C974() {
    return 0;
}

s32 func_1502CC34() {
    return 0;
}

s32 func_1502CCFC() {
    return 0;
}

s32 func_1502D54C() {
    return 0;
}

s32 func_1502D630() {
    return 0;
}

s32 func_1502D824() {
    return 0;
}

s32 func_1502DB20(s32 arg0) {
    switch (arg0) {
        case 59:
        case 117:
        case 130:
        case 136:
        case 144:
        case 150:
        case 152:
        case 156:
        case 157:
        case 159:
        case 160:
        case 177:
        case 178:
        case 180:
            return D_800C4ED0[arg0] - 4;
        default:
            return D_800C4ED0[arg0];
    }
}

s32 func_1502DB84() {
    return 0;
}

s32 func_1502DF38() {
    return 0;
}

void func_1502E474(void) {
    if (D_800C3E7A != 0) {
        func_150A9984(D_800C3E80[D_800BE9C0], D_800C3E7A);
    }
    D_800C3E90 = 1;
}

s32 func_1502E4C4() {
    return 0;
}

void func_1502E9FC(s32 arg0, s32 arg1) {
}

void func_1502EA0C(u8 *arg0, s32 arg1, s32 arg2, s32 arg3, s32 arg4, s32 arg5) {
    arg0[0xA4] = 4;
    arg0[0xA5] = 0;
    arg0[0xA6] = arg5;
    arg0[0xA7] = 0xFF;
    *(u32 *) (arg0 + 0xA0) = (arg4 << 24) | (arg1 << 16) | (arg2 << 8) | arg3;
}

void func_1502EA50(u8 *arg0) {
    arg0[0xA4] = 5;
}

void func_1502EA60(u8 *arg0, s32 arg1) {
    arg0[0xA4] = 2;
    arg0[0xA5] = 0xFF;
    arg0[0xA6] = arg1;
}

void func_1502EA7C(u8 *arg0, s32 arg1) {
    arg0[0xA4] = 3;
    arg0[0xA5] = 0xFF;
    arg0[0xA6] = arg1;
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_58F80/func_1502EA98.s")

s32 func_1502EAFC() {
    return 0;
}

s32 func_1502EC34() {
    return 0;
}

s32 func_1502EE8C(s32 arg0, s32 arg1) {
    s32 value = D_800CC33A[arg0 * 0x32C + arg1];
    s32 result;

    if (value < 2) {
        result = value;
    } else if (value < 4) {
        result = value - 2;
    } else {
        result = 2;
    }
    return result;
}

s32 func_1502EEF4() {
    return 0;
}

s32 func_1502F01C() {
    return 0;
}

s32 func_1502F264() {
    return 0;
}

s32 func_1502F3C8() {
    return 0;
}

s32 func_1502F490() {
    return 0;
}

s32 func_1502F948() {
    return 0;
}

s32 func_1502F9FC() {
    return 0;
}

s32 func_1502FBE8() {
    return 0;
}

// Matched with guarded sentinel allocation and fallback scheduling.
void func_1502FD70(u8 *arg0) {
    u8 index = arg0[4];
    u8 *state;
    s32 state_value;
    u8 *object;
    s32 object_value;
    s32 sentinel;
    s32 scaled;

    if ((D_80038080 == 0) && (D_800BE9F0 == 0x1D)) {
        D_800D2040[index] = 2;
        return;
    }

    state = &D_800D2040[index];
    state_value = *state;
    sentinel = 0xFF;
    if (state_value != sentinel) {
        object = *(u8 **)(arg0 + 0x144);
        if (object == NULL) {
            scaled = 3;
        } else {
            object_value = object[0x2E];
            if (object_value == sentinel) {
                return;
            }
            if (object_value == 0) {
                scaled = 3;
            } else {
                scaled = object_value * 30;
                if (state_value < scaled) {
                    *state = scaled;
                    return;
                }
                return;
            }
        }
        *state = scaled;
    }
}
