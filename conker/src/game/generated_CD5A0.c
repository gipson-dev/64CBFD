#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/CD5A0.s. */

typedef struct {
    u8 status;
    u8 pad1[3];
    s32 value;
    s32 unk8;
} GeneratedCD5A0Record;

extern GeneratedCD5A0Record D_800D3010[];

/* Clear the active bit and both counters in all ten records. */
void func_150A00F0(void) {
    s32 index;
    for (index = 0; index < 10; index++) {
        D_800D3010[index].status &= (u16)~0x80;
        D_800D3010[index].value = 0;
        D_800D3010[index].unk8 = 0;
    }
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

/* Apply the record flag/value commands and report whether one was handled. */
s32 func_150A02D0(u32 index, s32 command, const s32 *payload) {
    extern u8 D_800D3014[];

    switch (command) {
        case 0:
            D_800D3010[index].status = (D_800D3010[index].status & ~0x40) | 0x40;
            return 1;
        case 1:
            D_800D3010[index].status &= ~0x40;
            return 1;
        case 2:
            *(s32 *)(D_800D3014 + index * 12) = payload[2];
            return 1;
    }
    return 0;
}

s32 func_150A0374(s32 arg0, s32 arg1, s32 arg2) {
    extern u8 D_800D3014[];

    if (arg1 == 3) {
        return *(s32 *) (D_800D3014 + arg0 * 12);
    }
    return 0;
}
