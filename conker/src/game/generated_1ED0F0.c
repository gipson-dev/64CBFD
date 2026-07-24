#include <ultra64.h>

void func_151D5334(u8 *arg0, f32 arg1, f32 arg2, f32 arg3, s32 arg4, s32 arg5, s32 arg6);
void func_151D5404(u8 *arg0, f32 arg1, f32 arg2, f32 arg3, s32 arg4, s32 arg5, s32 arg6, s32 arg7);

extern u8 D_800AA954[];
extern u8 D_800AA958[][12];

/* Non-matching placeholders for the text-only asm slice asm/1ED0F0.s. */

s32 func_151BFC40() {
    return 0;
}

s32 func_151BFDA0() {
    return 0;
}

s32 func_151BFE84() {
    return 0;
}

s32 func_151C0098() {
    return 0;
}

s32 func_151C02E4(s32 arg0, s32 arg1, s32 arg2, s32 *arg3) {
    u8 i = 0;

    if (arg2 > 0) {
        do {
            if (arg0 == arg3[i]) {
                return 0;
            }
            i++;
        } while (i < arg2);
    }
    if (arg0 == arg1) {
        return 0;
    }
    if (*(s32 *) arg0 == 0) {
        return 0;
    }
    if (*(u8 *) (arg0 + 4) == 0xFF) {
        return 0;
    }
    return 1;
}

s32 func_151C0360() {
    return 0;
}

s32 func_151C0418() {
    return 0;
}

s32 func_151C04F8() {
    return 0;
}

void func_151C05A4(u8 *arg0, s32 arg1, s32 arg2) {
    func_151D5334(arg0, 800.0f, 2000.0f, 0.0005f, 5, (u8) arg1, arg2);
}

void func_151C05F0(u8 *arg0, s32 arg1, s32 arg2) {
    func_151D5404(arg0, 800.0f, 2000.0f, 0.0005f, 15, 20, (u8) arg1, arg2);
}

void func_151C0644(u8 *arg0, s32 arg1, s32 arg2) {
    func_150E83AC(arg0, (s16) ((func_150ADA20() % 62U) + 120), (u8) arg1, arg2);
}

s32 func_151C0698() {
    return 0;
}

void func_151C110C(u8 *arg0, s32 arg1, u8 *arg2, s32 arg3, s32 arg4, s32 arg5, u8 *arg6) {
    u8 *temp_v1 = *(u8 **) (arg0 + 0x18);

    if (temp_v1 != 0 && *(s32 *) arg2 != 0) {
        *(s16 *) (arg0 + 2) = (s32) *(f32 *) (temp_v1 + 0x38);
        *(s16 *) (arg0 + 4) = (s32) *(f32 *) (temp_v1 + 0x3C);
        *(s16 *) (arg0 + 6) = (s32) *(f32 *) (temp_v1 + 0x40);
        return;
    }
    *(s16 *) arg6 = 0;
}

s32 func_151C1180() {
    return 0;
}

void func_151C1570(u8 *arg0) {
    u8 *temp_v0;
    s32 temp;

    temp = *(s32 *) (arg0 + 0x1F0);
    if (temp != 0) {
        func_1516972C(temp);
    }
    temp = *(s32 *) (arg0 + 0x1F4);
    temp_v0 = arg0 + 0x170;
    if (temp != 0) {
        func_1516972C(temp);
    }
    temp = *(s32 *) (temp_v0 + 0x88);
    if (temp != 0) {
        *(s32 *) (temp + 0x110) = 0;
    }
    temp = *(s32 *) (temp_v0 + 0x8C);
    if (temp != 0) {
        func_1516972C(temp);
    }
    func_1000FD38(func_151C110C, arg0, 0);
}

s32 func_151C15FC(s32 arg0) {
    func_151C1570(arg0);
    func_15132570(arg0);
}

s32 func_151C1628(s32 arg0) {
    func_151C1570(arg0);
    func_1513259C(arg0);
}

s32 func_151C1654() {
    return 0;
}

s32 func_151C1798(u8 *arg0, s32 arg1) {
    u8 tag = *(u8 *) (arg0 + 4);
    s32 v0;

    if (tag == 0x28) {
        v0 = 2;
    } else if (tag == 0x77) {
        v0 = 1;
    } else {
        v0 = 0;
    }
    return func_15143134(D_800AA958[v0], arg1, (D_800AA954[v0] * 64) + *(s32 *) (arg0 + 0x1D4));
}

void func_151C1814(u8 *arg0, s32 *arg1, u8 arg2) {
    u8 *temp_v0 = arg0 + 0x170;

    if (arg2 == 0x2D) {
        s32 temp_v1 = arg1[0];
        s32 temp_a2 = *(s32 *) (temp_v0 + 0x6C);

        if (temp_v1 == temp_a2) {
            *(s32 *) (temp_v0 + 0x6C) = arg1[1];
            return;
        }
        if (temp_a2 == arg1[1]) {
            *(s32 *) (temp_v0 + 0x6C) = temp_v1;
        }
    }
}

s32 func_151C1860() {
    return 0;
}

void func_151C1940(s32 arg0, s32 arg1, s32 *arg2) {
    func_151C02E4(arg0, arg1, arg2[0], &arg2[1]);
}

s32 func_151C196C() {
    return 0;
}

s32 func_151C1D5C() {
    return 0;
}

s32 func_151C1FB8() {
    return 0;
}
