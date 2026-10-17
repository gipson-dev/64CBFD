#include <ultra64.h>
extern f32 D_800A0878, D_800A087C, D_800BE9A4;
f32 fabsf(f32);
#pragma intrinsic (fabsf)
extern s32 D_80082FA0;
/* The view byte occupies the first byte of a word-aligned descriptor cell. */
typedef union {
    u8 byte;
    s32 word;
} TransitionViewFC5F0;
typedef struct {
    f32 position[2];
    f32 scale[2];
    u8 tag;
    s16 id;
    u16 flags;
    s16 size0, size1;
    u8 kind, field1B, field1C, field1D, duration, field1F;
    u8 field20, field21, field22, opacity;
    s32 field24, field28, field2C, field30, field34, field38, field3C;
    u8 field40, field41;
    TransitionViewFC5F0 view;
    f32 field48, field4C, field50, field54;
} TransitionDescriptorFC5F0;
typedef struct {
    u8 state;
    f32 field04, field08, field0C;
} TransitionPayloadFC5F0;
void *func_1515548C(void *, s32, s32 *, s32, s32, u8, s32);
void func_151CF898(u8 *, f32, f32);
extern u8 D_800CC2D0[];
void *memcpy(void *dst, const void *src, unsigned int len);
extern s32 D_80088890;
extern s32 D_80088894;
extern s32 D_80088898;
extern s32 D_8008889C;
extern s32 D_800BE9E4;
extern s32 (*D_800888A0[])(u8 *arg0);
extern s32 (*D_800888B0[])(u8 *arg0, u8 *arg1, u8 arg2);

typedef struct {
    u8 pad0[0x14];
    u8 size;
    u8 index;
    u8 pad16[2];
    u8 *buffers[2];
} BufferState;

/* Non-matching placeholders for the text-only asm slice asm/FC5F0.s. */

s32 func_150CF140() {
    return 0;
}

s32 func_150CF484() {
    return 0;
}

void func_150CF530(s32 arg0) {
    func_151CF898(D_800CC2D0, *(f32 *) (D_800CC2D0 + 0x18) + 300.0f, -10000.0f);
}

void func_150CF578(s32 arg0) {
    s32 value = D_800BE9E4;
    s32 temp = value * 28;

    D_80088890 += value * 26;
    D_80088894 -= temp;
    D_80088898 -= temp;
}

/* Publish the two scrolling texture-tile windows. */
Gfx *func_150CF5E8(Gfx *commands) {
    gDPSetTileSize(commands++, 0, D_80088890 >> 7, D_80088894 >> 7, 0x47E, 0x47E);
    gDPSetTileSize(commands++, 1, D_80088898 >> 7, D_8008889C >> 7, 0x47E, 0x47E);
    return commands;
}

/* Create the fixed descriptor and attach its transition payload. */
void func_150CF680(s16 id, u8 slot, s32 context) {
    TransitionDescriptorFC5F0 descriptor;
    TransitionPayloadFC5F0 payload;
    u8 *event;

    descriptor.position[1] = 72.0f;
    descriptor.tag = 0xC1;
    descriptor.id = id;
    descriptor.flags = 0x31;
    descriptor.size0 = 1;
    descriptor.size1 = 0xFF;
    descriptor.kind = 8;
    descriptor.field1B = 0xFF;
    descriptor.field1C = 0xFF;
    descriptor.field1D = 0xFF;
    descriptor.duration = 0xFF;
    descriptor.field1F = 0xFF;
    descriptor.field20 = 0xFF;
    descriptor.field21 = 0xFF;
    descriptor.field22 = 0xFF;
    descriptor.opacity = 0xFF;
    descriptor.field28 = 0x200004;
    payload.state = 0;
    payload.field04 = 0.0f;
    descriptor.position[0] = -300.0f;
    payload.field08 = -300.0f;
    payload.field0C = 0.0f;
    descriptor.scale[1] = 7.5f;
    descriptor.scale[0] = 7.5f;
    descriptor.field24 = 0;
    descriptor.field2C = 0x9F0601;
    descriptor.field40 = 0;
    descriptor.field41 = 10;
    descriptor.field30 = 23;
    descriptor.field34 = 68;
    descriptor.field38 = 128;
    descriptor.field3C = 32;
    descriptor.field4C = 1.0f;
    descriptor.field48 = 1.0f;
    descriptor.field54 = 0.0f;
    descriptor.field50 = 0.0f;
    descriptor.view.byte = D_80082FA0;
    event = func_1515548C(&descriptor, 12, 0, 0, 16, slot, context);
    if (event != 0) {
        memcpy(event + 0x70, &payload, 16);
    }
}

s32 func_150CF800() {
    return 0;
}

void func_150CFBEC(u8 *arg0, f32 *arg1, u8 arg2) {
    u8 *temp_v0 = arg0 + 0x70;

    if (arg2 == 0x52) {
        *temp_v0 |= 1;
        *(f32 *) (temp_v0 + 4) = 0.0f;
        *(f32 *) (temp_v0 + 8) = *(volatile f32 *) (arg0 + 0x10);
        *(f32 *) (temp_v0 + 0xC) = *arg1 - *(volatile f32 *) (arg0 + 0x10);
    }
}

s32 func_150CFC38(f32 arg0) {
    f32 value = arg0;

    func_1515572C(&value, 0x52);
}

/* Advance the child and damp its velocity after crossing the floor. */
s32 func_150CFC60(u8 *record) {
    f32 velocityY = *(f32 *)(record + 0x74);
    f32 acceleration = *(f32 *)(record + 0x78);
    f32 *motion;

    *(f32 *)(record + 0x10) += *(f32 *)(record + 0x70) * D_800BE9A4;
    *(f32 *)(record + 0x14) += velocityY * D_800BE9A4 + 0.5f * acceleration * D_800BE9A4 * D_800BE9A4;
    *(f32 *)(record + 0x74) = velocityY + acceleration * D_800BE9A4;
    motion = (f32 *)(record + 0x70);
    if (*(f32 *)(record + 0x7C) < *(f32 *)(record + 0x14)) {
        *(f32 *)(record + 0x14) = motion[3];
        velocityY = fabsf(motion[1]);
        motion[0] *= D_800A0878;
        motion[1] = velocityY * D_800A087C;
    }
    return 1;
}

u8 *func_150CFD20(u8 *arg0) {
    if (*arg0 != 0xBD && *arg0 != 0) {
        do {
            arg0++;
        } while (*arg0 != 0xBD && *arg0 != 0);
    }
    return arg0;
}

u8 *func_150CFD5C(u8 *arg0) {
    if (*arg0 != 0) {
        do {
            arg0++;
        } while (*arg0 != 0);
    }
    return arg0;
}

s32 func_150CFD84(u8 *arg0, u8 **arg1) {
    u8 *end = (u8 *) func_150CFD20(arg0);

    *arg1 = end;
    return end - arg0;
}

s32 func_150CFDB8(u8 *arg0) {
    s32 max = 0;
    u8 *end = func_150CFD5C(arg0);
    u8 *next;

    if (arg0 < end) {
        do {
            s32 len = func_150CFD84(arg0, &next);

            if (max < len) {
                max = len;
            }
            arg0 = next + 1;
        } while (arg0 < end);
    }
    return max;
}

void func_150CFE3C(u8 *arg0) {
    BufferState *state;

    memcpy(*(void **) (arg0 + *(arg0 + 0x3D) * 4 + 0x40),
           *(void **) (arg0 + 0x34), *(arg0 + 0x3C));
    state = (BufferState *) (arg0 + 0x28);
    state->buffers[state->index][state->size] = 0;
}

void func_150CFE98(u8 *arg0) {
    u8 *sub = arg0 + 0x28;

    if (**(u8 **) (arg0 + 0x38) != 0) {
        *(sub + 0x14) = (u8) func_150CFD84(
            *(u8 **) (sub + 0xC) = *(u8 **) (sub + 0x10) + 1,
            (u8 **) (sub + 0x10));
        *(sub + 0x15) ^= 1;
        func_150CFE3C(arg0);
        *(sub + 0x8) |= 1;
    }
}

void *func_150CFF10(u8 arg0, u8 *arg1, s16 arg2, s32 arg3, s8 arg4,
                    u8 arg5, u8 arg6, s32 arg7) {
    return 0;
}

s32 func_150D0034(u8 *arg0, u8 *arg1, s32 arg2) {
    u8 *sub;

    if (*(volatile s8 *) (arg1 + 0x4C) == -1) {
        sub = arg1 + 0x28;
    } else {
        if (D_800888A0[*(volatile s8 *) (arg1 + 0x4C)](arg1) == 0) {
            *(s16 *) (arg1 + 0xE) = -1;
            return (s32) arg0;
        }
        sub = arg1 + 0x28;
    }
    *(sub + 8) &= ~1;
    return (s32) arg0;
}

void func_150D00C0(u8 *arg0, u8 *arg1, u8 arg2) {
    if (arg2 == 0x51) {
        if (*(arg0 + 0x28) == *arg1) {
            func_150CFE98(arg0);
        }
    } else {
        s32 (*fn)(u8 *, u8 *, u8) = D_800888B0[*(arg0 + 0x4D)];

        if (fn != 0) {
            fn(arg0, arg1, arg2);
        }
    }
}

void func_150D0134(u8 arg0, u8 *arg1, s16 arg2, u8 arg3, s32 arg4) {
    u8 zero[8];
    void *result;

    zero[0] = 0;
    result = func_150CFF10(arg0, arg1, arg2, 8, 0, 0, arg3, arg4);
    if (result != 0) {
        memcpy(*(void **) ((u8 *) result + 0x48), zero, 1);
    }
}

s32 func_150D01A0() {
    return 0;
}

void func_150D02B4(u8 arg0, u8 *arg1, s16 arg2, u8 arg3, s32 arg4) {
    struct { f32 word0; s16 half0; u8 tail[4]; } rec;
    void *result;

    rec.word0 = 0.0f;
    rec.half0 = 0;
    result = func_150CFF10(arg0, arg1, arg2, 8, 1, 0, arg3, arg4);
    if (result != 0) {
        memcpy(*(void **) ((u8 *) result + 0x48), &rec, 8);
    }
}

s32 func_150D032C() {
    return 0;
}

void func_150D04C4(u8 arg0, u8 *arg1, s16 arg2, u8 arg3, s32 arg4) {
    u8 zero[8];
    void *result;

    zero[0] = 0;
    result = func_150CFF10(arg0, arg1, arg2, 8, 2, 0, arg3, arg4);

    if (result != 0) {
        memcpy(*(void **) ((u8 *) result + 0x48), zero, 1);
    }
}

s32 func_150D0534() {
    return 0;
}
