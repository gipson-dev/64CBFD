#include <ultra64.h>

typedef struct {
    f32 coefficient;
    u8 pad4[0x14];
} struct1AFC80Coefficient;

extern struct1AFC80Coefficient D_8008D058[];
extern u8 D_800DDE54[];

/* Non-matching placeholders for the text-only asm slice asm/1AFC80.s. */

s32 func_151827D0() {
    return 0;
}

s32 func_15182C5C() {
    return 0;
}

f32 func_15182F58(s32 arg0, s32 arg1) {
    f32 value;

    value = D_8008D058[D_800DDE54[arg1]].coefficient * (f32) (arg0 * 40);
    if (value < 0.0f) {
        value = 0.0f;
    } else if (value > 39.0f) {
        value = 39.0f;
    }
    return value;
}

s32 func_15182FDC() {
    return 0;
}
