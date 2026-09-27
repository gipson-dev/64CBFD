#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/DAD60.s. */

// Handwritten vector cross product. IDO -O2 and -O3 both emit a 21-word
// body with an FP hazard nop and an empty return delay slot; retail uses a
// tightly interleaved 19-word schedule and stores y in the return delay slot.
// Keep the behaviorally equivalent C for documentation.
#if 0
void func_150AD8B0(f32 *arg0, f32 *arg1, f32 *arg2) {
    f32 x0 = arg0[0];
    f32 y0 = arg0[1];
    f32 z0 = arg0[2];
    f32 x1 = arg1[0];
    f32 y1 = arg1[1];
    f32 z1 = arg1[2];

    arg2[0] = y0 * z1 - z0 * y1;
    arg2[1] = z0 * x1 - x0 * z1;
    arg2[2] = x0 * y1 - y0 * x1;
}
#endif
#pragma GLOBAL_ASM("asm/nonmatchings/generated_DAD60/func_150AD8B0.s")
