#include <ultra64.h>
void func_150432CC(s32, s32);
void func_1504332C(u8, u8, u8, u8);
void func_15042D78(u8);
s32 func_15042E3C(s32, ...);
extern u8 D_800AB254[];

extern Gfx D_80083740[], D_800838C0[];
Gfx *func_15133EEC(Gfx *, u16, u8, s32);

extern s32 D_800BE9F0;

/* Recovered callbacks and remaining placeholders from asm/203E20.s. */

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

typedef struct {
    u8 retained00[0x14];
    f32 x, y, z;
} BufferedMatrixPosition151D6E60;

/* Only the observed prefix and the two matrix pages are described. */
typedef struct {
    u8 retained00[0x4C];
    BufferedMatrixPosition151D6E60 *position;
    u8 retained50[0x2C];
    f32 matrices[2][4][4];
} BufferedMatrixOwner151D6E60;
extern u8 D_800BE9C0;
extern f32 D_800AB278;
f32 func_15144AA8(s32);
void func_150A8050(f32 [4][4], f32, f32, f32);

/* Rebuild the selected matrix, copy the source position and scale its basis. */
s32 func_151D6E60(BufferedMatrixOwner151D6E60 *owner) {
    f32 scale;
    func_150A8050(owner->matrices[D_800BE9C0], 0.0f, func_15144AA8(0) + 25.0f, 0.0f);
    scale = D_800AB278;
    owner->matrices[D_800BE9C0][3][0] = owner->position->x;
    owner->matrices[D_800BE9C0][3][1] = owner->position->y + 120.0f;
    owner->matrices[D_800BE9C0][3][2] = owner->position->z;
    owner->matrices[D_800BE9C0][0][0] *= scale;
    owner->matrices[D_800BE9C0][0][1] *= scale;
    owner->matrices[D_800BE9C0][0][2] *= scale;
    owner->matrices[D_800BE9C0][1][0] *= scale;
    owner->matrices[D_800BE9C0][1][1] *= scale;
    owner->matrices[D_800BE9C0][1][2] *= scale;
    owner->matrices[D_800BE9C0][2][0] *= scale;
    owner->matrices[D_800BE9C0][2][1] *= scale;
    owner->matrices[D_800BE9C0][2][2] *= scale;
    return 1;
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
