#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/EEE70.s. */

s32 func_150C19C0(void *arg0, u8 *arg1, u8 arg2) {
    s32 command;

    switch (arg2) {
        case 1:
            command = 0x18;
            break;
        case 2:
            command = 0x15;
            break;
    }
    func_15142314(*(s32 *) (arg1 + 0x1D4), command, arg0);
    return 1;
}

s32 func_150C1A2C(s32 arg0, s32 arg1) {
    return 7;
}

s32 func_150C1A40() {
    return 0;
}

typedef struct {
    f32 position[3];
    u8 retained0C[10];
    s16 value16, value18, value1A, value1C, value1E, value20;
    s16 value22, value24, value26;
    u8 firstRGB[3], secondRGB[3], alpha, value2F;
    s8 value30;
    u8 flags;
} EffectDescriptor150C1E34;
extern f64 D_800A0228;
void func_151429E0(u8, u8 *, u8 *, u8 *);
s32 func_150ADA20(void);
void func_1518CA80(EffectDescriptor150C1E34 *, u8);

s32 func_150C1E34(s32 type, s32 index, f32 x, f32 y, f32 z,
                  f32 previousX, f32 previousY, f32 previousZ,
                  s32 angle, s32 originalAngle, f32 radius,
                  s32 unused, f32 scale, s32 extra, s32 flags) {
    EffectDescriptor150C1E34 descriptor;
    descriptor.position[0] = x;
    descriptor.position[1] = y;
    descriptor.position[2] = z;
    descriptor.value16 = (s16)(s32)scale;
    descriptor.value18 = (s16)(s32)scale;
    descriptor.value1A = (s16)(s32)(scale * D_800A0228);
    descriptor.value1C = (s16)(s32)(scale * D_800A0228);
    descriptor.value1E = (s16)(s32)((x - previousX) * 10.0f);
    descriptor.value20 = (s16)(s32)((z - previousZ) * 10.0f);
    descriptor.value22 = 150;
    descriptor.value24 = 20;
    descriptor.value26 = 600;
    func_151429E0(0, &descriptor.firstRGB[0], &descriptor.firstRGB[1], &descriptor.firstRGB[2]);
    func_151429E0(0, &descriptor.secondRGB[0], &descriptor.secondRGB[1], &descriptor.secondRGB[2]);
    descriptor.alpha = 255;
    descriptor.value2F = 255;
    descriptor.value30 = (func_150ADA20() & 15) + 12;
    descriptor.flags = 1;
    func_1518CA80(&descriptor, 1);
    return 1;
}
