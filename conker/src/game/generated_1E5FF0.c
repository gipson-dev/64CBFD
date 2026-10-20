#include <ultra64.h>
typedef struct {
    u8 header[0x20];
    f32 x;
    u8 reserved24[4];
    f32 z;
    u8 reserved2C[0x10];
    f32 oscillation;
    u8 reserved40[4];
    f32 phase;
    f32 base;
    f32 phaseRate;
    f32 velocityX;
    u8 reserved54[4];
    f32 velocityZ;
    f32 amplitude;
} OscillatingMotionRecord;


extern f32 D_800BE9A4;
f32 func_15144B68(f32 arg0);

/* Non-matching placeholders for the text-only asm slice asm/1E5FF0.s. */

/* Advance the oscillating field, phase and planar coordinates. */
s32 func_151B8B40(OscillatingMotionRecord *record) {
    record->oscillation = sinf(record->phase) * record->amplitude + record->base;
    record->phase += record->phaseRate * D_800BE9A4;
    record->phase = func_15144B68(record->phase);
    record->x += record->velocityX * D_800BE9A4;
    record->z += record->velocityZ * D_800BE9A4;
    return 1;
}

void func_151B8BE0(u8 *arg0, s32 arg1) {
    *(f32 *) (arg0 + 0x44) = sinf(*(f32 *) (arg0 + 0x58)) *
        *(f32 *) (arg0 + 0x64) + *(f32 *) (arg0 + 0x5C);
    *(f32 *) (arg0 + 0x58) += *(f32 *) (arg0 + 0x60) * D_800BE9A4;
    *(f32 *) (arg0 + 0x58) = func_15144B68(*(f32 *) (arg0 + 0x58));
    func_151D9450(arg0, arg1);
}

s32 func_151B8C54() {
    return 0;
}

s32 func_151B8CFC() {
    return 0;
}
