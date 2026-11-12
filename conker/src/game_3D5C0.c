#include <ultra64.h>
#include "functions.h"
extern s32 D_800B0E00[];
extern s32 D_80090298[];
extern struct180 D_800963A0[];
s32 func_151ACBD4(struct179 *, s32);

/* Scene setup callback. */
void func_15010110(void);
/* End local declarations. */

/* Submit six records derived from the scene data table. */
/* Retail uses the same record layout as the nearby scene callback. */
void func_15010110(void) {
    struct179 record;
    s32 i;
    func_15195AA8(D_800B0E00[0], D_80090298[20], 0, -1, 0, 0, 0, -8);
    func_15195AA8(D_800B0E00[1], D_80090298[20], 0, -1, 0, 1, 0, -8);
    record.unk20 = 0;
    for (i = 0; i < 6; i++) {
        record.unk4 = D_800963A0[i];
        record.unk0 = i + 1;
        record.unk1C = fabsf(record.unk4.unk4 - record.unk4.unk10);
        func_151ACBD4(&record, 0);
    }
}
