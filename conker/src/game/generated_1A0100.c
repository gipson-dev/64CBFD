#include <ultra64.h>
#include "structs.h"

/* Non-matching placeholders for the text-only asm slice asm/1A0100.s. */

extern s8 D_800DD2B0[];
extern u8 D_800DD2C0[];
extern u8 D_800BE9B4;
extern s32 D_800BE9F0;
s32 func_15085430();
void func_1517EE40(s32 arg0, s32 arg1, s32 arg2, s32 arg3, s8 arg4,
                    s32 arg5);
extern struct127 D_800CC2D0[];
void func_1501C730(s32, s32, s32, s32, s32);
s32 func_1517F40C(s32);

void func_15172C50(s32 value) {
    s32 i;

    for (i = 0; i < 16; i++) {
        D_800DD2B0[i] = -1;
        D_800DD2C0[i] = 0;
    }

    D_800DD2C0[0] = value;
}

/* Note 534: indexed slot teardown event pair. */
void func_15172CA8(s32 arg0) {
    if (D_800DD2B0[arg0] != -1) {
        D_800DD2B0[arg0] = -1;
        func_1517EE40(0, 0, 0, 0, 1, arg0);
        func_1517EE40(0, 0, 0, 0x32, 0, arg0);
    }
}

void func_15172D28(u8 *arg0, s32 arg1) {
    u8 *target;

    func_15085430(arg0, arg1, 1);
    *(u16 *) (arg0 + 0x2F8) &= ~0x10;

    if (D_800BE9B4 == 0) {
        target = *(u8 **) (arg0 + 0x31C);
        if (target != NULL) {
            target[0x56] = 3;
        }
    }
}

/* Release a channel effect and apply its pending payload to its actor. */
void func_15172D80(s32 channel) {
    s8 *slot;
    struct127 *actor;

    slot = &D_800DD2B0[channel];
    if (*slot != -1) {
        actor = &D_800CC2D0[channel];
        if (actor->health == 0) {
            *slot = -1;
            func_1517EE40(0, 0, 0, 0x32, 0, channel);
        }
        if (func_1517F40C(channel) != 0) {
            if (D_800BE9F0 != *slot) {
                func_1501C730(1, *slot, 0, 0, 0);
                return;
            }
            func_15172CA8(channel);
            func_15172D28((u8 *)actor, D_800DD2C0[channel]);
        }
    }
}

/* Route an actor's channel event through its active camera or fallback state. */
void func_15172E7C(struct127 *actor, s32 selector, s32 payload) {
    s32 channel = actor->unk127;

    if (actor->health != 0 &&
        (actor->unk31C == NULL || ((s8 *)actor->unk31C)[0x23] <= 0)) {
        if (actor->camera != NULL) {
            if (D_800DD2B0[channel] == -1) {
                func_1517EE40(0, 0, 0, 0xA, 1, channel);
                actor->unk2F8 |= 0x10;
                D_800DD2B0[channel] = selector;
                D_800DD2C0[channel] = payload;
            }
        } else if (selector == D_800BE9F0) {
            func_15172D28((u8 *)actor, payload);
        }
    }
}
