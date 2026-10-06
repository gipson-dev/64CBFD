#include <ultra64.h>

typedef struct ReloadRecord {
    u32 command;
    u32 base;
    u32 range;
    u32 timer;
    u8 parameters[1];
} ReloadRecord;

extern s32 D_800BE9E4;
s32 func_150D278C();
s32 func_150ADA20(void);

/* Non-matching placeholders for the text-only asm slice asm/FFBA0.s. */

void func_150D26F0(u8 *object) {
    ReloadRecord *record = (ReloadRecord *) (object + 0x28);

    if (object[0x78] & 1) {
        record->timer -= (u32) D_800BE9E4;
        if ((s32) record->timer < 0) {
            func_150D278C(record->command, record->parameters, object[0xC], object[1]);
            record->timer = (u32) func_150ADA20() % (record->range + 1) + record->base;
        }
    }
}

s32 func_150D278C() {
    return 0;
}

s32 func_150D2924() {
    return 0;
}

s32 func_150D2D6C() {
    return 0;
}

s32 func_150D317C() {
    return 0;
}

void func_150D32FC(u8 *arg0, u8 *arg1, u8 arg2) {
    u8 *record = arg0 + 0x28;

    if (arg2 == 0x34 && *arg1 == record[0x51]) {
        func_150D278C(*(s32 *) record, record + 0x10, arg0[0xC], arg0[1]);
    }
}
