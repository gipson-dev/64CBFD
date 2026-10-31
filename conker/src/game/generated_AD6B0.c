#include <ultra64.h>
extern s32 D_800427F0, D_800BE9E4;
extern s32 D_8009BD10[];
s32 func_151EF610(void);
extern s32 D_800D1930;
extern s32 D_800D192C;
extern s32 D_800D1928;

/* Non-matching placeholders for the text-only asm slice asm/AD6B0.s. */

/* Note 316: chained assignment preserves the retail global-address lifetimes. */
void func_15080200(void) {
    D_800D1930 = D_800D1928 = D_800D192C = 0;
}

s32 func_15080228() {
    return 0;
}

/* Update the actor channel gate or advance its timed five-entry cycle. */
void func_15080348(u8 *actor) {
    s32 index;
    s32 remaining;

    if (D_800D1928 != 0 && actor != NULL) {
        if (D_800D1928 == 1) {
            if (D_800427F0 < 1000) {
                actor[0x1FF] = 0;
            } else {
                actor[0x1FF] = 1;
            }
        } else {
            index = D_800D192C;
            if (D_800427F0 > 1000) {
                remaining = actor[0x135];
                remaining = (s32)((u32)remaining - (u32)D_800BE9E4);
                index = (s32)((u32)index + 1);
                if (remaining < 0) {
                    if (index >= 5) {
                        index = 0;
                    }
                    actor[0x134] = D_8009BD10[index];
                    actor[0x135] = func_151EF610() % 7 + 4;
                    D_800D192C = index;
                }
            }
        }
        D_800427F0 = 0;
    }
}

s32 func_1507E968(u8 *);
void func_1507E500(u8 *, s32, s32);
/* Apply a channel command and clamp its optional duration for an active actor. */
void func_15080430(u8 *actor, s32 channel, s32 duration) {
    if (actor != 0) {
        if (func_1507E968(actor) > 0) {
            if (channel == 0) {
                D_800D1928 = 0;
                *(u16 *)(actor + 0x72) = 20;
                func_1507E500(actor, 0, 10);
            } else {
                *(u16 *)(actor + 0x72) = 0xFFFE;
                if (channel == 1) {
                    D_800D1928 = 2;
                } else {
                    if (duration != 0) {
                        if (duration > 20) duration = 20;
                        if (duration <= 0) duration = 1;
                    }
                    func_1507E500(actor, channel, duration);
                }
            }
        } else {
            D_800D1928 = channel != 0;
            if (channel != 0) return;
            actor[0x1FF] = 0;
        }
    }
}
