#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/1C0B10.s. */

extern f32 D_800A81E8;

s32 func_15193660() {
    return 0;
}

typedef struct {
    u8 ownerTag;
    u8 padding1[3];
    u8 *owner;
    u8 field8;
    u8 padding9[3];
    f32 parameters[6];
    u8 kind;
    u8 padding25;
    s16 field26;
    s16 field28;
    s16 field2A;
    u8 padding2C[2];
    u8 field2E;
    u8 field2F;
    s8 field30;
    u8 padding31[3];
    f32 coefficient;
    u8 field38;
    s8 field39;
    u8 padding3A[2];
} GatedEffectPayload;
extern f32 D_800A81E4;
void *func_15134DAC(GatedEffectPayload *, s32);
/* Submit the sparse effect payload when its owner is present and enabled; retain guest padding. */
void func_151937F4(u8 *owner, s32 unused1, s32 unused2) {
    GatedEffectPayload payload;
    if (owner != 0 && *(u32 *)owner != 0) {
        payload.ownerTag = owner[0x3B];
        payload.owner = owner;
        payload.field8 = 0;
        payload.parameters[0] = -28.0f;
        payload.parameters[1] = 6.0f;
        payload.parameters[2] = 1.0f;
        payload.parameters[3] = -58.0f;
        payload.parameters[4] = -3.0f;
        payload.parameters[5] = -31.0f;
        payload.kind = 2;
        payload.field26 = 30;
        payload.field28 = 25;
        payload.field2A = 750;
        payload.field2E = 3;
        payload.field2F = 3;
        payload.field30 = -1;
        payload.field38 = 4;
        payload.field39 = -1;
        payload.coefficient = D_800A81E4;
        func_15134DAC(&payload, 0);
    }
}

s32 func_151938E4(u8 *arg0) {
    *(f32 *)(arg0 + 0x74) = D_800A81E8;
    return 1;
}

s32 func_151938FC() {
    return 0;
}
