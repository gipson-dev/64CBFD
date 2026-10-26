#include <ultra64.h>

u8 *func_151491F4(s16, s8, s8, u8, u8, s32, u8, s32);
void func_1516972C(u8 *record);


/* Non-matching placeholders for the text-only asm slice asm/108E90.s. */

s32 func_150DB9E0() {
    return 0;
}

s32 func_150DBC60() {
    return 0;
}

s32 func_150DBD70() {
    return 0;
}

s32 func_150DC558() {
    return 0;
}

s32 func_150DCEA0() {
    return 0;
}

s32 func_150DD640() {
    return 0;
}

/* Create a short-lived record, then select its byte mode from the owner's subtype. */
void func_150DDED0(u8 *owner) {
    u8 *record;

    record = func_151491F4(100, 2, -1, 1, 0, 1, 255, 0);
    if (record != NULL) {
        switch (owner[0x72]) {
            case 0xFB: record[0x28] = 1; break;
            case 0xFC: record[0x28] = 2; break;
            case 0xFD: record[0x28] = 4; break;
            case 0xFE: record[0x28] = 3; break;
            default: func_1516972C(record); break;
        }
    }
}

void func_150DDF88(u8 *arg0) {
    func_150DBD70(*(u8 *)(arg0 + 0x28), arg0);
}

s32 func_150DDFAC() {
    return 0;
}

s32 func_150DE12C() {
    return 0;
}

s32 func_150DE2A4(u8 *arg0) {
    s16 value = *(s16 *)(arg0 + 0x1C);

    if (value < 0x20) {
        arg0[0x28] = value << 3;
    }
    return 1;
}

void func_150DE2C4(u8 *arg0) {
    *(s16 *) (arg0 + 0x34) = *(s16 *) (arg0 + 0x34) - 0x1A;
    *(s16 *) (arg0 + 0x36) = *(s16 *) (arg0 + 0x36) - 0x1A;
    if ((*(s16 *) (arg0 + 0x34) < 0xA) || (*(s16 *) (arg0 + 0x36) < 0xA)) {
        *(s16 *) (arg0 + 0x38) = 0;
    }
}
