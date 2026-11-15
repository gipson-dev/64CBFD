#include <ultra64.h>

#include "functions.h"
extern u8 D_800BE616, D_800D2456, D_800D2457, D_800D2458;
extern struct102 *D_800D2E4C;
extern Mtx D_800D23D0;
extern u16 D_800D2454;
extern f32 D_800D2410[6], D_800D2428[3], D_800D2438[3];
extern s16 D_8009DCB4[3];
extern s32 D_800D2444, D_800D2588, D_800D24C0;
extern struct256 *D_800D245C;
extern u8 D_800D2460[6][16];
extern u8 D_800D24C8[0xC0];
extern f32 D_800968B0;

/* Generated placeholder declarations. */
void func_15017640(void);
/* End generated placeholder declarations. */

void func_150175E0(void) {
    if ((D_800BE616 == 0) && ((D_800D2E4C->unk18 & 1) == 0)) {
        D_800D2457 = D_800D2456 = 3;
    } else {
        D_800D2457 = D_800D2456 = 6;
    }
}

/* Reset view motion, six scale/record entries, and perspective state. */
void func_15017640(void) {
    s32 index;
    f32 *scale;

    D_800D2458 = 0;
    D_800D2588 = 0;
    D_800D2438[0] = 0.0f;
    D_800D2438[1] = 0.0f;
    D_800D2438[2] = 0.0f;
    D_800D2428[0] = D_8009DCB4[0];
    D_800D2428[1] = D_8009DCB4[1];
    D_800D2428[2] = D_8009DCB4[2];
    D_800D2444 = 0;
    D_800D245C = 0;
    for (scale = D_800D2410; scale < D_800D2410 + 6; scale++) {
        *scale = 1.0f;
    }
    for (index = 0; index < 6; index++) {
        D_800D2460[index][13] = 0;
    }
    D_800D24C0 = 0;
    bzero(D_800D24C8, sizeof(D_800D24C8));
    guPerspective(&D_800D23D0, &D_800D2454,
                  50.0f, 60.6f, 53.0f, D_800968B0, 1.0f);
}
