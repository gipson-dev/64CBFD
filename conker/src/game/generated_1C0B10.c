#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/1C0B10.s. */

extern f32 D_800A81E8;

typedef struct {
 s32 baseCount, countRange;
 f32 position[3];
 s16 field14,field16,field18,field1A;
 f32 parameters[5];
 s16 field30,field32;
 s32 field34,field38,field3C;
 f32 values[10];
 u8 colors[8];
 u8 field70,field71;
 s16 field72,field74;
 u8 padding76[2];
} PointEffectPayload;
void func_15142314(u8 *,s32,f32 *);
void func_15152520(PointEffectPayload *,u8,s32);
extern f32 D_800A81C0;
extern f32 D_800A81C4;
extern f32 D_800A81C8;
extern f32 D_800A81CC;
extern f32 D_800A81D0;
extern f32 D_800A81D4;
extern f32 D_800A81D8;
extern f32 D_800A81DC;
extern f32 D_800A81E0;
/* Resolve attached point 10 and submit its live particle parameters after validating the owner. */
void func_15193660(u8 *owner, s32 mode, s32 extra) {
    PointEffectPayload payload;
    u8 *attached;
    if (owner != 0 && *(u32 *)owner != 0) {
        attached = *(u8 **)(owner + 0x1D4);
        if (attached != 0) {
            func_15142314(attached, 10, payload.position);
            payload.baseCount = 8;
            payload.countRange = 7;
            payload.values[6] = D_800A81C0;
            payload.values[4] = D_800A81C0;
            payload.values[9] = D_800A81C4;
            payload.values[7] = D_800A81C4;
            payload.parameters[0] = D_800A81C8;
            payload.field14 = 0;
            payload.field16 = 255;
            payload.field18 = -33;
            payload.field1A = 24;
            payload.field30 = 40;
            payload.field32 = 35;
            payload.field34 = 160;
            payload.field38 = 19;
            payload.field3C = 0;
            payload.field70 = 33;
            payload.colors[0] = 255;
            payload.colors[1] = 255;
            payload.colors[2] = 255;
            payload.colors[3] = 255;
            payload.colors[4] = 255;
            payload.colors[5] = 255;
            payload.colors[6] = 255;
            payload.colors[7] = 255;
            payload.field71 = 15;
            payload.field72 = 25;
            payload.field74 = 10;
            payload.parameters[1] = D_800A81CC;
            payload.parameters[2] = D_800A81D0;
            payload.parameters[3] = D_800A81D4;
            payload.parameters[4] = D_800A81D8;
            payload.values[1] = D_800A81DC;
            payload.values[0] = 0;
            payload.values[3] = 0;
            payload.values[5] = 0.0f;
            payload.values[8] = 0.0f;
            payload.values[2] = D_800A81E0;
            func_15152520(&payload, (u8)mode, extra);
        }
    }
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
