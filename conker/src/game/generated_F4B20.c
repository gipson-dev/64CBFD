#include <ultra64.h>

extern f32 D_800A04C0;

void *memcpy(void *dst, const void *src, unsigned int len);
extern u8 D_80089470[];

/* Non-matching placeholders for the text-only asm slice asm/F4B20.s. */

/* Scale the linked data byte into the owner's output byte. */
s32 func_150C7670(u8 *owner) {
    f32 value = (u32)(*(u8 **)(*(u8 **)(owner + 0x170) + 0x14))[0x2F];

    owner[0x70] = (u32)(value * D_800A04C0);
    return 1;
}

s32 func_150C773C(void *arg0, u8 arg1) {
    memcpy(arg0, D_80089470, 0x40);
    return 1;
}
