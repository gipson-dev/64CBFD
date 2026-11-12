#include <ultra64.h>
#include "structs.h"
extern s32 D_800BE9E4, D_800BEA08;
extern u8 D_800BEA0C;
void func_100176C4(void);
void func_10010F30(s32, u16, u8, s16, u8);
void func_1000E2F4(s32);
void func_151254F4(struct108 *, s32);
void func_151D66F0(s32, s32);
void func_1516972C(struct102 *);
extern u8 *D_800CC5EC;
Gfx *func_1517F08C(Gfx *, s32, s32, s32, s32, s32);
void *func_15167A68(s32, s32, s32, s32, u8, u8);

/* Non-matching placeholders for the text-only asm slice asm/131620.s. */

void func_15104170(s32 arg0, s32 arg1, s32 arg2) {
    u8 *temp_v0 = func_15167A68(0x64, 0, 0x20, 0, 0xFF, 1);

    if (temp_v0 != NULL) {
        *(s16 *) (temp_v0 + 0x18) = 0xF;
        temp_v0[0x1A] = 0;
        temp_v0[0x1B] = 0;
        *(s32 *) (temp_v0 + 0x10) = arg1;
        *(s32 *) (temp_v0 + 0x14) = arg2;
        temp_v0[0x1C] = arg0;
    }
}
/* Advance the type-0x64 timer, fade, and release states. */
void func_151041E4(u8 *record) {
    u8 padding[16]; /* Preserve the retail frame; original use is unknown. */
    f32 height;
    u8 *actor;
    u8 *other;
    u8 *owner;
    s32 value;

    switch (record[0x1A]) {
    case 0: {
        s32 trigger;
        owner = *(u8 **)(record + 0x10);
        actor = *(u8 **)(owner + 0x2D0);
        height = *(volatile f32 *)(actor + 8);
        trigger = 0;
        if (record[0x1C] == 0) {
            if (height >= 19.0f) trigger = 1;
        } else if (record[0x1C] == 1) {
            if (D_800BE9E4 < *(u16 *)(record + 0x18)) {
                *(u16 *)(record + 0x18) = (u16)((u32)*(u16 *)(record + 0x18) - (u32)D_800BE9E4);
            } else trigger = 1;
        }
        if (trigger) {
            other = *(u8 **)(record + 0x14);
            owner = *(u8 **)(record + 0x10);
            record[0x1A] = 1;
            D_800BEA0C = 1;
            func_100176C4();
            func_10010F30(0x5B2, 0x7FFF, 0, 0, 0);
            func_10010F30(0x5B2, 0x7FFF, 0x7F, -100, 0);
            func_10010F30(0x5B2, 0x7FFF, 0, 0, 0);
            func_10010F30(0x5B2, 0x7FFF, 0x7F, -100, 0);
            func_151D66F0(0xD2, 2);
            func_151254F4(*(struct108 **)(owner + 0x318), other[0x13F]);
            *(f32 *)(*(u8 **)(owner + 0x318) + 0x674) = 0.0f;
        }
        break;
    }
    case 1:
        /* Match 32-bit wrap before the signed comparison. */
        value = (s32)((u32)record[0x1B] + (u32)D_800BEA08 * 10U);
        if (value >= 255) {
            record[0x1B] = 255;
            record[0x1A] = 2;
            *(u16 *)(record + 0x18) = 180;
        } else record[0x1B] = value;
        break;
    case 2:
        if (D_800BEA08 < *(u16 *)(record + 0x18)) {
            *(u16 *)(record + 0x18) = (u16)((u32)*(u16 *)(record + 0x18) - (u32)D_800BEA08);
        } else {
            owner = *(u8 **)(record + 0x10);
            D_800BEA0C = 0;
            func_1000E2F4(0);
            func_151254F4(*(struct108 **)(owner + 0x318), owner[0x13F]);
            *(f32 *)(*(u8 **)(owner + 0x318) + 0x674) = 0.0f;
            record[0x1A] = 3;
        }
        break;
    case 3:
        value = (s32)((u32)record[0x1B] - (u32)D_800BEA08 * 10U);
        if (value <= 0) {
            func_1516972C((struct102 *)record);
            func_151D66F0(0, 0);
        } else {
            func_151D66F0((s32)((u32)value * 210U) >> 8, 2);
            record[0x1B] = value;
        }
        break;
    }
}

s32 func_1510448C(s32 arg0, u8 *arg1, s16 arg2) {
    s16 gate = arg2;
    u8 **record = &arg1;
    s32 value;

    if ((gate != 0) || ((value = (*record)[0x1B]) == 0)) {
        return arg0;
    }
    return (s32)func_1517F08C((Gfx *)arg0, ((value << 6) - value) >> 8, 0, 0, 0, arg2);
}

s32 func_151044F4(void) {
    u8 *temp_v1 = D_800CC5EC;

    if (temp_v1 != 0) {
        return temp_v1[0x7D];
    }
    return 0;
}
