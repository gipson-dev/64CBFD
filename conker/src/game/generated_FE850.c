#include <ultra64.h>
extern u8 D_800CC2D0[];
extern f32 D_800A08B0;
extern f32 D_800A08B4;
extern f32 D_800A08B8;
extern f32 D_800A08C0;
extern u8 D_800DCD20[];
void func_15059C84(u8 *arg0);
void func_151467A4(f32 *, f32, f32 *, f32, f32, f32, f32, f32 *);
void func_1515D4D4(s32, s32, s32, s32);

typedef struct {
    u8 pad0[0x3C];
    f32 scale;
    u8 pad40[0x78];
    f32 position;
    f32 velocity;
    f32 padC0;
    f32 liftPosition;
    u8 padC8[0x80];
    f32 liftVelocity;
} D13A0State;

/* Non-matching placeholders for the text-only asm slice asm/FE850.s. */

void func_150D13A0(u8 *arg0) {
    D13A0State *state = (D13A0State *) arg0;
    f32 velocity = state->velocity;

    state->position += velocity;
    state->velocity = velocity * D_800A08B0;
    state->scale *= D_800A08B4;
    state->liftPosition += state->liftVelocity;
    state->liftVelocity *= D_800A08B8;
    func_15059C84(arg0);
}

void func_150D1410(u8 *arg0) {
    u8 *temp_v0 = (u8 *) func_151149AC(0xF9);

    if (temp_v0 != 0) {
        if ((arg0 - D_800CC2D0) / 0x32C == 0) {
            temp_v0[0x6E] = 1;
        } else {
            temp_v0[0x6E] = 0;
        }
    }
}

void func_150D146C(u8 arg0) {
    u8 *temp_v0 = (u8 *) func_151149AC(0xF9);

    if (temp_v0 != 0) {
        temp_v0[0x6E] = 1;
    }
}

void func_150D149C(u8 *arg0) {
    f32 *color = (f32 *)(arg0 + 0x28);

    func_151467A4((f32 *)(arg0 + 0x30), 10.0f,
                  (f32 *)(arg0 + 0x2C), 50.0f, 100.0f, 123.0f,
                  D_800A08C0, color);
    func_1515D4D4(*color, D_800DCD20[1], D_800DCD20[2], 0);
}
