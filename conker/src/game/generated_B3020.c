#include <ultra64.h>
extern u8 *D_800D23C0;
extern u32 D_80087380;
extern s16 D_80087290;
extern u8 *D_800D2350;
extern u8 *D_8008FDD4;
extern s8 D_8008FD90;
extern u8 *D_800872A0;

/* Non-matching placeholders for the text-only asm slice asm/B3020.s. */

extern s32 D_800D23B0;
extern u8 D_800CC40F[];
extern s16 D_80087294;
extern f32 D_800D2360[];
extern u8 D_800D237C[];
extern u8 D_800CC2D0[];
extern s32 D_800D2394;
extern s8 D_800D2398;
extern s8 D_800D2399;
s32 func_1502B5C8();
s32 func_1509BFB0();
s32 func_15085BE8();
s32 func_150888A8();

s32 func_15085B70(s32 arg0) {
    s16 *temp_v0 = (s16 *) func_1502B5C8(0, 2, 0x19, arg0);

    if (temp_v0 != 0) {
        D_80087290 = temp_v0[0];
        D_80087294 = temp_v0[1];
        D_800D2350 = (u8 *) temp_v0 + 4;
    } else {
        D_80087290 = 0;
        D_80087294 = 0;
        D_800D2350 = 0;
    }
    return func_15085BE8();
}

s32 func_15085BE8() {
    return 0;
}

s32 func_15085DA8(f32 arg0) {
    s32 i = 0;

    if (D_800D2360[0] <= arg0) {
        do {
            i++;
        } while (D_800D2360[i] <= arg0);
    }
    return D_800D237C[i];
}

s32 func_15085DF8() {
    return 0;
}

s32 func_15086098() {
    return 0;
}

s32 func_15086364() {
    return 0;
}

s32 func_15086BD0() {
    return 0;
}

void func_15086C70(arg0)
s32 arg0;
{
    u8 *temp_v0 = (u8 *) ((s32) D_800D2350 + arg0 * 16);
    s32 temp_v1 = *(s16 *) (temp_v0 + 4);

    func_150A3194(3, 0xB, *(s16 *) temp_v0, *(s16 *) (temp_v0 + 2), temp_v1);
}

s32 func_15086CBC(s32 arg0, f32 *arg1, f32 *arg2, f32 *arg3) {
    s32 offset;

    if (arg0 < 0 || arg0 >= D_80087290) {
        return 0;
    }
    offset = arg0 * 16;
    *arg1 = (f32) *(s16 *) (D_800D2350 + offset);
    *arg2 = (f32) *(s16 *) (D_800D2350 + offset + 2);
    *arg3 = (f32) *(s16 *) (D_800D2350 + offset + 4);
    return 1;
}

s32 func_15086D48(s32 arg0) {
    s32 temp_v0 = *(s16 *) &D_80087290;
    s32 i = 0;

    if (temp_v0 > 0) {
        u8 *ptr = D_800D2350;

        do {
            if (arg0 == *(ptr + 7)) {
                return i;
            }
            i += 1;
            ptr += 0x10;
        } while (i < temp_v0);
    }
    return 0xFF;
}

s32 func_15086D94() {
    return 0;
}

s32 func_150870D0() {
    return 0;
}

s32 func_15087350() {
    return 0;
}

s32 func_15087CC0() {
    return 0;
}

void func_15087DCC(s32 arg0, s32 arg1) {
    u8 *rec = D_800872A0;
    s32 value;

    if (rec == 0) {
        return;
    }
    rec = (u8 *) (arg0 * 0x84 + (s32) rec);
    if (*(s8 *) (rec + 0x2F) == arg1) {
        return;
    }
    if (arg1 != 0) {
        value = func_150888A8(rec[0x2B], rec[0x2C], 1);
        rec[0x2D] = value;
        value = func_150888A8(rec[0x2C], value & 0xFF, 1);
        rec[0x2E] = value;
    }
    rec[0x2F] = arg1;
}

s32 func_15087E54() {
    return 0;
}

s32 func_15087EF0() {
    return 0;
}

void func_15087FC4(s32 arg0, s32 arg1) {
    u8 *temp_v0 = D_800872A0;

    if (temp_v0 != 0) {
        *(u8 *) (arg0 * 0x84 + (s32) temp_v0 + 0x31) = arg1;
    }
}

void func_15087FEC(s32 arg0, s32 arg1) {
    u8 *temp_v0 = D_800872A0;

    if (temp_v0 != 0) {
        *(f32 *) (arg0 * 0x84 + (s32) temp_v0 + 4) = arg1 * 0.00390625f;
    }
}

s32 func_1508802C() {
    return 0;
}

s32 func_150880F8() {
    return 0;
}

s32 func_150881CC(s32 arg0) {
    u8 *temp_v1 = D_800872A0;
    u8 *ptr;

    if (temp_v1 == 0) {
        return 0;
    }
    ptr = (u8 *) (arg0 * 0x84 + (s32) temp_v1);
    return (s32) (*(f32 *) ptr * 256.0f);
}

s32 func_15088218(s32 arg0) {
    u8 *temp_v1 = D_800872A0;
    u8 *ptr;

    if (temp_v1 == 0) {
        return 0;
    }
    ptr = (u8 *) (arg0 * 0x84 + (s32) temp_v1);
    return (*(s16 *) (ptr + 0x24) << 4) + (s32) (*(f32 *) (ptr + 8) * 16.0f);
}

s32 func_15088270(s32 arg0) {
    u8 *temp_v1 = D_800872A0;
    u8 *ptr;

    if (temp_v1 == 0) {
        return 0;
    }
    ptr = (u8 *) (arg0 * 0x84 + (s32) temp_v1);
    return (s32) *(f32 *) (ptr + 0x14);
}

s32 func_150882B0(s32 arg0) {
    s32 idx = arg0;
    u8 *temp_v1 = D_800872A0;
    u8 *ptr;

    if (temp_v1 == 0) {
        return 0;
    }
    ptr = (u8 *) (idx * 0x84 + (s32) temp_v1);
    return *(s8 *) (ptr + 0x27);
}

s32 func_150882E4() {
    return 0;
}

s32 func_150883B0() {
    return 0;
}

s32 func_1508855C(s32 arg0) {
    u8 *temp_v1 = D_800872A0;
    s32 idx;
    s32 count;
    u8 *rec;
    s32 i;

    if (temp_v1 == 0) {
        return -1;
    }
    idx = (arg0 - (s32) D_800CC2D0) / 0x32C;
    if (idx == 0) {
        return 0;
    }
    count = D_800D2398 + D_800D2399;
    if (count < 2) {
        return -1;
    }
    rec = temp_v1 + 0x84;
    i = 1;
    do {
        if (*(s8 *) (rec + 0x31) == idx) {
            return i;
        }
        i += 1;
        rec += 0x84;
    } while (i < count);
    return -1;
}

s32 func_150885EC() {
    return 0;
}

s32 func_1508868C() {
    return 0;
}

void func_15088780(s32 arg0) {
    s32 idx;
    u8 *rec;

    if (D_800872A0 == 0) {
        return;
    }
    idx = func_1508855C(arg0);
    rec = (u8 *) (idx * 0x84 + (s32) D_800872A0);
    rec[0x31] = 0;
    D_800D2394 &= ~(1 << (idx - D_800D2398));
}

s32 func_150887F8(void) {
    u8 *temp_v1 = D_800872A0;

    if (temp_v1 == 0) {
        return 0;
    }
    return temp_v1[0x46] == 0xFF;
}

void func_15088824(u8 *arg0) {
    arg0[0x2B] = 0;
    arg0[0x2C] = 0;
    arg0[0x2D] = 0;
    arg0[0x2E] = 0;
    arg0[0x28] = 0;
    *(s32 *) (arg0 + 0x1C) = 0;
    *(s32 *) (arg0 + 0x18) = 0;
    *(s32 *) (arg0 + 0x20) = -1;
    arg0[0x2F] = 0;
    *(f32 *) (arg0 + 0x8) = 0.0f;
    *(f32 *) (arg0 + 0x0) = 0.5f;
    *(f32 *) (arg0 + 0x4) = 0.5f;
    *(s16 *) (arg0 + 0x24) = 0;
    arg0[0x26] = 0;
    arg0[0x27] = 0;
    arg0[0x31] = 0;
    *(f32 *) (arg0 + 0xC) = 0.0f;
    *(f32 *) (arg0 + 0x14) = 0.0f;
    arg0[0x33] = 2;
    arg0[0x30] = 0;
    arg0[0x2A] = 0x7F;
    arg0[0x49] = 0;
    *(f32 *) (arg0 + 0x10) = 1.0f;
}

s32 func_150888A8() {
    return 0;
}

s32 func_15088A08() {
    return 0;
}

s32 func_15088D58() {
    return 0;
}

s32 func_15088F30() {
    return 0;
}

s32 func_1508907C() {
    return 0;
}

s32 func_150891E8() {
    return 0;
}

s32 func_150896EC() {
    return 0;
}

void func_15089BB0() {
    D_800D23B0 = 0;
}

s32 func_15089BC0() {
    return 0;
}

s32 func_15089F9C() {
    return 0;
}

s32 func_1508A1BC() {
    return 0;
}

s32 func_1508A6FC() {
    return 0;
}

s32 func_1508B194(s32 arg0) {
    if (arg0 < D_8008FD90) {
        return *(s16 *) (D_8008FDD4 + arg0 * 12 + 0x70);
    }
    return 0;
}

void func_1508B1D4(s32 arg0) {
    if (arg0 < D_8008FD90) {
        *(u16 *) (D_8008FDD4 + arg0 * 12 + 0x70) = 0;
    }
}

s32 func_1508B20C() {
    return 0;
}

s32 func_1508B2A8() {
    return 0;
}

s32 func_1508B3F8() {
    return 0;
}

s32 func_1508B9BC() {
    return 0;
}

s32 func_1508BC20() {
    return 0;
}

s32 func_1508BF14() {
    return 0;
}

s32 func_1508C194(s32 arg0) {
    return 0;
}

s32 func_1508C1A4() {
    return 0;
}

s32 func_1508C5B8() {
    return 0;
}

s32 func_1508C9CC() {
    return 0;
}

s32 func_1508CA88() {
    u8 *ptr = (u8 *) D_800D23B0;

    ptr[0x1703] += 1;
    ptr = (u8 *) D_800D23B0;
    if (*(s8 *) (ptr + 0x1703) < D_8008FD90) {
        return *(s8 *) (ptr + 0x1703);
    }
    ptr[0x1703] = 0;
    ptr = (u8 *) D_800D23B0;
    return *(s8 *) (ptr + 0x1703);
}

s32 func_1508CAD8() {
    return 0;
}

s32 func_1508D850() {
    return 0;
}

s32 func_1508DA1C() {
    return 0;
}

s32 func_1508DAEC() {
    return 0;
}

s32 func_1508DC24() {
    return 0;
}

void func_1508E6C8() {
}

s32 func_1508E6D0() {
    return 0;
}

s32 func_1508E780() {
    return 0;
}

s32 func_1508E89C() {
    return 0;
}

s32 func_1508EB90(s32 arg0, s32 arg1, s32 arg2) {
    s32 temp_v0 = D_800CC40F[arg0 * 0x32C];

    return func_1509BFB0(1, temp_v0 | 0x2000, arg1, arg2);
}

void func_1508EBF8(s32 arg0, s32 arg1) {
    s32 temp_v0 = D_800CC40F[arg0 * 0x32C];

    func_1509BFB0(1, temp_v0 | 0x2000, 0x14, arg1);
}

void func_1508EC5C(s32 arg0, s32 arg1) {
    s32 temp_v0 = D_800CC40F[arg0 * 0x32C];

    func_1509BFB0(1, temp_v0 | 0x2000, 0x61, arg1);
}

s32 func_1508ECC0() {
    return 0;
}

void func_1508EDBC(u32 arg0) {
    if (arg0 < D_80087380) {
        s32 off = arg0 * 24;

        *(u16 *) (D_800D23C0 + off + 2) = 0;
        *(u32 *) (D_800D23C0 + off + 4) = 0;
        *(u16 *) (D_800D23C0 + off) = 0;
    }
}

s32 func_1508EE0C() {
    return 0;
}
