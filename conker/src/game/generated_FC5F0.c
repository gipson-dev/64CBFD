#include <ultra64.h>
void func_151CF898(u8 *, f32, f32);
extern u8 D_800CC2D0[];
void *memcpy(void *dst, const void *src, unsigned int len);
extern s32 D_80088890;
extern s32 D_80088894;
extern s32 D_80088898;
extern s32 D_800BE9E4;
extern s32 (*D_800888A0[])(u8 *arg0);
extern s32 (*D_800888B0[])(u8 *arg0, u8 *arg1, u8 arg2);

/* Non-matching placeholders for the text-only asm slice asm/FC5F0.s. */

s32 func_150CF140() {
    return 0;
}

s32 func_150CF484() {
    return 0;
}

void func_150CF530(s32 arg0) {
    func_151CF898(D_800CC2D0, *(f32 *) (D_800CC2D0 + 0x18) + 300.0f, -10000.0f);
}

void func_150CF578(s32 arg0) {
    s32 temp = D_800BE9E4 * 28;

    D_80088890 += D_800BE9E4 * 26;
    D_80088894 -= temp;
    D_80088898 -= temp;
}

s32 func_150CF5E8() {
    return 0;
}

s32 func_150CF680() {
    return 0;
}

s32 func_150CF800() {
    return 0;
}

void func_150CFBEC(u8 *arg0, f32 *arg1, u8 arg2) {
    if (arg2 == 0x52) {
        u8 *temp_v0 = arg0 + 0x70;

        *temp_v0 |= 1;
        *(f32 *) (temp_v0 + 4) = 0.0f;
        *(f32 *) (temp_v0 + 8) = *(f32 *) (arg0 + 0x10);
        *(f32 *) (temp_v0 + 0xC) = *arg1 - *(f32 *) (arg0 + 0x10);
    }
}

s32 func_150CFC38(f32 arg0) {
    f32 value = arg0;

    func_1515572C(&value, 0x52);
}

s32 func_150CFC60() {
    return 0;
}

u8 *func_150CFD20(u8 *arg0) {
    if (*arg0 != 0xBD && *arg0 != 0) {
        do {
            arg0++;
        } while (*arg0 != 0xBD && *arg0 != 0);
    }
    return arg0;
}

u8 *func_150CFD5C(u8 *arg0) {
    if (*arg0 != 0) {
        do {
            arg0++;
        } while (*arg0 != 0);
    }
    return arg0;
}

s32 func_150CFD84(u8 *arg0, u8 **arg1) {
    u8 *end = (u8 *) func_150CFD20(arg0);

    *arg1 = end;
    return end - arg0;
}

s32 func_150CFDB8(u8 *arg0) {
    u8 *end = func_150CFD5C(arg0);
    u8 *p = arg0;
    s32 max = 0;

    if (p < end) {
        do {
            u8 *next;
            s32 len = func_150CFD84(p, &next);

            if (max < len) {
                max = len;
            }
            p = next + 1;
        } while (p < end);
    }
    return max;
}

void func_150CFE3C(u8 *arg0) {
    u8 idx = *(arg0 + 0x3D);
    void *src = *(void **) (arg0 + 0x34);
    u8 size = *(arg0 + 0x3C);
    void *dst = *(void **) (arg0 + idx * 4 + 0x40);

    memcpy(dst, src, size);
    idx = *(arg0 + 0x28 + 0x15);
    size = *(arg0 + 0x28 + 0x14);
    *(u8 *) (*(u8 **) (arg0 + 0x28 + idx * 4 + 0x18) + size) = 0;
}

void func_150CFE98(u8 *arg0) {
    u8 *sub = arg0 + 0x28;
    u8 *ptr38 = *(u8 **) (arg0 + 0x38);

    if (*ptr38 != 0) {
        u8 *field10 = *(u8 **) (sub + 0x10);
        s32 len;

        *(u8 **) (sub + 0xC) = field10 + 1;
        len = func_150CFD84(field10 + 1, (u8 **) (sub + 0x10));
        *(sub + 0x14) = (u8) len;
        *(sub + 0x15) ^= 1;
        func_150CFE3C(arg0);
        *(sub + 0x8) |= 1;
    }
}

s32 func_150CFF10() {
    return 0;
}

s32 func_150D0034(u8 *arg0, u8 *arg1, s32 arg2) {
    u8 *sub;

    if (*(s8 *) (arg1 + 0x4C) == -1) {
        sub = arg1 + 0x28;
    } else {
        s32 (*fn)(u8 *) = D_800888A0[*(s8 *) (arg1 + 0x4C)];

        if (fn(arg1) == 0) {
            *(s16 *) (arg1 + 0xE) = -1;
            return (s32) arg0;
        }
        sub = arg1 + 0x28;
    }
    *(sub + 8) &= 0xFE;
    return (s32) arg0;
}

void func_150D00C0(u8 *arg0, u8 *arg1, u8 arg2) {
    if (arg2 == 0x51) {
        if (*(arg0 + 0x28) == *arg1) {
            func_150CFE98(arg0);
        }
    } else {
        s32 (*fn)(u8 *, u8 *, u8) = D_800888B0[*(arg0 + 0x4D)];

        if (fn != 0) {
            fn(arg0, arg1, arg2);
        }
    }
}

void func_150D0134(u8 arg0, s32 arg1, s32 arg2, u8 arg3, s32 arg4) {
    u8 zero = 0;
    void *result = func_150CFF10(arg0, arg1, (s16) arg2, 8, 0, 0, arg3, arg4);

    if (result != 0) {
        memcpy(*(void **) ((u8 *) result + 0x48), &zero, 1);
    }
}

s32 func_150D01A0() {
    return 0;
}

void func_150D02B4(u8 arg0, s32 arg1, s32 arg2, u8 arg3, s32 arg4) {
    struct { f32 word0; s16 half0; } rec;
    void *result;

    rec.word0 = 0.0f;
    rec.half0 = 0;
    result = func_150CFF10(arg0, arg1, (s16) arg2, 8, 1, 0, arg3, arg4);
    if (result != 0) {
        memcpy(*(void **) ((u8 *) result + 0x48), &rec, 8);
    }
}

s32 func_150D032C() {
    return 0;
}

void func_150D04C4(u8 arg0, s32 arg1, s32 arg2, u8 arg3, s32 arg4) {
    u8 zero = 0;
    void *result = func_150CFF10(arg0, arg1, (s16) arg2, 8, 2, 0, arg3, arg4);

    if (result != 0) {
        memcpy(*(void **) ((u8 *) result + 0x48), &zero, 1);
    }
}

s32 func_150D0534() {
    return 0;
}
