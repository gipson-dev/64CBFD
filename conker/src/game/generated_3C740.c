#include <ultra64.h>
#include "structs.h"
typedef struct {
    u32 flags;
    s16 count;
    u8 category;
    u8 pad7;
    s32 zero;
    s32 phase;
    u8 color[6];
    u8 pad16[2];
    u32 mode;
    u8 pad1C[12];
} RandomEffectDescriptor;
s32 func_151EF610(void);
struct210 *func_1513C5B0(s32, s32, u8, u8, f32, f32, f32, f32, f32, u8, u8, s32, u8, s32);

#include "functions.h"
#include "variables.h"

/* Non-matching placeholders for the text-only asm slice asm/3C740.s. */

/* Spawn an effect with a signed random phase and fixed dimensions. */
struct210 *func_1500F290(f32 x, f32 y, f32 z) {
    RandomEffectDescriptor descriptor;
    s32 random;

    descriptor.category = 0x38;
    descriptor.zero = 0;
    random = func_151EF610();
    descriptor.phase = random % 0x1000 + 0x4000;
    descriptor.flags = 0x20014;
    descriptor.count = 1;
    descriptor.color[0] = 255;
    descriptor.color[1] = 255;
    descriptor.color[2] = 0;
    descriptor.color[3] = 0;
    descriptor.color[4] = 0;
    descriptor.color[5] = 255;
    descriptor.mode = 0x30001;
    return func_1513C5B0((s32)&descriptor, 0, 0, 0, x, y, z, 110.0f, 110.0f, 0, 0, 0, 255, 0);
}

void func_1500F378(s32 arg0, s32 arg1, s32 arg2, s32 arg3) {
    struct04 *record = (struct04 *)func_151491F4(
        (s16)((func_150ADA20() & 0x7F) + 10), 1, -1, 1, 0, 10, 255, 0);

    if (record != NULL) {
        record->unk28 = arg0;
        record->unk2A = arg1;
        record->unk2C = arg2;
        record->unk2E = arg3;
        record->unk30 = 1;
    }
}

s32 func_1500F40C() {
    return 0;
}
