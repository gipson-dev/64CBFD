#include <ultra64.h>

extern u8 *D_800B0DF0;
extern u8 D_80038080;
extern s32 *D_800891BC[];
extern void *D_800DBE80;
void func_10004074(void *);
void func_1510D694(s32);
s32 func_15111858(void);
void func_1502B7F0(void **, s32, s32, s32);


extern s32 D_80082FA0, D_80082FA4;
s32 func_1501A490(Gfx *, s16, s32, s32, s32, s32);
Gfx *func_1501A6CC(Gfx *, s32, s32, s32, s32);
Gfx *func_15110544(Gfx *, s32, s32, s32, s32, u8, u8, u8);

extern s32 D_800BE9F0, D_800BE620, D_800BE624;
extern u8 *D_800DBFF0;
extern u8 D_800DBEA8[];

void func_150A7CB0(f32 matrix[4][4], f32 x, f32 y, f32 z);
void func_150A8050(f32 [4][4], f32, f32, f32);
void func_150A7A48(f32 [4][4], f32 [4][4], f32 [4][4]);
typedef struct {
    u8 pad0[0x24];
    f32 top, bottom, left, right;
    u8 pad34[0x88];
    f32 mtx[4][4];
    u8 padFC[0x84];
} Record13D350;
extern Record13D350 *D_800BE628;
extern s32 D_800DBEF0;
extern u8 *D_800DBEF4;
extern s32 *D_800DBF94;

/* Partially recovered text-only slice asm/13D350.s. */

s32 func_1510FEA0() {
    return 0;
}

/* Compose separate Y, X and Z rotations using one temporary matrix. */
void func_151102CC(f32 matrix[4][4], f32 x, f32 y, f32 z) {
    f32 temporary[4][4];

    func_150A8050(matrix, 0.0f, y, 0.0f);
    func_150A8050(temporary, x, 0.0f, 0.0f);
    func_150A7A48(matrix, temporary, matrix);
    func_150A8050(temporary, 0.0f, 0.0f, z);
    func_150A7A48(matrix, temporary, matrix);
}

void func_15110360(s32 arg0, f32 arg1[4][4], f32 arg2, f32 arg3, f32 arg4) {
    func_151102CC(arg1, arg2, arg3, arg4);
    func_150A7A48(arg1, D_800BE628[arg0].mtx, arg1);
}

/* Fill the selected view and append the active split-screen dividers. */
Gfx *func_151103C8(Gfx *commands, f32 unusedX, f32 unusedY, f32 unusedZ) {
    Record13D350 *view = (Record13D350 *)((u32)D_800BE628 + (u32)D_80082FA4 * 0x180);

    commands = func_15110544(commands, (s32)view->left, (s32)view->top,
        (s32)(view->right - 1.0f), (s32)view->bottom,
        D_800DBEA8[0], D_800DBEA8[1], D_800DBEA8[2]);
    if (D_80082FA0 != 0 && D_80082FA4 == 0) {
        gDPPipeSync(commands++);
        commands = (Gfx *)func_1501A490(commands, 0xFF, 0, 0, 0, 0);
        gDPSetFillColor(commands++, 0x00010001);
        commands = func_1501A6CC(commands, 0, (D_800BE624 >> 1) - 6,
            D_800BE620, (D_800BE624 >> 1) + 6);
        if (D_80082FA0 != 1) {
            commands = func_1501A6CC(commands, (D_800BE620 >> 1) - 1, 0,
                (D_800BE620 >> 1) + 1, D_800BE624);
        }
    }
    return commands;
}

Gfx *func_1501A680(Gfx *commands);
Gfx *func_1501A6CC(Gfx *commands, s32 left, s32 top, s32 right, s32 bottom);

/* Append an RGBA16 fill rectangle, with the retail legacy blend-mask bits. */
Gfx *func_15110544(Gfx *commands, s32 left, s32 top, s32 right, s32 bottom,
                    u8 red, u8 green, u8 blue) {
    gDPPipeSync(commands++);
    gDPSetOtherMode(commands++, G_CYC_FILL | G_TF_BILERP | G_TC_FILT | 0xF,
        G_AC_NONE | G_ZS_PRIM | G_RM_NOOP | G_RM_NOOP2);
    commands = func_1501A680(commands);
    gDPSetFillColor(commands++, ((u32)GPACK_RGBA5551(red, green, blue, 1) << 16) |
        GPACK_RGBA5551(red, green, blue, 1));
    return func_1501A6CC(commands, left, top, right, bottom);
}

/* Fill the frame for the selected categories and qualifying child state. */
Gfx *func_15110600(Gfx *commands, f32 unusedX, f32 unusedY, f32 unusedZ) {
    if (D_800BE9F0 == 0x1B || D_800BE9F0 == 0x1E ||
        (D_800BE9F0 == 0x31 && (*(u8 **)(D_800DBFF0 + 0x3D4))[0x78] == 3)) {
        commands = (Gfx *)func_15110544(commands, 2, 0,
            (s32)((u32)D_800BE620 - 2), D_800BE624,
            D_800DBEA8[0], D_800DBEA8[1], D_800DBEA8[2]);
    }
    return commands;
}

s32 func_151106A8() {
    return 0;
}

s32 func_151108C4() {
    return 0;
}

s32 func_15110CFC() {
    return 0;
}

/* Process a requested mode change and optional slot cleanup. */
void func_1511172C(s32 mode) {
    s32 index;
    if (mode == 1) {
        D_800B0DF0[8] = 1;
        if (D_800DBE80) { void *allocation = D_800DBE80; func_10004074(allocation); }
        func_15111858();
    } else if (mode != D_800B0DF0[9] && D_800B0DF0[8] == 4) {
        if (D_80038080 != 0) {
            for (index = 0; index < 360; index++) {
                func_1510D694(D_800891BC[D_800B0DF0[9]][0] + index);
            }
        }
        func_10004074(D_800DBE80);
        D_800B0DF0[9] = mode;
        func_1502B7F0(&D_800DBE80, 2, 13, D_800B0DF0[9]);
    }
}

s32 func_15111858() {
    return 0;
}

s32 func_15111AF4() {
    return 0;
}

s32 func_15112520() {
    return 0;
}

s32 func_15112A80() {
    return 0;
}

/* Refresh bit 0x40 from each record's flags and attached-object state. */
void func_15113180(void) {
    s32 index = 0;
    u32 offset = 0;
    u8 *record;
    u32 flags;

    if (D_800DBEF0 > 0) {
        do {
            record = D_800DBEF4 + offset;
            record[0x6F] &= ~0x40;
            record = D_800DBEF4 + offset;
            flags = record[0x6F];
            if (((flags & 0x0F) != 0 || (record[0x70] & 4) == 4) &&
                *(s32 *)(record + 0x38) != 0) {
                record[0x6F] = flags | 0x40;
            }
            index++;
            offset += 0xA0;
        } while (index < D_800DBEF0);
    }
}

s32 func_15113218() {
    return 0;
}

s32 func_151135C4() {
    return 0;
}

s32 func_151137D4() {
    return 0;
}

s32 func_15113C88() {
    return 0;
}

s32 func_15113E54() {
    return 0;
}

s32 func_15114050(u8 *arg0, s32 arg1) {
    if (arg0[0x4F] & 0x80) {
        if (arg1 == -1) {
            return 1;
        }
        if (D_800DBF94[(arg0 - D_800DBEF4) / 0xA0] & (1 << arg1)) {
            return 1;
        }
    }
    return 0;
}

/* Return the first set record-mask bit, or zero when disabled or empty. */
s32 func_151140C4(u8 *record) {
    s32 index = 0;
    s32 mask;
    if (record[0x4F] & 0x80) {
        mask = D_800DBF94[(record - D_800DBEF4) / 0xA0];
        for (; index < 32; index++) {
            if (mask & (1U << index)) {
                return index;
            }
        }
    }
    return 0;
}

s32 func_15114188() {
    return 0;
}

s32 func_15114348() {
    return 0;
}

extern f32 D_800A2F60;
extern u8 D_800CC2D0[];
extern u16 D_800CBDA0[];
/* Update actor fields and a running halfword from an indexed record. */
void func_1511473C(u8 *actor, s32 index) {
    u32 value;
    if (actor != 0 && index < D_800DBEF0) {
        func_15114348(index, actor + 0x14, actor + 0x18, actor + 0x1c);
        value = (u32)(*(f32 *)((u32)D_800DBEF4 + (u32)index * 0xa0 + 0x64) * D_800A2F60 + *(u16 *)(actor + 0x76));
        *(u16 *)(actor + 0x76) = value;
        if (actor[0x137] != 0 && (u32)index + 1 == D_800CBDA0[(s32)((u32)actor - (u32)D_800CC2D0) / 0x32c]) {
            *(u16 *)(actor + 0x7a) = value;
        }
    }
}

void func_151148A8(f32 arg0[4][4], f32 arg1[3]) {
    f32 temp[4][4];

    func_150A8050(arg0, 0.0f, arg1[1], 0.0f);
    func_150A8050(temp, arg1[0], 0.0f, arg1[2]);
    func_150A7A48(temp, arg0, arg0);
}

/* Build the actor's rotated, translated and scaled world matrix. */
void func_1511490C(f32 matrix[4][4], u8 *actor) {
    f32 scale[4][4];

    func_151148A8(matrix, (f32 *)actor);
    matrix[3][0] = *(s16 *)(actor + 0x10);
    matrix[3][1] = *(f32 *)(actor + 0x18) + *(s16 *)(actor + 0x12);
    matrix[3][2] = *(s16 *)(actor + 0x14);
    func_150A7CB0(scale, *(f32 *)(actor + 0x2C), *(f32 *)(actor + 0x30), *(f32 *)(actor + 0x34));
    func_150A7A48(scale, matrix, matrix);
}

u8 *func_151149AC(u8 arg0) {
    s32 offset;
    s32 i;
    u8 *base;
    u8 *record;

    if (arg0 == 0) {
        return NULL;
    }

    i = 0;
    if (D_800DBEF0 > 0) {
        base = D_800DBEF4;
        offset = 0;
        record = base;
        do {
            if (record[0x72] == arg0) {
                return offset + base;
            }
            i++;
            offset += 0xA0;
            record += 0xA0;
        } while (i < D_800DBEF0);
    }
    return NULL;
}

s32 func_15114A1C() {
    return 0;
}

#include "structs.h"
extern u32 D_800DBF98;
void func_1516972C(struct102 *);

/* Mark a record as released, then trim released records from the tail. */
void func_15114B94(u32 index) {
    u32 count, boundary, offset;
    u8 *record;
    if (index < (u32)D_800DBEF0) {
        offset = index * 0xA0;
        record = D_800DBEF4 + offset;
        if (*(struct102 **)(record + 0x94) != NULL) {
            func_1516972C(*(struct102 **)(record + 0x94));
            *(struct102 **)(D_800DBEF4 + offset + 0x94) = NULL;
        }
        D_800DBEF4[offset + 0x70] |= 8;
        D_800DBEF4[offset + 0x6E] = 1;
    }
    count = (u32)D_800DBEF0;
    boundary = count - D_800DBF98;
    while (count != 0 && (D_800DBEF4[(count - 1) * 0xA0 + 0x70] & 8)) {
        if (count - 1 >= boundary && D_800DBF98 != 0) D_800DBF98--;
        else boundary--;
        D_800DBEF0 = --count;
    }
}

extern s32 func_15114CC4();

#pragma GLOBAL_ASM("asm/nonmatchings/generated_13D350/func_15114CC4.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_13D350/func_15114D24.s")

void func_15114F04(s32 arg0, s32 arg1, s32 arg2) {
    func_1001001C(func_15114CC4, arg0, 0, arg1, arg2);
}

s32 func_15114F44() {
    return 0;
}
