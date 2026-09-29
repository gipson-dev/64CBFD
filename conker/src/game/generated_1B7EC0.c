#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/1B7EC0.s. */

typedef struct {
    u8 pad0[0x10];
    s32 owner;
    s32 unk14;
    s32 unk18;
    u8 selector;
    u8 pad1D[3];
} Generated1B7EC0Command1E;

void *func_15167A68(s32 arg0, s32 arg1, s32 arg2, s32 arg3, u8 arg4, u8 arg5);

s32 func_1518AA10() {
    return 0;
}

s32 func_1518AADC() {
    return 0;
}

Generated1B7EC0Command1E *func_1518AB60(s32 arg0, volatile u8 arg1) {
    volatile Generated1B7EC0Command1E *record;
    u8 selector;

    record = func_15167A68(0x1E, 0, 0x20, 1, 0xFF, 1);
    if (record == NULL) {
        return NULL;
    }

    record->owner = arg0;
    selector = arg1;
    record->unk14 = 0;
    record->unk18 = 0;
    record->selector = selector;
    return (Generated1B7EC0Command1E *)record;
}

s32 func_1518ABD0() {
    return 0;
}
