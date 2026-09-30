#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/12B1C0.s. */

extern u8 D_800C35EA;
extern u8 D_800CC2D0[];
extern s32 D_800D121C;

void func_150ED638(void *arg0, s32 arg1, s32 arg2);
void func_15103828(void);

// Retail leaves v0 unspecified; five guards normalize one saved-register cycle.
s32 func_150FDD10(void *arg0) {
    u8 *record;
    s32 targetType;
    u8 *end;

    func_15103828();
    if (D_800C35EA == 1) {
        targetType = 0x28;
        record = D_800CC2D0;
        end = (u8 *)&D_800D121C;
        do {
            if (record[4] == targetType) {
                func_150ED638(record, 0x14, 0x14);
            }
            record += 0x32C;
        } while (record != end);
    }
}
