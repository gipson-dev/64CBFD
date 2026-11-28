#include <ultra64.h>
#include "structs.h"

extern f32 D_800BE9A4;
typedef struct { f32 height; s16 vertices[9]; s16 pad16; u32 metadata; u8 flags; u8 state; u16 pad1e; s32 value; } HeightResult71820;
s32 func_15046C80(f32 *, u16, f32, HeightResult71820 *);
typedef struct { f32 x, z, dx, dz, height, queryHeight, remaining; HeightResult71820 result; } EffectMotion;

extern u8 *D_800DBEF4;

/* Non-matching placeholders for the text-only asm slice asm/117490.s. */

s32 func_150E5AE0();

#pragma GLOBAL_ASM("asm/nonmatchings/generated_117490/func_150E9FE0.s")

s32 func_150EA10C(u8 *arg0) {
    *(s32 *)(arg0 + 0x80) = 0;
    return 1;
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_117490/func_150EA11C.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_117490/func_150EA490.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_117490/func_150EA500.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_117490/func_150EA5CC.s")

void func_150EA8E0(s32 arg0) {
    func_150E5AE0();
}

// Matched with guarded base/index and byte-update register lifetimes.
void func_150EA904(u8 arg0, s32 arg1) {
    u8 *temp_v0 = D_800DBEF4 + arg1 * 0xA0;

    if (*(temp_v0 + 0x72) == 0xE0) {
        *(temp_v0 + 0x73) |= 3;
    }
}

extern s32 D_800BE9E4;

/* Integrate the enabled effect's angles, fixed-point motion and life byte. */
void func_150EA944(u8 *effect) {
    f32 ticks;
    s32 remaining;

    if ((effect[0x73] & 3) == 3) {
        ticks = (f32)D_800BE9E4;
        *(f32 *)(effect + 0) += *(f32 *)(effect + 0x60) * ticks;
        if (*(f32 *)(effect + 0) < 0.0f) {
            *(f32 *)(effect + 0) += 360.0f;
        } else if (*(f32 *)(effect + 0) >= 360.0f) {
            *(f32 *)(effect + 0) -= 360.0f;
        }
        *(f32 *)(effect + 4) += *(f32 *)(effect + 0x64) * ticks;
        if (*(f32 *)(effect + 4) < 0.0f) {
            *(f32 *)(effect + 4) += 360.0f;
        } else if (*(f32 *)(effect + 4) >= 360.0f) {
            *(f32 *)(effect + 4) -= 360.0f;
        }
        *(f32 *)(effect + 8) += *(f32 *)(effect + 0x68) * ticks;
        if (*(f32 *)(effect + 8) < 0.0f) {
            *(f32 *)(effect + 8) += 360.0f;
        } else if (*(f32 *)(effect + 8) >= 360.0f) {
            *(f32 *)(effect + 8) -= 360.0f;
        }
        remaining = effect[0x8A];
        *(s16 *)(effect + 0x5C) = (u32)*(s16 *)(effect + 0x5C) -
            (u32)*(s32 *)(effect + 0x3C) * (u32)D_800BE9E4;
        *(s16 *)(effect + 0x10) = (u32)*(s16 *)(effect + 0x5A) * (u32)D_800BE9E4 +
            (u32)*(s16 *)(effect + 0x10);
        *(u32 *)(effect + 0x7C) += (u32)*(s16 *)(effect + 0x5C) * (u32)D_800BE9E4;
        *(s16 *)(effect + 0x12) = (s32)*(u32 *)(effect + 0x7C) >> 3;
        *(s16 *)(effect + 0x14) = (u32)*(s16 *)(effect + 0x5E) * (u32)D_800BE9E4 +
            (u32)*(s16 *)(effect + 0x14);
        remaining = (s32)((u32)remaining - ((u32)D_800BE9E4 << 2));
        if (remaining > 0) {
            effect[0x8A] = remaining;
        } else {
            effect[0x6E] = 1;
        }
    }
}


s32 func_150EAB10() {
    return 0;
}

/* Advance a moving effect, update its position and query ground height. */
s32 func_150EAE24(struct225 *record) {
    u8 *actor = (u8 *)record;
    f32 position[3];
    EffectMotion *motion = (EffectMotion *)(actor + 0x18);
    motion->x += motion->dx * D_800BE9A4;
    motion->z += motion->dz * D_800BE9A4;
    position[0] = motion->x;
    position[1] = motion->height;
    position[2] = motion->z;
    record->unk14->unkE = (s32)motion->x;
    record->unk14->unk12 = (s32)motion->z;
    if (func_15046C80(position, 0, motion->queryHeight, &motion->result)) {
        record->unk14->unk10 = (s32)motion->result.height;
    } else {
        record->unk14->unk10 = (s32)motion->height;
    }
    motion->remaining -= D_800BE9A4;
    if (motion->remaining <= 0.0f) return 0;
    return 1;
}
