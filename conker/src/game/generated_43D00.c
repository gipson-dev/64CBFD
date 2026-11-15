#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/43D00.s. */

#include "structs.h"
extern u8 D_800BE590, D_800D2100;
extern struct258 *D_800D20FC;
extern u16 D_800BE598[];
extern void *D_800BE5A8[];
u32 func_1502B7F0(void **output, u32 depth, ...);

/* Cache each distinct record resource, retaining the loader's live output. */
void func_15016850(void) {
    s32 offset, index, found;
    void *handle;
    s32 resource, limit;

    handle = 0;
    D_800BE590 = 0;
    offset = 0;
    if (D_800D2100 > 0) {
      do {
        resource = ((u8 *)D_800D20FC)[offset + 4];
        found = 0;
        for (index = 0; index < D_800BE590; index++) {
            if (resource == D_800BE598[index]) {
                found = 1;
                break;
            }
        }
        if (!found) {
            if (resource < 187) func_1502B7F0(&handle, 2, 18, resource);
            if (handle != 0) {
                D_800BE5A8[D_800BE590] = handle;
                D_800BE598[D_800BE590] = resource;
                D_800BE590++;
            }
        }
        limit = D_800D2100 << 2;
        limit -= D_800D2100;
        limit <<= 4;
        offset += 48;
      } while (offset < limit);
    }
}

s32 func_150169A0() {
    return 0;
}

s32 func_15017114() {
    return 0;
}
