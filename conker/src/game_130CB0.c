#include <ultra64.h>

#include "functions.h"
#include "variables.h"

/* Generated placeholder declarations. */
s32 func_15103910();
s32 func_15103C14();
/* End generated placeholder declarations. */

void func_15103800(void) {
    bzero(D_800D9AB0, 8); // bzero
}

void func_15103828(void) {
    u16 temp_v1;
    s32 i;

    for (i = 0; i < 4; i++)
    {
        if (D_800D9AB0[i]) {
            if (D_800D9AB0[i] > D_800BE9E4)
            {
                D_800D9AB0[i] -= D_800BE9E4;
            } else {
              D_800D9AB0[i] = 0;
            }
        }
    }
}

// need to figure out the structs
/* Non-matching C placeholders for asm/nonmatchings/game_130CB0/func_15103910.s. */
s32 func_15103910() {
    return 0;
}
typedef struct {
    u16 token;
    s16 x, y, z;
    u16 parameter8;
    s16 parameterA;
    u32 opaqueC;
    u32 flags;
    u32 opaque14;
    s32 packedTimer;
    struct127 *actor;
    u32 opaque20;
    u16 handle;
    u16 opaque26;
} SoundTimerState130CB0;

/* Snapshot the actor position and advance its pending sound token. */
s32 func_15103AA0(SoundTimerState130CB0 *state, s32 unused1, s32 unused2, s32 unused3, s32 unused4, s32 unused5, u16 *pending) {
    s32 remaining;
    struct127 *actor;

    actor = state->actor;
    remaining = state->packedTimer & 0x7FFF;

    state->x = (s32)actor->x_position;
    state->y = (s32)actor->y_position;
    state->z = (s32)actor->z_position;
    if (remaining != 0) {

        if (*pending != 0) {
            state->packedTimer = ((u32)*pending << 16) | (state->packedTimer & 0xFFFF);
            state->token = 0;
            *pending = 0;
            func_10010344(0x5B0, actor, -25000, state->parameterA, state->parameter8);
            return 0;
        }
        if ((u32)remaining <= (u32)D_800BE9E4) {
            *pending = state->packedTimer >> 16;
            state->token = *pending;
            state->packedTimer &= -0x8000;
            return 0;
        }
        remaining -= D_800BE9E4;
    } else {
        if (state->handle == 0) {
            func_10010344(0x5B1, actor, -25000, state->parameterA, state->parameter8);
            return 1;
        }
        if (state->packedTimer != 0) {
            if (!(state->packedTimer & 0x8000)) {
                func_1000F85C(state->handle, -0x8000, 2);
            }
            state->packedTimer = 0;
        }
        state->flags &= ~0x80;
    }
    state->packedTimer = (state->packedTimer & -0x8000) | remaining;
    return 0;
}
/* Non-matching C placeholders for asm/nonmatchings/game_130CB0/func_15103C14.s. */
s32 func_15103C14() {
    return 0;
}
