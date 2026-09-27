#include <ultra64.h>
#include "structs.h"

/* Non-matching placeholders for the text-only asm slice asm/135780.s. */

typedef struct {
    s32 unk0;
    s32 unk4;
    u8 flags;
} EventFlags;

s32 func_151082D0() {
    return 0;
}

s32 func_15108658() {
    return 0;
}

void func_151087FC(struct126 *arg0, s32 arg1, u8 arg2) {
    EventFlags *value = (EventFlags *)((s32)arg0 + 0x28);

    if (arg2 == 0x2B) {
        value->flags |= 1;
    } else if (arg2 == 0x2C) {
        value->flags &= ~1;
    }
}
