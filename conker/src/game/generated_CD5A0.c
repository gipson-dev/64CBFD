#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/CD5A0.s. */

typedef struct {
    u8 status;
    u8 pad1[3];
    s32 value;
    s32 unk8;
} GeneratedCD5A0Record;

extern GeneratedCD5A0Record D_800D3010[];

s32 func_150A00F0() {
    return 0;
}

s32 func_150A019C() {
    return 0;
}

s32 func_150A0264(s32 index, GeneratedCD5A0Record *arg1) {
    s32 value;
    GeneratedCD5A0Record *record = &D_800D3010[index];

    if ((*(u32 *) record >> 31) != 0) {
        return 0;
    }

    record->status |= 0x80;
    record->status &= 0xBF;
    value = arg1->value;
    record->value = 0;
    record->status = (record->status & 0xC3) | ((value << 2) & 0x3C);
    return 1;
}

s32 func_150A02D0() {
    return 0;
}

s32 func_150A0374(s32 arg0, s32 arg1, s32 arg2) {
    extern u8 D_800D3014[];

    if (arg1 == 3) {
        return *(s32 *) (D_800D3014 + arg0 * 12);
    }
    return 0;
}
