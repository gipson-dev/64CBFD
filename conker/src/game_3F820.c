#include <ultra64.h>

#include "functions.h"
#include "variables.h"

typedef struct {
    f32 unused0;
    f32 horizontalExtent;
    f32 verticalExtent;
    u8 opaqueC[0x174];
} ViewProjectionSetup15012370;

/* Generated placeholder declarations. */
void func_15012370(void);
s32 func_150124A0();
/* End generated placeholder declarations. */

/* Rebuild each active view's projection matrix from its half extents. */
void func_15012370(void) {
    f32 halfWidth;
    f32 halfHeight;
    u8 index;
    f32 farPlane;

    index = 0;
    if (D_80082FA0 >= 0) {
        farPlane = D_80096560;
        do {
            halfWidth = ((ViewProjectionSetup15012370 *)(u32)D_800BE628)[index].horizontalExtent * 0.5f;
            halfHeight = ((ViewProjectionSetup15012370 *)(u32)D_800BE628)[index].verticalExtent * 0.5f;
            func_151EF954(((f32 (*)[4][4])D_800DCC10)[index],
                -halfWidth, halfWidth, -halfHeight, halfHeight,
                1.0f, farPlane, 1.0f);
            index++;
        } while (index <= D_80082FA0);
    }
}

void func_15012470(void) {
    D_80088750 = func_1518AADC(4, 300, 0);
}

/* Non-matching C placeholders for asm/nonmatchings/game_3F820/func_150124A0.s. */
s32 func_150124A0() {
    return 0;
}
