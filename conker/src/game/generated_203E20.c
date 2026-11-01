#include <ultra64.h>
void func_150432CC(s32, s32);
void func_1504332C(u8, u8, u8, u8);
void func_15042D78(u8);
s32 func_15042E3C(s32, ...);
extern u8 D_800AB254[];

extern Gfx D_80083740[], D_800838C0[];
Gfx *func_15133EEC(Gfx *, u16, u8, s32);

extern s32 D_800BE9F0;

/* Non-matching placeholders for the text-only asm slice asm/203E20.s. */

void func_151D6970(u8 *arg0, s32 arg1) {
    s32 temp_v0 = D_800BE9F0;

    if ((temp_v0 == 0x32) || (temp_v0 == 0x33)) {
        func_150D6730(arg0, 0xFF, 1);
    }
}

s32 func_151D69B4() {
    return 0;
}

s32 func_151D6BFC() {
    return 0;
}

s32 func_151D6E60() {
    return 0;
}

/* Draw the live attached cash amount with its signed lifetime fade. */
s32 func_151D7000(u8 *owner) {
    u8 *actor;
    u8 *label;
    s16 remaining;
    u16 opacity;
    label = *(u8 **)(owner + 0x48);
    actor = *(u8 **)label;
    if (*(s32 *)actor == 0 || label[4] != actor[0x3B]) return 0;
    remaining = *(s16 *)(owner + 0xE);
    opacity = 255;
    if (remaining < *(s16 *)(label + 0xC)) {
        opacity = remaining * *(s16 *)(label + 0xE);
        if ((s16)opacity < 0) opacity = 0;
    }
    func_150432CC((s32)actor, 0x109);
    func_1504332C(50, 125, 28, opacity);
    func_15042D78(0x81);
    return func_15042E3C((s32)D_800AB254, *(s32 *)(label + 8));
}

void func_151D70CC(u8 *arg0, s32 arg1, u8 arg2) {
    u8 *target = *(u8 **) (arg0 + 0x48);

    func_15169850(arg1, arg2, (s32) target, (s32) (target + 4), (s32) arg0);
}

/* Select the segment-8 bank, submit segments 6/7 and mark the draw state. */
Gfx *func_151D710C(Gfx *commands, u8 *descriptor, s32 unused2, s32 unused3, u8 *changed) {
    if (descriptor[0x43] < 0xFF) {
        gSPSegment(commands++, 8, D_80083740);
    } else {
        gSPSegment(commands++, 8, D_800838C0);
    }
    commands = func_15133EEC(commands, 0xC3, 6, 3);
    commands = func_15133EEC(commands, 0xC3, 7, 3);
    *changed = 1;
    return commands;
}
