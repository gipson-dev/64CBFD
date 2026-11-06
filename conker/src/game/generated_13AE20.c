#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/13AE20.s. */

void *func_15167A68(s32, s32, s32, s32, u8, u8);
/* Allocate two quad-coordinate banks and optional signed-halfword state. */
void *func_1510D970(s32 kind, void *owner, s32 mode, s32 flags, s32 variant) {
    u8 *record;
    s32 bytes = 0x128;
    s32 i;

    if (flags & 1) {
        bytes = 0x13A;
    }
    record = func_15167A68(0x4B, 0, bytes, 1, 0xFF, 1);
    if (record != NULL) {
        /* Each bank contains four vertex flags and texture-coordinate pairs. */
        for (i = 0; i < 2; i++) {
            ((Vtx *)(record + i * 0x40 + 0x90))[0].v.flag = 0;
            ((Vtx *)(record + i * 0x40 + 0x90))[0].v.tc[0] = 0x800;
            ((Vtx *)(record + i * 0x40 + 0x90))[0].v.tc[1] = 0;
            ((Vtx *)(record + i * 0x40 + 0x90))[1].v.flag = 0;
            ((Vtx *)(record + i * 0x40 + 0x90))[1].v.tc[0] = 0;
            ((Vtx *)(record + i * 0x40 + 0x90))[1].v.tc[1] = 0;
            ((Vtx *)(record + i * 0x40 + 0x90))[2].v.flag = 0;
            ((Vtx *)(record + i * 0x40 + 0x90))[2].v.tc[0] = 0;
            ((Vtx *)(record + i * 0x40 + 0x90))[2].v.tc[1] = 0x800;
            ((Vtx *)(record + i * 0x40 + 0x90))[3].v.flag = 0;
            ((Vtx *)(record + i * 0x40 + 0x90))[3].v.tc[0] = 0x800;
            ((Vtx *)(record + i * 0x40 + 0x90))[3].v.tc[1] = 0x800;
        }
        record[0x120] = kind;
        *(void **)(record + 0x110) = owner;
        record[0x121] = mode;
        record[0x124] = variant;
        if (flags & 1) {
            for (i = 0; i < 9; i++) {
                ((s16 *)(record + 0x128))[i] = 0x7FFF;
            }
        }
    }
    return record;
}

s32 func_1510DA84() {
    return 0;
}

s32 func_1510E120() {
    return 0;
}

s32 func_1510E388() {
    return 0;
}

/* Note 317: guarded expansion preserves the retail display-list cursor lifetime. */
Gfx *func_1510E634(Gfx *arg0, s32 arg1, s32 arg2) {
    extern u8 D_80089470[];
    Gfx *g = arg0++;

    g->words.w0 = 0xDA380003;
    g->words.w1 = (u32) D_80089470;
    return arg0;
}
