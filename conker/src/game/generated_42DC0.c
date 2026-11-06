#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/42DC0.s. */

extern u8 D_800CBD4C;

void func_15015910(void) {
    D_800CBD4C = 0;
}

typedef struct AssetRange15015920 { s32 start, end; } AssetRange15015920;
extern AssetRange15015920 D_80082F80[];
s32 func_10003C6C(s32, s32, s32, s32, s32);
s32 func_10004514(s32, void *, u32, s32);
void func_10004074(void *);
/* Retail consumes (u8 *, s32, s32); keep the unfinished consumer's existing declaration. */
s32 func_15015A38();
/* Load the selected asset range, consume its blocks, and free the temporary copy. */
void func_15015920(s16 selector) {
    u8 *base;
    u8 *cursor;
    s32 index;

    base = (u8 *)func_10003C6C(0x2800, 1, 2, 1, 0);
    func_10004514(D_80082F80[selector].start, base,
                 (u32)D_80082F80[selector].end - (u32)D_80082F80[selector].start, 1);
    cursor = base;
    index = 0;
    if ((u32)cursor + 15 < (u32)base + D_80082F80[selector].end - D_80082F80[selector].start) {
        do {
            func_15015A38(cursor, index, selector);
            /* Read the live big-endian size after the consumer; unsigned sums wrap. */
            cursor = (u8 *)((u32)cursor + ((u32)cursor[5] << 16) +
                           ((u32)cursor[6] << 8) + (u32)cursor[7] + ((u32)cursor[4] << 24));
            index++;
        } while ((u32)cursor + 15 < (u32)base + D_80082F80[selector].end - D_80082F80[selector].start);
    }
    func_10004074(base);
}

s32 func_15015A38() {
    return 0;
}
