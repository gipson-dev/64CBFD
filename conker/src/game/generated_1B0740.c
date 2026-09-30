#include <ultra64.h>

typedef struct {
    s32 words[5];
} Record15183974;

extern Record15183974 D_800DDE80[11];
s32 func_15183ACC();

/* Non-matching placeholders for the text-only asm slice asm/1B0740.s. */

s32 func_15183290() {
    return 0;
}

s32 func_151838B0() {
    return 0;
}

void func_15183974(s32 arg0) {
    Record15183974 *record;

    record = &D_800DDE80[arg0];

    if (record[0].words[0] == 0) {
        func_15183ACC(arg0);
    }
    if (record[1].words[0] == 0) {
        func_15183ACC(arg0 + 1);
        record[1].words[3] = record[0].words[3];
    }
}

s32 func_151839F0() {
    return 0;
}

s32 func_15183ACC() {
    return 0;
}

s32 func_15183BA4() {
    return 0;
}

s32 func_15183C28() {
    return 0;
}

s32 func_15183D28() {
    return 0;
}

s32 func_15184118(u8 *arg0) {
    u8 *temp_v0 = *(u8 **) (arg0 + 0x31C);

    if ((temp_v0 != 0) && (*(temp_v0 + 0x57) != 0)) {
        return 1;
    }
    return 0;
}
