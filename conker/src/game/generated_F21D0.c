#include <ultra64.h>

extern s32 D_800BE9E4;
extern f32 D_800A03F0, D_800A03F4, D_800A03F8;
u16 func_10010F88(s32, u16, s16, u8, s32, s16, s16, s16, s16, s16);
f32 func_15048A40(u8);
/* Known prefix of the script-object record; the rest is owned by the engine. */
typedef struct {
    f32 angle;
    u8 pad4[0xC];
    s16 x, y, z;
    u8 pad16[0x39];
    u8 flags;
    u8 pad50[0x10];
    f32 angular_velocity;
    u8 pad64[0x18];
    s32 phase;
} AnglePhaseRecord;

extern u8 D_800C35E8;
extern u8 D_800C35EA;
extern s32 (*D_8008ADA8)();
extern void *D_800D98D0[4];
extern void *D_800D98E0;
extern void func_1516972C(void *arg0);

/* Non-matching placeholders for the text-only asm slice asm/F21D0.s. */

/* Advance angular spring motion and its periodic positional sound. */
void func_150C4D20(AnglePhaseRecord *state) {
    f32 velocity;
    f32 oscillation;
    f32 scale;
    s32 phase;
    f32 angle;

    angle = state->angle;
    velocity = state->angular_velocity;
    if (angle > 180.0f) {
        angle -= 360.0f;
    }
    phase = state->phase;
    phase = (s32)((u32)phase + (u32)D_800BE9E4);
    velocity -= angle * D_800A03F0;
    if ((f32)phase >= 256.0f) {
        phase = (s32)((f32)phase - 256.0f);
        func_10010F88(15, 0x55F0, 0, 0, 0, state->x, state->y, state->z, 500, 1000);
    }
    state->phase = phase;
    oscillation = func_15048A40((u8)phase);
    scale = D_800A03F4;
    velocity += oscillation * scale;
    if ((state->flags & 4) == 4) {
        velocity += scale;
    }
    velocity *= D_800A03F8;
    state->angular_velocity = velocity;
    state->angle += velocity;
    if (state->angle < 0.0f) {
        state->angle += 360.0f;
    } else if (state->angle >= 360.0f) {
        state->angle -= 360.0f;
    }
}

s32 func_150C4E9C() {
    return 0;
}

void func_150C522C(void) {
    void **current = D_800D98D0;
    void **end = &D_800D98E0;

    do {
        if (*current != NULL) {
            func_1516972C(*current);
        }
        *current++ = NULL;
    } while (current != end);
}

s32 func_150C5280(void) {
    if (D_800C35EA == 1) {
        u8 temp_v0 = D_800C35E8;

        if ((temp_v0 == 0xB) || (temp_v0 == 0xC) || (temp_v0 == 0xD)) {
            return 1;
        }
    }
    return 0;
}

s32 func_150C52CC(u8 *arg0) {
    if (func_150C5280() != 0) {
        return 0;
    }
    return D_8008ADA8(arg0);
}

s32 func_150C5310(u32 *arg0) {
    if (func_150C5280() != 0) {
        arg0[0x18] |= 0x20000;
    } else {
        arg0[0x18] &= ~0x20000;
    }
    return 1;
}
