#include <ultra64.h>

/* Recovered routines and remaining placeholders for asm/1A6360.s. */

extern u8 *D_800DBFF0;
extern s16 D_800DD436;
extern u8 **D_800DD440;

s32 func_15178EB0() {
    return 0;
}

s32 func_15178EFC() {
    return 0;
}

s32 func_15179008() {
    return 0;
}

s32 func_151794C8() {
    return 0;
}

s32 func_15179600() {
    return 0;
}

s32 func_151797B0() {
    return 0;
}

void func_15179AB8(void) {
    s32 i;
    u8 *object;
    u32 flags;

    for (i = D_800DD436 - 1; i >= 0; i--) {
        object = D_800DD440[i];
        if (object != NULL) {
            flags = *(u32 *) (object + 0x90);
            if (!(flags & 2)) {
                *(u32 *) (object + 0x90) = flags | 2;
                return;
            }
        }
    }
}

s32 func_15179B14() {
    return 0;
}

/* Derive the record opacity byte from planar viewer distance. */
void func_15179CB0(u8 *record) {
    f32 dx;
    f32 dz;
    f32 distance;
    u8 *viewer;

    viewer = D_800DBFF0;
    dx = (f32)*(s16 *)(record + 0xA0) - *(f32 *)(viewer + 0x300);
    dz = (f32)*(s16 *)(record + 0x9C) - *(f32 *)(viewer + 0x2F8);
    distance = sqrtf(dx * dx + dz * dz);
    record[0xB4] = (u32)(255.0f - distance * 160.0f / 1000.0f);
}
