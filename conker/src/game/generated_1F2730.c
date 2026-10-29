#include <ultra64.h>
#include "structs.h"

/* Non-matching placeholders for the text-only asm slice asm/1F2730.s. */

s32 func_151C5280() {
    return 0;
}

s32 func_151C5588() {
    return 0;
}

s32 func_150ADA20(void);
struct225 *func_151602C0(Header *, Header2 *, s32, s32, s32, s32, u8, u8, s32, u8, s32);

/* Submit a randomized effect at the position's truncated integer coordinates. */
void func_151C56A4(f32 *position, u8 kind, s32 mode) {
    Header header;
    Header2 coordinates;

    header.unk0 = 3;
    header.unk1 = -1;
    header.unk2 = (u32)func_150ADA20() % 3U + 3;
    header.unk4 = 0;
    coordinates.unk0 = position[0];
    coordinates.unk4 = position[1];
    coordinates.unk8 = position[2];
    func_151602C0(&header, &coordinates, ((u32)func_150ADA20() & 1) + 6,
                 0xFF, 0xE8, 0xAB, 0xFF, 0, 0, kind, mode);
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1F2730/func_151C577C.s")


#pragma GLOBAL_ASM("asm/nonmatchings/generated_1F2730/func_151C5E74.s")


s32 func_151C5F44() {
    return 0;
}

s32 func_151C61A0() {
    return 0;
}

s32 func_151C6290(u8 *arg0, u8 arg1, u8 arg2) {
    u8 temp_v0 = *(arg0 + 4);

    if ((temp_v0 == 0x5A) || (temp_v0 == 0x74) || (temp_v0 == 0x7A)) {
        return 0;
    }
    return 1;
}
