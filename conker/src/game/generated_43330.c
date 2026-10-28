#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/43330.s. */

#include "structs.h"
extern struct104 *D_800B0DF0;
extern s32 D_800BE9C8[];
extern s32 D_800BEBA4;
s32 allocate_memory(s32, s32, s32, s32);

/* Allocate both display-list buffers and reserve 400 commands below their address gap. */
void func_15015E80(void) {
    if (*(u16 *)((u8 *)D_800B0DF0 + 0x1C) == 0) {
        *(u16 *)((u8 *)D_800B0DF0 + 0x1C) = 8000;
    }
    *(u16 *)((u8 *)D_800B0DF0 + 0x1C) += 400;
    D_800BE9C8[0] = allocate_memory(*(u16 *)((u8 *)D_800B0DF0 + 0x1C) << 3, 255, 2, 0);
    D_800BE9C8[1] = allocate_memory(*(u16 *)((u8 *)D_800B0DF0 + 0x1C) << 3, 255, 2, 0);
    D_800BEBA4 = ((s32)((u32)D_800BE9C8[1] - (u32)D_800BE9C8[0]) >> 3) - 400;
}
