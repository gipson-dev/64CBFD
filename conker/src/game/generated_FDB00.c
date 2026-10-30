#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/FDB00.s. */

extern u8 *D_800D2E4C;
extern u8 D_800CC335;
s32 func_1509BE40(s32, ...);
s32 func_15123934(u8 *, s32, s32, s32, s32);
s32 func_151239CC(u8 *, s32);
void func_151254F4(u8 *, s32);

/* Select the actor mode from event availability and initialize its timer. */
void func_150D0650(u8 *actor) {
    if ((D_800D2E4C[0] & 0x80) != 0) {
        return;
    }
    if (func_1509BE40(0, 0x2000, 0xBB) != -1) {
        if (func_15123934(actor, *(s32 *)(actor + 0x2C), 0,
                          *(s32 *)(actor + 0x134), 8) != 0) {
            *(u32 *)(actor + 0x84) |= 0x1000000;
            func_151254F4(actor, (s32)D_800CC335 - 1);
            *(f32 *)(actor + 0x190) = 100.0f;
        }
    } else if (func_151239CC(actor, 8) != 0) {
        func_151254F4(actor, 0);
        *(f32 *)(actor + 0x190) = 0.0f;
    }
}
