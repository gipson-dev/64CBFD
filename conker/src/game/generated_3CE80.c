#include <ultra64.h>

#include "functions.h"
#include "variables.h"

/* Non-matching placeholders for the text-only asm slice asm/3CE80.s. */

void func_1500F9D0(s32 arg0, s32 arg1, s32 arg2, s32 arg3, s32 arg4) {
    struct04 *record = (struct04 *)func_151491F4(
        (s16)((func_150ADA20() & 0x7F) + 10), 1, -1, 1, 0, 10, 255, 0);

    if (record != NULL) {
        record->unk28 = arg0;
        record->unk2A = arg1;
        record->unk2C = arg2;
        record->unk2E = arg3;
        record->unk30 = arg4;
    }
}

s32 func_1500FA64() {
    return 0;
}
