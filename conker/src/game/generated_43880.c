#include <ultra64.h>

/* Resource table loader recovered from the text-only asm slice asm/43880.s. */

extern u32 *D_800D18B0;
u32 func_1502B7F0(void **output, u32 depth, ...);

/* Load the zero-terminated offset table and relocate each entry in place. */
void func_150163D0(u32 resource) {
    s32 count, i;
    u32 *cursor;
    if ((s32)func_1502B7F0((void **)&D_800D18B0, 3, 12, resource, 9) > 0) {
        count = 0;
        cursor = D_800D18B0;
        if (*cursor != 0) {
            do { count++; cursor += 2; } while (*cursor != 0);
        }
        for (i = 0; i < count; i++) {
            D_800D18B0[i * 2] += (u32)D_800D18B0;
        }
    } else {
        D_800D18B0 = NULL;
    }
}
