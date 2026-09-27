#include <ultra64.h>

typedef struct {
    u8 pad0[0x28];
    f32 unk28;
    f32 unk2C;
    u8 pad30[0x20];
    s32 unk50;
    f32 unk54;
    f32 unk58;
    f32 unk5C;
    f32 unk60;
    u8 pad64[4];
} D_800DC2C0Record;

extern D_800DC2C0Record D_800DC2C0[];

/* Non-matching placeholders for the text-only asm slice asm/15ABA0.s. */

void func_1512D6F0(u8 *arg0) {
    D_800DC2C0Record *temp_v0 = &D_800DC2C0[arg0[0x23D]];

    temp_v0->unk50 = 5;
    temp_v0->unk54 = 0.0f;
    temp_v0->unk58 = 0.0f;
    temp_v0->unk5C = 0.0f;
    temp_v0->unk60 = 0.0f;
    temp_v0->unk2C = 0.0f;
    temp_v0->unk28 = -1.0f;
}

s32 func_1512D748() {
    return 0;
}

s32 func_1512D980() {
    return 0;
}
