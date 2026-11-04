#include <ultra64.h>
#include "structs.h"
void func_1506160C(struct127 *, s32, u8, u8, s32);
void func_151C9ED4(void *);

/* Restored functions and remaining placeholders for asm/14D110.s. */

s32 func_1511FC60() {
    return 0;
}

s32 func_15120158() {
    return 0;
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_14D110/func_15121490.s")

s32 func_151216F8() {
    return 0;
}

typedef struct {
    u8 pad0[0x2C];
    f32 angle;
    u8 pad30[0x1C];
    u8 active;
} ResetView151218C4;

typedef struct {
    u8 pad0[0x34];
    s32 kind;
    u8 pad38[0xFC];
    s32 angleInteger;
    u8 pad138[0x58];
    f32 reset190;
    u8 pad194[0x4];
    f32 reset198;
    u8 pad19C[0xA1];
    u8 commandByte;
    u8 pad23E[0x10A];
    f32 distance348;
    u8 pad34C[0x20];
    u16 *resourceFlags;
    u8 pad370[0x4];
    f32 distance374;
    u8 pad378[0x58];
    struct127 *commandTarget;
    struct127 *target;
    u8 pad3D8[0x324];
    s32 mode;
    u8 pad700[0x3C];
    s16 state;
    u8 pad73E[0x2];
    ResetView151218C4 view;
    u8 pad790[0xBA];
    s16 timer;
    u8 cleanupPending;
    u8 pad84D[0x4B];
    f32 reset898;
    f32 reset89C;
    u8 pad8A0[0xFC];
    f32 reset99C;
} ResetActor151218C4;

/* Reset the actor's view state unless its resource blocks the reset. */
void func_151218C4(volatile ResetActor151218C4 *actor) {
    volatile ResetView151218C4 *view;

    if ((*actor->resourceFlags & 0x10) == 0) {
        if (actor->kind == 0x40) {
            if (actor->mode == 0xF) {
                actor->reset898 = 0.0f;
                actor->reset89C = 0.0f;
            }
            actor->target->unk198 = 0;
            actor->state = 0;
            actor->timer = 0x3C;
            view = &actor->view;
        } else {
            actor->timer = 0x3C;
            actor->state = 3;
            view = &actor->view;
        }
        actor->distance374 = 200.0f;
        actor->distance348 = 100.0f;
        actor->angleInteger = (s32)view->angle;
        view->active = 0;
        ((ResetActor151218C4 *)actor)->reset190 = 0.0f;
        ((ResetActor151218C4 *)actor)->reset99C = 0.0f;
        ((ResetActor151218C4 *)actor)->reset198 = 0.0f;
        func_1506160C(actor->commandTarget, 2, 0xFF, 0x20,
                      ((ResetActor151218C4 *)actor)->commandByte);
        if (actor->cleanupPending != 0) {
            func_151C9ED4((void *)actor);
            actor->cleanupPending = 0;
        }
    }
}
