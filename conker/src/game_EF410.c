#include <ultra64.h>

#include "functions.h"
#include "variables.h"

typedef struct PacketEF410 {
    f32 *x;
    f32 *y;
    f32 *z;
    f32 parameter0;
    f32 parameter1;
    s16 delta;
    u8 flags;
    u8 byte17;
    u8 byte18;
    s8 sentinel;
} PacketEF410;

extern f32 D_800A0280;
extern f32 D_800A0284;
f32 *func_15144B34(s32);
void *func_15134908(void *arg0, s32 arg1, u8 arg2, s32 arg3);

/* Generated placeholder declarations. */
s32 func_150C1F60();
s32 func_150C2290();
s32 func_150C2424();
s32 func_150C2558();
s32 func_150C2700();
void func_150C2804(f32 *x, f32 *y, f32 *z, s16 delta, u8 channel, s32 context);
s32 func_150C2898();
s32 func_150C29F0();
s32 func_150C2C00();
s32 func_150C308C(u8 *);
Gfx *func_150C3160(Gfx *, u8 *);
void func_150C3230();
s32 func_150C3574();
s32 func_150C3994();
s32 func_150C3D5C();
/* End generated placeholder declarations. */

/* Non-matching C placeholders for asm/nonmatchings/game_EF410/func_150C1F60.s. */
s32 func_150C1F60() {
    return 0;
}
/* Non-matching C placeholders for asm/nonmatchings/game_EF410/func_150C2290.s. */
s32 func_150C2290() {
    return 0;
}
// TODO: figure out this struct!
// void func_150C2290(s32 arg0) {
//     s16 sp9A;
//     s16 sp98;
//     s8 sp95;
//     s8 sp94;
//     ?32 sp90;
//     ?32 sp8C;
//     ?32 sp88;
//     ?32 sp84;
//     ?32 sp80;
//     ?32 sp7C;
//     ?32 sp78;
//     ?32 sp74;
//     ?32 sp70;
//     s8 sp6E;
//     s8 sp6D;
//     s8 sp6C;
//     ?32 sp68;
//     ?32 sp64;
//     ?32 sp60;
//     ?32 sp5C;
//     ?32 sp58;
//     ?32 sp54;
//     s8 sp52;
//     s8 sp51;
//     s8 sp50;
//     s16 sp4E;
//     s16 sp4C;
//     s16 sp4A;
//     s16 sp48;
//     s16 sp46;
//     s16 sp44;
//     s16 sp42;
//     s16 sp40;
//     s16 sp3E;
//     s16 sp3C;
//     f32 sp38;
//     f32 sp34;
//     f32 sp30;
//     f32 sp2C;
//     f32 sp28;
//     f32 sp24;
//     f32 sp20;
//     f32 sp1C;
//     f32 sp18;
//
//     sp18 = *(void *)0x800A0258;
//     sp1C = 40.0f;
//     sp3E = 3;
//     sp40 = -0x29;
//     sp44 = -0x16;
//     sp42 = 0x15;
//     sp46 = 0x16;
//     sp48 = 7;
//     sp4E = 0x15;
//     sp50 = 0xB;
//     sp20 = *(void *)0x800A025C;
//     sp3C = 2;
//     sp4C = 0x30;
//     sp52 = 0x28;
//     sp54 = 1;
//     sp58 = 4;
//     sp6C = 0xFF;
//     sp6D = 0xFF;
//     sp70 = 3;
//     sp4A = 0;
//     sp51 = 1;
//     sp5C = 0;
//     sp60 = 0;
//     sp64 = 0;
//     sp68 = 0;
//     sp6E = 0;
//     sp74 = 0xFF;
//     sp78 = 0;
//     sp7C = 0x220005;
//     sp80 = 0x1D0600;
//     sp84 = (?32) (u8)1;
//     sp88 = 0x3B;
//     sp8C = 0x80;
//     sp90 = 0x20;
//     sp94 = 0;
//     sp95 = 7;
//     sp98 = 0xC;
//     sp9A = 0x15;
//     sp34 = 100.0f;
//     sp38 = 57.5f;
//     sp24 = *(void *)0x800A0260;
//     sp28 = 39.0f;
//     sp2C = *(void *)0x800A0264;
//     sp30 = 1.0f;
//     func_15151A38(&sp18, arg0 & 0xFF, 1);
// }

/* Non-matching C placeholders for asm/nonmatchings/game_EF410/func_150C2424.s. */
s32 func_150C2424() {
    return 0;
}
// NON-MATCHING: ported from ects_proto (ECTS ROM build), not yet byte-verified for us
s32 func_150C251C(struct202 *arg0) {
    u8 *p;
    s32 val;

    p = (u8 *) arg0->unk98;
    val = arg0->unk1C * 8;
    if (val >= 0x100) {
        val = 0xFF;
    }
    p[0x1B] = val;
    if ((u8) val < 0) {
        return 0;
    }
    return 1;
}
/* Non-matching C placeholders for asm/nonmatchings/game_EF410/func_150C2558.s. */
s32 func_150C2558() {
    return 0;
}
/* Non-matching C placeholders for asm/nonmatchings/game_EF410/func_150C2700.s. */
s32 func_150C2700() {
    return 0;
}
/* Float-reference effect packet dispatch. */
void func_150C2804(f32 *x, f32 *y, f32 *z, s16 delta, u8 channel, s32 context) {
    PacketEF410 packet;

    packet.parameter0 = D_800A0280;
    packet.x = x;
    packet.y = y;
    packet.z = z;
    packet.parameter1 = D_800A0284;
    packet.delta = delta;
    packet.flags = 5;
    packet.byte17 = 6;
    packet.byte18 = 3;
    packet.sentinel = -1;
    func_15134908(&packet, 0, channel, context);
}
/* Non-matching C placeholders for asm/nonmatchings/game_EF410/func_150C2898.s. */
s32 func_150C2898() {
    return 0;
}
/* Non-matching C placeholders for asm/nonmatchings/game_EF410/func_150C29F0.s. */
s32 func_150C29F0() {
    return 0;
}
/* Non-matching C placeholders for asm/nonmatchings/game_EF410/func_150C2C00.s. */
s32 func_150C2C00() {
    return 0;
}
/* Apply damping and vertical acceleration; report whether both extents remain valid. */
s32 func_150C2FCC(void *effect) {
    *(f32 *) ((char *) effect + 0x2C) -= *(f32 *) ((char *) effect + 0x2C) * *(f32 *) ((char *) effect + 0x150);
    *(f32 *) ((char *) effect + 0x30) -= *(f32 *) ((char *) effect + 0x30) * *(f32 *) ((char *) effect + 0x150);
    *(f32 *) ((char *) effect + 0x38) += *(f32 *) ((char *) effect + 0x50) * D_800BE9A4 + 0.5f * *(f32 *) ((char *) effect + 0x4C) * D_800BE9A4 * D_800BE9A4;
    *(f32 *) ((char *) effect + 0x50) += *(f32 *) ((char *) effect + 0x4C) * D_800BE9A4;
    if (*(f32 *) ((char *) effect + 0x2C) < 10.0f || *(f32 *) ((char *) effect + 0x30) < 10.0f) {
        return 0;
    }
    return 1;
}
/* Move an active actor to state five when either motion test succeeds. */
s32 func_150C308C(u8 *actor) {
    u8 stop = 0;
    f32 *motion;
    f32 x, z;

    if (*(s16 *)(actor + 0x1C) >= 6) {
        motion = func_15144B34(D_80082FA4);
        x = motion[0];
        z = motion[2];
        x = x * x + z * z;
        if (x < D_800A0310) {
            stop = 1;
        } else {
            x = func_150484A0(motion[0], motion[2]);
            x = func_15144C8C(x, *(f32 *)(actor + 0x160));
            if (D_800A0314 < x) {
                stop = 1;
            }
        }
    }
    if (stop != 0) {
        *(s16 *)(actor + 0x1C) = 5;
    }
    return 1;
}

/* Emit the special actor texture phase and retain the previous phase for wrapping. */
Gfx *func_150C3160(Gfx *commands, u8 *actor) {
    f32 ratio;
    s32 coordinate, previous;

    if (*(s32 *)(actor + 0x2E8) != 0) {
        ratio = (f32)*(s32 *)(actor + 0x2E4) / (f32)*(s32 *)(actor + 0x2E8);
    } else {
        ratio = 1.0f;
    }
    ratio = 1.0f - ratio;
    coordinate = (s32)(500.0f * ratio + 2.0f);
    previous = (s32)(2U - *(u32 *)(actor + 0x2EC));
    *(s32 *)(actor + 0x2EC) = coordinate / 3;
    while (previous < 0) {
        previous += 64;
    }
    gDPSetTileSize(commands++, 4, coordinate, previous, 0x1FE, 0x3E);
    return commands;
}
/* Original bomb animation, fuse and explosion lifecycle. */
#pragma GLOBAL_ASM("asm/nonmatchings/game_EF410/func_150C3230.s")
/* Non-matching C placeholders for asm/nonmatchings/game_EF410/func_150C3574.s. */
s32 func_150C3574() {
    return 0;
}
/* Non-matching C placeholders for asm/nonmatchings/game_EF410/func_150C3994.s. */
s32 func_150C3994() {
    return 0;
}

s32 func_150C3D48(s32 arg0) {
    return arg0 + 0xEDCBA988;
}

/* Non-matching C placeholders for asm/nonmatchings/game_EF410/func_150C3D5C.s. */
s32 func_150C3D5C() {
    return 0;
}
