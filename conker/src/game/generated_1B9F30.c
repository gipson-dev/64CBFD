#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/1B9F30.s. */

typedef struct {
    u8 pad0[0x14];
    s32 packedOffset;
    u8 pad18[0x1C];
    s16 x;
    s16 y;
    s16 z;
    u8 pad3A;
    u8 callback;
} Generated1B9F30Record;

extern void (*D_8008D5D0[])(Generated1B9F30Record *);

s32 func_1518CA80() {
    return 0;
}

void func_1518CCA8(Generated1B9F30Record *arg0) {
    s32 packedOffset = arg0->packedOffset;
    s32 callback;

    arg0->x = (s16)(arg0->x + ((u32)(packedOffset & 0xFFFF0000) >> 16));
    arg0->y = (s16)(arg0->y + packedOffset);
    if (arg0->z == 0) {
        callback = arg0->callback & 0xF;
        if (callback != 0) {
            D_8008D5D0[callback](arg0);
        }
    }
}
