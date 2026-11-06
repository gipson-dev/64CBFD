#include <ultra64.h>
extern u8 D_80084494;
extern u8 D_80084490;
extern s32 D_8008448C;
extern f32 D_800C6850;
extern s32 D_80084488;

/* Non-matching placeholders for the text-only asm slice asm/6CEA0.s. */

typedef struct ControllerAxes1503F9F0 { u16 buttons; s8 x, y; } ControllerAxes1503F9F0;
extern ControllerAxes1503F9F0 **D_800BE728;
extern s16 D_80084484;
/* Sample the controller axes every fifth tick, consuming movement outside the dead zone. */
void func_1503F9F0(s16 slot, s16 *x, s16 *y) {
    s16 countdown;
    ControllerAxes1503F9F0 *pad;
    s32 value;

    pad = D_800BE728[slot];
    countdown = D_80084484 - 1;
    if (countdown != 0) {
        D_80084484 = countdown;
        *x = 0;
        *y = 0;
    } else {
        /* The table lookup has consumed slot; reuse its signed local for X. */
        slot = pad->x;
        D_80084484 = 5;
        if (slot < -20 || slot > 20) {
            *x = slot;
        } else {
            *x = 0;
        }
        value = pad->y;
        if (value < -20 || value > 20) {
            *y = value;
        } else {
            *y = 0;
        }
        pad->x = 0;
        pad->y = 0;
        *x = *x < -1 ? -1 : *x > 1 ? 1 : *x;
        *y = *y < -1 ? -1 : *y > 1 ? 1 : *y;
    }
}

void func_1503FB08(void) {
    D_80084488 = 0;
    D_800C6850 = 0.0f;
    D_8008448C = 0;
    D_80084490 = 0x1E;
    D_80084494 = 0;
}

s32 func_1503FB40() {
    return 0;
}
