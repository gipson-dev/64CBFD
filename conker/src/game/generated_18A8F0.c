#include <ultra64.h>
extern void (*D_8008B0C0[])();
extern s32 D_800DCD7C;
extern u8 D_800DCD20[];
extern u8 D_800DCD27;
extern void (*D_8008B090[])();
extern u8 *D_800DCD78;
extern f32 D_800A6520;
extern f32 D_800A6524;
extern s32 D_800DCD10[];
extern u8 D_800CC2D0[];

/* Non-matching placeholders for the text-only asm slice asm/18A8F0.s. */

s32 func_1515D5F8();
f32 func_1515F008(u8 *arg0, s32 arg1);
void func_1515F040(f32 arg0, s32 arg1);
void func_1515F0AC(f32 arg0, s32 arg1);

u8 *func_1515D440(void) {
    u8 *temp_v0 = (u8 *) allocate_memory(0x10, 1, 2, 0);

    bzero(temp_v0, 0x10);
    return temp_v0;
}

u8 *func_1515D480(s32 arg0) {
    s32 size = arg0 * 0x60;
    u8 *temp_v0 = (u8 *) allocate_memory(size, 1, 2, 0);

    bzero(temp_v0, size);
    return temp_v0;
}

void func_1515D4D4(s32 arg0, s32 arg1, s32 arg2, u8 arg3) {
    if (arg3 >= D_800DCD27) {
        D_800DCD20[0] = arg0;
        D_800DCD20[1] = arg1;
        D_800DCD20[2] = arg2;
        D_800DCD7C = 1;
        D_800DCD27 = arg3;
    }
}

u8 *func_1515D520(void) {
    u8 *node = (u8 *) allocate_memory(0x34, 1, 2, 2);
    u8 *ptr;
    u8 *prev;

    if (node != 0) {
        bzero(node, 0x34);
        ptr = D_800DCD78;
        if (ptr == 0) {
            D_800DCD78 = node;
        } else {
            prev = ptr;
            ptr = *(u8 **) ptr;
            if (ptr != 0) {
                do {
                    prev = ptr;
                    ptr = *(u8 **) ptr;
                } while (ptr != 0);
            }
            *(u8 **) prev = node;
        }
        *(u8 **) node = 0;
    }
    return node;
}

void func_1515D5AC(s32 arg0, s32 arg1, s32 arg2, s32 arg3, s32 arg4, s32 arg5, s32 arg6, s32 arg7, s32 arg8, u8 arg9) {
    func_1515D5F8(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9);
}

s32 func_1515D5F8() {
    return 0;
}

void func_1515D69C(void) {
    u8 *ptr = D_800DCD78;

    if (ptr != 0) {
        do {
            ptr[0xC] = 0;
            ptr[0x30] = 0;
            ptr = *(u8 **) ptr;
        } while (ptr != 0);
    }
}

void func_1515D6C8() {
}

s32 func_1515D6D0() {
    return 0;
}

s32 func_1515D914() {
    return 0;
}

s32 func_1515E278() {
    return 0;
}

s32 func_1515E43C() {
    return 0;
}

s32 func_1515E544() {
    return 0;
}

s32 func_1515E888() {
    return 0;
}

s32 func_1515EB84() {
    return 0;
}

s32 func_1515EC78() {
    return 0;
}

void func_1515EF74(u8 *arg0) {
    func_1515F040(1.0f / func_1515F008(arg0, 0), 0);
    func_1515F040(1.0f / func_1515F008(arg0, 5), 1);
    func_1515F040(1.0f / func_1515F008(arg0, 10), 2);
    func_1515F0AC(-func_1515F008(arg0, 14), 3);
}

f32 func_1515F008(u8 *arg0, s32 arg1) {
    s32 temp_v0;
    u8 *temp_v1 = arg0 + arg1 * 2;

    temp_v0 = *(s16 *) temp_v1;
    temp_v0 = *(u16 *) (temp_v1 + 0x20) | (temp_v0 << 16);
    return temp_v0 * 1.52587890625e-05f;
}

void func_1515F040(f32 arg0, s32 arg1) {
}

void func_1515F0AC(f32 arg0, s32 arg1) {
}

void func_1515F10C(u8 *arg0) {
    u8 *node = D_800DCD78;
    u8 *prev = 0;

    if (node != arg0) {
        do {
            prev = node;
            node = *(u8 **) node;
        } while (node != arg0);
    }
    if (prev != 0) {
        *(u8 **) prev = *(u8 **) node;
    } else {
        D_800DCD78 = *(u8 **) node;
    }
    func_10004074(node);
}

void func_1515F170(s32 arg0, u8 arg1) {
    u8 *ptr = D_800DCD78;

    if (ptr != 0) {
        do {
            if (arg0 == *(ptr + 0xB)) {
                *(ptr + 9) = arg1;
            }
            ptr = *(u8 **) ptr;
        } while (ptr != 0);
    }
}

s32 func_1515F1B0() {
    return 0;
}

void func_1515F25C(u8 **arg0, u8 *arg1) {
    *(u8 **)(arg1 + 0xC) = *arg0;
    *arg0 = arg1;
}

void func_1515F270(u8 *arg0, u8 *arg1) {
    s32 idx = *(s32 *) (arg1 + 0x18);

    if (idx >= 0) {
        if (idx < 0xC) {
            if (D_8008B090[idx] != 0) {
                D_8008B090[idx](arg0, arg1);
            }
        }
    }
}

void func_1515F2B8(u8 *arg0, s32 arg1) {
    func_1505D024(arg0, 0x6001D, *(u16 *) (arg0 + 0x7A), -1);
}

void func_1515F2E8(u8 *arg0, u8 *arg1) {
    if (*(arg0 + 0x3B) == 1) {
        s32 idx = *(s32 *) (arg1 + 0x1C);

        if (idx >= 0) {
            if (idx < 3) {
                D_8008B0C0[idx]();
            }
        }
    }
}

s32 func_1515F338() {
    return 0;
}

s32 func_1515F5C4() {
    return 0;
}

s32 func_1515F850() {
    return 0;
}

s32 func_1515FB70(u8 *arg0, u8 *arg1) {
    s32 t;
    if (*(arg0 + 0x3B) != 1) {
        return;
    }
    t = *(s32 *) (arg1 + 0x1C);
    if (t >= 0) {
    }
}

void func_1515FB94(u8 *arg0, s32 arg1) {
    func_1505D024(arg0, 0x6002D, *(u16 *) (arg0 + 0x7A), -1);
}

void func_1515FBC4(u8 *arg0, s32 arg1) {
    s32 index;
    s32 temp_v1 = 0;
    s32 temp_v0 = func_15105C24(arg1);

    if (temp_v0 != 0) {
        temp_v1 = *(s32 *) (temp_v0 + 0x98);
    }
    if (temp_v1 != 0) {
        index = (temp_v1 - (s32) D_800CC2D0) / 0x32C;
    } else {
        index = -1;
    }
    func_1505D024(arg0, 0x6002E, *(u16 *) (arg0 + 0x7A), index);
}

void func_1515FC34(s32 arg0, u8 arg1) {
    func_1505D024(arg0, 0x33, 0xC000, -1);
}

s32 func_1515FC60() {
    return 0;
}
