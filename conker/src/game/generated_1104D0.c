#include <ultra64.h>
extern f32 D_800BE9A4;
extern f32 D_800A1054;

typedef struct {
    u8 type;
    u8 pad1[0xF];
    f32 x;
    f32 y;
    f32 z;
} Generated1104D0Actor;

extern Generated1104D0Actor *D_800D99D0[8];

void func_151C3B0C(void *, f32, f32, f32, f32, s32, s32, s32);

/* Non-matching placeholders for the text-only asm slice asm/1104D0.s. */

s32 func_150E3020() {
    return 0;
}

s32 func_150E3208() {
    return 0;
}

s32 func_150E32D0() {
    return 0;
}

s32 func_150E3340() {
    return 0;
}

s32 func_150E33CC(s32 arg0, s32 arg1, s32 *arg2, s32 arg3) {
    s32 temp_v0 = *arg2;

    if (temp_v0 == 0) {
        return 1;
    }
    func_1000E7A0(2, temp_v0);
    return 0;
}

s32 func_150E3414() {
    return 0;
}

s32 func_150E3514() {
    return 0;
}

s32 func_150E35DC() {
    return 0;
}

void func_150E36BC(s32 arg0, s32 *arg1, s32 *arg2, s32 *arg3) {
    Generated1104D0Actor *actor;

    arg0--;
    if ((arg0 >= 0) && (arg0 < 8)) {
        actor = D_800D99D0[arg0];
        if ((actor != NULL) && (actor->type == 0x27)) {
            *arg1 = actor->x;
            *arg2 = actor->y;
            *arg3 = actor->z;
        }
    }
}

s32 func_150E3738() {
    return 0;
}

s32 func_150E4010() {
    return 0;
}

void func_150E411C(void *arg0) {
    func_151C3B0C(arg0, 0.352000028f, 0.701000035f, 0.566000044f, D_800A1054,
                  0xFF, 0xFF, 0xFF);
}

s32 func_150E4174(u8 *arg0) {
    *(f32 *) (arg0 + 0x2C) = *(f32 *) (arg0 + 0x4C) * D_800BE9A4 + *(f32 *) (arg0 + 0x2C);
    *(f32 *) (arg0 + 0x30) = *(f32 *) (arg0 + 0x54) * D_800BE9A4 + *(f32 *) (arg0 + 0x30);
    return 1;
}
