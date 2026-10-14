#include <ultra64.h>
extern f32 D_800A0700;
extern f32 D_800A0704;
extern f32 D_800A0708;
extern f32 D_800A070C;

/* Non-matching placeholders for the text-only asm slice asm/FA240.s. */

/* Compute the three-channel piecewise color ramp. */
void func_150CCD90(f32 level, f32 *red, f32 *green, f32 *blue) {
    f32 temp_f0;
    f32 temp_f0_2;

    if (level > 0.0f) {
        *red = 255.0f;
        *green = 255.0f;
        *blue = 255.0f;
        return;
    }
    if (D_800A0700 < level) {
        temp_f0 = -level * D_800A0704;
        *red = 255.0f - (temp_f0 * 83.0f);
        *green = 255.0f - (temp_f0 * 113.0f);
        *blue = 255.0f - (temp_f0 * 173.0f);
        return;
    }
    temp_f0_2 = -(level + D_800A0708) * D_800A070C;
    *red = 172.0f - (temp_f0_2 * 50.0f);
    *green = 142.0f - (temp_f0_2 * 42.0f);
    *blue = 82.0f - (temp_f0_2 * -1.0f);
}
