#include <ultra64.h>
extern u8 D_800CC2D0[];
void func_151B47D8(u8 *, u8 *, s32, u8);
void func_1516972C(u8 *);

/* Non-matching placeholders for the text-only asm slice asm/1DF510.s. */

void func_151B222C(u8 *);

s32 func_151B2060() {
    return 0;
}

s32 func_151B2100() {
    return 0;
}

void func_151B220C(u8 *arg0) {
    func_151B222C(arg0);
}

void func_151B222C(u8 *arg0) {
    u8 *base = arg0 + 0x28;
    s32 i;
    u8 *entry;

    i = 0;
    do {
        entry = *(u8 **)(base + 0x10 + i * 4);
        if (entry != NULL) {
            func_1516972C(entry);
        }
        i = (u8)(i + 1);
    } while (i < 3);

    entry = *(u8 **)(base + 0x1C);
    if (entry != NULL) {
        func_1516972C(entry);
    }
}

s32 func_151B229C(s32 arg0) {
    func_151B220C(arg0);
    func_1514933C(arg0);
}

s32 func_151B22C8(s32 arg0) {
    func_151B220C(arg0);
    func_15149368(arg0);
}

s32 func_151B22F4(u8 *arg0) {
    s32 temp_v0 = *(s32 *)(arg0 + 0x28);
    u8 *temp_v1 = *(u8 **)(arg0 + 0x30);

    if ((((temp_v0 - (s32)D_800CC2D0) / 0x32C) + 1 == temp_v1[0x65]) &&
        (*(s32 *)(temp_v1 + 0x5C) == 1)) {
        return 1;
    }
    return 2;
}

s32 func_151B2348() {
    return 0;
}

s32 func_151B2690() {
    return 0;
}

void func_151B2950(u8 *arg0) {
    u8 *temp_v0 = *(u8 **)(arg0 + 0x178);

    if (temp_v0 != NULL) {
        *(s32 *)(temp_v0 + (*(u8 *)(arg0 + 0x17C) * 4) + 0x38) = 0;
    }
}

s32 func_151B2974() {
    return 0;
}

void func_151B2EC4(u8 *arg0, s32 arg1, u8 arg2) {
    func_15169850(arg1, arg2, (s32) (arg0 + 0x28), (s32) (arg0 + 0x2C), (s32) arg0);
}

void func_151B2F04(u8 *owner, u8 *packet, u8 kind) {
    u8 *pair = owner + 0x28;

    if (kind == 0x2D) {
        if (*(s32 *)packet == *(s32 *)pair) {
            *(s32 *)pair = *(s32 *)(packet + 4);
            pair[4] = packet[9];
        } else if (*(s32 *)(packet + 4) == *(s32 *)pair) {
            *(s32 *)pair = *(s32 *)packet;
            pair[4] = packet[8];
        }
        if (*(s32 *)packet == *(s32 *)(pair + 8)) {
            *(s32 *)(pair + 8) = *(s32 *)(packet + 4);
            pair[12] = packet[9];
        } else if (*(s32 *)(packet + 4) == *(s32 *)(pair + 8)) {
            *(s32 *)(pair + 8) = *(s32 *)packet;
            pair[12] = packet[8];
        }
    }
}

void func_151B2FA0(u8 *arg0, s32 arg1, u8 arg2) {
    func_151B47D8(arg0, arg0 + 0x150, arg1, arg2);
}

void func_151B2FD0(u8 *arg0) {
    u8 *temp_v0 = *(u8 **)(arg0 + 0x4C);

    if (temp_v0 != NULL) {
        *(s32 *)(temp_v0 + 0x44) = 0;
    }
}

s32 func_151B2FE8(s32 arg0) {
    func_151B2FD0(arg0);
    func_1514933C(arg0);
}

s32 func_151B3014(s32 arg0) {
    func_151B2FD0(arg0);
    func_15149368(arg0);
}

void func_151B3040(u8 *arg0, s32 arg1, volatile u8 arg2) {
    u8 *base = arg0 + 0x150;

    func_15169850(arg1, arg2, (s32) base, (s32) (base + 4), (s32) arg0);
    func_15169850(arg1, arg2, (s32) (base + 0x14), (s32) (base + 0x18), (s32) arg0);
}
