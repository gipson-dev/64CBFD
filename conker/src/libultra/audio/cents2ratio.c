/*
 * alCents2Ratio()
 *
 * Calculates the pitch shift ratio from the number of cents according to
 *      ratio = 2^(cents/1200)
 *
 * This is accurate to within one cent for ratios up an octave and down
 * two ocataves.
 */

#include <libaudio.h>

extern f32 D_8002C760;
extern f32 D_8002C764;

/* Original rodata at 0x8002C760; keep the external retail address aliases. */
const f32 conkerCentsRatios[] = {1.0005778074264526f, 0.999422550201416f};

f32 alCents2Ratio(s32 cents) {
    f32 x;
    f32 ratio = 1.0f;

    if (cents >= 0) {
        x = D_8002C760; /* 2^(1/1200) */
    } else {
        x = D_8002C764;  /* 2^(-1/1200) */
        cents = -cents;
    }
    while (cents) {
        if (cents & 1) {
            ratio *= x;
        }
        x *= x;
        cents >>= 1;
    }
    return ratio;
}
