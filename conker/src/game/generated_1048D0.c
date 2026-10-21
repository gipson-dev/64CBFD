#include <ultra64.h>
extern s32 D_800BE9E4;
extern u16 D_800D9910;

/* Non-matching placeholders for the text-only asm slice asm/1048D0.s. */

/* Apply selector-dependent flag and byte updates for command 0x36. */
void func_150D7420(u8 *actor, u8 *event, u8 command) {
    if (command == 0x36) {
        switch (event[0]) {
            case 1:
                *(u32 *)(actor + 0x58) |= 2;
                actor[0x28] = 0xFF;
                actor[0x29] = 0;
                actor[0x2A] = 0;
                break;
            case 2:
                *(u32 *)(actor + 0x58) |= 2;
                actor[0x28] = 0xFF;
                actor[0x29] = 0;
                actor[0x2A] = 0;
                break;
            case 3:
                *(u32 *)(actor + 0x58) |= 2;
                actor[0x28] = 0;
                actor[0x29] = 0xFF;
                actor[0x2A] = 0;
                break;
            case 0:
            default:
                *(u32 *)(actor + 0x58) &= ~2;
                break;
        }
    }
}

/* Apply selector-dependent flag and byte updates for command 0x36. */
void func_150D74DC(u8 *actor, u8 *event, u8 command) {
    if (command == 0x36) {
        switch (event[0]) {
            case 1:
                *(u32 *)(actor + 0x58) &= ~2;
                break;
            case 2:
                *(u32 *)(actor + 0x58) |= 2;
                actor[0x28] = 0xFF;
                actor[0x29] = 0;
                actor[0x2A] = 0;
                break;
            case 3:
                *(u32 *)(actor + 0x58) |= 2;
                actor[0x28] = 0;
                actor[0x29] = 0xFF;
                actor[0x2A] = 0;
                break;
            case 0:
            default:
                *(u32 *)(actor + 0x58) &= ~2;
                break;
        }
    }
}

/* Apply selector-dependent flag and byte updates for command 0x36. */
void func_150D758C(u8 *actor, u8 *event, u8 command) {
    if (command == 0x36) {
        switch (event[0]) {
            case 1:
                *(u32 *)(actor + 0x58) &= ~2;
                break;
            case 2:
                *(u32 *)(actor + 0x58) &= ~2;
                break;
            case 3:
                *(u32 *)(actor + 0x58) |= 2;
                actor[0x28] = 0;
                actor[0x29] = 0xFF;
                actor[0x2A] = 0;
                break;
            case 0:
            default:
                *(u32 *)(actor + 0x58) &= ~2;
                break;
        }
    }
}

void func_150D7630(s32 arg0) {
    if (arg0 == 0) {
        D_800D9910 = D_800D9910 + (D_800BE9E4 << 6);
    }
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1048D0/func_150D765C.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1048D0/func_150D7790.s")

s32 func_150D7928() {
    return 0;
}
