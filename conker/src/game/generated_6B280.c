#include <ultra64.h>
#include "structs.h"

/* Non-matching placeholders for the text-only asm slice asm/6B280.s. */

extern struct160 *D_800C6650;
extern s32 D_800C6654;

void func_1503DDD0(s32 arg0) {
    s32 count;
    struct160 *entry;

    if ((arg0 < 0) || ((u32)arg0 >= (u32)D_800C6654)) {
        return;
    }

    D_800C6650[arg0].unk6 = 2;
    count = D_800C6654;
    if (count != 0) {
        entry = &D_800C6650[count - 1];
        while ((entry->unk6 & 2) != 0) {
            count--;
            D_800C6654 = count;
            if (count == 0) {
                break;
            }
            entry--;
        }
    }
}
